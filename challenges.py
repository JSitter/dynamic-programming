class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]:  # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else:  # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.

    return dp_table[rows-1][cols-1]


def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    pass


def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.

    return dp_table[rows-1][cols-1]


def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2))

    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[-1])
    else:
        return 1 + min(edit_distance(str1, str2[:-1]), edit_distance(str1[:-1], str2), edit_distance(str1[:-1], str2[:-1]))


def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for index in range(len(cols)):
        dp_table[0][index] = index

    for index in range(cols):
        dp_table[index][0] = index

    for row_index in range(len(dp_table)-1):
        for col_index in range(len(row)-1):
            if dp_table[col_index + 1][row_index + 1] == dp_table[row_index + 1][col_index + 1]:
                dp_table
            else:

    return dp_table[rows-1][cols-1]


if __name__ == "__main__":
    s1 = 'cat'
    s2 = 'halt'
    print(edit_distance(s1, s2))
