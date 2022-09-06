# biomeddatadesignweek1


Method 1:

This method solves the linear sum assignment problem by forming it into a convex optimization problem. The input matrix should have each of the doctor's prreferences as rows, with each column corresponding to a particular hospital. 

The convex optimization minimizes cost in producing a permutation matrix of only entries of 1 and 0, where 1=assignment to position and 0=no assignment to this position. The constraints for the convex optimization problem was that each row should have a sum of 1 (only one assignment per doctor) and that each column should have a sum equal to the number of assignments to that hospital. 

The number of assignments for each hospital was calculated so that each hospital would have a roughly equal number of doctors. For example, if there were 5 doctors and 5 hospitals, each hospital would only have one assignment. However, if there were 6 doctors and 5 hospitals, each hospital is calculated to have at most two possible assignments. 

A 5x4 example preference matrix was included in this code as a test. This matrix can be replaced with any desired preference matrix. 

Method 2:


