**MTD: A minimal todo list written in Python.**

This is a simple script for managing a todo list. It is meant to work on Unix-based systems. Using this you can add, remove, edit, and display todo list items. You can also study the fairly straightforward source code in order to understand how to build simple scripts in Python.

**How To Install**

First, clone the repository. Then copy the `mtd.py` script into `/usr/local/bin`.

**How To Uninstall**

Remove the `mtd.py` script from `/usr/local/bin`.

**How to use**

    $ sudo cp mtd.py /usr/local/bin/mtd
    $ mtd add Do the laundry
    $ mtd add Code a minimal todo list
    $ mtd show
    TODOS:
    1 Do the laundry
    2 Code a minimal todo list
    $ mtd remove 1
    $ mtd show
    TODOS:
    1 Code a minimal todo list
    $ mtd edit 1 Program a minimal todo list in Python
    $ mtd show
    TODOS:
    1 Program a minimal todo list in Python
    $ mtd remove 1
    $ mtd show
    NO TODOS

**Unlicensed**

This software is unlicensed using the [Unlicense](https://unlicense.org/), meaning you are free to copy the source code anywhere and for whatever purpose without having to worry about copyright whatsoever.
