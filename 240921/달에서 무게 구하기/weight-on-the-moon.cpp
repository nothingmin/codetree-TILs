#include <iostream>
using namespace std;

int main() {
    int a = 13;
    double g= 0.165000;
    cout << fixed;
    cout.precision(6);
    cout << a << " * " << g << " = " << a*g ;
    return 0;
}