#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
Class_Dict = {"BaseModel": BaseModel, "User": User, "City": City, "Place": Place: "Review": Review, "State": State, "Amenity": Amenity}

"""Command interprater that uses quit and EOF to exit the program, help and an empty line that does not execute anything.
"""
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    classes = {"BaseModel": BaseModel, "User": User, "City": City, "Place": Place: "Review": Review, "State": State, "Amenity": Amenity}

    """Question 7"""

    def do_create(self, args):
        """Creates new instance of BaseModel and saves to JSON"""
        if not args:
            print("** class name missing **")
        elif args not in Class_Dict:
            print("** class doesn't exist **")
        else:
            """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
            for key, value in Class_Dict.items():
                if key == args:
                    new_instance = Class_Dict[key]()
                    storage.save()
                    print(new_instance.id)
    
    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        elif class_name not in Class_Dict:
            print("** class doesn't exist **")
        """
        
        Do show not done

        """
    def do_destroy(self, args):
        """
        Not done
        """

    def all(self, args):
        """Prints all string representation of all instances"""
        if args is not Class_Dict:
            print("** class doesn't exist **")
        else:
            """Print the string representation"""

    def update(self):
        """
        Not done
        """
        pass

    """Question 6"""
    def do_quit(self, args):
        """Quits program"""
        exit()
    
    def do_EOF(self, args):
        """Quits program"""
        print()
        exit()

    def do_help(self, args):
        """Help"""
        cmd.Cmd.do_help(self, args)

    def empty_line(self):
        """Empty line + ENTER does not execute anything"""
        pass

"""Last part"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
