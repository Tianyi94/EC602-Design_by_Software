# Copyright 2017 Michael Graziano mjgrazia@bu.edu

import sys
import numpy

earth_mass = 5.972 * (10**24)
atoms_in_mole = 6.022 * (10**23)
tera_convert = 4 * (10**12)
element_info = {"Iron": [0.321, 55.84 * (10**-3), 26],
                "Oxygen": [0.301, 15.99 * (10**-3), 8],
                "Silicon": [0.151, 28.08 * (10**-3), 14],
                "Magnesium": [0.139, 24.30 * (10**-3), 12],
                "Sulfur": [0.029, 32.06 * (10**-3), 16],
                "Nickel": [0.018, 58.69 * (10**-3), 28],
                "Calcuim": [0.015, 40.07 * (10**-3), 20],
                "Aluminum": [0.014, 26.998 * (10**-3), 13],
                "Other": [0.012, 75 * (10**-3), 60]
               }

electrons = numpy.float32(0)
for element in element_info:
   electrons = (electrons
               + earth_mass 
               * element_info[element][0] 
               / element_info[element][1] 
               * atoms_in_mole 
               * element_info[element][2]
               )
terabytes = electrons / tera_convert 

print(terabytes, 
      terabytes - 1*(10**38), 
      terabytes + 1*(10**38),
      sep = "\n"
     )

