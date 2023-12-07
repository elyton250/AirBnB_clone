#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models import storage
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
            except NameError:
                print("** class doesn't exist **")
    
    def do_destroy(self, arg):
        """this method destroys an instance"""
    if not arg:
        print("** class name missing **")
        return

    args = arg.split()
    if len(args) < 2:
        print("** instance id missing **")
        return

    cls_name = args[0]
    i_id = args[1]

    all_instances = storage.all()

    for key, value in all_instances.item():
        if instance.id == i_id and instance.__class__.__name__ == cls_name:
            del all_instance[key]
            """print(f"Instance with ID {i_id} in class {cls_name} deleted.")"""
            storage.save()
            return

    if not any(instance.__class__.__name__ == cls_name for instance in BaseModel.instances):
        print("** class doesn't exist **")
        return

    print("** no instance found **")
    storage.save()

    def do_all(self
        
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
