def n_gram(s, n):
    ngram_list = []
    for i in range(len(s)-n+1):
        ngram_list.append(s[i:i+n])
    return ngram_list

x = set(n_gram("paraparaparadise", 2))
y = set(n_gram("paragraph", 2))

print(x | y)  # 和集合
print(x & y)  # 積集合
print(x - y)  # 差集合
print("se" in x)
print("se" in y)
