Bacon_dict = { 
    'AAAAA':'a','AAAAB':'b','AAABA':'c','AAABB':'d','AABAA':'e','AABAB':'f','AABBA':'g',
    'AABBB':'h','ABAAA':'{i|j}','ABAAB':'k','ABABA':'l','ABABB':'m','ABBAA':'n',
    'ABBAB':'o','ABBBA':'p','ABBBB':'q','BAAAA':'r','BAAAB':'s','BAABA':'t','BAABB':'{u|v}',
    'BABAA':'w','BABAB':'x','BABBA':'y','BABBB':'z'
}

bacon = "01011 11111 10110 11011 01100 10001 01011 11111 10110 11011 01100 10001 11001 01111 11111 11110 11111 11110 01111 01100 01110 11000 11111 10011 11100 10001 01100 01101 11111 10101 10111 01101 01101 10101 11011 10100 11111 10110 11011 01100 10001 11000 10111 11100 11011 01101".replace("0","B").replace("1","A")

listBacon = bacon.split(" ")

for i in range(len(listBacon)):
    listBacon[i] = Bacon_dict[listBacon[i]]
print("\n" + ''.join(listBacon).upper()+"\n")
print(''.join(listBacon).replace("{","").replace("}","").replace("|","").replace("j","").replace("v","").upper())