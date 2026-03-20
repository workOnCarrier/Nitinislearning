# product manager
## July 4 2025

Lottery Coupons: Most Popular Digit-Sum Values

Problem

You have consecutively numbered lottery coupons from 1 to n (inclusive). A coupon is a winner if the sum of its digits equals some value s.
Among all valid digit sums s in the range 1 to 9·d, where d is the number of digits of n, determine how many distinct s values produce the maximum number of winners (i.e., the most frequent digit-sum(s) among coupons 1…n).
Implement a function lotteryCoupons(n) that returns this count, and explain the algorithm’s time and space complexity.
Assume n ≥ 1 and base-10 representation.
Note: Values of s that are not achievable for 1…n simply have zero winners and do not affect the maximum.
Hints

Only the frequency of each digit-sum matters; you do not need to materialize each coupon.
Think about how to compute digit-sum frequencies efficiently for the range 1…n.