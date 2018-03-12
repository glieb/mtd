#!/usr/bin/env python
import sys
import csv
import os
from itertools import count


# change to whichever address you prefer
address = os.path.expanduser("~/.mtd/")
filename = address + "todos.csv"


class Todo(object):
    
    def __init__(self, id_num, description):
        self.id_num = id_num
        self.description = description

    def show(self):
        print(" ".join([str(self.id_num), self.description]))


class TodoList(object):

    def __init__(self, todos):
        self.todos = todos

    def show(self):
        if not self.todos:
            print("NO TODOS")
        else:
            print("TODOS:")
            for todo in self.todos:
                todo.show()

    def add(self, description):
        self.todos.append(Todo(self.generate_id(), description))

    def remove(self, rm_num):
        for todo in self.todos:
            if todo.id_num == rm_num:
                self.todos.remove(todo)

    def edit(self, edit_num, new_description):
        for todo in self.todos:
            if todo.id_num == edit_num:
                todo.description = new_description

    def generate_id(self):
        for i in count(1):
            if all(todo.id_num != i for todo in self.todos):
                return i


def list_from_csv(file_address):
    with open(file_address, "r") as csv_file:
        list_reader = csv.reader(csv_file)
        #  For every line in the CSV file, create todo item
        new_list = TodoList([])
        for row in list_reader:
            new_list.todos.append(Todo(new_list.generate_id(), row[1]))
        return new_list

def list_to_csv(file_address, flush_list):
    with open(file_address, "w") as csv_file:
        list_writer = csv.writer(csv_file)
        for todo in flush_list.todos:
            list_writer.writerow([todo.id_num, todo.description])


def main(args):
    
    #  Create directory if it does not exist
    if not os.path.exists(address):
        os.makedirs(address)

    #  Create csv file if it does not exist
    with open(filename, "a+") as new_file:
        pass

    the_list = list_from_csv(filename)

    #  If commands empty, show list and exit
    if not args:
        the_list.show()
        return

    command = args[0]

    if command == "show":
        the_list.show()

    elif command == "add":
        the_list.add(" ".join(args[1:]))

    elif command == "remove":
        the_list.remove(int(args[1]))

    elif command == "edit":
        the_list.edit(int(args[1]), " ".join(args[2:]))

    list_to_csv(filename, the_list)


if __name__ == "__main__":
    main(sys.argv[1:])
