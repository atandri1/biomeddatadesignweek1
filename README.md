# biomeddatadesignweek1

This code uses the hungarian algorithm to solve the linear sum assignment problem of assigning doctors to hospitals. This is a common optimization technique that minimizes (or maximizes, depending on how preference is reported) "cost", assigning the maximum number of people to their largest preference. 

In our code, we interpreted higher scores as greater preference. For example, if a doctor rates a hospital a "3" and another a "1", this says he prefers the hospital rated "3" more as it has been assigned more preference points. Therefore, we use the hungarian algorithm to maximize, rather than minimize cost. 

The first step in this method is creating a workable cost matrix. As there may be more doctors than hospitals, each hospital can have multiple positions, ultimately making the number of positions >= the number of doctors. However, the doctor's preferences were for hospitals, not positions, so the matrix had to be expanded so the positions within a hospital had the same ranking from the same doctor. This process of matrix construction can be seen in the "expandmatrix" function and previous lines of code.

The next steps are mathematical matrix functions that ultimately calculates a permutation matrix with one "assignment" in each row and column (i.e. one doctor is assigned to one position).

