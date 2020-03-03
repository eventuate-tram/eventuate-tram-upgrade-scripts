import os
from os import walk
import itertools

MODULE_REPLACEMENTS = "module.replacements"
CLASS_REPLACEMENTS = "class.replacements"

PROJECT_FOLDER = "eventuate-examples-java-customers-and-orders"

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
		r = replacement.replace("\n", "").split("->")
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


files = get_files_in_folder_and_subfolders(PROJECT_FOLDER)

gradles = filter_files(files, ".gradle")
poms = filter_files(files, "pom.xml")
classes = filter_files(files, ".java")

module_replacements = load_replacements(MODULE_REPLACEMENTS)
class_replacements = load_replacements(CLASS_REPLACEMENTS)

replace_dependencies(gradles, module_replacements, ":", ":")
replace_dependencies(poms, module_replacements, "<artifactId>", "</artifactId>")
replace_dependencies(classes, class_replacements)