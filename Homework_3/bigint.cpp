// Copyright 2017 Michael Graziano mjgrazia@bu.edu
#include <string>
#include <vector>

typedef vector<int> Poly; 
typedef string BigInt;

Poly add_poly(const Poly &a, const Poly &b) {
    
    //Variable Definitions:
    Poly sum;
    int max_size, car_out, car_in, a_val, b_val;

    //Defining max_size based on largest Poly
    if (a.size() >= b.size())
        max_size = a.size();
    else
        max_size = b.size();

    car_out = 0;

    for (int i = 0; i < max_size; i++) {
        car_in = car_out;

        if (i >= a.size()) { 
            a_val = 0;
            b_val = b[i];
        } 
        else if (i >= b.size()) {
            a_val = a[i];
            b_val = 0;
        }
        else {
            a_val = a[i];
            b_val = b[i];
        }

        sum.push_back((a_val+b_val+car_in) % 10);
        car_out = (a_val+b_val+car_in) / 10;
    }
    
    if (car_out != 0) { 
        sum.push_back(car_out);
        return sum;
    }
    else
        return sum;
}

Poly BigInt_to_Poly(BigInt a) {
    Poly convert;
    
    for (int i = a.size()-1; i >= 0; i--) 
        convert.push_back(stoi(string(1, a[i]),nullptr,10)); 

    return convert;
}

BigInt Poly_to_BigInt(Poly a) {
    BigInt convert = "";

    for (int i = a.size()-1; i >= 0; i--)
        convert = convert + to_string(a[i]);

    return convert;
}

BigInt multiply_int(const BigInt &a, const BigInt &b) {
    
    // Variable Declarations:
    vector<Poly> products;
    Poly final_prod, single_prod, run_sum, temp_sum, larger, smaller;
    BigInt a_copy = a;
    BigInt b_copy = b;
    int new_pos;

    // Determine if "0" is present in BigInt a or b
    // If not, then figure out which one is longer. 
    if ((a.size() == 1 && a == "0") || (b.size() == 1 && b == "0"))
        return "0";

    else if (a.size() >= b.size()) {
        larger = BigInt_to_Poly(a_copy);
        smaller = BigInt_to_Poly(b_copy);
    }

    else {
        larger = BigInt_to_Poly(b_copy);
        smaller = BigInt_to_Poly(a_copy);
    }

    // Product Operations
    for (int i = 0; i < smaller.size(); i++) {
        single_prod = Poly(larger.size() + smaller.size() - 1, 0);
        for (int j = 0; j < larger.size(); j++) {
            new_pos = i + j;
            single_prod[new_pos] = larger[j] * smaller[i];
        }
        products.push_back(single_prod);
    }

    // Sum Operations
    for (int i = 0; i < products.size(); i++) {
        if (i == 0 && products.size() == 1)
            run_sum = products[i];

        else if (i == 0) {
            run_sum = add_poly(products[i], products[i+1]);
            i++;
        }

        else {
            temp_sum = run_sum;
            run_sum = add_poly(products[i], temp_sum);
        }

        final_prod = run_sum;
    }
   
    return Poly_to_BigInt(final_prod);
}
