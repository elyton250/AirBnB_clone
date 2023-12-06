#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    def help_introduction(self):
        print("This is the cmd prompt for the AirBnB clone")
    def emptyline(self):
        passs
    def preloop(self):
        print("(hbnb)")
    def postcmd(self, stop, line):
        if line.lower() == 'quit'
            return true
        return false
