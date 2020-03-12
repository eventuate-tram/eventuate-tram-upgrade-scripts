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

`1. git clone https://github.com/eventuate-tram/eventuate-tram-upgrade-scripts.git`

`2. cd <root-directory-of-eventuate-based-project-to-update>`

`3. python <eventuate-tram-upgrade-scripts>/replace_dependencies.py`

It also supports updating of micronaut applications by passing MICRONAUT option.
To update micronaut application step 3 should be changed to:

`python <eventuate-tram-upgrade-scripts>/replace_dependencies.py MICRONAUT`

##### required manual changes

The script cannot replace removed `eventuate-jpa-sagas-framework` dependency.
It should be replaced manualy by eventuate-tram-sagas-<spring/micronaut>-orchestration and/or eventuate-tram-sagas-<spring/micronaut>-participant depending on used API.
If that dependency found during dependency replacements, warning will be printed.
