from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'angus@sn6uv.com:22'
dest_path = '/var/www/vhosts/sn6uv.com/htdocs'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))
    if os.path.exists('pelicanconf.pyc'):
        local('rm pelicanconf.pyc')
    if os.path.exists('publishconf.pyc'):
        local('rm publishconf.pyc')

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python2 -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
