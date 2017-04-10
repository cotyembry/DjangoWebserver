# Request




# Response



# the **Web Server** handles and serves these, respectfully

# Static files versus, what, Dynamic files
separation of concern for these file types - Django has different ways of serving these file types


# Routing
























# Django installation
make sure django is installed
from the command line do

	python -m django --version


# Create a project

	django-admin startproject simpleWebsite

this creates some files

These files are:

*The outer* 
`simpleWebsite/` root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.


`manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.


*The inner*
`simpleWebsite/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. simpleWebsite.urls).


`mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.


`mysite/settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.


`mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.


`mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.


# Development server
make sure you are in the `simpleWebsite` directory and type


    python manage.py runserver


this will start a development server to use and should now allow navigating to `127.0.0.1:8000` in your web browser (that is on the same wifi network) where it will render a default web page


# Development Webserver Vs Production Webserver

You would not typically use this type of server in production (i.e. as a final real world application you are charging a client for)

A _development_ web server would just be used during development of the project and iterating on the code. Some development web servers have fancy tools that can seriously speed up your iteration times

__I will use the term server from here on for the web server as an interchangable term__

# Quit the server
enter the following on the command line to stop this 

    ctrl+c


# Auto reloading
Automatic reloading of runserver

    The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.


Now that the environment – a “project” – is set up, we can start doing work.

# Projects vs. apps

    django-admin startproject simpleWebsite
    python manage.py startapp App1


What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.


# Create the App
now we can create the actual app with

    python manage.py startapp App1

which makes the following changes to the tree

    App1/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py

# Write your first view
yay!

whats a view...

I would say a view in this context is basically a page to be rendered for a particular route that the user navigates to


Open `App1/views.py`


I will put the following code in the views.py file


    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Boom, in App1 app's index view")



`TODO:` write explanation for the above code

This view does not send back a file to render, it sends back just the text "Boom, in App1 app's index view" - pretty simple so far


Now create the file `urls.py` located in `App1/urls.py` include the following code


    from django.conf.urls import url

    from . import views

    urlpatterns = [
        url(r'^$', views.index, name='index'),
    ]


The App1 app should have the following structure now


    App1/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        urls.py
        views.py
        urls.py

The next step is to point the root URLconf at the App1.urls module. In simpleWebsite/urls.py, add an import for django.conf.urls.include and insert an include() in the urlpatterns list, so you have:


    from django.conf.urls import include, url
    from django.contrib import admin

    urlpatterns = [
        url(r'^App1/', include('App1.urls')),
        url(r'^admin/', admin.site.urls),
    ]



# url pattern example

They can get pretty sophisticated so +1 for this

    urlpatterns = [
        # ex: /polls/
        url(r'^$', views.index, name='index'),
        # ex: /polls/5/
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
        # ex: /polls/5/results/
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
        # ex: /polls/5/vote/
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    ]




# include() discussion about URLs

The include() function allows referencing other URLconfs. Note that the regular expressions for the include() function doesn’t have a $ (end-of-string match character) but rather a trailing slash. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since App1 are in their own URLconf (App1/urls.py), they can be placed under “/App1/”, or under “/fun_App1/”, or under “/content/App1/”, or any other path root, and the app will still work.


This makes a Django app super dynamic and I can see this helping with maintenance issues when wanting to restructure a website quickly


# Viewing `App1/` in the browser ^_^

You have now wired an index view into the URLconf. We can verify it is working by running the following command:


    python manage.py runserver


in the *browser* - Chrome is nice - navigate to the following (if you used the default runserver command line config to start the server):

    127.0.0.1:8000/App1/

This should render the text

    Boom, in App1 app's index view


# this is cool

Because once you have the feel for this, making awesome urls that tie together your application will be easier much easier (im comparing to not using Django to manage the routing)

I have found that tieing the application state to the url helps with understanding the application structure and even it's state



# Database setup
I am not going through this, but you could set up a database backend here.
Django has its own implemented it looks like
































# Separation of Code


# Potential for hosting multiple websites
this creates other problems like

-namespacing - for multiple websites? that could be messy
-subdomain? but those are 'ugly' and possibly 'unprofessional'
