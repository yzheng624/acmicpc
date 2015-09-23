#include <iostream>

using namespace std;

int main() {
    int num_case;
    cin >> num_case;
    for (int i = 0; i < num_case; ++i) {
        int pole_length;
        int n;
        cin >> pole_length >> n;
        int pos;
        int dist_min_max = -1, dist_max_max = -1;
        for (int j = 0; j < n; ++j) {
            cin >> pos;
            int max_pos = max(pos, pole_length - pos);
            int min_pos = min(pos, pole_length - pos);
            dist_min_max = max(dist_min_max, min_pos);
            dist_max_max = max(dist_max_max, max_pos);
        }
        cout << dist_min_max << " " << dist_max_max << endl;
    }
    return 0;
}