from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'angus@angusgriffith.com'
dest_path = '/var/www/html/blog'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python2 -m SimpleHTTPServer'.format(**env))
    # local('cd {deploy_path} && python -m http.server'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s pelicanconf.py')

@hosts(production)
def publish():
    local('pelican -s pelicanconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )

def symlinktheme():
    local('sudo pelican-themes -s mytheme')
