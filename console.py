#!/usr/bin/python3
import cmd, sys, json

class HBNBCommand(cmd.Cmd):
	'''Class HBNB command line console prompt'''
	prompt = '(hbnb) '


	def default(self, line):
		"""default response for unknown commands"""
		pass

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