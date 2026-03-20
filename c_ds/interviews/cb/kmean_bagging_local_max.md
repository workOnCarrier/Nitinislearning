# machine learning engineer
Task 1 — Find local maxima

Given an integer array a of length n (1 <= n <= 2e5), return all indices i that are local maxima.
Definition:
For 0 < i < n-1 : a[i] is a local maximum if a[i] > a[i-1] and a[i] > a[i+1] .
For endpoints: i = 0 is a local maximum if n==1 or a[0] > a[1] ; i = n-1 is a local maximum if a[n-1] > a[n-2] .
Output the indices in increasing order.
Task 2 — Implement a bagging classifier

Implement a BaggingClassifier that trains M base classifiers on bootstrap samples and predicts by majority vote.
You are given a BaseClassifier object with:
fit(X, y)
predict(X) which returns a label for each row of X
Your BaggingClassifier should support:
constructor parameters: n_estimators=M , sample_size (default = len(X) ), random_seed
fit(X, y) that trains M independent base models on bootstrap samples (sample with replacement)
predict(X) that returns the majority-vote label per example; if there is a tie, return the smallest label.
Constraints: N = len(X) <= 2e5, M <= 200.
Task 3 — Implement k-means clustering

Implement k-means clustering given:
X : N x D array of floats
k : number of clusters
dist(p, q) : provided distance function between two points
max_iter (e.g., 100)
Requirements:
Initialize centroids using the first k points of X (deterministic).
Repeat until convergence or max_iter :
Assign each point to the nearest centroid (break ties by choosing the smallest centroid index).
Recompute each centroid as the mean of its assigned points.
If a cluster becomes empty, keep its centroid unchanged.
Return final centroids and the cluster assignment for each point.
(You may assume 1 <= k <= N, D <= 50.)