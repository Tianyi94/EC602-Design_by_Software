#include <iostream>
#include <vector>

using namespace std;

#include "bigint.cpp"

int main()
{ 

  BigInt A,B;

  cin >> A >> B;

  cout << multiply_int(A,B) << endl;

//  cout << "Changing A to int: " << stoi(A, nullptr, 10) << endl;
//  cout << "Changing B to int: " << stoi(B, nullptr, 10) << endl;

/*  for (int i = 0; i < A.size(); i++)
    cout << "A String - " << i << " - " << stoi(string(1, A[i]), nullptr, 10) << endl;

  for (int i = 0; i < B.size(); i++)
    cout << "B String - " << i << " - " << stoi(string(1, B[i]), nullptr, 10) << endl;
*/
}
