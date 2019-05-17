#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int a, b;
    int t, i;
    cin >> t;
    for (i = 0; i < t ; i++) {
        cin >> a >> b;
        cout << "Case #" << i+1 << ": " << a << " + " << b << " = " << a+b << endl;    
    }    
    return 0;
}