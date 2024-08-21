class Solution:
    def strangePrinter(self, s: str) -> int:
        ss = "".join(char for char in s)
        n = len(ss)
        if n<1:
            return 0
            
        mins = [[0] * n for _ in range(n)]

        for i in range(n):
            mins[i][i] = 1

        for l in range(2, n + 1):
            for start in range(n - l + 1):
                end = start + l - 1

                mins[start][end] = l

                for subs in range(l - 1):
                    total = (mins[start][start + subs]+ mins[start + subs + 1][end])

                    if ss[start + subs] == ss[end]:
                        total -= 1

                    mins[start][end] = min(mins[start][end], total)

        return mins[0][n - 1] 