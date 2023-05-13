#!/usr/bin/python3
"""console module, contains entry point of the command interperator"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interperator class to manage BaseModel objects
    """

    prompt = "(HBNB) " # The Command prompt (overrides the default)

    def do_quit(self, arg):
        """Quit: command to exit the program
        Args:
            arg: argument to command
        """

        cmd.sys.exit()

    def do_EOF(self, command):
        """EOF: exit the program when 'Ctrl-d is pressed"""
        print()
        return True

    def help(self):
        """Show help on available commands"""

    def emptyline(self):
        """Implements behaviour when 'Enter-key' is pressed on empty line"""

        pass  # (Don't repeat last command)

    def do_create(self, command):
        """Create: create a new object of BaseModel, save it to a JSON file
        and print the id
        """

        if not command:
            print("** class name missing **")  # No argument given
        elif command !=  "BaseModel":
            print("** class doesn't exist **")  # Invalid argument
        else:
            # Create and save an instance to a JSON file
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, command):
        """Show: display string representation of object base on
        <class name> and id
        """

        if not command:
            print("** class name missing **")  # No argument given
        else:
            # Extract <class name> and <id> from command line
            args = command.split()
            if args[0] !=  "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                # Get saved objects from storage
                models = storage.all()
                # create key from commandline entry
                key = f"{args[0]}.{args[1]}"
                if key not in models.keys():
                    print("** no instance found **")
                else:
                    # create an instance from a saved one and print it
                    print(BaseModel(**models[key]))

    def do_destroy(self, command):
        """Destroy: delete an object base on <class name> and <id>,
        save the change into a JSON file
        """

        if not command:
            print("** class name missing **")  # No argument given
        else:
            # Extract <class name> and <id> from command line
            args = command.split()
            if args[0] !=  "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                # Get saved objects from storage
                models = storage.all()
                # create key from commandline entry
                key = f"{args[0]}.{args[1]}"
                if key not in models.keys():
                    print("** no instance found **")
                else:
                    # delete the object and saved the change
                    models.pop(key)
                    storage.save()

    def do_all(self, command):
        """All: displays string representation of available class instances,
        an optional argument [class name] can also be specified display instance
        of the class
        """

        # Get saved objects from storage
        models = storage.all()

        if not command or command == "BaseModel":
            for key in models.keys():
                print(BaseModel(**models[key]))
        else:
            if command != "BaseModel":
                print("** class doesn't exist **")

    def do_update(self, command):
        """Update: update an object base onthe  class name and id
        by adding and attribute or updating an attribute,
        save the change in a JSON file
        """

        if not command:
            print("** class name missing **")  # No argument given
        else:
            # Extract arguments from command line
            args = command.split()
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                # get objects from storage
                models = storage.all()
                # create key from <class name> and <id>
                key = f"{args[0]}.{args[1]}"
                if args[0] != "BaseModel":
                    print("** class doesn't exist **")
                elif key not in models.keys():
                    print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
