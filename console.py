#!/usr/bin/python3
"""This is the console for the Holberton HNBN project"""


import cmd
import sys
import json
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class HBNB command line console prompt
       prompt - The start prompt for the HBNB console
       group - contains all the classes used in the project
    """
    prompt = "(hbnb) "
    group = {'BaseModel'}
    file_path = storage._FileStorage__file_path

    def err_msg(self, n):
        """Function to return error messages"""
        msg_dict = {1: "** class name missing **",
                    2: "** class doesn't exist **",
                    3: "** instance id missing **",
                    4: "** no instance found **"
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
            arg = BaseModel()
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
