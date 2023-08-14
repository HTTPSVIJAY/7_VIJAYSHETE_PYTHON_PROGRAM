n = 5

# Upper triangle
for rows in range(1, n + 1):
    # Print spaces
    for columns in range(n, rows, -1):
        print(" ", end="")

    # Print asterisk
    print("*", end="")

    # Print spaces between edges
    for columns in range(1, (rows - 1) * 2 + 1):
        print(" ", end="")

    # Print asterisk at the end or newline
    if rows == 1:
        print()
    else:
        print("*")

# Lower triangle
for rows in range(n - 1, 0, -1):
    # Print spaces
    for columns in range(n, rows, -1):
        print(" ", end="")

    # Print asterisk
    print("*", end="")

    # Print spaces between edges
    for columns in range(1, (rows - 1) * 2 + 1):
        print(" ", end="")

    # Print asterisk at the end or newline
    if rows == 1:
        print()
    else:
        print("*")
