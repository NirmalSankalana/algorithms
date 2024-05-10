def LevenshteinDistance(X, m, Y, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if X[m-1] == Y[n-1]:
        cost = 0
    else:
        cost = 1

    return min(
        LevenshteinDistance(X, m-1, Y, n) + 1,
        LevenshteinDistance(X, m, Y, n-1) + 1,
        LevenshteinDistance(X, m-1, Y, n-1) + cost,
    )


s1 = "Moratuwa"
s2 = "Colombo"

print(LevenshteinDistance(s1, len(s1), s2, len(s2)))
