sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word_list = sentence[:-1].replace(",", "").split(" ")

result = []
for word in word_list:
    result.append(len(word))

print(result)
