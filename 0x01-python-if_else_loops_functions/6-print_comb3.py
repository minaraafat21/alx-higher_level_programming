#!/usr/bin/python3
for i in range(10):
    for d in range(i+1, 10):

        print("{}".format(str(i)), end="")
        if i == 8 and d == 9:
            print("{}".format(str(d)), end="\n")
        else:
            print("{}".format(str(d)), end=", ")
