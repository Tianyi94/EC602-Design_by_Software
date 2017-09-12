# Copyright 2017 Michael Graziano mjgrazia@bu.edu
import sys

if len(sys.argv) >= 2:
    arguments = sys.argv[1::]
    for position in range(len(arguments)):
        # print(position, end = " ")
        if position <= 3:
            # print("Adding value to sys.stdout:")
            sys.stdout.buffer.write((arguments[position]+"\n").encode())
        else:
            # print("Adding value to sys.stderr:")
            sys.stderr.buffer.write((arguments[position]+"\n").encode())

