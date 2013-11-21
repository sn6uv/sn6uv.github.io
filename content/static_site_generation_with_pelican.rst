Static site generation with pelican.
####################################
:date: 2013-11-21 16:24
:category: programming
:author: Angus Griffith

Introduction
------------

I'd like to start by talking about pelican_, a neat python based static site
generator.
Pelican allows you to generate static content (HTML and CSS) from reStructuredText_ (RST) files.


Installing Pelican
------------------

You can install pelican with pip:

.. code-block:: bash

    pip install pelican

The code is on github_ if you're curious.

Creating a blog
---------------

Let's begin by creating a new directory

.. code-block:: bash

    $ mkdir blog
    $ cd blog/

From here we need to add some config files so pelican knows how to generate
the site.
We can do this manually, but pelican includes this useful tool

.. code-block:: bash

    $ pelican-quickstart

It will then ask you a series of questions, like where you want the website
to be created:

.. code-block:: bash

    Welcome to pelican-quickstart v3.3.0.
    
    This script will help you create a new Pelican-based website.
    
    Please answer the following questions so this script can generate the files
    needed by Pelican.
    
        
    > Where do you want to create your new web site? [.] 
    > What will be the title of this web site? my blog
    > Who will be the author of this web site? me
    > What will be the default language of this web site? [en] 
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n) n
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) 
    > Do you want to upload your website using FTP? (y/N) 
    > Do you want to upload your website using SSH? (y/N) 
    > Do you want to upload your website using Dropbox? (y/N) 
    > Do you want to upload your website using S3? (y/N) 
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) 
    Done. Your new project is available at /home/angus/blog

Lets test our new blog!

.. code-block:: bash

    $ fab build
    $ fab serve

and point your browser at http://localhost:8000/.

.. image:: /images/myblog.png
   :width: 100 %
   :alt: myblog.png

Sucess!

Tip:
If `python` refers to Python 3 on your system you'll have to edit `fabfile.py`
and the `Makefile` accordingly.
E.g. Change

.. code-block:: python

    def serve():
        local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

to either

.. code-block:: python

    def serve():
        local('cd {deploy_path} && python2 -m SimpleHTTPServer'.format(**env))

or
    
.. code-block:: python

    def serve():
        local('cd {deploy_path} && python -m http.server'.format(**env))

in `fabfile.py` depending on whether you want to test your blog with a
Python 2 or Python 3 http server.

Adding Content
--------------
We've got an empty blog working. Let's add some content

.. code-block:: bash

    $ vim content/firstpost.rst

and then add:

.. code-block:: rst

    Firstpost
    #########
    :date: 2012-03-30 23:47
    :category: programming
    :author: Angus Griffith
    
    RST is cool! We can include code snippets like this
    
    .. code-block:: python
    
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
    
    and links like this Python_.
    
    .. _Python: http://python.org/

rebuild the site

.. code-block:: bash

    $ fab build

.. image:: /images/firstpost.png
   :width: 100 %
   :alt: firstpost.png

Hooray!

.. _pelican: http://docs.getpelican.com/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _github: https://github.com/getpelican/pelican/
