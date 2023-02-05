# ReMoodWork by Peter Ossipov
Project that I'm doing for CPSC 597

# Steps to install and run a server of my software application
Dependency frameworks and tools to run this application: 
* Python 3.10.6 (Might work with the early versions of Python such as 3.7 or higher)
* Django 4.1.5 (Might work with the early versions of Django) 
* SQLite (Database)
* HTML and I think CSS
# Instructions to set up and install Django on a virtual envrionment (Note that this done on an Ubuntu virtual machine environment)
1. Create a Python virtual environment
```python3 -m venv my-django-env```  
Or whatever virtual environment you want to name as...  
2. Once the virtual environment set up is finished, then activate its current environment of Python by using this command
```source my-django-env/bin/activate```  
3. Check for a Python version:
```python --version```
4. Check which Python the environment is using: 
```which python```
5. Deactivate virtual current environment of Python:
```deactivate```
6. Check which pip or pip3 the environment is using: 
```which pip3```
7. Installing other modules/libraries (such as Django) of a current Python virtual environment using requirements.txt found in this project repository (More will be added later this semester)  
a. ```pip install -r requirements.txt```
8. Lists all of the modules/libraries and their versions used in the current virtual environment of Python:  
* ```pip freeze```
* ```pip freeze --local```  
9. Create requirements.txt as a redirect output source file (in case of a copy):
```pip freeze --local > requirements.txt```

# Instructions on executing Django commands
1. Check the current version of Django: 
```python -m django --version```
2. List all of the commands of Django:
```django-admin```
3. Check for the content help based on the given command in Django: 
```django-admin help <django command>``` (Like startproject)
4. Run the Django server of remoodwork (Project Name) project:  
* ```python3 manage.py runserver```
* [Alternative to run a server on a PyCharm IDE](https://www.youtube.com/watch?v=WluSpfSMj2Y)

# List of URL path names used in this project (URL route paths will be modified later this semester)
Main Home page of the website: ```http://127.0.0.1:8000/```   
Future Pulse Survey page of the website for my first milestone: ```http://127.0.0.1:8000/pulsesurvey/```  
Django Admin Page: ```http://127.0.0.1:8000/admin``` (after a superuser has been created)  
User registration page for employees/employers: ```http://127.0.0.1:8000/register/```  


# Migration commands in Django 
First run command to add a new database table or to modify and update fields of an existing database table  
```python manage.py makemigrations```  
Second, write a command to apply or unapply migration changes happening in a database table  
```python manage.py migrate```  
Optionally display an SQL statement for a database migration in Django 
```python manage.py sqlmigrate```  

# Run a shell console of Django to do some operations and play around with other objects in the project
```python manage.py shell```  


