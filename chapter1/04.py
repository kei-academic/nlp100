sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = sentence.replace(",", "").replace(".", "").split(" ")
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

alphabets = []
for i in range(len(word_list)):
    if i+1 in num_list:
        alphabets.append(word_list[i][0])
    else:
        alphabets.append(word_list[i][:2])

result = {}
n = 0
for a in alphabets:
    n += 1
    result[a] = n

print(result)
