# Copyright 2017 Michael Graziano mjgrazia@bu.edu

Table = "{:<6}{:<22}{:<22}{:<22}" # Format string for output table
print(Table.format("Bytes",
                   "Largest Unsigned Int",
                   "Minimum Signed Int",
                   "Maximum Signed Int"
                  ))

for byte in range(1, 9):
    n = byte * 8
    max_uint = 2**n - 1
    min_sint = -2**(n-1)
    max_sint = 2**(n-1) - 1
    print(Table.format(byte, max_uint, min_sint, max_sint))
