import concurrent.futures

def paint_quadrant(matrix, start_row, end_row, start_col, end_col, color):
    # Todo
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            matrix[row][col] = color

def divide_and_paint(matrix, colors):
    # Todo
    r1, c1 = 0, 0
    r2, c2 = 0, len(matrix[0])//2
    r3, c3 = len(matrix)//2, 0
    r4, c4 = len(matrix)//2, len(matrix)//2

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
        futures = []
        futures.append(e.submit(paint_quadrant, matrix, r1, r2, c1, c2, colors[0]))
        futures.append(e.submit(paint_quadrant, matrix, r2, r3, c2, c3, colors[1]))
        futures.append(e.submit(paint_quadrant, matrix, r3, r4, c3, c4, colors[2]))
        futures.append(e.submit(paint_quadrant, matrix, r4, len(matrix), c4, len(matrix[0]), colors[3]))

        for future in concurrent.futures.as_completed(futures):
            future.result()

# Example usage:
matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# color is given
colors = ["red","blue","green","yellow"]

divide_and_paint(matrix, colors)

# Print the painted matrix
for row in matrix:
    print(row)