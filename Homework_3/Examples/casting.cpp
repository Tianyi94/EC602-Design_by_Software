#include <iostream>
int main(int argc, char const *argv[])
{
	double x;

	x = 12 / 10 * 245 / 100;
	std::cout << x << std::endl;
	
	x = 1.2 * 245 / 100;
	std::cout << x << std::endl;

	x = (double) 1.2 * (245 / 100);
	std::cout << x << std::endl;

	return 0;
}