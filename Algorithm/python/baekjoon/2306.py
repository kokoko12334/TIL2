dna = input()

n = len(dna)
dp = [[0] * n for _ in range(n)]

for l in range(1, n):
    for i in range(n-l):
        j = i + l
        dp[i][j] = dp[i+1][j-1]
        if (dna[i] == "a" and dna[j] == "t") or (dna[i] == "g" and dna[j] == "c") :
            dp[i][j] += 2
        
        for k in range(j-i):
            dp[i][j] = max(dp[i][i+k]+dp[i+k+1][j], dp[i][j])

print(dp[0][-1])