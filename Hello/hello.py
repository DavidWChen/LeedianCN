#!/usr/bin/python

import string
usr_list = []
mylist=[]
class Dict:
    def __init__(self,position,name):
            self.position = position
            self.name = name

def collect():
    global usr_list
    entering = 1
    while (entering):
        str = raw_input("Enter intput (Position,Name): ")
        if str == "end":
            break
        spltstr = str.split(",")
        b = Dict(spltstr[0], spltstr[1])
        usr_list.append(b)
        print "Entered"

def main():
    print "Hello World!"
    global mylist
    mylist = open("list.txt", "w")
    collect()
    for i in range(len(usr_list)):
        print ("Position: " + usr_list[i].position + 
                ", Name: " + usr_list[i].name)
        mylist.write("Position: " + usr_list[i].position + 
        ", Name: " + usr_list[i].name + "\n")


if __name__ == "__main__":
    main()