Got it 👍 — you want a **C++ LeetCode-oriented cheat sheet** that’s **concise**, **minimalistic**, and in the style of masters like *votrubac* and *lee215* (who are known for short, STL-heavy, trick-based code). This isn’t about everyday C++ coding — it’s about competitive shortcuts and patterns. I’ll cover **50+ snippets** grouped by category.

---

# 🚀 C++ Competitive Coding Cheat Sheet (LeetCode-style)

## 1. Headers & Setup

```cpp
#include <bits/stdc++.h>  // all-in-one (works on GCC/Clang)
using namespace std;

#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define pb push_back
#define eb emplace_back
#define sz(x) (int)(x).size()
```

---

## 2. Integer Types

```cpp
int x; long y; long long z; 
unsigned u; long double ld;
const int INF = 1e9; 
const long long LINF = 1e18;
```

---

## 3. Arrays & Vectors

```cpp
vector<int> v(n);             // size n, default 0
vector<int> v(n, 5);          // size n, filled with 5
vector<int> a = {1,2,3};      // init list
v.push_back(4); v.pop_back();
v.insert(v.begin()+i, 7);
v.erase(v.begin()+i); 
reverse(all(v));
```

---

## 4. Strings

```cpp
string s = "abc";
s.substr(1,2);        // "bc"
s.find("bc");         // pos or npos
s.push_back('z');     
reverse(all(s));
```

---

## 5. Sorting & Searching

```cpp
sort(all(v));                 // ascending
sort(rall(v));                // descending
sort(all(v), greater<int>()); // descending alt
auto it = lower_bound(all(v), x); // >=x
auto jt = upper_bound(all(v), x); // >x
int idx = it - v.begin(); 
```

---

## 6. Priority Queue

```cpp
priority_queue<int> pq;                // max-heap
priority_queue<int,vector<int>,greater<int>> pq; // min-heap
pq.push(5); pq.top(); pq.pop();
```

---

## 7. Queue & Deque

```cpp
queue<int> q; q.push(1); q.front(); q.pop();
deque<int> dq; dq.push_back(2); dq.push_front(3);
dq.pop_back(); dq.pop_front();
```

---

## 8. Stack

```cpp
stack<int> st; st.push(1); st.top(); st.pop();
```

---

## 9. Sets & Multisets

```cpp
set<int> s = {1,2,3}; 
s.insert(4); s.count(2); s.erase(3);
auto it = s.lower_bound(2); // >=2
multiset<int> ms = {1,1,2};
ms.erase(ms.find(1)); // erase one occurrence
```

---

## 10. Maps & Unordered Maps

```cpp
map<int,int> mp; mp[1]=10;
for(auto &[k,v]: mp) {}
unordered_map<int,int> um;
if (um.count(5)) {}
```

---

## 11. Pairs & Tuples

```cpp
pair<int,int> p = {1,2}; p.first; p.second;
tuple<int,int,int> t = {1,2,3};
auto [a,b,c] = t; // structured binding
```

---

## 12. Iteration Tricks

```cpp
for (int i=0;i<n;i++);
for (auto x: v); 
for (auto &[k,v]: mp);
```

---

## 13. Min/Max

```cpp
min({a,b,c}); max({a,b,c});
swap(a,b);
```

---

## 14. Math

```cpp
abs(x); pow(2,10); sqrt(x);
__gcd(a,b); lcm(a,b); // C++17
int bits = __builtin_popcount(x); // 1-bits
int lead = __builtin_clz(x); // leading zeros
```

---

## 15. Random

```cpp
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
uniform_int_distribution<int> dist(1,100);
int r = dist(rng);
```

---

## 16. Bit Tricks

```cpp
x & -x;         // lowest set bit
x >> k; x << k; // shift
x & (x-1);      // remove lowest set bit
```

---

## 17. Algorithms

```cpp
accumulate(all(v),0);           // sum
count(all(v), x);               // frequency
find(all(v), x);                // iterator
unique(all(v));                 // dedup (needs erase)
next_permutation(all(v));       // lexicographic
```

---

## 18. Custom Sort & Lambda

```cpp
sort(all(v), [](int a,int b){return a>b;});
```

---

## 19. Linked List (LeetCode style)

```cpp
struct ListNode{
    int val; ListNode* next;
    ListNode(int x): val(x), next(NULL){}
};
```

---

## 20. Binary Tree (LeetCode style)

```cpp
struct TreeNode{
    int val; TreeNode *left,*right;
    TreeNode(int x): val(x),left(NULL),right(NULL){}
};
```

---

## 21. 2D Vector / Grid

```cpp
vector<vector<int>> g(n, vector<int>(m,0));
for(int i=0;i<n;i++) for(int j=0;j<m;j++){}
```

---

## 22. BFS / DFS Templates

```cpp
// BFS
queue<int> q; q.push(start);
while(!q.empty()){
    auto u=q.front(); q.pop();
    for(auto v: adj[u]) if(!vis[v]){vis[v]=1; q.push(v);}
}

// DFS
function<void(int)> dfs=[&](int u){
    vis[u]=1;
    for(auto v: adj[u]) if(!vis[v]) dfs(v);
};
```

---

## 23. Heapify (vector to heap)

```cpp
make_heap(all(v)); 
push_heap(all(v)); 
pop_heap(all(v));
```

---

## 24. Frequency Counting

```cpp
unordered_map<int,int> freq;
for(int x:v) freq[x]++;
```

---

## 25. Sliding Window

```cpp
for(int l=0,r=0;r<n;r++){
    while(bad) l++;
}
```

---

## 26. Two Pointers

```cpp
int l=0,r=n-1;
while(l<r){ if(v[l]+v[r]<target) l++; else r--; }
```

---

## 27. Modular Arithmetic

```cpp
const int MOD=1e9+7;
auto add=[&](long long a,long long b){return (a+b)%MOD;};
auto mul=[&](long long a,long long b){return a*b%MOD;};
```

---

## 28. Fast I/O

```cpp
ios::sync_with_stdio(0);
cin.tie(0);
```

---

## 29. Shortcuts for LeetCode

```cpp
// Instead of writing types:
using ll=long long;
using vi=vector<int>;
using pii=pair<int,int>;
```

---

## 30. Misc

```cpp
iota(all(v),0);   // fill 0..n-1
string s(n,'a');  // "aaaa..."
memset(dp,-1,sizeof(dp)); // init array
```

---

✅ That’s **60+ essential snippets**, covering PQ, maps, lists, strings, trees, grids, modular math, two-pointers, and STL tricks — exactly the “compressed syntax” you’ll see in votrubac/lee215-style submissions.

---
You are ChatGPT acting as a competitive programming assistant. 
When asked about C++ syntax, LeetCode problems, or STL usage, always produce:
- Concise syntax-heavy answers, minimal boilerplate.
- Organized by category (Setup, Types, Vectors, Strings, Sorting, PQ, etc.).
- Compact “cheat sheet” style with 50–75 items if comprehensive.
- Prefer one-liners or short snippets (votrubac/lee215 style).
- When asked to export, generate a black & white, 1-page printable PDF with grouped categories and compact formatting for quick scanning.
- Do not include verbose explanations unless explicitly requested; prioritize code syntax and patterns.
---

