#!/usr/bin/python3
"""do_pack function definition"""

from fabric.api import local
import glob
from os.path import exists, getctime


def do_pack():
    """creates a .tgz archive file for web_static folder"""
    task = "tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz web_static"
    if not exists("./versions"):
        local('mkdir versions')
    local(task)
    list_of_files = glob.glob('versions/*')
    latest_file = max(list_of_files, key=getctime)
    return latest_file
