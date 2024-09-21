#include <iostream>
using namespace std;

int main() {
double a= 9.2;
double b= 1.3;
double c = 30.48;
double d = 160934;
cout <<fixed;
cout.precision(1);
cout << "9.2ft = " << a*c << "cm\n";
cout << "1.3mi = " << b*d << "cm";
    return 0;
}