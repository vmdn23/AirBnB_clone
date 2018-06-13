# 0x00. AirBnB clone - The console
![Image of Holberton B&B Logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

## Airbnb Clone - Command Interpreter Project Description
### This is the first of a multipart project working towards building a full web application clone of AirBnb. In this first part, the Python programming language is used to build a command interpreter for the clone's web app. This command interpreter is similar to a BASH shell but it is designed for a specific use case. The following projects will incorporate additional sections like HTML/CSS templating, database storage, API and front-end integration.

## How to start the interpreter
### In the command line run `./console.py` or `echo help | ./console.py`

## Usage
### This interpreter has basic console commands such as EOF, quit, help, create, destroy, update, show, and all.

Command | Syntax | Output
------- | ------ | ------
help | `help *[option]*` | Lists all available commands, or displays what option does
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter
create | `create *[class_name]*` | Creates an instance of class_name
update | `update *[class_name] [object_id] [update_key] [update_value]*` | Updates the key:value of class_name.object_id instance
show | `show *[class_name] [object_id]*` | Displays all attributes of class_name.object_id
all | `all *[class_name]*` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy *[class_name] [object_id]*` | Deletes all attributes of class_name.object_id

### Files
File Name | Description
--- | ---
`models/base_model.py` | Base Class with public instance attributes and methods
`models/user.py` | A user class that inherits from BaseModel
`tests/test_models/` | Unittests for BaseModel, User, amenity, city, place, review, and state
`tests/test_models/test_engine/` | Unittest for file storage

## Example Usage
```python3
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
[]
(hbnb) create User
5426ec97-ad7e-49a5-8540-8e09253de2ef
(hbnb) show User 5426ec97-ad7e-49a5-8540-8e09253de2ef
[User] (5426ec97-ad7e-49a5-8540-8e09253de2ef) {'id': '5426ec97-ad7e-49a5-8540-8e09253de2ef', 'updated_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583799), 'created_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583728)}
(hbnb) update User 5426ec97-ad7e-49a5-8540-8e09253de2ef 'name' 'Holberton'
(hbnb) show User 5426ec97-ad7e-49a5-8540-8e09253de2ef
[User] (5426ec97-ad7e-49a5-8540-8e09253de2ef) {'updated_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583799), "'name'": "'Holberton'", 'id': '5426ec97-ad7e-49a5-8540-8e09253de2ef', 'created_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583728)}
(hbnb) create Place
8ae17ae8-99f3-4c7b-a89e-353b943b0bfb
(hbnb) show Place 8ae17ae8-99f3-4c7b-a89e-353b943b0bfb
[Place] (8ae17ae8-99f3-4c7b-a89e-353b943b0bfb) {'id': '8ae17ae8-99f3-4c7b-a89e-353b943b0bfb', 'updated_at': datetime.datetime(2018, 6, 13, 16, 50, 52, 637387), 'created_at': datetime.datetime(2018, 6, 13, 16, 50, 52, 637328)}
(hbnb) all
[Place] (8ae17ae8-99f3-4c7b-a89e-353b943b0bfb) {'id': '8ae17ae8-99f3-4c7b-a89e-353b943b0bfb', 'updated_at': datetime.datetime(2018, 6, 13, 16, 50, 52, 637387), 'created_at': datetime.datetime(2018, 6, 13, 16, 50, 52, 637328)}
[User] (5426ec97-ad7e-49a5-8540-8e09253de2ef) {'updated_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583799), "'name'": "'Holberton'", 'id': '5426ec97-ad7e-49a5-8540-8e09253de2ef', 'created_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583728)}
(hbnb) all User
[User] (5426ec97-ad7e-49a5-8540-8e09253de2ef) {'updated_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583799), "'name'": "'Holberton'", 'id': '5426ec97-ad7e-49a5-8540-8e09253de2ef', 'created_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583728)}
(hbnb) all Place
[Place] (8ae17ae8-99f3-4c7b-a89e-353b943b0bfb) {'id': '8ae17ae8-99f3-4c7b-a89e-353b943b0bfb', 'updated_at': datetime.datetime(2018, 6, 13, 16, 50, 52, 637387), 'created_at': datetime.datetime(2018, 6, 13, 16, 50, 52, 637328)}
(hbnb) destroy Place 8ae17ae8-99f3-4c7b-a89e-353b943b0bfb
(hbnb) all
[User] (5426ec97-ad7e-49a5-8540-8e09253de2ef) {'updated_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583799), "'name'": "'Holberton'", 'id': '5426ec97-ad7e-49a5-8540-8e09253de2ef', 'created_at': datetime.datetime(2018, 6, 13, 16, 42, 32, 583728)}
(hbnb)
```

### About
This project was created by [Adekunle Adeniran](https://github.com/flourishcodes) and
[Victor Nguyen](https://github.com/vmdn23) at [Holberton
School](http://holbertonschool.com).
