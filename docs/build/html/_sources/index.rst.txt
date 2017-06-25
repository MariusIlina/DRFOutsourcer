OutSourcer
======================================

.. |br| raw:: html

   <br />

OutSourcer is a self-hosted, minimalist Backend API which aims to ease the development of B2B project-bidding applications. |br| |br|
OutSourcer is composed of a "Browsable API" and an "Admin Interface". |br|

At this point, OutSourcer provides boilerplate code for giving a boost in starting your project. While the API is functional, you will more than likely need to tune it, cause no project is the same.

How does it wo work?
^^^^^^^^^^^^^^^^^^^^^

* **Users** can create **Companies**
* **Companies** can publish **Projects**
* **Companies** can bid on other companies’ **Projects**
* **Projects** fall into **Categories**
* **Companies** can add **Comments** about other companies on a **Project**.
* **Companies** can add **Recommendations** for other companies.

How is ownership implemented?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Companies can publish projects, as long as the authenticated user owns the company that is posting the project.
- Companies can only post comments on projects that they have published (This one will change in a future release).
- Users can edit/delete only their own companies.
- Generally any edit/delete operation is ownership-based.
- As a general rule, companies belong to users and anything else belongs to companies.

.. toctree::
    :maxdepth: 800
    :caption: Documentation

    prequisites
    installation
    using_admin
    using_api
    faq