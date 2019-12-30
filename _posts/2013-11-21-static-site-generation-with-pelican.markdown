# Introduction
I'd like to start by talking about [pelican](http://docs.getpelican.com/), a
neat python based static site generator.
Pelican allows you to generate static content (HTML and CSS) from
[reStructuredText](http://docutils.sourceforge.net/rst.html) (RST) files.


# Installing Pelican
You can install pelican with pip:

{% highlight bash %}
pip install pelican
{% endhighlight %}

The code is on [github](https://github.com/getpelican/pelican/) if you're curious.

# Creating a blog
Let's begin by creating a new directory

{% highlight bash %}
mkdir blog
cd blog/
{% endhighlight %}

From here we need to add some config files so pelican knows how to generate
the site.
We can do this manually, but pelican includes this useful tool

{% highlight bash %}
pelican-quickstart
{% endhighlight %}

It will then ask you a series of questions, like where you want the website
to be created:

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

{% highlight bash %}
fab build
fab serve
{% endhighlight %}

and point your browser at `http://localhost:8000/`.

![myblog.png](/assets/myblog.png)

Sucess!

Tip:
If `python` refers to Python 3 on your system you'll have to edit `fabfile.py`
and the `Makefile` accordingly.
E.g. Change


{% highlight python %}
def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))
{% endhighlight %}

to either

{% highlight python %}
    def serve():
        local('cd {deploy_path} && python2 -m SimpleHTTPServer'.format(**env))
{% endhighlight %}

or
    
{% highlight python %}
    def serve():
        local('cd {deploy_path} && python -m http.server'.format(**env))
{% endhighlight %}

in `fabfile.py` depending on whether you want to test your blog with a
Python 2 or Python 3 http server.

Adding Content
--------------
We've got an empty blog working. Let's add some content

{% highlight bash %}
vim content/firstpost.rst
{% endhighlight %}

and then add:

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


{% highlight bash %}
fab build
{% endhighlight %}

![firstpost.png](/assets/firstpost.png)

# Hooray!

Obviously this is only a very short introduction to pelican.
The [getting started](http://docs.getpelican.com/en/3.3.0/getting_started.html)
 pelican documentation is excellent.
It tells you how to add other pages, include images,
link to internal content and much more.
