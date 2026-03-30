
#include <iostream>
#include <vector>

using namespace std;
using tint = long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    tint n;
    cin >> n;

    vector<pair<tint, tint>> v;    //value, index

    for(tint i = 1; i <= n; ++i) {
        tint x;
        cin >> x;
        while(not v.empty() and x <= v.back().first)
            v.pop_back();
        cout << (v.empty() ? 0 : v.back().second) << ' ';
        v.push_back({x, i});
    }

    cout << '\n';

    return 0;
}
