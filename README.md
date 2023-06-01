# ReMoodWork by Peter Ossipov
# Installation  Instructions
This project provides steps to install other software applications and module libraries shown below: 
1.	Download the project’s zip folder and extract all contents of the project folder to your local directory.
2.	Install Python 3.10.6 or higher [Python download](https://www.python.org/downloads/)
3.	After placing the project folder in your local directory, there are a couple of instructions to install modules or dependencies needed for running the project (Note that my-django-env is used an example to set up a virtual environment in Python).  
a. After installing Python to your OS drive (Windows, Ubuntu, Mac, etc.), go to “ReMoodWork-master” folder using a terminal (highly recommend Ubuntu Linux) or an IDE environment (highly recommend PyCharm) and began creating a Python virtual environment name of your choice using this command in the terminal:  
•	```python3 -m venv my-django-env```  
b.	Once the virtual environment set up is finished, then activate its current environment of Python by using this command in the terminal:   
•	```source my-django-env/bin/activate``` 
c.	Check for a Python version in the terminal: ```python --version```  
d.	Use the ```deactivate``` command if you want to shut off your current virtual environment of Python in the terminal.  
e.	Install other modules/libraries (It includes Django and is required to run the ReMoodWork server) of a current Python virtual environment using requirements.txt found in this command in the terminal: ```pip install -r requirements.txt```  
f.	Lists all of the modules/libraries and their versions used in the current virtual environment of Python in the terminal:  
•	```pip freeze```  
•	```pip freeze --local```  
g.	After installing the necessary modules/libraries found from requirements.txt, reactivate your Python virtual environment: source my-django-env/bin/activate and check the current version of Django using this command in the terminal:  
•	```python -m django --version```  
h.	Once you have Django installed to the project, then follow the rest of the steps to complete installing parts and components of Django shown below:  
I.	Execute this command that changes from “ReMoodWork-master” directory to “remoodwork” directory in the terminal: ```cd remoodwork/```  
II.	Execute ```python manage.py makemigrations``` command to install db.sqlite3 (Note that SQLite is a required database needed in this project) in the terminal.   
III.	Execute ```python manage.py migrate command``` to install and load database models of Django and ReMoodWork in the terminal.  
IV.	Run the Django server of ReMoodWork (Project Name) project using this command: ```python manage.py runserver```  to launch the website in the terminal.  
o	You can also run the server with PyCharm IDE through this link: [PyCharm configuration setup] https://www.youtube.com/watch?v=WluSpfSMj2Y 

# Operating  Instructions  
This section provides Django commands that are helpful to use in this project, shown below:  
A.	(Optional) Show a list of url routes of ReMoodWork using this command:  
•	```python manage.py show_urls | grep 'remoodwork'```  
B.	(Optional but highly recomended) Create an admin using this command:   
•	```python manage.py createsuperuser```  
•	Tutorial Reference: [Django tutorial](https://docs.djangoproject.com/en/1.8/intro/tutorial02/)  
C.	Run test command to evaluate ReMoodWork used through Django (must perform in “remoodwork” directory):   
•	Run all tests of ReMoodWork applications (users, workrecords, etc.):  
	```python manage.py test .```  
•	Run all tests of ReMoodWork’s users applications:  
	```python manage.py test users```  
•	Run all tests of ReMoodWork’s workrecords applications:  
	```python manage.py test workrecords```  
•	Run individual test script file of ReMoodWork’s workrecords applications:   
	```python manage.py test workrecords.tests.<test_script>```  
•	Run individual test script file of ReMoodWork’s users applications:   
	```python manage.py test users.tests.<test_script>```  
•	Run individual test script file of an application name in ReMoodWork:  
	```python manage.py test <app_name>.tests.<test_script>```  
