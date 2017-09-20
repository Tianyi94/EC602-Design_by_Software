#include <iostream>
#include <vector>

int main() {
  std::vector<float> v(3, 0);
  v.push_back(1.2);
  v.push_back(4.1);


  for (int i = 0; i < v.size(); i++)
    std::cout << v[i] << " ";
  std::cout << std::endl;

  for (double e : v) {
    std::cout << e << " ";
    e = 0;
  }
  std::cout << std::endl;
  for (double e : v) {
    std::cout << e << " ";
    e = 0;
  }
  std::cout << std::endl;

  for (double &e : v)
    e = 1;

  for (double e : v)
    std::cout << e << " ";
  std::cout << std::endl;

  for (auto e : v)
    std::cout << e << " ";
  std::cout << std::endl;

  for (auto &e : v)
    e = 9;

  for (int i = 0; i < v.size(); i++)
    std::cout << v[i] << " ";
  std::cout << std::endl;

}