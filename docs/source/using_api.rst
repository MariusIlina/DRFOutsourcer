.. toctree::
    :maxdepth: 800
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


Using the REST API
======================================

Creating a new user
^^^^^^^^^^^^^^^^^^^^

Below is a sample code for creating a user. If successful, you should see something like: |br|
```Object {username: "myUser", email: "myUser@email.com"}```

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:9999/register/',
        type: 'POST',
        data: {
          username: 'myUser',
          email: 'myUser@email.com',
          password: 'mySecretPass'
        },
        success: function (response) {
            console.log(response); // Should log
        }
    });

Token authentication
^^^^^^^^^^^^^^^^^^^^^

For authentication, we'll send some credentials and store the token for further use.

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/token-auth/',
        type: 'POST',
        data: {
          username: 'myUser',
          password: 'mySecretPass'
        },
        success: function (response) {
          localStorage.setItem('token', response.token);
        }
    });

Managing companies
^^^^^^^^^^^^^^^^^^^

.. toctree::

    mg_companies

Managing projects
^^^^^^^^^^^^^^^^^^

.. toctree::

    mg_projects

Managing bids
^^^^^^^^^^^^^^^^^^^^

.. toctree::

    mg_bids

Managing recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

    mg_recommendations

Managing comments
^^^^^^^^^^^^^^^^^^^

.. toctree::

    mg_comments
