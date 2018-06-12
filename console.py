#!/usr/bin/python3
"""This is the console for the Holberton HNBN project"""


import cmd
import sys
import json
import models
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class HBNB command line console prompt
       prompt - The start prompt for the HBNB console
       group - contains all the classes used in the project
    """
    prompt = "(hbnb) "
    group = {'BaseModel', 'User'}
    file_path = storage._FileStorage__file_path

    def err_msg(self, n):
        """Function to return error messages"""
        msg_dict = {1: "** class name missing **",
                    2: "** class doesn't exist **",
                    3: "** instance id missing **",
                    4: "** no instance found **",
                    5: "** attribute name missing **",
                    6: "** value missing **"
                    }
        for key, item in msg_dict.items():
            if key == n:
                print(item)

    def do_create(self, arg):
        """Used to create a new instance of BaseModel and saves
        the instance to a JSON file"""
        if arg == "":
            self.err_msg(1)
        elif arg not in self.group:
            self.err_msg(2)
        else:
            arg = eval(arg)()
            arg.save()
            print(arg.id)

    def do_show(self, line):
        """Function to print string representation of instance"""
        arg = line.split()
        if line == "":
            self.err_msg(1)
        elif arg[0] not in self.group:
            self.err_msg(2)
        elif len(arg) < 2:
            self.err_msg(3)
        else:
            data_dump = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            try:
                obj = data_dump[key]
                print(obj)
            except KeyError:
                self.err_msg(4)

    def do_destroy(self, line):
        """Function to print string representation of instance"""
        arg = line.split()
        if line == "":
            self.err_msg(1)
        elif arg[0] not in self.group:
            self.err_msg(2)
        elif len(arg) < 2:
            self.err_msg(3)
        else:
            data_dump = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in data_dump:
                    del data_dump[key]
                    storage._FileStorage__objects = data_dump
                    storage.save()
                    return
            self.err_msg(4)

    def do_all(self, line=""):
        """Function that displays all class instances of given argument or all
        if no argument given"""
        data_dump = models.storage.all()
        if line is "":
            for instance_key, instance_obj in data_dump.items():
                print(instance_obj)
        else:
            arg = line.split()
            if arg[0] not in self.group:
                self.err_msg(2)
            else:
                for instance_key, instance_obj in data_dump.items():
                    obj = instance_obj.to_dict()
                    if obj['__class__'] == arg[0]:
                        print(instance_obj)

    def splitter(self, line):
        """Function to split line into arguments using shlex"""
        lex = shlex.shlex(line)
        lex.quotes = '"'
        lex.whitespace_split = True
        lex.commenters = ''
        return list(lex)

    def do_update(self, line=""):
        """Updates an instance based on the class name and id by adding or
        updating attribute and save the change into the JSON file"""
        data_dump = models.storage.all()
        arg = self.splitter(line)

        if not line:
            self.err_msg(1)
        elif arg[0] not in self.group:
            self.err_msg(2)
        elif len(arg) < 2:
            self.err_msg(3)
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in data_dump:
                if len(arg) < 3:
                    self.err_msg(5)
                elif len(arg) < 4:
                    self.err_msg(6)
                else:
                    obj = data_dump[key]
                    setattr(obj, arg[2], arg[3])
            else:
                self.err_msg(4)

    def emptyline(self):
        """Called when an empty line is entered
        Prints the prompt again
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Executes the EOF (Ctrl -D/ Ctrl-Z) commands on console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
