#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    int n = 0, i = 0;
    cin >> n;
    vector <pair<int, int>> arr(n);
    string name_list[n];
    for (i = 0; i < n ;i++) {
        cin >> arr[i].first >> name_list[i];
        arr[i].second = i;
    }
    sort(arr.begin(), arr.end());
    for (i = 0; i < n; i++) {
        cout << arr[i].first << " " << name_list[arr[i].second] << "\n";
    }
    return 0;
}