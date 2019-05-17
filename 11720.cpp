#include <iostream>
#include <string>
using namespace std;

int main() {
    int index, result;
    cin >> index;
    int intVal, i;
    string input;
    cin >> input;
    result = 0;
    for (i = 0 ; i < index ; i++) {
        result = result + (int)input[i]-48;
    }
    cout << result;
}