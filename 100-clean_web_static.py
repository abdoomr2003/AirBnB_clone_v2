#!/usr/bin/python3
"""
Deletes out-of-date archives,
using the function do_clean
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['52.72.74.64', '3.90.80.21']
env.user = 'ubuntu'


def deploy():
    ''' Deploys archive '''
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
