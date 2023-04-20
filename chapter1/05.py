def n_gram(s, n):
    ngram_list = []
    for i in range(len(s)-n+1):
        ngram_list.append(s[i:i+n])
    return ngram_list

sentence = "I am an NLPer"
print(n_gram(sentence.split(" "), 2))  # 単語bi-gramの出力
print(n_gram(sentence.replace(" ", ""), 2))  # 文字bi-gramの出力
