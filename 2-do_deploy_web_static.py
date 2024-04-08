#!/usr/bin/python3
"""do_pack function definition"""

from fabric.api import local, run, put, env
import glob
from os.path import exists, getctime

env.hosts = ['54.210.174.151', '18.235.234.102']


def do_pack():
    """creates a .tgz archive file for web_static folder"""
    task = "tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz web_static"
    if not exists("./versions"):
        local('mkdir versions')
    local(task)
    # used to retrieve files/pathnames matching a specified pattern
    list_of_files = glob.glob('versions/*')
    latest_file = max(list_of_files, key=getctime)
    return latest_file


def do_deploy(archive_path):
    """deploy a web_static archive to remote servers"""
    name = archive_path.split("/")[-1].split(".")[0]
    path = "/data/web_static/releases"
    command_list = [
        "mkdir -p {}/{}".format(path, name),
        "tar -xzf /tmp/{}.tgz -C {}/{}".format(name, path, name),
        "rm /tmp/{}.tgz".format(name),
        "mv {}/{}/web_static/* {}/{}/".format(path, name, path, name),
        "rm -rf {}/{}/web_static".format(path, name),
        "rm -rf /data/web_static/current",
        "ln -s {}/{} /data/web_static/current".format(path, name),
    ]
    results = []

    if not exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    for command in command_list:
        result = run(command)
        results.append(result.failed)
    if True in results:
        return False
    return True
