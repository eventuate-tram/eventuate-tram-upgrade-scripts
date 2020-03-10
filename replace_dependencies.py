import sys
import os
from os import walk
import itertools

PROJECT_FOLDER = os.getcwd()

MODULE_REPLACEMENTS_FILE = "module.replacements"
CLASS_REPLACEMENTS_FILE = "class.replacements"

if (len(sys.argv) > 1 and sys.argv[1] == "MICRONAUT"):
	MODULE_REPLACEMENTS_FILE = "module.micronaut.replacements"
	CLASS_REPLACEMENTS_FILE = "class.micronaut.replacements"

MODULE_REPLACEMENTS = os.path.join(sys.path[0], MODULE_REPLACEMENTS_FILE)
CLASS_REPLACEMENTS = os.path.join(sys.path[0], CLASS_REPLACEMENTS_FILE)

GRADLE_PROPERTIES = os.path.join(os.getcwd(), "gradle.properties")
LIBRARY_VERSIONS = os.path.join(sys.path[0], "library.versions")

def get_files_in_folder_and_subfolders(folder):
	return list(
		itertools.chain.from_iterable(
				[[os.path.join(root, file) for file in files] for root, dirs, files in walk(PROJECT_FOLDER)]
			)
		)

def load_replacements(file):
	f = open(file, "r")
	replacements = f.readlines()
	f.close()
	replacement_map = {}
	for replacement in replacements:
		replacement = replacement.replace("\n", "")
		if replacement:
			r = replacement.split("->")
			replacement_map[r[0]] = r[1]
	return replacement_map

def filter_files(files, extension):
	return [file for file in files if file.endswith(extension)]

def read_file(file):
	f = open(file, "r")
	content = f.read()
	f.close()
	return content

def write_file(file, content):
	f = open(file, "w")
	f.write(content)
	f.close()

def replace_dependencies(files, replacements, prefix = None, postfix = None):
	for file in files:
		content = read_file(file)
		new_content = content
		for k in replacements:
			original = k
			replacement = replacements[k]
			if prefix and postfix: 
				original = prefix + original + postfix
				replacement = prefix + replacement + postfix
			content = content.replace(original, replacement)
		if (content != new_content): write_file(file, content)

def update_libraries():
	library_versions = load_replacements(LIBRARY_VERSIONS)
	f = open(GRADLE_PROPERTIES, "r")
	lines = f.readlines()
	f.close()
	new_lines = []
	for line in lines:
		for lib in library_versions:
			if (line.startswith(lib + "=")): line = lib + "=" + library_versions[lib] + "\n"
		new_lines.append(line)
	f = open(GRADLE_PROPERTIES, "w")
	f.writelines(new_lines)
	f.close()

files = get_files_in_folder_and_subfolders(PROJECT_FOLDER)

gradles = filter_files(files, ".gradle")
poms = filter_files(files, "pom.xml")
classes = filter_files(files, ".java")

module_replacements = load_replacements(MODULE_REPLACEMENTS)
class_replacements = load_replacements(CLASS_REPLACEMENTS)

replace_dependencies(gradles, module_replacements, ":", ":")
replace_dependencies(poms, module_replacements, "<artifactId>", "</artifactId>")
replace_dependencies(classes, class_replacements)

update_libraries()