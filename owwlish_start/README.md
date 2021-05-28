#Owlish Project

### Install virtualenv
<p>Fist of all, you need to install virtualenv to create a virtual environment for libs. The python version used in this</p>
<p>project is Python 3.8. I suggest you  use a version greater than equal to 3.8. To install virtualenv use the command:</p>


```sh
$ sudo apt-get install virtualenv
```

To create a virtual environment, for example with python 3.8 (recommended), use this:
```sh
$ virtualenv --python=python3.8 <your_env_name>
```

Then, active your virtual environment:
```sh
$ source <your_env_name>/bin/activate
```

### Requirements
To install the requirement to run this project:
```sh
$ pip install -r requirements.txt
```

###Database
To create a database for this project, use the following commands:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

<p>To fill database with the csv data (customers.csv), first you will need a Google API key. If you have the key, put in<p/>
<p>owwlish_start/.ini file and run the command:</p>

```sh
$ python manage.py customers_2_db customers.csv
```

PS - The command above can take some minutes, please wait =)
<br>

Finally, you can run a server with the project with the following command:
```sh
$ python manage.py runserver <port>
```

### API
To navigate by the rest API, use:
```sh
http://localhost:<port>/rest
```

### Web Pages:
####Home: 
```sh
http://localhost:<port>
```
####Customers:
```sh
http://localhost:<port>/customers
```

### API Documentation
To navigate by the API Documentation, use:
```sh
http://localhost:<port>/swagger
```

