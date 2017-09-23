// Copyright 2017 Michael Graziano mjgrazia@bu.edu
#include <vector>

typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a, const Poly &b) {

    // Variable Definitions:
    Poly sum;
    int max_size;

    // Defining max_size based on largest Poly
    if (a.size() >= b.size())
        max_size = a.size();

    else 
        max_size = b.size(); 

    // Calculation of each individual position
    for (int i = 0; i < max_size; i++) {
        if (i >= a.size()) 
            sum.push_back(b[i]);
    
        else if (i >= b.size())
            sum.push_back(a[i]);
 
        else
            sum.push_back(a[i] + b[i]);
    }
    
    // Remove leading zeros
    for (int i = sum.size()-1; i >= 1; i--) {
        if (sum[i] == 0) 
            sum.pop_back();
        else
            break;
    }

    return sum;
}

// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a, const Poly &b) {
    
    // Variable Declarations:
    vector<Poly> products;
    Poly final_prod, single_prod, run_sum, temp_sum, larger, smaller;
    int new_pos;
    
    // Determine if coefficient of pow(x, 0) is 0 and the only element.
    // If not, determine which vector is larger.
    if ((a.size() == 1 && a[0] == 0) || (b.size() == 1 && b[0] == 0))
        return Poly(1, 0);

    else if (a.size() >= b.size()) {
        larger = a;
        smaller = b; 
    }

    else {
        larger = b;
        smaller = a;
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

        else if(i == 0) { 
            run_sum = add_poly(products[i], products[i+1]);
            i++;
        } 
        
        else {
            temp_sum = run_sum;
            run_sum = add_poly(products[i], temp_sum);
        }    
        
        final_prod = run_sum;
    }
    
    return final_prod;
}
