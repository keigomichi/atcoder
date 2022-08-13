import itertools
h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]
index_lists = [i for i in range(w1)]
for comb_rows in itertools.combinations(a, h2):
    comb_rows = list(comb_rows)
    for index_list in itertools.combinations(index_lists, w2):
        index_list = list(index_list)
        cnt = 0
        for i, comb_row in enumerate(comb_rows):
            for j, index in enumerate(index_list):
                if comb_row[index] == b[i][j]:
                    cnt += 1
        if cnt == h2 * w2:
            print('Yes')
            exit()
print('No')
