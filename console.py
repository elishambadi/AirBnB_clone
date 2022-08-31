#!/usr/bin/env python3
'''
   Console program for Airbnb
'''

import cmd


class HBNBCommand(cmd.Cmd):
    
    def do_foo(self, name):
        '''Prints foo
	'''
        print("Foo; {}".format(name))

    def do_quit(self, id):
        '''Quit command to exit the program
	'''
        exit(0)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
