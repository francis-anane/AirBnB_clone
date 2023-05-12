#!/usr/bin/python3
"""console module, contains entry point of the command interperator"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interperator class to manage AirBnB objects
    """

    prompt = "(HBNB) " # The Command prompt (overrides the default)

    def do_quit(self, cm):
        """quit: command to exit the program"""

        cmd.sys.exit()

    def do_EOF(self, cm):
        """EOF: exit the program when 'Ctrl-d is pressed"""
        print()
        return True

    def help(self):
        """Show help on available commands"""

    def emptyline(self):
        """Empty line behaviour when 'Enter' is pressed"""
        pass  # Do nothing (don't repeat commands)






if __name__ == '__main__':
    HBNBCommand().cmdloop()
