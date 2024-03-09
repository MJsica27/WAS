<p align="center">
  <img src="https://i.imgur.com/zMWjD2l.png" alt="Alt text" title="WAS LOGO">
</p>

# WAS (Wildcats Academic Sync)
Wildcats Academic Sync or WAS is a user-friendly web application that helps students organize their academic responsibilities effortlessly. With a focus on simplicity, WAS offers the basic CRUD (Create, Read, Update, Delete) functions for managing student's courses with their respective study tasks and grades. Students can easily add, view, update, and delete information related to their studies, allowing them to stay on top of their academic journey.

In WAS, We Aim for Success!

<br>

## Downloading/Cloning the Project
### Download:
1. Download the project by downloading the Zip file
2. Extract it and open the project via **VSCode** or **PyCharm**
### Clone:
1. Clone the project by using `git clone` through git bash
```
git clone https://github.com/MJsica27/WAS.git
```
2. Open the project via **VSCode** or **PyCharm**

<br>

## Activating the Virtual Environment (`activate.bat` File)
1. Go to the **Scripts** directory
```
cd venv
```
```
cd Scripts
```
2. Activate the **.bat** file
```
.\activate.bat
```
**OR**
1. Activate the **.bat** file without changing directories
```
.\venv\Scripts\activate.bat
```

<br>

## Running the Server
1. Open your **Xampp** and start the database
> Assuming that you already have a database named **was** and migrated
2. Go to the **iMan2Project** directory
```
cd iMan2Project
```
3. Run the server
```
py manage.py runserver
```

<br>

## Other Info

| Softwares Used: | | | 
| ------ | ------- | ------ |
| IDE: | [PyCharm](https://www.jetbrains.com/pycharm/) | [VSCode](https://code.visualstudio.com/) | 

| Database | |
| ------ | ------ | 
| **DBMS:** | MySQL (managed with [XAMPP](https://www.apachefriends.org/)) |
| **Database Name:** | was |

<br>

## Fixes
### ImportError: No module named 'MySQL'
1. Open `cmd` and run the commands
  ```
  pip install mysql_connector
  ```
  ```
  pip install mysql
  ```

### ImportError: No module named 'Django'
1. Open `cmd` and run the commands
  ```
  pip install django
  ```
