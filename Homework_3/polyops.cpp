typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a, const Poly &b) {

    // Variable Definitions:
    Poly sum;
    int a_val, b_val, max_size, carry_in;
    int carry_out = 0;

    // Defining max_size based on largest Poly
    if(a.size() >= b.size()) {
        max_size = a.size();
    } 

    else {
        max_size = b.size(); 
    }

    // Calculation of each individual position
    for(int i = 0; i < max_size; i++) {
        carry_in = carry_out;
        if(i >= a.size()) {
            a_val = 0;
            b_val = (int)b[i];
        }

        else if(i >= b.size()){
            a_val = (int)a[i];
            b_val = 0;
        }

        else {
            a_val = (int)a[i];
            b_val = (int)b[i];
        }
        
        sum.push_back((a_val+b_val+carry_in) % 10);
        carry_out = (a_val+b_val+carry_in) / 10;   
    }
    
    if(carry_out > 0) {
        sum.push_back(carry_out);
    }

    return sum;
}

// Multiply two polynomials, returning the result.
//Poly multiply_poly(const Poly &a, const Poly &b);
