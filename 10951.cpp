#include <iostream>

using namespace std;

int main() {
    int a, b;
    while (scanf("%d %d", &a, &b) != EOF) {
        if (a+b == 0) {
            return 0;
        }
        cout << a + b << endl;
    }
    return 0;
}