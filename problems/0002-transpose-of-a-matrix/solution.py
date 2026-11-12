def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rows = len(a)
    cols = len(a[0])

    ans=[]
    for i in range(cols):
        cur=[]
        for j in range(rows):
            cur.append(a[j][i])
        ans.append(cur)
    return ans