<p align="center">
  <img src="https://i.imgur.com/zMWjD2l.png" alt="Alt text" title="WAS LOGO">
</p>

<h2 align='center'>WAS<br><sub align='center'>(Wildcats Academic Sync)</sub></h2>
<br>
Wildcats Academic Sync or WAS is a user-friendly web application that helps students organize their academic responsibilities effortlessly. With a focus on simplicity, WAS offers the basic CRUD (Create, Read, Update, Delete) functions for managing student's courses with their respective study tasks and grades. Students can easily add, view, update, and delete information related to their studies, allowing them to stay on top of their academic journey.

In WAS, We Aim for Success!

<br>

<h2 align='center'>💻 Downloading/Cloning the Project</h2>
<br>

### Download:
1. Download the project by downloading the Zip file
2. Extract it and open the project via **[VSCode](https://code.visualstudio.com/)** or **[PyCharm](https://www.jetbrains.com/pycharm/)**
### Clone:
1. Clone the project by using `git clone` with [Git Bash](https://git-scm.com/downloads):
```
git clone https://github.com/MJsica27/WAS.git
```
2. Open the project via **[VSCode](https://code.visualstudio.com/)** or **[PyCharm](https://www.jetbrains.com/pycharm/)**

<br>

<h2 align='center'>💻 Running the Project</h2>
<br>

### Activate the Virtual Environment (`activate.bat` File):
1. Go to the **[Scripts](https://github.com/MJsica27/WAS/tree/main/venv/Scripts)** directory:
```
cd venv
```
```
cd Scripts
```
2. Activate the **.bat** file:
```
.\activate.bat
```
**OR**
1. Activate the **.bat** file without changing directories:
```
.\venv\Scripts\activate.bat
```
### Install the Dependencies/Requirements:
1. Go to the **[iMan2Project](https://github.com/MJsica27/WAS/tree/main/iMan2Project)** directory
```
cd iMan2Project
```
2. Install the dependencies/requirements by doing so:
```
pip install -r requirements.txt
```
### Run the Server:
1. Open your **[Xampp](https://www.apachefriends.org/)**.
2. Start Apache and MySQL.
3. Create a new database named **was**; skip this step if you already have the database:
4. Open your terminal and go to the **[iMan2Project](https://github.com/MJsica27/WAS/tree/main/iMan2Project)** directory
```
cd iMan2Project
```
5. Perform migration commands to ensure that the **was** database creates/updates tables and matches the models defined in the app:
```
py manage.py makemigrations
```
```
py manage.py migrate           
```
6. Run the server:
```
py manage.py runserver
```

<br>

<h2 align='center'>💻 Project Info</h2>
<br>

| Softwares Used: | | | 
| ------ | ------- | ------ |
| IDE: | [PyCharm](https://www.jetbrains.com/pycharm/) | [VSCode](https://code.visualstudio.com/) | 

| Database | |
| ------ | ------ | 
| **DBMS:** | MySQL (w/ [XAMPP](https://www.apachefriends.org/)) |
| **Database Name:** | was |

<br>

<h2 align='center'>💻 Fixes</h2>
<br>

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