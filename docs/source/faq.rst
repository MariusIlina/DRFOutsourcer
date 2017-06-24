.. toctree::
    :maxdepth: 800
    :caption: General information

.. |br| raw:: html

   <br />

.. |django| raw:: html

   <a href="https://www.djangoproject.com/" target="_blank">Django</a>

.. |python| raw:: html

   <a href="https://www.python.org/" target="_blank">Python</a>

.. |drf| raw:: html

   <a href="http://www.django-rest-framework.org/" target="_blank">Django Rest Framework</a>

.. |psql| raw:: html

   <a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a>

.. |redis| raw:: html

   <a href="https://redis.io/" target="_blank">Redis</a>

Frequently asked questions
======================================

What's this about?
^^^^^^^^^^^^^^^^^^^^

OutSourcer is a self-hosted, minimalist Backend API which aims to ease the development of B2B project-bidding applications. |br| |br|
OutSourcer is composed of a "Browsable API" and an "Admin Interface". |br| |br|

How it works?
^^^^^^^^^^^^^^^

* **Users** can create **Companies**
* **Companies** can publish **Projects**
* **Companies** can bid on other companies’ **Projects**, as long as the user owns the company that is posting the project.
* **Projects** fall into **Categories**
* **Companies** can add **Comments** about other companies on a **Project**, if the project belongs to the company that is adding the comment.
* **Companies** can add **Recommendations** for other companies.

How will it improve?
^^^^^^^^^^^^^^^^^^^^

As it is the first version, we are planning on developing a lot of features in the future, as well as improving some behaviours. |br|
While the application is functional at this moment, we are expecting feedback and improvement ideas from people who use this app. |br|
For the next release, we'll be completing some features like: |br|

- search |br|
- date-time filtering |br|
- results ordering |br|

which are now either missing or buggy.

Is it free?
^^^^^^^^^^^^^^

Yes, you can use OutSourcer API absolutely free of charge.

Is it open-source?
^^^^^^^^^^^^^^^^^^^

Yes, OutSourcer is open-source and it is distributed under BSD License.

What's it written in?
^^^^^^^^^^^^^^^^^^^^^^^^

OutSourcer is written in |python|, using |django| and |drf|. |br|
For the data-storage it uses |psql| and |redis|.

I need to change code
^^^^^^^^^^^^^^^^^^^^^^^^
If your project needs something different than the default functionality (and it almost surely will), feel free to adapt the code to fit your needs. |br|
Anyway, in order to make this easier for you, make sure you are comfortable with |drf|.