#include <iostream>
#include <vector>

using namespace std;

class DSU {
private:
    vector<int> parent;
    vector<int> size;
    
public:
    DSU(int n) {
        parent.resize(n+1);
        size.resize(n+1, 1);

        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY) {
            return false;
        }

        if (size[rootX] < size[rootY]) {
            swap(rootX, rootY);
        }

        parent[rootY] = rootX;
        size[rootX] += size[rootY];

        return true;
    }

    bool same(int x, int y) {
        return find(x) == find(y);
    }

    int getSize (int x) {
        return size[find(x)];
    }
};
