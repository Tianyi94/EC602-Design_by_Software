typedef vector<double> Poly;

// Add two polynomials, returning the result
Poly add_poly(const Poly &a, const Poly &b){

    // Variable Definitions:
    Poly sum;
    int max_size;
    double carry = 0;

    if(a.size() >= b.size()){
        max_size = a.size();
    } 
    else {
        max_size = b.size(); 
    }

    for(i = 0; i < max_size; i++){
        if(i >= a.size()){
            sum.push_back(b[i]+carry);
        } 
        else if(i >= b.size()){
            sum.push_back(a[i]+carry);
        } 
        else if(a[i]+b[i]+carry >= 10){
            sum.push_back((a[i]+b[i]+carry) % 10)
        }
            
}

// Multiply two polynomials, returning the result.
Poly multiply_poly(const Poly &a, const Poly &b);
