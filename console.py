#!/usr/bin/python3
"""This is the console for the Holberton HNBN project"""


import cmd
import sys
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class HBNB command line console prompt
       prompt - The start prompt for the HBNB console
       group - contains all the classes used in the project
    """
    prompt = "(hbnb) "
    group = {'BaseModel'}

    def err_mg(self, n):
        """Function to return error messages"""
        msg_dict = {1: "** class name missing **",\
                    2: "** class doesnt't exist**",
                    3: "instance id missing**"
        }
        for key, item in msg_dict.items():
            if key == n:
                print(item)

    def do_create(self, arg):
        """Used to create a new instance of BaseModel and saves
        the instance to a JSON file"""
        if arg == "":
           self.err_mg(1)
        elif arg not in self.group:
            self.err_mg(2)
        else:
            arg = BaseModel()
            arg.save()
            print(arg.id)

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
