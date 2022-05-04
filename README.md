# Resource-Portal

This is a Resource Portal for College to encourage sharing of resources like notes, books, etc. online by the teachers to the students.

## Table of Contents

1. [Features](#features)
2. [Technology Stack to be used](#technology-stack-to-be-used)
3. [Getting Started](#getting-started)
	1. [Fork, clone locally and create a branch](#fork-clone-locally--create-a-branch)
	1. [Setting Environment First Time](#setting-environment-first-time)
		1. [Basic Requirements](#basic-requirements)
		1. [Creating Virtual Environment](#creating-virtual-environment)
		1. [Installing Requirements](#installing-requirements)
		1. [Migrating Database](#migrating-database)
		1. [Create Superuser](#create-superuser)
	1. [Starting Development Server](#starting-development-server)
	1. [Leaving the virtual environment](#leaving-the-virtual-environment)
	1. [Update requirements file](#update-requirements-file-critical)
	1. [Update Database](#update-database)  
4. [Maintainers](#maintainers)

## Features

1. Different entity portal (student, teacher).
2. Add individual resources for each year, department, etc.
3. View list of uploaded notes, assignments, books, etc.
4. Filter resources based on department, year and resource type.
5. Mark favourites or save resources from list of uploaded one.
6. Able to download existing resources.
7. User can add his/her profile details.
8. Login/Sign Up.
 
## Technology Stack to be used:

<img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> 
<img src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> 
<img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/>
<img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/> 
<img src="https://img.shields.io/badge/postgres-0B96B2?style=for-the-badge&logo=postgresql&logoColor=white"/> 
<img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white"/>


- **Frontend**: HTML, CSS
- **Backend**: Django
- **IDE**: VS Code
- **API Testing & Documentation**: Postman
- **Version Control**: Git and GitHub
- **Database**: PostgreSQL
- **Hosting**: Heroku

## Getting Started

### Fork, clone locally & create a branch

Fork [Resource-Portal](https://github.com/todi-2000/Resource-Portal) repository and clone at your local 

- Fork and Clone the repo using
```
$ https://github.com/todi-2000/Resource-Portal.git
```

### Setting Environment First Time

#### Basic Requirements 
1. [Python](https://www.python.org/downloads/)
1. [pip](https://pip.pypa.io/en/stable/installation/)

#### Creating [Virtual Environment](https://docs.python.org/3/library/venv.html) 

A virtual environment is a tool that helps keep dependencies required and the project isolated. If you wish to install a new library and write
```
pip install name_of_library
``` 
on the terminal without activating an environment, all the packages will be installed globally which is not a good practice if you’re working with different projects on your computer.

If this sounds a bit complicated, don’t worry so much because a virtual environment is just a directory that will contain all the necessary files for our project to run.

**Installing venv (required once)**

**Windows**
```
py -m pip install --user virtualenv
py -m venv env
```
**Linux**
```
python3 -m pip install --user virtualenv
python3 -m venv env
```

You have to start virtual environment everytime you start new terminal -

**Windows**

Using gitbash
```
. env/Scripts/activate
```
Using Powershell
```
. env\Scripts\activate
```
**Linux**
```
source env/bin/activate
```

#### Installing Requirements 

**Windows**
```
pip install -r requirements.txt
```
**Linux**
```
pip3 install -r requirements.txt
```

#### Migrating Database
**Windows**
```
py manage.py migrate
```
**Linux**
```
python3 manage.py migrate
```

#### Create Superuser
**Windows**
```
py manage.py createsupeser
```
**Linux**
```
python3 manage.py createsupeser
```

### Starting Development Server
**Windows**
```
py manage.py runserver
```
**Linux**
```
python3 manage.py runserver
``` 

### Leaving the virtual environment
```
deactivate
```

### Update requirements file (Critical)
If you have installed new dependency, the pip freeze command lists the third-party packages and versions installed in the environment. 

**Windows**
```
pip freeze > requirements.txt
```
**Linux**
```
pip3 freeze > requirements.txt
```

### Update Database  
Everytime you change db models, you need to run makemigrations and migrate to update on database.

**Windows**
```
py manage.py makemigrations
py manage.py migrate
```
**Linux**
```
python3 manage.py makemigrations
python3 manage.py migrate
``` 

## Maintainers✨

<table>
  <tbody><tr>
    <td align="center"><a href="https://github.com/todi-2000"><img alt="" src="https://avatars.githubusercontent.com/todi-2000" width="100px;"><br><sub><b>Manshi Todi</b></sub></a><br><a href="https://github.com/todi-2000/Resource-Portal/commits/master?author=todi-2000" title="Code">💻</a></td>
  </tr>
</tbody></table>

[![Uses Git](https://forthebadge.com/images/badges/uses-git.svg)](https://github.com/todi-2000/Resource-Portal) [![Uses HTML](https://forthebadge.com/images/badges/uses-html.svg)](https://github.com/todi-2000/Resource-Portal) [![Uses CSS](https://forthebadge.com/images/badges/uses-css.svg)](https://github.com/todi-2000/Resource-Portal) [![Uses JS](https://forthebadge.com/images/badges/uses-js.svg)](https://github.com/todi-2000/Resource-Portal)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/todi-2000/Resource-Portal)
[![Built with love](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/todi-2000/Resource-Portal) [![Built By Developers](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/todi-2000/Resource-Portal) 
