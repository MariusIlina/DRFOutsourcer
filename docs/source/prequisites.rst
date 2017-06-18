.. toctree::
    :maxdepth: 20
    :caption: Before installing

.. |br| raw:: html

   <br />

.. |psql| raw:: html

   <a href="https://www.postgresql.org/download/" target="_blank">PostgreSQL downloads page</a>

.. |redis| raw:: html

   <a href="https://redis.io/download" target="_blank">here</a>

.. |python| raw:: html

   <a href="https://www.python.org/downloads/" target="_blank">here</a>

.. |pip| raw:: html

   <a href="https://pip.pypa.io/en/stable/installing/" target="_blank">here</a>


Prequisites
======================================

PostgreSQL
^^^^^^^^^^^^^^^^^^^^

OutSourcer uses PosgreSQL for its data storage. |br|
One of the reasons why we chose it is because it is the most compatible RDBMS with Django’s migration system. |br|
Please make sure you have it installed on your system before installing the application. |br|
You can download it from |psql|. |br| |br|
Make sure your system has ```psycopg2``` module installed.
For example on Ubuntu, ```psycopg2``` can be installed like this:

.. code-block:: bash

    sudo apt-get install python-psycopg2

You might also need this:

.. code-block:: bash

    sudo apt-get install libpq-dev

Redis
^^^^^^^^^^^^^^^

Running a new database query each time a visitor wants to see a listing page can be really bad for the application’s performance. |br|
Redis is used for caching result-sets and page-listings. |br|
It is compulsory for the application to work. |br|
You can download Redis from |redis|.

Python
^^^^^^^^^^^^^^

OutSourcer is written using Django, which is a framework for Python. |br|
Thus, in order to run OutSourcer, you have to install Python first. |br|
Always be aware of the Python version you have installed. For OutSourcer, we recommend using version 2.7. |br|
You can download Python from |python|.

PIP
^^^^^^^^^^^^^^^^^^^

Pip is the package manager for Python. OutSourcer has multiple dependencies that have to be installed and PIP will take care of those for you. |br|
You can install PIP for Python using the instrunctions from |pip|.
