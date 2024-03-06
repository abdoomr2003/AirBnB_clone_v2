#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers,
using the function do_deploy"""

from fabric.api import env, put, run
from os import path
env.hosts = ['52.72.74.64', '3.90.80.21']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        folder = "/data/web_static/releases/" + archive_path.split('/')[1][:-4]
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}/".format(archive_path.split('/')[1], folder))
        run("rm /tmp/{}".format(archive_path.split('/')[1]))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False
