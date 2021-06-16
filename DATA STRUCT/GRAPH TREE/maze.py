# Consider a rat placed at(0, 0) in a square matrix of order N * N. It has to reach the destination at(N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
# Note: In a path, no cell can be visited more than one time.

from typing import List


def isSafe(row: int, col: int,
           m: List[List[int]], n: int,
           visited: List[List[bool]]) -> bool:

    if (row == -1 or row == n or
        col == -1 or col == n or
            visited[row][col] or m[row][col] == 0):
        return False

    return True


def printPathUtil(row: int, col: int,
                  m: List[List[int]],
                  n: int, path: str,
                  possiblePaths: List[str],
                  visited: List[List[bool]]) -> None:

    # This will check the initial point
    # (i.e. (0, 0)) to start the paths.
    if (row == -1 or row == n or
        col == -1 or col == n or
            visited[row][col] or m[row][col] == 0):
        return

    # If reach the last cell (n-1, n-1)
    # then store the path and return
    if (row == n - 1 and col == n - 1):
        possiblePaths.append(path)
        return

    visited[row][col] = True

    # Try for all the 4 directions (down, left,
    # right, up) in the given order to get the
    # paths in lexicographical order

    # Check if downward move is valid
    if (isSafe(row + 1, col, m, n, visited)):
        path += 'D'
        printPathUtil(row + 1, col, m, n,
                      path, possiblePaths, visited)
        path = path[:-1]

    # Check if the left move is valid
    if (isSafe(row, col - 1, m, n, visited)):
        path += 'L'
        printPathUtil(row, col - 1, m, n,
                      path, possiblePaths, visited)
        path = path[:-1]

   # Check if the right move is valid
    if (isSafe(row, col + 1, m, n, visited)):
        path += 'R'
        printPathUtil(row, col + 1, m, n,
                      path, possiblePaths, visited)
        path = path[:-1]

    # Check if the upper move is valid
    if (isSafe(row - 1, col, m, n, visited)):
        path += 'U'
        printPathUtil(row - 1, col, m, n,
                      path, possiblePaths, visited)
        path = path[:-1]

    # Mark the cell as unvisited for
    # other possible paths
    visited[row][col] = False

# Function to store and print
# all the valid paths


def printPath(m: List[List[int]], n: int) -> None:

    # vector to store all the possible paths
    possiblePaths = []
    path = ""
    visited = [[False for _ in range(MAX)]
               for _ in range(n)]

    # Call the utility function to
    # find the valid paths
    printPathUtil(0, 0, m, n, path,
                  possiblePaths, visited)

    # Print all possible paths
    for i in range(len(possiblePaths)):
        print(possiblePaths[i], end=" ")


# Driver code
if __name__ == "__main__":

    m = [[1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1]]
    n = len(m)

    printPath(m, n)
