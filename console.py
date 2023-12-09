#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from shlex import split
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.__init__ import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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

        """(type help <topic>):
        ========================"""
        super().do_help(arg)

    def emptyline(self):
        """does nothing on enter"""
        pass

    def do_create(self, arg):
        """Create a new class instance and print its id
        Usage: create <class>
        """
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
        """Prints the string representation of an instance.
        Usage: show <class> <id> or <class>
        """
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

    def do_destroy(self, arg):
        """Deletes a class instance by its id
        Usage: destroy <class> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            idd = args[1]
            key_to_del = "{}.{}".format(cls_name, idd)
            all_objects = FileStorage().all()
            if key_to_del not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[key_to_del]
                storage.save()

    def do_all(self, arg):
        """this prints a string represantation of an instance"""
        argl = split(arg)
        if len(argl) > 0 and argl[0] not in globals():
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        Usage: update <class name> <id>
        <attribute name> "<attribute value>" """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(cls_name, instance_id)
        all_objects = FileStorage().all()

        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]
        attr_value = self.cast_type(attr_value)

        if attr_name not in ["id", "created_at", "updated_at"]:
            setattr(all_objects[key], attr_name, attr_value)
            FileStorage().save()

    @staticmethod
    def cast_type(attr_value):
        """Convert attr_value to the
        appropriate type by trying multiple types"""
        try:
            for data_type in [int, float, HBNBCommand.cast_bool]:
                attr_value = data_type(attr_value)
                return (attr_value)
        except (ValueError, TypeError):
            return (attr_value)

    @staticmethod
    def cast_bool(value):
        """Converts a string to boolean."""
        if value.lower() in ['true', '1']:
            return (True)
        elif value.lower() in ['false', '0']:
            return (False)
        else:
            raise ValueError("Invalid boolean value")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
