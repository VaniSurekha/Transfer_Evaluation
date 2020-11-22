# Transfer_Evaluation_ Django Backend Environment Set up

Install Python latest version into your system.

Create a virtual environment in the your project root directory by following below steps:

  > pip install virtualenv
  > virtualenv <name_of_env>
 - Now redirect to the path > <name_of_env>\scripts and execute activate.
	> venv\scripts\activate
 
Now, your terminal will directed to virtual environment.

Install required packages for the project using pip install command.
 > pip install <package_name>

and Freeze all the required packages into requirements.txt file using below command:
 > pip freeze >requirements.txt
 
 It will create requirements.txt file in root directory which contains a list of packages along with versions installed.
 
 Run the migrations of db using below command:
  > python manage.py makemigrations
  > python manage.py migrate
 
 Now run the python server:
  > python manage.py runserver
 
 Everything is setup to run Django web environment.
