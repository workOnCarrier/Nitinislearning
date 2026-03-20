# software engineer
## Dec 7 2025

Problem 2: Efficient Tasks Across 3 Servers
You are given:
An integer n (n ≥ 3), the number of software modules.
An integer array difficulty of length n , where difficulty[i] is the difficulty of the i -th software module.
You must assign all modules to 3 servers subject to:
Each server must receive at least one module.
Every module must be assigned to exactly one server.
After a particular assignment (partition) of modules into 3 non-empty groups S1, S2, and S3 (one group per server) is fixed, you are allowed to choose one module from each server:
Choose index i1 ∈ S1 with difficulty d1 = difficulty[i1] .
Choose index i2 ∈ S2 with difficulty d2 = difficulty[i2] .
Choose index i3 ∈ S3 with difficulty d3 = difficulty[i3] .
For this assignment, define the value:
F ( S 1 , S 2 , S 3) = min[ ⁡ i 1 ∈ S 1 , i 2 ∈ S 2 , i 3 ∈ S 3] ( ∣ d 1 − d 2 ∣ + ∣ d 2 − d 3 ∣)
That is, for the given partition of modules into three servers, you choose one module from each server so that the expression 
∣ d 1 − d 2 ∣ + ∣ d 2 − d 3 ∣ ∣d1−d2∣+∣d2−d3∣ is as small as possible, and that minimal value is F for this partition.
Your overall goal is to choose an assignment of modules to the three servers that maximizes this minimal value.
In other words, over all valid partitions (S1, S2, S3) of the modules into three non-empty, disjoint sets whose union is all modules, compute:
max ⁡ ( S 1 , S 2 , S 3) F ( S 1 , S 2 , S 3)
and output this maximum.
Input:
 n,  Array difficulty[0..n-1]
Output
A single integer: the maximum possible value of F ( S 1 , S 2 , S 3) over all valid assignments.
Design an algorithm that is significantly more efficient than enumerating all possible assignments (which is exponential in n) and can handle large n (e.g., up to around 2 × 10^5).
