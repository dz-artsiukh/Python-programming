en_alpha_0 = 'abcdefghijklmnopqrstuvwxyz'
en_alpha_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encr_EN(text, step):
    enc_text = ''
    for i in text:
        if i in en_alpha_0:
            enc_text += en_alpha_0[(en_alpha_0.index(i) + step) % 26]
        elif i in en_alpha_1:
            enc_text += en_alpha_1[(en_alpha_1.index(i) + step) % 26]
        else:
            enc_text += i
    return enc_text    

text = input().split()
for i in text:
    a = ''
    for j in i:
        if j in en_alpha_0 or j in en_alpha_1:
            a += j
    print(encr_EN(i, len(a)), end=' ')