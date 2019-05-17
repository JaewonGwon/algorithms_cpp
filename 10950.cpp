#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int t;
    int a, b;
    cin >> t;
    int i;
    for(i = 0 ; i < t ; i++) {
        cin >> a >> b;
        cout << a + b << endl;
    }
}