
// The input is a list of hospitals and schedule of doctors corresponding to each hospital that are scheduled
// i.e. if there are n hospitals and m schedules... each element A[i][j] for 0 <= i < n and 0 <= j < m 
// gives the id of the doctor on duty
// how will you find the number of doctors who visit more than one hospital

#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;


template <class F>
void parallelFor(size_t begin, size_t end, size_t numThreads, F fn) {
    if (end <= begin) return;
    numThreads = max<size_t>(1, min(numThreads, end - begin));

    vector<thread> threads;
    threads.reserve(numThreads);

    size_t total = end - begin;
    size_t chunk = (total + numThreads - 1) / numThreads;

    for (size_t t = 0; t < numThreads; ++t) {
        size_t b = begin + t * chunk;
        if (b >= end) break;
        size_t e = min(end, b + chunk);
        threads.emplace_back([=, &fn]() {
            for (size_t i = b; i < e; ++i) fn(i);
        });
    }
    for (auto& th : threads) th.join();
}


/**
 * Count how many doctors appear in more than one hospital.
 * A is n x m where A[i][j] is the doctorId scheduled at hospital i, slot j.
 *
 * Strategy:
 * 1) Parallel over hospitals: build unordered_set<int> of doctors per hospital (dedupe within hospital).
 * 2) Parallel aggregation: for each hospital-set, increment a global doctor->hospitalCount
 *    using striped shards (to reduce contention).
 * 3) Count how many doctors have hospitalCount > 1.
 */
size_t countDoctorsVisitingMoreThanOneHospital(const vector<vector<int>>& A) {
    if (A.empty()) return 0;
    const size_t n = A.size();

    // -------- Phase 1: build per-hospital sets in parallel --------
    vector<unordered_set<int>> perHospitalSets(n);
    const size_t numThreads = max<size_t>(1, thread::hardware_concurrency());
    parallelFor(0, n, numThreads, [&](size_t i) {
        const auto& row = A[i];
        unordered_set<int> s;
        s.reserve(row.size() * 2);
        for (int doc : row) s.insert(doc);
        perHospitalSets[i] = std::move(s);
    });

    // -------- Phase 2: aggregate into global map with striped shards --------
    // Choose number of shards (power of two usually good). 64 is a decent default.
    const size_t SHARDS = 64;
    vector<unordered_map<int, int>> shardMaps(SHARDS);
    vector<mutex> shardLocks(SHARDS);

    auto shardIndex = [&](int key) -> size_t {
        return std::hash<int>{}(key) & (SHARDS - 1); // SHARDS must be power of two
    };

    parallelFor(0, n, numThreads, [&](size_t i) {
        for (int doc : perHospitalSets[i]) {
            size_t si = shardIndex(doc);
            lock_guard<mutex> g(shardLocks[si]);
            shardMaps[si][doc] += 1;  // increment # of distinct hospitals for this doc
        }
    });

    // -------- Phase 3: count how many doctors appear in > 1 hospital --------
    size_t answer = 0;
    for (size_t si = 0; si < SHARDS; ++si) {
        for (const auto& kv : shardMaps[si]) {
            if (kv.second > 1) ++answer;
        }
    }
    return answer;
}

// ------------------- Demo -------------------
int main() {
    // 3 hospitals, 5 time slots each
    vector<vector<int>> A = {
        {1, 2, 3, 1, 4},  // hospital 0 -> {1,2,3,4}
        {3, 3, 5, 6, 7},  // hospital 1 -> {3,5,6,7}
        {8, 2, 9, 7, 7}   // hospital 2 -> {8,2,9,7}
    };

    size_t cnt = countDoctorsVisitingMoreThanOneHospital(A);
    cout << "Doctors visiting > 1 hospital: " << cnt << "\n";

    return 0;
}
