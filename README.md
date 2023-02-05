ToDoList Application
A simple task management system built with Django web framework. With this application, you can create, edit, delete, and complete tasks and categories.

Requirements <br>
Django (3.1 or later)<br>
Python (3.7 or later)<br><br>
Installation<br>
Clone the repository to your local machine:


'''
git clone https://github.com/[YOUR_GITHUB_USERNAME]/ToDoList.git 
'''''<br><br>
Install the required packages:

pip install -r requirements.txt<br><br>
Run the following command to apply the database migrations:


python manage.py migrate<br><br>
Start the development server:


python manage.py runserver<br>
You can now access the application at http://localhost:8000/

Usage<br>
Tasks<br>
You can view all the tasks by clicking on the 'Tasks' link in the navigation bar.<br>
You can add a new task by clicking on the 'Add Task' button.<br>
You can edit an existing task by clicking on the 'Edit' button next to the task.<br>
You can delete a task by clicking on the 'Delete' button next to the task.<br>
You can mark a task as complete by clicking on the 'Mark as Complete' button next to the task.<br><br>
Categories<br>
You can view all the categories by clicking on the 'Categories' link in the navigation bar.<br>
You can add a new category by clicking on the 'Add Category' button.<br>
You can edit an existing category by clicking on the 'Edit' button next to the category.<br>
You can delete a category by clicking on the 'Delete' button next to the category.<br><br>

The ToDoList application was developed using the Django web framework, which is written in Python. HTML, CSS and JavaScript were also used for front-end development. The database used is SQLite, which is integrated into Django.
