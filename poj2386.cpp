#include <iostream>

using namespace std;

char map[102][102];

int dir[8][2] = {{1, 0}, {0, 1}, {1, 1}, {1, -1}, {-1, 0}, {0, -1}, {-1, -1}, {-1, 1}};

void dfs(int x, int y) {
    map[x][y] = '.';
    for (int i = 0; i < 8; ++i) {
        if (map[x + dir[i][0]][y + dir[i][1]] == 'W') {
            dfs(x + dir[i][0], y + dir[i][1]);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> map[i][j];
        }
    }

    int count = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (map[i][j] == 'W') {
                count += 1;
                dfs(i, j);
            }
        }
    }

    cout << count << endl;
    return 0;
}