#!/usr/bin/env python3
'''Importing models'''
from models.base_model import BaseModel
import cmd


'''
   Console program for Airbnb
'''


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_foo(self, args=None):
        '''Prints foo
        '''
        args_list = args.split()
        for arg in args_list:
            print("Arg: {}".format(arg))

    def do_quit(self, id):
        '''Quit command to exit the program
        '''
        exit(0)

    def emptyline(self):
        pass

    def do_EOF(self, id):
        '''EOF to exit the program
        '''
        exit(0)

    '''BASE MODEL COMMANDS'''

    def do_create(self, class_name=None):
        '''Creates a base model\nUsage: create <model_name>
        '''
        valid_names = ["BaseModel", "Place", "Amenity", "City", "State"]
        if len(class_name) == 0:
            print("** class name missing **")
        elif class_name not in valid_names and len(class_name) != 0:
            print("** class doesn't exist **")
        else:
            print("New {} created".format(class_name))
            '''This is where to implement BaseModel code
            '''

    def do_show(self, args):
        '''Show details about an object\nUsage: show <class_name> <id>
        '''
        args_list = args.split()

        valid_names = ["BaseModel", "Place", "Amenity", "City", "State"]
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in valid_names and len(args) != 0:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            class_name = args_list[0]
            id = args_list[1]
            print("Show {} ID: {}".format(class_name, id))

    def do_destroy(self, args):
        '''Destroy a base model\nUsage: destroy <class name> <id>
        '''
        args_list = args.split()

        valid_names = ["BaseModel", "Place", "Amenity", "City", "State"]
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in valid_names and len(args) != 0:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            class_name = args_list[0]
            id = args_list[1]
            """Retrieve model using id given and destroy it
	    """
            print("Base model destroyed")

    def do_all(self, args):
        '''Prints all instances of Model\nusage: all <class name>
        '''
        args_list = args
        valid_names = ["BaseModel", "Place", "Amenity", "City", "State"]
        if len(args_list) == 0:
            """Print all instances of all objects
            """
        elif args_list not in valid_names and len(args) != 0:
            print("** class doesn't exist **")
        else:
            """
            Execute BaseModel.all()
            """
            print("Here's all we have")

    def do_update(self, args):
        '''Updates an instance\nUsage: update <class name> <id> <attribute name> "<attribute value>"
        '''
        args_list = args.split()
        valid_names = ["BaseModel", "Place", "Amenity", "City", "State"]

        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in valid_names and len(args) != 0:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** attribute value missing **")
        elif len(args_list) > 4:
            print("Too many arguments. Check: help update")
        else:
            print("Instance updated")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
