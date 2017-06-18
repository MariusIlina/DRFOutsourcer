.. toctree::
    :maxdepth: 7
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
^^^^^^^^^^^^^^^^^^^^

Users must create at least one company, because everything in this app is company-based rather than user-based. |br| |br|
**CREATING A COMPANY** |br|
To create a company, we use the HTTP ```POST``` method:

.. code-block:: javascript

      $.ajax({
          url: 'http://localhost:8000/companies/',
          type: 'POST',
          // Fetch the stored token from localStorage and set in the header
          beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
          },
          data: {
            company_name: "SC Some Company SRL",
            employees_no: 4,
            description: "Lorem ipsum",
            country: 1, // Foreign key
            county: "Bucuresti", // String, can come from Google Places
            city: "Bucuresti", // String, can come from Google Places
            slug_name: "some_company",
            email: "admin@hi.com",
            phone: "0222999222",
            external_link: "www.google.com",
          },
          success: function (response) {
            console.log(response);
          }
      });

**ACCESSING A COMPANY** |br|
In order to access the data about a company, we use the HTTP ```GET``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:9000/companies/2/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        // beforeSend: function (xhr) {
        //   xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        // },
        success: function (response) {
          console.log(response);
        }
    });

As you can notice here, the token section is commented out. That is because company data can be accessed with or without being authenticated. |br| |br|
However, trying to achieve this for other operations will result in ```HTTP 401 UNAUTHORIZED```



**UPDATING A COMPANY** |br|
To update a company, we can use the HTTP ```PUT``` method. |br| This method requires that all the company fields are sent.

.. code-block:: javascript

      $.ajax({
          url: 'http://localhost:8000/companies/2/',
          type: 'PUT',
          content_type: 'application/json',
          // Fetch the stored token from localStorage and set in the header
          beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
          },
          data: {
            company_name: "SC The firm SRL",
            employees_no: 7,
            description: "Lorem ipsum dolor sic amet",
            country: 1, // Foreign key
            county: "Brasov", // String, can come from Google Places
            city: "Rupea", // String, can come from Google Places
            slug_name: "the_firm",
            email: "the_firm@gmail.com",
            phone: "2342342342",
            external_link: "www.yahoo.com",
          },
          success: function (response) {
            console.log(response);
          }
      });

If we only want to change some specific fields, and not all the data, we can use the HTTP ```PATCH``` method. |br|
However, when using ```PATCH```, you are required to send the ```email``` key all the time, even if you change it or not. (to be fixed in a future release)

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/companies/2/',
        type: 'PATCH',
        content_type: 'application/json',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
          employees_no: 99,
          email: "fict@email.com"
        },
        success: function (response) {
          console.log(response);
        }
    });

**DELETING A COMPANY** |br|
In order to remove a company, we use the HTTP ```DELETE``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/companies/2/',
        type: 'DELETE',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        success: function (response) {
          console.log(response);
        }
    });

!!! VERY IMPORTANT - Please note that **the company that is being edited or deleted must belong to the user that is currently authenticated**. |br| |br|
Trying to edit a company that belongs to another user will result in a ```HTTP 403 FORBIDDEN``` error.

Managing projects
^^^^^^^^^^^^^^^^^^

Managing bids
^^^^^^^^^^^^^^^^^^^^

Managing recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^

Managing comments
^^^^^^^^^^^^^^^^^^^
