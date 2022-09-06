"""
This program matches the number of patient/hospitals to doctors who have limited capacity.
The matching is based on the preference of the patients/hospitals request using Hungarian methods.
The whole program implements the following functions:
1. sanitation check for a given matrix
2. finding minimal values in a given matrix
3. subtracting a certain value from a given matrix
4. calculating the minimum number of lines needed to cover a certain value in a given matrix
5. printing out final matching list for patients/hospitals and doctors
"""

import numpy


# This function performs a sanity check before matrix operations
def sanity_check(matrix):
    # Record the row and column size of a matrix
    row_num = len(matrix)
    col_num = len(matrix[0]) if row_num > 0 else 0

    # Return false if matrix is empty
    if row_num == 0 or col_num == 0:
        return False

    # Return false if column size varies in different row
    for row in matrix:
        if len(row) != col_num:
            return False

    return True


# This function returns the minimum value in each row of the given matrix
def min_value_in_row(matrix):
    min_row_value_list = []

    for row in matrix:
        min_row_value = row[0]
        for col in row:
            if col < min_row_value:
                min_row_value = col
        min_row_value_list.append(min_row_value)

    return min_row_value_list


# This function returns the minimum value in each column of the given matrix
def min_value_in_col(matrix):
    min_col_value_list = matrix[0]

    for row in matrix:
        position = 0
        for col in row:
            if col < min_col_value_list[position]:
                min_col_value_list[position] = col
            position += 1

    return min_col_value_list


# This function subtract given values in the value list from each row in the matrix
def subtract_value_from_row_matrix(matrix, value_list):
    subtracted_matrix = []
    row_num = 0

    for row in matrix:
        subtracted_matrix.append([])
        for col in row:
            subtracted_matrix[row_num].append(col - value_list[row_num])
        row_num += 1

    return subtracted_matrix


# This function subtract given values in the value list from each column in the matrix
def subtract_value_from_col_matrix(matrix, value_list):
    subtracted_matrix = []
    row_num = 0

    for row in matrix:
        col_num = 0
        subtracted_matrix.append([])
        for col in row:
            subtracted_matrix[row_num].append(col - value_list[col_num])
            col_num += 1
        row_num += 1

    return subtracted_matrix


# check whether a position has a zero covering it
def covered_by_star_zero(matrix, row_index, col_index):
    row_size = len(matrix)
    col_size = len(matrix[0])

    for i in (0, row_size):
        if (matrix[i][col_index] == -1):
            return True

    for j in (0, col_size):
        if (matrix[row_index][j] == -1):
            return True

    return False


# return the column covered with 0*
def column_covering(matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])

    covered_list = []

    for j in (0, col_size):
        for i in (0, row_size):
            if matrix[i][j] == -1:
                covered_list.append([i, j, 0])

    return covered_list


# non-covered zero with star in same row
def non_covered_zero_with_zero_in_same_row(covered_list, row_index, col_index):
    for i in (0, len(covered_list)):
        if covered_list[i][0] == row_index:
            covered_list[i][1] == col_index
            covered_list[i][2] = 1

    return covered_list


# non-covered zero without star in same row
def non_covered_zero_without_zero_in_same_row(matrix, covered_list, row_index, col_index):
    position = find_zero_in_same_col(matrix, col_index)

    if not position[0] == 0:
        star = find_zero_in_same_row(matrix, position[1][0])
        matrix[position[1][0]][position[1][1]] = -2
        matrix[star[0]][star[1]] = -1
        matrix[row_index][col_index] = -1

    return matrix


def find_zero_in_same_row(matrix, row_index):
    col_size = len(matrix[0])

    position = []

    for j in (0, col_size):
        if matrix[row_index][j] == -2:
            position = [row_index][j]

    return position


def find_zero_in_same_col(matrix, col_index):
    row_size = len(matrix)

    position_of_zero_with_star = [0, []]

    for i in (0, row_size):
        if matrix[i][col_index] == -1:
            position_of_zero_with_star[0] = 1
            position_of_zero_with_star[1] = [i, col_index]

    return position_of_zero_with_star


# assign zeros in the matrix with "stars" value: -1
def star_zero_in_matrix(matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])

    new_matrix = []

    for i in (0, row_size):
        new_matrix.append([])
        for j in (0, col_size):
            if matrix[i][j] == 0 and not covered_by_star_zero(matrix, i, j):
                new_matrix[i][j] = -1
            else:
                new_matrix[i][j] = matrix[i][j]

    return new_matrix


def doc_match(preference_matrix):
    if not sanity_check(preference_matrix):
        print("Input Matrix had invalid size.")
        return

    operation_matrix = subtract_value_from_row_matrix(preference_matrix, min_value_in_row(preference_matrix))
    operation_matrix = subtract_value_from_col_matrix(operation_matrix, min_value_in_col(operation_matrix))

    return 0


test_matrix = [[1]]

doc_match(test_matrix)
