import concurrent.futures

def paint_quadrant(matrix, start_row, end_row, start_col, end_col, color):
    # Todo
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            matrix[row][col] = color

def divide_and_paint(matrix, colors):
    # Todo
    futures = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:

        futures.append(e.submit(paint_quadrant, matrix, 0, len(matrix)//2, 0, len(matrix[0])//2, colors[0]))
        futures.append(e.submit(paint_quadrant, matrix, 0, len(matrix)//2, len(matrix[0])//2, len(matrix[0]), colors[1]))
        futures.append(e.submit(paint_quadrant, matrix, len(matrix)//2, len(matrix), 0, len(matrix[0])//2, colors[2]))
        futures.append(e.submit(paint_quadrant, matrix, len(matrix)//2, len(matrix), len(matrix[0])//2, len(matrix[0]), colors[3]))

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