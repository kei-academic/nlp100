word = "stressed"
n = len(word)

ans = ""
for i in range(n):
    ans += word[n-i-1]

print(ans)
