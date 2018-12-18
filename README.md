Prometheus Role
=========

This about install Prometheus just to monitoring static targets.

Requirements
------------

N/A

Role Variables
--------------
```
home_directory_prometheus -> Prometheus Home
storage_directory_prometheus: -> Prometheus base static metrics directory
static_job: [] -> Where you can define the static targets
version_prometheus: "2.5.0"
prometheus_rule: [] -> Where you can define Alerts rules
```

Example Playbook
----------------

    - hosts: servers
      roles:
         - ansible-prometheus
      vars:
        static_job:
          - name: kafka-exporter
            nodes: {
              "localhost:9308"
            }

Test Molecule
---------------------

```
   Install dependencies:
   
    Ansible >= 2.4
    Python 2.7
    Python >= 3.6 with Ansible >= 2.4

    $ pip install virtualenv
    $ virtualenv --no-site-packages .venv
    $ source .venv/bin/activate

    $ pip install molecule docker testinfra

```
```
   Run kitchen on root repository:
   
   $ molecule test

```

License
-------

BSD
