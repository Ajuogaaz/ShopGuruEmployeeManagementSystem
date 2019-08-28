# Shop Guru Employee Management System
__This is a Python web application in Flask using jinja2 template and Postgresql__ that will help administrators manage employees in an ecommerce startup, Shop Guru __by__ [Linus Brian Okoth](https://github.com/Ajuogaaz)

## Getting Started ##
These instructions will get you a copy of the project up and running on your local machine for development.

## Set Up/ Installation Requirements. ##
* A PC mainly with an Operating system.
* Python3.6 or later is installed in your PC.
* Postgresql installed
* Clone the directory into your local machine
* Navigate to the cloned folder by ```cm ShopGuruEmployeeManagementSystem ```
* Create a virtual environment
* Run source virtual/bin/activate
* Install Flask ``` pip install flask=1.11 ```
* Install SQLAlchemy ``` pip install Flask-SQLAlchemy ```
* Install psycopgy2 ``` pip install psycopgy2 ```  
* pip install ``` requirements.txt ```
* run python3.6 manage.py runserver
* The application should work
* For the test run python ``` main.py ``` test the app

## Known Bugs ##
No known bugs. If you run into any kindly contact [Developer](brianlinus1753@gmailcom)

## Behavior Driven Development ##

| __Behavior__ | __Input Example__ | __Output Example__ |
| --- | --- | --- |
| The user should see the landing page on first sight | [www.ShopGuruEmployeeManagementSystem.com](https://shop-guru.herokuapp.com/) | Home 
| The application should provide an option to register or login to the app | login/register | true |
| The application should authenticate Users base on details the user provides | password/username | Access or No access |
| The user should be redirected to home page once logged in | access | Homepage |
| The user should be able to view existing departments | --- | departments |
| The application should restrict addition of other departments from unauthorized users | denied | redirect back to department page |
| The user should be able to view emloyees and their related data | --- | employees |
| The application should allow authorized users to edit, delete or add employees | edit/delete/add | database altered succesfully |
| You should be able to give instructions to generate chats to display different aspects of the database | --- | pygal charts |
| Produce Payslips for different employees | generate | Payslip Pdf |
| The user should be able to logout at will | logout | True |

## Technologies Used ##
### Main Languages Used ###
- Python
- Material design
- Flask
- Amazon s3
- JavaScript
- CSS
- Bootstrap
- PostgreSQL Database 

## Support Contact ##
__Contact__ [Linus Brian Okoth](brianlinus1753@gmail.com)
