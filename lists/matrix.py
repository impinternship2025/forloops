def print_the_rows_and_sums(matrix):

    for row in matrix:
        row_sum = 0

        for number in row:
            row_sum += number

        print(row, "Sum =", row_sum)


matrix = [[1, 2], [3, 4], [5, 6]]

print_the_rows_and_sums(matrix)     