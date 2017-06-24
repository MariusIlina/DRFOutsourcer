.. toctree::
    :maxdepth: 800
    :caption: Getting started

.. |br| raw:: html

    <br />

.. |apache| raw:: html

   <a href="https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/modwsgi/" target="_blank">Using Django 1.8 with Apache</a>

.. |nginx| raw:: html

   <a href="https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html" target="_blank">Using Django 1.8 with NGINX</a>


Installation
======================================

Getting started
^^^^^^^^^^^^^^^^^^^^

.. code-block:: html

    git clone https://github.com/paramount-consulting/OutSourcer

Under the project-root directory run the following command:

.. code-block:: bash

    sudo pip install -r requirements.txt

Create a database named ```outsourcer```. |br| |br|
Open ```OutSourcer/settings.py``` and edit the database section and REDIS section, so that they correspond to your credentials. |br| |br|
Under the project-root directory run the following commands, in this order: |br|

.. code-block:: bash

    sudo python manage.py migrate

Now run this command and answer the question you are asked. |br|

!!! IMPORTANT - the credentials you set here will be used to authenticate to the admin panel of the application. |br|

.. code-block:: bash

    sudo python manage.py createsuperuser

Starting the application
^^^^^^^^^^^^^^^^^^^^^^^^

Run the test server (will run on port 8000) |br|

.. code-block:: bash

    sudo python manage.py runserver

or if you want it to run on a specific port: |br|

.. code-block:: bash

    sudo python manage.py runserver 9999

Go to the administration panel, located at ```http://localhost:8000/admin``` (or whatever port you set) and log in using the credentials that you have earlier set for the superuser. |br|

You can now go to ```http://localhost:8000``` and play with the Browsable API feature, provided by Django Rest Framework. |br|

Going in production
^^^^^^^^^^^^^^^^^^^^^^^^

If you take the app into production, you should not use the built-in test server. |br|
OutSourcer is built on top of Django Framework, so let's have a look on how to deploy a Django app to production. |br| |br|
|apache| |br|
|nginx| |br| |br|
For production it is important to disable the Browsable API feature of Django's Rest Framework.
To disable it, go to ```settings.py```, find the REST_FRAMEWORK section and add this to it:

.. code-block:: python

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),

Now find the ```DEBUG``` setting in ```settings.py``` and change it to:

.. code-block:: python

    DEBUG = False

because you don't need error reporting in a production environment.