// Copyright 2017 Michael Graziano mjgrazia@bu.edu
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {

    if (argc == 1) {
        return 0;
    }

    else {

        for(int i = 1; i < argc; i++) {

            if (i <= 4) {
                cout << argv[i] << "\n";
            }
            
            else {
                cerr << argv[i] << "\n";
            }
        }
    }
    
    return 0;
}
