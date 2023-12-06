#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Represents command interpreter"""
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Exits the program"""
        return (True)

    def do_EOF(self, arg):
        """Exit the program (Ctrl-D)"""
        print()
        return (True)
    def do_help(self, arg):
        """Documented commands (type help <topic>):
        ========================================"""
        super().do_help(arg)
        

    def emptyline(self):
        """does nothing on enter"""
        pass

    def do_create(self, arg):
        """ create commad to Creates 
        a new instance of a class and prints its id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                cls_name = arg.split()[0]
                new_instance = globals()[cls_name]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        arguments = arg.split()

        if not arguments:
            print("** class name missing **")

        else:
            cls_name = arguments[0]

            if cls_name not in globals():
                print("** class doesn't exist **")

            if len(arguments) < 2:
                print("** instance id missing **")

            else:
                instance_id = arguments[1]
                key = "{}.{}".format(cls_name, instance_id)
                all_objects = FileStorage().all()
                if key in all_objects:
                    print(all_objects[key])
                else:
                    print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
