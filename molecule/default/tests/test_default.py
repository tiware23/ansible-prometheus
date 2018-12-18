import os

import testinfra

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config(host):
    config = host.run("sudo grep 'localhost:9090' prometheus.yml |wc -l ")
    assert config.rc == 0


def test_prometheus_config(host):
    config = host.run("sudo systemctl status prometheus")
    assert config.rc == 0


def test_prometheus_local_port(host):
    local_port = host.socket("tcp://127.0.0.1:9090")
    assert local_port.is_listening


def test_prometheus_running_and_enabled(host):
    prometheus_service = host.service("prometheus")
    assert prometheus_service.is_running
    assert prometheus_service.is_enabled
