# Data Structures - Linked Lists

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this file of the data structures, linked lists are created and tested.

A linked list is a reference to a sequence of 'Nodes'. A singly linked list has single references to other Nodes. Each Node is connected to another in the singly list, starting at the first or 'head' node and linking to the next node and then the next node until a referenced node is reached that has no next value linking it to any other nodes.

## Getting Started
Running tests is straight forward and involves using pytest.

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](/assets/Click_to_download_x6c0g16lz.png)


In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##by default: Downloads is a directory inside of your root; and where your file will be downloaded
$ cd python_data_structures_and_algorithims ##and now you are in this directory
```
This module is running tests on given data imputs. Install [pytest](https://docs.pytest.org/en/latest/getting-started.html) to get started:
Installing pytest:
```
$ pip install -U pytest
```
Running tests:
```
$ pytest
```
## Functionality/Architecture
This application is running tests on Linked Lists. The linked list class is defined and so is the node class.

Creating - When an instance of a list is created it is created without any nodes i.e an empty linked list. Nodes can be created and added by using the insert method of the linked list class. By passing in a value as an arguement for the node, the insert method defines the next_node as the current node and then sets the head of the list to be the inserted node.

Searching - A linked list can be searched for a specific node using the includes method of the linked list. By passing in the search parameter as an arguement, includes will traverse the linked list and return "True" if the search value is found and "False" if not found by the end of the list.

Printing - The values of every node in the linked list can be determined in two separate ways. Using python's built in global object method, print, you can create a linked list and invoke print(name of your list). This will return every value as a string and total the number of values. Additionally the return list method of a linked list can be invoked, which will return an array of the values.

## Change Log
Sat Dec 07 2019 14:24:42<br>Created linked list and node classes. Developed tests to ensure proper functionality.
