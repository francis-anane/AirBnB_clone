#!/usr/bin/python3
"""console module, contains entry point of the command interperator"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interperator class to manage BaseModel objects
    """

    prompt = "(hbnb) "  # The Command prompt (overrides the default)

    # get dictionary of classes
    __classes = storage.classes()

    # Get saved objects from storage
    __models = storage.all()

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
        """Create: create a new class object, save it to a JSON file
        and print the id
        """

        if not command:
            print("** class name missing **")  # No argument given
        elif command not in self.__classes.keys():
            print("** class doesn't exist **")  # Invalid argument
        else:
            # Create and save an instance to a JSON file
            new_model = self.__classes[command]()
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
            if args[0] not in self.__classes.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                # create key from commandline entry
                key = f"{args[0]}.{args[1]}"
                if key not in self.__models.keys():
                    print("** no instance found **")
                else:
                    # print object by mapping keys to values
                    print(self.__models[key])

    def do_destroy(self, command):
        """Destroy: delete an object base on <class name> and <id>,
        save the change into a JSON file
        """

        if not command:
            print("** class name missing **")  # No argument given
        else:
            # Extract <class name> and <id> from command line
            args = command.split()
            if args[0] not in self.__classes.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                # create key from commandline entry
                key = f"{args[0]}.{args[1]}"
                if key not in self.__models.keys():
                    print("** no instance found **")
                else:
                    # delete the object and saved the change
                    self.__models.pop(key)
                    storage.save(self)

    def do_all(self, command):
        """All: displays string representation of available class instances,
        an optional argument [class name] can also be specified display
        instanceof the class
        """

        if not command:
            # print models by mapping keys to values
            for key in self.__models.keys():
                print(self.__models[key])
        elif command in self.__classes.keys():
            # display models based on specified <class name>
            for key in self.__models.keys():
                if command in key:
                    print(self.__models[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, command):
        """Update: update an object base onthe  class name and id
        by adding and attribute or updating an attribute,
        save the change in a JSON file
        """

        if not command:
            print("** class name missing **")  # No argument given
        else:
            # mapping <class names> to attributes
            attr = storage.attributes()
            # attributes that shouldn't be updated
            excluded_attr = ("id", "created_at", "updated_at")
            # Extract arguments from command line
            args = command.split(" ", 3)
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                # create key from <class name> and <id>
                key = f"{args[0]}.{args[1]}"
                if args[0] not in attr.keys():
                    print("** class doesn't exist **")
                elif key not in self.__models.keys():
                    print("** no instance found **")
                # check attributes that shouldn't be changed
                elif args[2] in excluded_attr:
                    return
                else:
                    value = args[3]
                    # check for quoted attribute values
                    if value.startswith('"') and value.endswith('"'):
                        value = value.replace('"', '')
                    elif value.startswith("'") and value.endswith("'"):
                        value = value.replace("'", "")
                    elif not value.startswith('"') and not value.endswith(
                            '"') and " " in value:
                        # get string at first i ndex
                        value = value.split(" ")[0]
                    elif not value.startswith("'") and not value.endswith(
                            "'") and " " in value:
                        # get string at first index
                        value = value.split(" ")[0]

                    try:
                        # cast value to attribute type
                        value = attr[args[0]][args[2]](value)
                        # update attribute by updating <object.__dict__>
                        self.__models[key].__dict__[args[2]] = value
                        # save the change
                        self.__models[key].save()
                    except (KeyError, ValueError) as err:
                        # Add a new attribute if specified in command
                        # not found
                        if type(err).__name__ == "KeyError":
                            self.__models[key].__dict__[args[2]] = value
                            self.__models[key].save()  # save the change


if __name__ == "__main__":
    HBNBCommand().cmdloop()
