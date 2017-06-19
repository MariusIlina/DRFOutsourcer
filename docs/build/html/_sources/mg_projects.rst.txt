.. toctree::
    :maxdepth: 800
    :caption: General information

.. |br| raw:: html

   <br />

Creating a project
===================

Companies publish projects. This means projects are linked directly to companies rather than to users. |br|
A project cannot be published on behalf of a company that does not belong to the authenticated user. This will result in a ```HTTP 403 FORBIDDEN``` error. |br| |br|
That being said, to create a project, we use the HTTP ```POST``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/projects/',
        type: 'POST',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
            "project_name": "RedAlert",
            "by_company": 3,
            "approximate_duration": "30",
            "approximate_duration_time_unit": 3,
            "description": "Lorem ipsum dolor sic amet",
            "work_description": "programming",
            "slug_name": "outsourcer",
            "required_techs": "python, javascript, redis",
            "approximate_hours_per_week": 50,
            "payment_type": 3,
            "payment_amount": 40,
            "currency": 3,
            "min_ppl_required": 9,
            "category": 3
        },
        success: function (response) {
          console.log(response);
        }
    });

Accessing all projects
================================

In order to obtain an object of all projects, we use the HTTP ```GET``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/projects/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        // beforeSend: function (xhr) {
        //   xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        // },
        success: function (response) {
          console.log(response);
        }
    });

Paginating a list of projects
================================

By default, the API will return an object containing 3 projects, and will indicate the url to the next page. |br|
For example, if we have 5 projects in total, then we'll have 2 pages. |br|
For obtaining the first 3, ```http://localhost:8000/projects/``` is enough. |br|
To go to the last 2, we need to change page: ```http://localhost:8000/projects/?page=2``` |br|

The default number of items per page can be set by changing the ```PAGE_SIZE``` setting in ```settings.py```, under ```REST_FRAMEWORK``` options.

Filtering a list of projects
================================

When listing projects, filters can be applied:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/projects/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        // beforeSend: function (xhr) {
        //   xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        // },
        data: {
          category: 1, // Ex. "1" could mean "Backend development" or other categories...
          by_company: 1, // Let's say this stands for "SC Some Company SRL"
          currency: 1, // Let's say this stands for EUR etc.
          payment_type: 4, // Say this means "hourly" etc.
          min_amount: 15, // If currency is EUR and payment type is "hourly", then this is "40"-"EUR"-"hourly"
        },
        success: function (response) {
          console.log(response);
        }
    });

Other filters will be added in a future release.

Accessing one specific project
================================

In order to access the data about a project, we use also the HTTP ```GET``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/projects/2/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        // beforeSend: function (xhr) {
        //   xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        // },
        success: function (response) {
          console.log(response);
        }
    });

As you can notice here, the token section is commented out. That is because project data can be accessed with or without being authenticated. |br| |br|
However, trying to achieve this for other operations will result in ```HTTP 401 UNAUTHORIZED```

Updating a project
===================

To update a project, we can use the HTTP ```PUT``` method. |br|
This method requires that all the project fields are sent. |br|
In this example, we'll only change the project title.

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/projects/2/',
        type: 'PUT',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
            "project_name": "Red Alert",
            "by_company": 3,
            "approximate_duration": "30",
            "approximate_duration_time_unit": 3,
            "description": "Lorem ipsum dolor sic amet",
            "work_description": "programming",
            "slug_name": "outsourcer",
            "required_techs": "python, javascript, redis",
            "approximate_hours_per_week": 50,
            "payment_type": 3,
            "payment_amount": 40,
            "currency": 3,
            "min_ppl_required": 9,
            "category": 3
        },
        success: function (response) {
          console.log(response);
        }
    });

Doing a ```PUT``` may be a little too much if we only want to change a field or two. |br| It could be easier to just use the HTTP ```PATCH``` method for this. |br|

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/projects/3/',
        type: 'PATCH',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
            "project_name": "Red Alert v.1.0",
        },
        success: function (response) {
          console.log(response);
        }
    });


Deleting a project
===================

Take note that a project can only be deleted if it was published by a company that belongs to the currently authenticated user. |br| |br|
In order to remove a project, we use the HTTP ```DELETE``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/projects/3/',
        type: 'DELETE',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        success: function (response) {
          console.log(response);
        }
    });
