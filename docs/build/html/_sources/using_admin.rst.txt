.. toctree::
    :maxdepth: 40
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


The Admin Interface
======================================

The following entities are designed to be managed through the Admin panel. |br|
They can be handled via API as well, if you wish so, but you probably don't want to have these exposed while in production. |br| |br|
```Categories``` |br|
```Countries``` |br|
```Time-units``` |br|
```Payment-types``` |br|
```Currencies```

The administration panel is the default Django implementation and is used by staff-users rather than end-users. |br| |br|
The only staff-user that exists in the beginning is the superuser that was created during installation. |br| |br|
The superuser can add other staff-users or give regulars the staff status. |br|
Staff-users can edit virtually anything as long as they have the permission.
