#!/usr/bin/python3
"""do_pack function definition"""

from fabric.api import local
from os.path import exists


def do_pack():
    """creates a .tgz archive file for web_static folder"""
    task = 'tar -cvzf versions/"web_static_$(date +%Y%m%d%H%M%S)" web_static'
    if not exists("./versions"):
        local('mkdir versions')
    archive = local(task)
    return archive
