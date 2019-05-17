#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main() {
    int i, input;
    cin >> input;
    for(i = 0 ; i < input ; i++) {
        cout << i + 1 << endl;
    }
    return 0;
}