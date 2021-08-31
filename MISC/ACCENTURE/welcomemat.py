# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be NxM. (N is an odd natural number, and M is 3 times N).
# The design should have ‘WELCOME’ written in the center.
# The design pattern should only use |, . and – characters.


# Input Format

# A single line containing the space separated values of N and M.

# Output Format

# Output the design pattern.

# Size: 7 x 21

# ---------. | .---------

# ------. | .. | .. | .------

# ---. | .. | .. | .. | .. | .---

# -------WELCOME-------

# ---. | .. | .. | .. | .. | .---

# ------. | .. | .. | .------

# ---------. | .---------


N, M = map(int, input().split())

for i in range(1, N, 2):

    print((i*".|.").center(3*N, "-"))

    print("-WELCOME-".center(3*N, "-"))

for i in range(N - 2, -1, -2):

    print((i*".|.").center(3*N, "-"))
