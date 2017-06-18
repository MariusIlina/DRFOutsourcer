.. toctree::
    :maxdepth: 20
    :caption: General information

.. |br| raw:: html

   <br />

Creating a company
===================

Users must create at least one company, because almost everything in the application is company-based rather than user-based. |br| |br|
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

Accessing a company
====================

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

Updating a company
===================

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

Deleting a company
===================
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

Final notes
============

Please note that **the company that is being edited or deleted must belong to the user that is currently authenticated**. |br| |br|
Trying to ```edit/delete``` a company that belongs to another user will result in a ```HTTP 403 FORBIDDEN``` error.
