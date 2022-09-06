# biomeddatadesignweek1

## Goal

The goal of the project will be to write a piece of software (possible languages are Python, Julia, and MATLAB), that matches N patients with K doctors. Each patient is allowed to provide a ranked list of their preference for doctors, however doctors are prohibited from displaying preferences for patients. Thus the code should takes in the following:

- A list of ranked preferences, 1 list for each patient
- A maximum capacity for each doctor (can initially assume the same capacity - note the
total capacity should exceed the number of patients

And the code should return:

- A list of assignments indicating which doctors are to take care of which patients

## Solution

The first step is to "duplicate" doctors. For example, if there is a doctor with max capacity of C, then we replace the doctor with C doctors with max capacity of 1. Of course patients have the same preference for these C doctors as the replaced doctors.

After that, assuming that we have N patients and K doctors. We have an expanded preference matrix and now we should find the best matching for max preference sum. This problem can be sovled by direct calling ``scipy.linear_sum_assignment()``. We solved the problem using two methods: convex optimization Kuhn–Munkres algorithm.

**Convex Optimization (method_1)**

This method solves the linear sum assignment problem by forming it into a convex optimization problem. The input matrix should have each of the doctor's prreferences as rows, with each column corresponding to a particular hospital.

The convex optimization minimizes cost in producing a permutation matrix of only entries of 1 and 0, where 1=assignment to position and 0=no assignment to this position. The constraints for the convex optimization problem was that each row should have a sum of 1 (only one assignment per doctor) and that each column should have a sum equal to the number of assignments to that hospital.

The number of assignments for each hospital was calculated so that each hospital would have a roughly equal number of doctors. For example, if there were 5 doctors and 5 hospitals, each hospital would only have one assignment. However, if there were 6 doctors and 5 hospitals, each hospital is calculated to have at most two possible assignments.

A 5x4 example preference matrix was included in this code as a test. This matrix can be replaced with any desired preference matrix.

**Hungarian (Kuhn–Munkres) Algorithm (method_2)**

Let X be the set of N nodes (patients), Y be the set of K nodes (doctors), C be the preference matrix. X, Y and C forms an undirected bipartite graph. 

Every node in X and Y is given a label. Let LX be the vector of label for nodes in X, and LY be the vector of label for nodes in Y. Label must satisfy:

```python 
LX[x]+LY[y]>=C[x,y]
```
 
We initialize label by:

```python
LX = np.max(C,axis=1)
LY = np.zeros((K))
```

Then we begin to match every x in X, from the 0-th to (N-1)-th. Every time when we match a new node x, we try to find an augmenting path through matched x-y, which starts on x and ends on unmatched y. Every edge in the augmenting path must satisfy:

```python
LX[x]+LY[y]==C[x,y]
```

We use bool vector visitx (or visity) to mark whether x in X (or y in Y) is in the augmenting path. We use depth-first search ```DFS()``` to find the the augmenting path. 
- If ```DFS()``` returns True, then we found the augmenting path. By reversing matched and unmatched edges in the augmenting path we achieve the best matching for this part of x in X.
- If ```DFS()``` returns False, there must be the condition below between {matched x in X, the new added x} and {unmatched y in Y}:
  ```python
    LX[x]+LY[y]>C[x,y]
  ```
  Then LX and LY should be updated. We only update LX and LY for x,y in the augmenting path. Let Delta be min LX+LY-C between {matched x in X, the new added x} and {unmatched y in Y}. Update:

  ```python
  LX = LX - Delta*visitx
  LY = LY + Delta*visity
  ```
  Then try to find the augpathing again.

Reference:

[Hungarian algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm)

[Hungarian (Kuhn–Munkres) Algorithm with DFS](https://blog.csdn.net/lemonxiaoxiao/article/details/108704280?ops_request_misc=&request_id=&biz_id=102&utm_term=KM%E7%AE%97%E6%B3%95&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-108704280.nonecase&spm=1018.2226.3001.4187)