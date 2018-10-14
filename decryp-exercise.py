### Encrypted text ###

#list
crypt: list = [letter for letter in "NCYXYWCSZBVXSVQKCYZYXRCIYAZRNCTZVMKTCTXYZIZSVUKICXYZIZAKBKPVSXRCIC\
RKQCYWCSZTZTXMKIRZBCTYRCIZFSZWCTXCRZBPKTPVTYZQCTXCUKTWCTYYZZIXPSKC\
YWCBKPKRCZXRCAWSVQCYYZWVFVQCXWCSYZIVZSKRVXRCSWCSVRKCIYVIFBCZTZKEVX\
YZICTXNVIYQKRNCZRCACXVMVIEVYZIVZCAKICTVXWCTKUKBKQVQYZZIVXFSVIYNVAU\
SZIVZXKAVFKICYZXTCBCYZIZSZACSXYZYXVWVFCYBVZSVQKCXYZZIXSZACSYZXZKEV\
XTCBCYWSCWVFVIQVZXWZSVYWSCWVFVIQVZWCBKPKRVXVBVSAKTPVYZAZSAZSCXWVSV\
YAKZAKTACXYAVTZBVXCWKIKCIYWZUBKRVZWCRCXVYWCRCZBCXQVYWCSZMVBKQCXYAZ\
RNCTZFSZWCTXRCIYKIQKMKQZCTZVSAVQCTXRCIYWVBCTZXSCRVTYYZCPSVTXVSAVTY\
WSKAKPKMVTZFSKPVIXWCSYPCQCTZBVQCTXYRCAKQVZXFBCSKCTVYRCAKQVZXYWSCMC\
RVIQCZVXBCTYWCBKRKVTZXKITZBPVIQCYVZBCTXRVWKPVBKTPVTYZBVXWCBKRKVYXZ\
KPCZTZTXSCIQVTYICRPZSIVTZXTKIYWSKTVZIKXSZKQCYZYXYRBVSCZXTKIYWVSPKR\
KWVSZVXIKIFZIYPSKUZIVBZXZIVYAZBPKPZQZKIQKFIVQVXRCBFCYVZCRNCXKIJCSP\
ZIVQCTYOZIPCZVXBVYAZIKRKWVBKQVQZXY"]

### Decryption methods ###

#string
cryptStr = ''.join(crypt)

#Letter frequency
letter_histogram: dict = {}

for l in crypt:
    try:
        letter_histogram[l] = letter_histogram[l] + 1
    except:
        letter_histogram[l] = 1

#Letter patterns
patterns={}

for sublen in range(2,int(len(cryptStr)/2)):
    for i in range(0,len(cryptStr)-sublen):
        sub = cryptStr[i:i+sublen]
        cnt = cryptStr.count(sub)
        if cnt >= 2 and sub not in patterns:
             patterns[sub] = cnt

### Replacement algorithm ###

test_crypt: list = []

for i in crypt:
    if(i == ''):               
       test_crypt.append('')
    elif(i == ''):
       test_crypt.append('')
    elif(i == ''):             
       test_crypt.append('') 
    elif(i == ''):             
        test_crypt.append('')  
    else:                                 
        test_crypt.append(i)

decrypt = ''.join(test_crypt)

### Print results ###
print("____________________Letter Frequency____________________\n")
print(sorted(letter_histogram.values()))
print(sorted(letter_histogram, key=letter_histogram.__getitem__))
print("\n____________________Letter Patterns____________________\n")
print(sorted(patterns, key=patterns.__getitem__))
print("\n____________________Replacement Decryption____________________\n")
#print(decrypt)

