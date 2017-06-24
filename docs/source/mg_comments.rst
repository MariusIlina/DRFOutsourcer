.. toctree::
    :maxdepth: 800
    :caption: General information

.. |br| raw:: html

   <br />

Creating a comment
===========================

Companies can comment on any projects. |br|
A comment cannot be posted on behalf of a company that does not belong to the authenticated user. This will result in a ```HTTP 403 FORBIDDEN``` error. |br| |br|
That being said, to create a comment, we use the HTTP ```POST``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/comments/',
        type: 'POST',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
          by_company: 1,
          on_project: 3,
          comment: "I like working with this company"
        },
        success: function (response) {
          console.log(response);
        }
    });

Accessing all comments
================================

In order to obtain an object of all comments, we use the HTTP ```GET``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/comments/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        success: function (response) {
          console.log(response);
        }
    });

Paginating a list of comments
=====================================

By default, the API will return an object containing 3 comments, and will indicate the url to the next page. |br|
For example, if we have 5 comments in total, then we'll have 2 pages. |br|
For obtaining the first 3, ```http://localhost:8000/comments/``` is enough. |br|
To go to the last 2, we need to change page: ```http://localhost:8000/comments/?page=2``` |br|

The default number of items per page can be set by changing the ```PAGE_SIZE``` setting in ```settings.py```, under ```REST_FRAMEWORK``` options.

Filtering a list of comments
=====================================

When listing companies, several filters can be applied:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/comments/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        // beforeSend: function (xhr) {
        //   xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        // },
        data: {
          by_company: 1, // Foreign key Integer
          on_project: 3 // Foreign key Integer
        },
        success: function (response) {
          console.log(response);
        }
    });

Other filters will be added in a future release.

Accessing one specific comment
=========================================

In order to access the data about a comment, we use also the HTTP ```GET``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/comments/2/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        // beforeSend: function (xhr) {
        //   xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        // },
        success: function (response) {
          console.log(response);
        }
    });

As you can notice here, the token section is commented out. That is because comments data can be accessed with or without being authenticated. |br| |br|
However, trying to achieve this for other operations will result in ```HTTP 401 UNAUTHORIZED```

Updating a comment
==========================

To update a comment, we can use the HTTP ```PUT``` method. |br|
This method requires that all the comment fields are sent.  For less restrictive, use ```PATCH``` |br|

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/comments/3/',
        type: 'PUT',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
          by_company: 1,
          on_project: 5,
          comment: "I don't like working with this company"
        },
        success: function (response) {
          console.log(response);
        }
    });


Deleting a comment
==========================

Take note that a comment can only be deleted if it was published by a company that belongs to the currently authenticated user. |br| |br|
In order to remove a comment, we use the HTTP ```DELETE``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/comments/3/',
        type: 'DELETE',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        success: function (response) {
          console.log(response);
        }
    });
