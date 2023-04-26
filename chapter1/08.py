def cipher(text):
    ans = ""
    for t in text:
        if (97 <= ord(t) <= 122):
            ans += chr(219 - ord(t))
        else:
            ans += t
    return ans

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

print(cipher(sentence))  # 暗号化
print(cipher(cipher(sentence)))  # 復号化


