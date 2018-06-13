# 0x00. AirBnB clone - The console
![Image of Holberton B&B Logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

## Airbnb Clone - Command Interpreter Project Description
### This is the first of a multipart project working towards building a full web application clone of AirBnb. In this first part, the Python programming language is used to build a command interpreter for the clone's web app. This command interpreter is similar to a BASH shell but it is designed for a specific use case. The following projects will incorporate additional sections like HTML/CSS templating, database storage, API and front-end integration.

## How to start the interpreter
### In the command line run `./console.py` or `echo help | ./console.py`

## Usage
### This interpreter has basic console commands such as EOF, quit, help, create, destroy, update, show, count and all.

## Command Sytax and Usage:

Command | Syntax | Output
------- | ------ | ------
help | `help *[option]*` | Lists all available commands, or displays what option does
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter
create | `create [class_name]` or `[class_name].create()`| Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]` or  `[class].update([object_id] [update_key] [update_value]()`| Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` or `[class_name].show([object_id])()` | Displays all attributes of class_name.object_id
all | `all [class_name]`, `[class_name].all()` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()` | Deletes all attributes of class_name.object_id
count | `count [class_name]` or `[class_name].count()`| Counts all the instances with class name specified


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
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb) help quit
Quit command to exit the program
(hbnb)
(hbnb) show User
** instance id missing **
(hbnb) show User (24ed1cb3-8f8a-4081-878e-60fdce47a42d)
** no instance found **
(hbnb) show User 24ed1cb3-8f8a-4081-878e-60fdce47a42d
[User] (24ed1cb3-8f8a-4081-878e-60fdce47a42d) {'password': 'root', 'last_name': 'Holberton', 'created_at': datetime.datetime(2018, 6, 12, 13, 7, 27, 53126), 'updated_at': datetime.datetime(2018, 6, 12, 13, 7, 27, 53158), 'email': 'airbnb@holbertonshool.com', 'id': '24ed1cb3-8f8a-4081-878e-60fdce47a42d', 'first_name': 'Betty'}
(hbnb)
(hbnb) User.show(24ed1cb3-8f8a-4081-878e-60fdce47a42d)
[User] (24ed1cb3-8f8a-4081-878e-60fdce47a42d) {'password': 'root', 'last_name': 'Holberton', 'created_at': datetime.datetime(2018, 6, 12, 13, 7, 27, 53126), 'updated_at': datetime.datetime(2018, 6, 12, 13, 7, 27, 53158), 'email': 'airbnb@holbertonshool.com', 'id': '24ed1cb3-8f8a-4081-878e-60fdce47a42d', 'first_name': 'Betty'}
(hbnb)
(hbnb) User.count()
12
(hbnb) Amenity.show()
** instance id missing **
(hbnb) Amenity.show(58ceeeb9-7a28-4554-af76-f5dff402be70)
[Amenity] (58ceeeb9-7a28-4554-af76-f5dff402be70) {'id': '58ceeeb9-7a28-4554-af76-f5dff402be70', 'created_at': datetime.datetime(2018, 6, 13, 13, 57, 34, 149032), 'updated_at': datetime.datetime(2018, 6, 13, 13, 57, 34, 149117)}
(hbnb) User.show(deaf744b-c904-4b56-8823-71acc18a529c)
[User] (deaf744b-c904-4b56-8823-71acc18a529c) {'created_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138370), 'updated_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138489), 'id': 'deaf744b-c904-4b56-8823-71acc18a529c', 'first_name': 'Ben'}
(hbnb) User.update("deaf744b-c904-4b56-8823-71acc18a529c", 'first_name', "Bimpe")
(hbnb) User.show(deaf744b-c904-4b56-8823-71acc18a529c)
[User] (deaf744b-c904-4b56-8823-71acc18a529c) {'created_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138370), 'updated_at': datetime.datetime(2018, 6, 13, 9, 16, 53, 138489), 'id': 'deaf744b-c904-4b56-8823-71acc18a529c', 'first_name': 'Bimpe'}
(hbnb)
```

### About
This project was created by [Adekunle Adeniran](https://github.com/flourishcodes) and
[Victor Nguyen](https://github.com/vmdn23) at [Holberton
School](http://holbertonschool.com).