function FLOYD_WARSHALL_BLACK_WHITE(Ww, Wb):
    D_white = FLOYD_WARSHALL_WHITE_ONLY(Ww)
    n = Ww.rows

    D_bw = matrix(n, n, infinity)

    for i from 1 to n:
        for j from 1 to n:
            for a from 1 to n:
                for b from 1 to n:
                    if Wb[a][b] > 0: 
                        path_length = D_white[i][a] + Wb[a][b] + D_white[b][j]
                        D_bw[i][j] = min(D_bw[i][j], path_length)

    return D_bw
