// Copyright 2017 Michael Graziano mjgrazia@bu.edu

#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>

using namespace std;

int main(){
    double earth_mass = 5.972 * pow(10, 24);
    double atoms_in_mole = 6.022 * pow(10, 23);
    double tera_convert = 4 * pow(10, 12);
    double element_info[9][3] = {
        {0.321, 55.84 * pow(10, -3), 26},  // Iron Values
        {0.301, 15.99 * pow(10, -3), 8},   // Oxygen Values
        {0.151, 28.08 * pow(10, -3), 14},  // Silicon Values
        {0.139, 24.30 * pow(10, -3), 12},  // Magnesium Values
        {0.029, 32.06 * pow(10, -3), 16},  // Sulfur Values
        {0.018, 58.69 * pow(10, -3), 28},  // Nickel Values
        {0.015, 40.07 * pow(10, -3), 20},  // Calcuim Values
        {0.014, 26.998 * pow(10, -3), 13}, // Aluminum Values 
        {0.012, 75 * pow(10, -3), 60}      // Other Values
    };
    double electrons = 0;
    double terabytes;

for (int e=0; e<9; e++){
    electrons = electrons + earth_mass * element_info[e][0] / element_info[e][1] * atoms_in_mole * element_info[e][2];
}

terabytes = electrons / tera_convert;
cout << terabytes << endl << terabytes - pow(10, 38) << endl << terabytes + pow(10, 38) << endl;

return 0;
}
