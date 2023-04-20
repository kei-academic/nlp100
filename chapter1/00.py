word = "stressed"
n = len(word)

result = ""
for i in range(n):
    result += word[n-i-1]

print(result)
