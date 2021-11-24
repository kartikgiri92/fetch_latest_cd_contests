#include<bits/stdc++.h>
using namespace std;

// DEFINE
#define LL long long
#define PB push_back
#define REP(i, a, b) for (i=a; i<b; i++)

typedef vector <LL> VLL;

// TEMPLATE CONSTANTS
const LL MOD = 1e9 + 7;
const LL INF = 1e9;

// TEMPLATE FUNCTIONS
LL MOD_MULTIPLY(LL a, LL b) {
    return ((a % MOD) * (b % MOD)) % MOD;
}
LL MOD_ADDITION(LL a, LL b) {
    return ((a % MOD) + (b % MOD)) % MOD;
}
LL MOD_SUBTRACTION(LL a, LL b) {
    return ((a % MOD) - (b % MOD) + MOD) % MOD;
}

LL FIND_GCD(LL a, LL b) {
    if (b == 0)
        return (a);
    return (FIND_GCD(b, a % b));
}

LL FIND_LCM(LL a, LL b) {
    return (a / FIND_GCD(a, b)) * b;
}

void solve();
int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("error.txt", "w", stderr);
    freopen("output.txt", "w", stdout);
#endif

    solve();

#ifndef ONLINE_JUDGE
    cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl;
#endif
    return 0;
}

/* ----- LOGIC CODE ----- */


void solve() {
    cout << "HeLLo world\n";
}
