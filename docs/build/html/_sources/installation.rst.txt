.. toctree::
    :maxdepth: 40
    :caption: Getting started

.. |br| raw:: html

    <br />


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

    sudo python manage.py migrate auth

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

You can now go to ```http://localhost:8000``` (or whatever port you set). |br|

Here you can see the Graphical User Interface for the API. |br|

You can also go to the administration panel, located at ```http://localhost:8000/admin``` and log in using the credentials that you have earlier set for the superuser.
