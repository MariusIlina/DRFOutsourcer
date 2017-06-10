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
3. Open `wsgi/OutSourcer/settings.py` and edit the database settings, so that they correspond to your credentials.
4. Under `wsgi/OutSourcer` directory run the following commands, in this order:


```
python manage.py migrate auth
```
```
python manage.py migrate
```
5. Now run this command and answer the question you are asked .

!!! IMPORTANT - the credentials you set here will be used to authenticate to the admin panel of the application.


```
python manage.py createsuperuser
```

Running the application
===================

Run the test server (will run on port 8000)
```
python manage.py runserver
```
or if you want it to run on a specific port:
```
python manage.py runserver 9999
```

You can now go to `http://localhost:8000` (or whatever port you set).

Here you can see the Graphical User Interface fot the API.

You can also go to the administration panel, located at  `http://localhost:8000/admin` and log in using the credentials that you have earlier set for the superuser.

Using the application
===================

#### Application flow
- `Users` can create `Companies`

- `Companies` can publish `Projects`

- `Companies` can bid on other companies' `Projects`

- `Projects` fall into `Categories`

- `Companies` can add comments about other `Companies` on a `Project`, if the project belongs to the company that is adding the comment

- `Companies` can add recommendations for other companies

#### Business-logic dependencies

Business-logic dependencies are pieces of information needed throughout the application in different logical decisions.

These are set by staff users, not by end-users.

- `Currencies` - are used for determining the money type that is going to be used in a transaction.

- `Time units` - can be any, like for example `hours`, `months`, `weeks`, `days` etc. These are used to determine the desired duration for a project.

- `Payment type` - These tell how the payment for a project is going to be done. Can be something like `hourly`, `monthly`, `weekly`, `daily` etc.

- `Categories` - Used for grouping projects. Can be any.

#### Company location

- `Countries` - A company is based in a country. That's where this is used. Countries are stored in a database table with the same name.

- `Counties` & `Cities` - Used for the same as `Countries`. However they are not stored in the database, at the moment (not implemented yet). They must be provided as strings, from Google Places or other APIs.

#### Users

#### Ownership behaviour







