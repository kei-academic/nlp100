def n_gram(s, n):
    ngram_list = []
    for i in range(len(s)-n+1):
        ngram_list.append(s[i:i+n])
    return ngram_list

word1 = "paraparaparadise"
word2 = "paragraph"

x = set(n_gram(word1, 2))
y = set(n_gram(word2, 2))

print(x | y)  # 和集合
print(x & y)  # 積集合
print(x - y)  # 差集合
print("se" in x)
print("se" in y)
