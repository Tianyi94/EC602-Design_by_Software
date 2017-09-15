// Copyright 2017 Michael Graziano mjgrazia@bu.edu

#include <iostream>
#include <ctime>
#include <cstdint>
#include <cmath>

using namespace std;

double time_estimate_32bit(double us){
    double raw_us = us * pow(2, 16);
    double raw_s = raw_us / pow(10, 6);
    return raw_s;
}

double time_estimate_64bit(double us){
    double raw_us = us * pow(2, 48);
    double raw_s = raw_us / pow(10, 6);
    double years = raw_s / (60 * 60 * 24 * 365);
    return years;
}

int main()
{
    // Variable Definitions
    clock_t start_clock, end_clock; 
    uint16_t i = 1;

    start_clock = clock();

    while(i > 0)
    {
        i++;
    }
    
    double test_value = 105;
    end_clock = clock();
    double seconds = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;
    double calc_16_bit = seconds * pow(10, 6);
    double est_8_bit = calc_16_bit * pow(10, 3) / pow(2, 8);
    double est_32_bit = time_estimate_32bit(calc_16_bit);
    double est_64_bit = time_estimate_64bit(calc_16_bit); 
    cout << "estimated int8 time (nanoseconds): " << est_8_bit << endl;
    cout << "measured int16 time (microseconds): " << calc_16_bit << endl;
    cout << "estimated int32 time (seconds): " << est_32_bit << endl;
    cout << "estimated int64 time (years): " << est_64_bit << endl;
    return 0;
}
