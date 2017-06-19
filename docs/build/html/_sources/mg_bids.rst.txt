.. toctree::
    :maxdepth: 800
    :caption: General information

.. |br| raw:: html

   <br />

Creating a bid
===================

Companies bid on other companies` projects. This means bids are linked directly to companies rather than to users. |br|
A bid cannot be posted on behalf of a company that does not belong to the authenticated user. This will result in a ```HTTP 403 FORBIDDEN``` error. |br| |br|
That being said, to create a bid, we use the HTTP ```POST``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/bids/',
        type: 'POST',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
          payment_type: 1,
          payment_amount: 30,
          currency: 1,
          project: 1,
          by_company: 1
        },
        success: function (response) {
          console.log(response);
        }
    });

Accessing all bids
================================

In order to obtain an object of all bids, we use the HTTP ```GET``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/bids/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        success: function (response) {
          console.log(response);
        }
    });

Paginating a list of bids
================================

By default, the API will return an object containing 3 bids, and will indicate the url to the next page. |br|
For example, if we have 5 bids in total, then we'll have 2 pages. |br|
For obtaining the first 3, ```http://localhost:8000/bids/``` is enough. |br|
To go to the last 2, we need to change page: ```http://localhost:8000/bids/?page=2``` |br|

The default number of items per page can be set by changing the ```PAGE_SIZE``` setting in ```settings.py```, under ```REST_FRAMEWORK``` options.

Filtering a list of bids
================================

When listing companies, several filters can be applied:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/bids/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        // beforeSend: function (xhr) {
        //   xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        // },
        data: {
          payment_type: 1,
          currency: 3,
          by_company: 1,
          project: 3,
          min_amount: 40,
          max_amount: 130
        },
        success: function (response) {
          console.log(response);
        }
    });

Other filters will be added in a future release.

Accessing one specific bid
================================

In order to access the data about a bid, we use also the HTTP ```GET``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/bids/2/',
        type: 'GET',
        // Fetch the stored token from localStorage and set in the header
        // beforeSend: function (xhr) {
        //   xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        // },
        success: function (response) {
          console.log(response);
        }
    });

As you can notice here, the token section is commented out. That is because bids data can be accessed with or without being authenticated. |br| |br|
However, trying to achieve this for other operations will result in ```HTTP 401 UNAUTHORIZED```

Updating a bid
===================

To update a bid, we can use the HTTP ```PUT``` method. |br|
This method requires that all the bid fields are sent. |br|

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/bids/2/',
        type: 'PUT',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
          payment_type: 2,
          payment_amount: 60,
          currency: 3,
          project: 5,
          by_company: 1
        },
        success: function (response) {
          console.log(response);
        }
    });

Doing a ```PUT``` may be a little too much if we only want to change a field or two. |br| It could be easier to just use the HTTP ```PATCH``` method for this. |br|

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/bids/2/',
        type: 'PATCH',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        data: {
            payment_amount: 45,
        },
        success: function (response) {
          console.log(response);
        }
    });


Deleting a bid
===================

Take note that a bid can only be deleted if it was published by a company that belongs to the currently authenticated user. |br| |br|
In order to remove a bid, we use the HTTP ```DELETE``` method:

.. code-block:: javascript

    $.ajax({
        url: 'http://localhost:8000/bids/3/',
        type: 'DELETE',
        // Fetch the stored token from localStorage and set in the header
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Authorization", 'Token '+ localStorage.getItem('token'));
        },
        success: function (response) {
          console.log(response);
        }
    });
