#!/usr/bin/env python3
'''Importing models'''
from models.base_model import BaseModel
import cmd


'''
   Console program for Airbnb
'''


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    intro = "Welcome to Hbnb Console!\n\
    Type 'help' to view available commands\n"

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

    def do_destroy(self, id):
        '''Destroy a base model
        '''
        print("Base model destroyed")

    def do_all(self, id):
        '''Prints all instances of Model given
           If no params passed, displays all instances of everything
        '''
        print("Here's all we have")

    def do_update(self, id):
        '''Updates an instance
        '''
        print("Instance updated")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
