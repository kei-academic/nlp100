sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word_list = sentence[:-1].replace(",", "").split(" ")

ans = []
for word in word_list:
    ans.append(len(word))

print(ans)
