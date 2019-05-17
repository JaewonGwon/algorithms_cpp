#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    int a, b;
    int i;
    for(i = 0 ; i < t ; i++) {
        scanf("%d,%d", &a, &b);
        cout << "Case #" << i+1  << ": " << a + b << endl;
    }
    return 0;
}