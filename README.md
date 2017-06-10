About the OutSourcer project
===================

OutSourcer is B2B-oriented application which enables software companies of all sizes to outsource projects to other companies.

IT professionals who start software companies find it quite difficult to get contracts for their firm (being a lot more difficult than applying to a personal job based on past professional experience).

The application's purpose is to help small-company owners to apply to projects for their company just like they would apply to a job.

Before running the application
===================

#### PosgreSQL
OutSourcer uses PosgreSQL for its data storage. 
One of the reasons why we chose it is because it is the most compatible RDBMS with Django's migration system.

Please make sure you have it installed on your system before installing the application.

You can download it from <a href="https://www.postgresql.org/download/" target="_blank">PostgreSQL downloads page</a>.

#### Redis
Running a new database query each time a visitor wants to see a listing page can be really bad for the application's performance. Redis is used for caching result-sets and page-listings. 

It is compulsory for the application to work.

You can download Redis from <a href="https://redis.io/download" target="_blank">here</a>.

#### Python
OutSourcer is written using Django, which is a framework for Python. Thus, in order to run OutSourcer, you have to install Python first. 

Always be aware of the Python version you have installed. For OutSourcer, we recommend using version 2.7.

You can download Python from <a href="https://www.python.org/downloads/" target="_blank">here</a>.

#### PIP
Pip is a package manager for Python. OutSourcer has multiple dependencies that have to be installed and PIP will take care of those for you.

You can install PIP for Python using the instrunctions from <a href="https://pip.pypa.io/en/stable/installing/" target="_blank">here</a>.

Installing the application
===================

1. Under `wsgi/OutSourcer` directory run the following command:
```
pip install -r requirements.txt
``` 
2. Create a database named `outsourcer`
3. Open `wsgi/OutSourcer/settings.py` and edit the database settings, so that they corresponds to your credentials.
4. Under `wsgi/OutSourcer` directory run the following commands, in this order:
```
python manage.py migrate auth
```
```
python manage.py migrate
```
5. Now run this command and answer the question you are asked
```
python manage.py createsuperuser
```
6. Run the test server
```
python manage.py runserver
```
or if you want it to run on a specific port:
```
python manage.py runserver 9999
```

Before you push this app for the first time, you will need to change
the [Django admin password](#admin-user-name-and-password).
Then, when you first push this
application to the cloud instance, the sqlite database is copied from
`wsgi/myproject/db.sqlite3` with your newly changed login
credentials. Other than the password change, this is the stock
database that is created when `python manage.py syncdb` is run with
only the admin app installed.

On subsequent pushes, a `python manage.py syncdb` is executed to make
sure that any models you added are created in the DB.  If you do
anything that requires an alter table, you could add the alter
statements in `GIT_ROOT/.openshift/action_hooks/alter.sql` and then use
`GIT_ROOT/.openshift/action_hooks/deploy` to execute that script (make
sure to back up your database w/ `rhc app snapshot save` first :) )

You can also turn on the DEBUG mode for Django application using the
`rhc env set DEBUG=True --app APP_NAME`. If you do this, you'll get
nicely formatted error pages in browser for HTTP 500 errors.

Do not forget to turn this environment variable off and fully restart
the application when you finish:

```
$ rhc env unset DEBUG
$ rhc app stop && rhc app start
```

Running on OpenShift
--------------------

Create an account at https://www.openshift.com

Install the RHC client tools if you have not already done so:
    
    sudo gem install rhc
    rhc setup

Select the version of python (2.7 or 3.3) and create a application

    rhc app create django python-$VERSION

Add this upstream repo

    cd django
    git remote add upstream -m master git://github.com/openshift/django-example.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

Now, you have to create [admin account](#admin-user-name-and-password), so you 
can setup your Django instance.
	
That's it. You can now checkout your application at:

    http://django-$yournamespace.rhcloud.com

Admin user name and password
----------------------------
Use `rhc ssh` to log into python gear and run this command:

	python $OPENSHIFT_REPO_DIR/wsgi/myproject/manage.py createsuperuser

You should be now able to login at:

	http://django-$yournamespace.rhcloud.com/admin/
