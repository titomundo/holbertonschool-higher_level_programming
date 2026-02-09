#!/usr/bin/python3

"""task_02_verboselist: VerboseList Module"""


class VerboseList(list):
    """Base VerboseList class"""

    def append(self, object):
        """append method: override append method from list class
        Args:
            object (object) element to add to the list"""

        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        """extend method: override extend method from list class
        Args:
            iterable (iterable object): iterable to add to the list"""

        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value):
        """remove method: override remove method from list class
        Args:
            value (int): value to remove from the list"""

        try:
            super().remove(value)
            print(f"Removed [{value}] from the list")
        except Exception as err:
            raise err

    def pop(self, pos=-1):
        """pop method: override pop method from list class
        Args:
            pos (int): index of the element to pop"""

        try:
            p = super().pop(pos)
            print(f"Popped [{p}] from the list")
        except Exception as err:
            raise err
