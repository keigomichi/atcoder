# if (S > T) return 0;

#     int res = INF;
#     auto first = [&](int i) -> int {
#         int j = i;
#         for (; j < S.size(); ++j) if (S[j] > T[i]) break;
#         return (j < S.size() ? j - i : INF);
#     };
#     for (int i = 0; i < S.size() && i < T.size(); ++i) {
#         res = min(res, first(i));
#         if (S[i] < T[i]) break;
#     }
#     return (res < INF/2 ? res : -1);

t = 'atcoder'
s = input()
res = 10**10
