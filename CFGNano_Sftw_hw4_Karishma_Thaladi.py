"""
SEARCH IN MATRIX
--------
You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.
Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].
EXAMPLE INPUT
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]
target =44
EXAMPLE OUTPUT
result = [3,3]
"""


def search_in_matrix(matrix, target):
    # Matrix has a [nxm] dimension:
    rows = len(matrix)
    columns = len(matrix[0])
    # Go through the matrix
    for i in range(rows):
        for j in range(columns):

            # If the element is found
            if (matrix[i][j] == target):
                print("Element found at [", i, ",", j, "]")
                return 1

    print("Element not found: [-1,-1]")
    return 0


matrix = [[1,4,7,12,15,1000],
        [2,5,19,31,32,1001],
        [3,8,24,33,35,1002],
        [40,41,42,44,45,1003],
        [99,100,103,106,128,1004]]

search_in_matrix(matrix, 24)
search_in_matrix(matrix, 44)
search_in_matrix(matrix, 404)
