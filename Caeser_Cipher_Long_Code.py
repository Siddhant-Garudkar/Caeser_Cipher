a = int(input("1.Encrypt\n2.Decrypt\nChoose: "))
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
if(a == 1):

    input = input("Enter the text which you have to encrypt: ")
    input = input.lower()
    i = 0
    j = 0
    ans = ""
    while (i!=len(input)):
        if (input[i] == " "):
            ans = ans + " "
            i = i + 1
            continue
        if (input[i] == list[j]):
            j = j + 3
            if (j > 25):
                j = j % 26
            ans = ans + list[j]
            i = i + 1
            j = 0
        else:
            j = j + 1
    print(ans)
elif(a == 2):
    input = input("Enter the text which you have to decrypt: ")
    i = 0
    j = 0
    ans = ""
    while (i!=len(input)):
        if (input[i] == " "):
            ans = ans + " "
            i = i + 1
            continue
        if (input[i] == list[j]):
            j = j - 3
            if (j > 25):
                j = j % 26
            ans = ans + list[j]
            i = i + 1
            j = 0
        else:
            j = j + 1
    print(ans)
else:
    print("Entered number is invalid")