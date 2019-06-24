#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n = 0, i = 0;
    cin >> n;
    vector<pair<int, int>> arr(n);
    for ( i = 0 ; i < n ; i++ ) {
        cin >> arr[i].first >> arr[i].second;
    }

    sort(arr.begin(), arr.end());

    for ( i = 0 ; i < n ; i++ ) {
        cout << arr[i].first << " " << arr[i].second << "\n";
    }
    return 0;
}