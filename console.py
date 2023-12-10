#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import re
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


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return ([i.strip(",") for i in split(arg)])
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return (retl)
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return (retl)


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

    def emptyline(self):
        """does nothing on enter"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return (False)

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
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = split(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in globals():
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Deletes a class instance by its id
        Usage: destroy <class> <id>
        """
        args = arg.parse()
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

        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return (False)
        if argl[0] not in globals():
            print("** class doesn't exist **")
            return (False)
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return (False)
        if len(argl) == 2:
            print("** attribute name missing **")
            return (False)
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return (False)

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = split(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
