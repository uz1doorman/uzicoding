#include <vector>
#include <algorithm>

using namespace std;

//index starting from 0

template <typename T, typename Func>
class SparseTable {
private:
    int n;
    vector<int> lg;
    vector<vector<T>> st;
    Func func;

public:
    SparseTable() = default;

    SparseTable(const vector<T>& a, Func f) {
        build(a, f);
    }

    void build(const vector<T>& a, Func f) {
        func = f;
        n = a.size();

        lg.assign(n+1, 0);
        for (int i = 2; i <= n; i++) {
            lg[i] = lg[i / 2] + 1;
        }

        int K = lg[n] + 1;
        st.assign(n, vector<T>(K));

        for (int i = 0; i < n; ++i) {
            st[i][0] = a[i];
        }

        for (int j = 1; j < K; ++j) {
            for (int i = 0; i + (1 << j) <= n; ++i) {
                st[i][j] = func(st[i][j-1], st[i+(1<<(j-1))][j-1]);
            }
        }
    }

    T query(int l, int r) const {
        int len = r - l + 1;
        int k = lg[len];

        return func(st[l][k], st[r - (1 << k) + 1][k]);
    }
};
