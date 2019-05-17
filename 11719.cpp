#include <iostream>
#include <string>

using namespace std;

int main(void) {
        cin.tie(0);
        string s, result;
        while (1)
        {
                getline(cin, s);
                if (cin.eof())
                        break;
                result = result + s + '\n';
        }
        result.erase(result.length()-1, result.length()-1);
        cout << result;
        return 0;
}