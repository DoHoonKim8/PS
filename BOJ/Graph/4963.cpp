#include <iostream>
#include <memory.h>
#define MAX 50

using namespace std;

int width, height;
int map[MAX][MAX];
int visited[MAX][MAX];
int islands;

bool togo(int x, int y) {
    return
        x >= 0 &&
        x <= height - 1 &&
        y >= 0 &&
        y <= width - 1 && 
        !visited[x][y] &&
        map[x][y];
}

void dfs(int x, int y) {
    visited[x][y] = true;
    if (togo(x - 1, y - 1)) dfs (x - 1, y - 1);
    if (togo(x - 1, y)) dfs (x - 1, y);
    if (togo(x - 1, y + 1)) dfs (x - 1, y + 1);
    if (togo(x, y - 1)) dfs (x, y - 1);
    if (togo(x, y + 1)) dfs (x, y + 1);
    if (togo(x + 1, y - 1)) dfs (x + 1, y - 1);
    if (togo(x + 1, y)) dfs (x + 1, y);
    if (togo(x + 1, y + 1)) dfs (x + 1, y + 1);
}

int main() {
    while(1) {
        cin >> width >> height;
        if (width == 0 && height == 0) break;

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) cin >> map[i][j];
        }

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) visited[i][j] = false;
        }

        islands = 0;
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (!visited[i][j] && map[i][j]) {
                    dfs(i, j);
                    islands++;
                }
            }
        }
        cout << islands << endl;
    }

    return 0;
}
