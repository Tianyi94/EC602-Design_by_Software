// Copyright 2017 J Carruthers jbc@bu.edu
// Copyright 2017 Michael Graziano mjgrazia@bu.edu
// Definitions:
// Rs = factor by which float is better than int at representing small numbers
// Rm = factor by which float is better than int at representing large numbers
// Ri = factor by which int is better than float at representing integers
//
// Formulas:
//
// Rs = 1 / smallest_float_greater_than_zero
// Rm = maximum_float_value / largest_int_value
//
// Ri = largest_int_value / N
// where N is the largest integer such that all integers 1,2,3,...,N can be
// represented without loss of accuracy by a float of this size.

#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>

int main(){

    double Rs,Rm,Ri;

    // calculate Rs, Ri, and Rm for half/binary16 vs int16_t
    
    Rs = 1 / pow(2, -14);
    Rm = ((2-pow(2, -10))*pow(2, 15)) / INT16_MAX;
    Ri = INT16_MAX / pow(2, 11);
    std::cout<< "16 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

    // calculate Rs, Ri, and Rm for float/single/binary32 vs int32_t
    Rs = 1 / FLT_MIN;
    Rm = FLT_MAX / INT32_MAX;
    Ri = INT32_MAX / pow(2, 24);
    std::cout<< "32 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

    // calculate Rs, Ri, and Rm for double/binary64 vs int64_t

    Rs = 1 / DBL_MIN;
    Rm = DBL_MAX / INT64_MAX;
    Ri = INT64_MAX / pow(2, 53);
    std::cout<< "64 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;
  
    return 0;
}
