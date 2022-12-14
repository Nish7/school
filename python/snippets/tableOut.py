def table():
    """
    Write a function timestable(n), which prints a multiplication table of size n.
    """

    def row(n, m):
        col = ""
        for y in range(1, n + 1):
            col += f"{m*y:3}"

        return col

    def timestable(n):
        for i in range(1, n + 1):
            print(row(n, i))

    def question_5():
        n = int(input("Input the n: "))
        timestable(n)
        return
