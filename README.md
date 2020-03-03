# eventuate-tram-upgrade-scripts

### replace_dependencies.py

It is a python script that adapts eventuate based applications to
multi-framework versions of libraries by replacing modules and packages by actual versions.

For example, to update application that uses eventuate-tram-core to multi-module version
it is necessary to replace modules:

**eventuate-tram-events** by **eventuate-tram-spring-events**, **eventuate-tram-commands** by **eventuate-tram-spring-commands**, etc.

Also it is necessary to replace packages by actual names.

The script does it for you.

##### how to use

Edit script and specify project folder to update by changing **PROJECT_FOLDER** variable.

Currently script supposes that project is located in the same folder as script.
And project name folder is **eventuate-examples-java-customers-and-orders**:

`PROJECT_FOLDER = "eventuate-examples-java-customers-and-orders"`

then you can run it:

**`python replace_dependencies.py`**

Note that class.replacements and module.replacements files should be in the same folder as the python script.
Or you can change it, by editing variables:

`MODULE_REPLACEMENTS = "module.replacements"`

`CLASS_REPLACEMENTS = "class.replacements"`