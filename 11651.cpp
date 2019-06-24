#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
    if (a.second < b.second) {
        return true;
    }
    else if (a.second == b.second && a.first < b.first) {
        return true;
    }
    return false;
}

int main() {
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    int n = 0, i = 0;
    cin >> n;
    vector<pair<int, int>> arr(n);
    
    for(i = 0; i < n; i++) {
        cin >> arr[i].first >> arr[i].second;
    }

    sort(arr.begin(), arr.end(), compare);

    for(i = 0; i < n; i++) {
        cout << arr[i].first << " " << arr[i].second << "\n";
    }
}