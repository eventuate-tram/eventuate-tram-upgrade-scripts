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

1. git clone https://github.com/eventuate-tram/eventuate-tram-upgrade-scripts.git
2. cd <root-directory-of-eventuate-based-project-to-update>
3. python <eventuate-tram-upgrade-scripts>/replace_dependencies.py