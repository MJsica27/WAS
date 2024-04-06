<!-- Project Banner -->

<p align="center">
  <img src="https://i.imgur.com/Uk5wTGY.png" alt="Alt text" title="WAS LOGO">
</p>

<!-- Project Title -->

<h1 align="center">WILCATS ACADEMIC SYNC</h1>

<!-- Project Descripton -->

<p align="justify">
  Wildcats Academic Sync or WAS is a user-friendly web application that helps students organize their academic responsibilities effortlessly. With a focus on simplicity, WAS offers the basic CRUD (Create, Read, Update, Delete) functions for managing students' courses with their respective study tasks and grades. Students can easily add, view, update, and delete information related to their studies, allowing them to stay on top of their academic journey. In WAS, We Aim for Success!
</p>

<br>

<!-- Project Table of Contents -->

## Table of Contents
- [Installation](#installation)
- [Running The Project](#running-the-project)
- [Project Info](#project-info)
- [Fixes](#fixes)

<br>

<!-- Project Installation -->
## Installation

#### Download:
1. Download the project by downloading the [ZIP](https://github.com/MJsica27/WAS/archive/refs/heads/main.zip)
2. Extract it and open the project via **[VSCode](https://code.visualstudio.com/)** or **[PyCharm](https://www.jetbrains.com/pycharm/)**
#### Clone:
1. Clone the project by using `git clone` with [Git Bash](https://git-scm.com/downloads):
```
git clone https://github.com/MJsica27/WAS.git
```
2. Open the project via **[VSCode](https://code.visualstudio.com/)** or **[PyCharm](https://www.jetbrains.com/pycharm/)**

<br>

<!-- Project Running -->

## Running the Project

#### Activate Virtual Environment (`activate.bat` File):
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
#### Or Activate without changing directories:
1. Activate the **.bat** file without changing directories:
```
.\venv\Scripts\activate.bat
```
#### Install the Dependencies/Requirements:
1. Go to the **[iMan2Project](https://github.com/MJsica27/WAS/tree/main/iMan2Project)** directory
```
cd iMan2Project
```
2. Install the dependencies/requirements by doing so:
```
pip install -r requirements.txt
```
#### Run the Server:
1. Open your **[Xampp](https://www.apachefriends.org/)**.
2. Start Apache and MySQL.
3. Create a new database named **`was`**; skip this step if you already have the database:
4. Open your terminal and go to the **[iMan2Project](https://github.com/MJsica27/WAS/tree/main/iMan2Project)** directory
```
cd iMan2Project
```
5. Perform migration commands to ensure that the **`was`** database creates/updates tables and matches the models defined in the app:
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

<!-- Project Info -->

## Project Info

#### Languages:

<a href="#languages">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
</a>
<a href="#languages">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
</a>
<a href="#languages">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</a>
<a href="#languages">
    <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
</a>
<a href="#languages">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
</a>

#### Database:
<a href="#database">
    <img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white" />
</a>

#### Tools:

<a href="#tools">
    <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" />
</a>
<a href="#tools">
    <img src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white" />
</a>
<a href="#tools">
    <img src="https://img.shields.io/badge/Xampp-F37623?style=for-the-badge&logo=xampp&logoColor=white" />
</a>
<a href="#tools">
    <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white" />
</a>
<a href="#tools">
    <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" />
</a>

#### Contributors:
  <img src = "https://contrib.rocks/image?repo=MJsica27/WAS"/>

<br>

## Fixes

#### ImportError: No module named 'MySQL'
1. Open `cmd` and run the commands
```
pip install mysql_connector
```
```
pip install mysql
```

#### ImportError: No module named 'Django'
1. Open `cmd` and run the commands
```
pip install django
```