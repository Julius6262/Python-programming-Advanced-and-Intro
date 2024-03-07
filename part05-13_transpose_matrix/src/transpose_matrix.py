# Write your solution here
def transpose(matrix: list):
    n = len(matrix)
    print(n)
    for i in range(n):
        for j in range(i, n):
            print(range(i,n))
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

# Your transpose function here

# Main program outside if __name__ == "__main__": block
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose(matrix)

# Print the transposed matrix
for row in matrix:
    print(row)

