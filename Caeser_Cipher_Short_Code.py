def ceaserEncrypt(s):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = s.upper()
    l = s.split()
    str = ""
    for ch in l:
        i = 0
        while i<len(ch):
            d = ch[i]
            i+=1
            pos = alphabet.index(d)
            if pos + 3 > 25:
                str += alphabet[(pos+3)%26]
            else:
                str += alphabet[pos+3]
        str +=" "

    return str

def ceaserDecrypt(s):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = s.upper()
    l = s.split()
    str = ""
    for ch in l:
        i = 0
        while i<len(ch):
            d = ch[i]
            i+=1
            pos = alphabet.index(d)
            if pos - 3 < 0:
                str += alphabet[(pos-3)+26]
            else:
                str += alphabet[pos-3]
        str +=" "
    str = str.lower()

    return str
a = int(input("1.Encrypt\n2.Decrypt\nChoose: "))
if a == 1:
    print(ceaserEncrypt(input("Enter your plain text to encrypt: ")))
elif a == 2:
    print(ceaserDecrypt(input("Enter your plain text to encrypt: ")))
else:
    print("Number is not valid")