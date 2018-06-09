#!/usr/bin/python3
"""This is the console for the Holberton HNBN project"""


import cmd
import sys
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class HBNB command line console prompt"""
    prompt = "(hbnb) "
    group = {'BaseModel'}

    def do_create(self, arg):
        """Used to create a new instance of BaseModel and saves
        the instance to a JSON file"""
        if arg == "":
            print("** class name missing **")
        elif arg not in self.group:
            print("** class doesn't exist **")
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
