# ansible-pex

Run ansible inside a pex that includes all playbooks, the inventory file and even custom modules.

## but.. why.. ??

Several reasons, but primarily, in a "cloudy" world, we should not be dependent on a master that "is out of date" with
the inventory (hosts, etc.) as they come and go. One way to do that is to run playbooks locally against a host, which
may be done by using AWS/GCE tags, user-data, etc. - I will leave the details to others to figure out.

Some benefits

- ```INSTALL + DEPENDENCIES``` : no need to install Ansible (and any / all of its dependencies) on a host anymore
- ```DISTRIBUTION``` : no need to git pull / clone a repository that has your inventory file, roles, playbooks and custom modules, you provide everything with the .pex file, which is versioned (or can be), which you could progress through environments (dev => qa => prod)
- ```SPEED``` : can be run as part of a cloud bootstrap to apply the play to the host, as it's run locally, it'll be very very fast 

## pre-requisites

- vagrant or docker (a host that's linux w/ python-dev(el) and general build-utils installed)

## create the pex

set up the environment

```
vagrant up
vagrant ssh
cd /vagrant
```

and create the pex

```
pex --disable-cache --python-shebang='/usr/bin/env python' plays -e plays -o distribution/builds/plays.pex
```

## run a playbook

copy ```plays.pex``` to a host you'd like to *config* manage, and run 

```
./plays.pex -p test.yml
```

The playbook must be inside the plays/plays/ directory; or the playbooks must reside in the same directory as the does ```run.py```.

## options

currently the following options have been implemented

| option         | description                        |
| -------------- | ---------------------------------- |
| -h             | help                               |
| --debug        | should return debug output         | 
| --noop         | do not actually execute            |
| --diff         | show diff, best to run with --noop |
| --playbook, -p | the playbook file name             |
