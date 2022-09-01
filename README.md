# biomeddatadesignweek1

This code uses the hungarian algorithm to solve the linear sum assignment problem of assigning doctors to hospitals. This is a common optimization technique that minimizes (or maximizes, depending on how preference is reported) "cost", assigning the maximum number of people to their largest preference. 

The first step in this method is creating a workable cost matrix. As there may be more doctors than hospitals, each hospital can have multiple positions, ultimately making the number of positions >= the number of doctors. However, the doctor's preferences were for hospitals, not positions, so the matrix had to be expanded so the positions within a hospital had the same ranking from the same doctor. This process of matrix construction can be seen in the "expandmatrix" function and previous lines of code.

The next steps are mathematical matrix functions that ultimately calculates a permutation matrix with one "assignment" in each row and column (i.e. one doctor is assigned to one position).

First, the minimum/maximum value of each row is determined, and subtracted from every other element in the row. 
Zeros are then found and marked. The column(s) with zeros are covered, and the process of finding the maximum value and subtracting is repeated on the resulting smaller matrix. 

