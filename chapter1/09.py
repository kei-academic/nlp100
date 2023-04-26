import random

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

s_list = []
for s in sentence.split(" "):
    if len(s) > 4:
        s = s[0] + ''.join(random.sample(s[1:-1], len(s) - 2)) + s[-1]
    s_list.append(s)
    result = ' '.join(s_list)

print(result)
