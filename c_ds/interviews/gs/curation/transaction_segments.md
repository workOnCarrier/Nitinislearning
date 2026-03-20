# software engineer
## Dec 07 2025

Problem 1: Transaction Segments
You are given:
An integer n , the length of an array.
An integer k (1 ≤ k ≤ n).
An integer array transactionValues of length n , where transactionValues[i] represents the transaction amount at time i (0-based index).
A contiguous segment transactionValues[l..r] (where 0 ≤ l ≤ r < n) is called strictly increasing if:
For every i with l ≤ i < r , we have transactionValues[i] < transactionValues[i + 1] .
Your task is to count how many contiguous subarrays of length exactly k are strictly increasing.
Formally, count the number of starting indices s such that:
0 ≤ s ≤ n - k , and
transactionValues[s] < transactionValues[s + 1] < ... < transactionValues[s + k - 1] .
Input
n , k
Array transactionValues[0..n-1]
Output
A single integer: the number of strictly increasing contiguous subarrays of length exactly k .
Design an algorithm that runs efficiently for large n (e.g., up to around 2 × 10^5).