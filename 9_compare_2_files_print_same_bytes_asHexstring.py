#this script is example of finding same bytes at same position in two different files

with open ("C:\\Users\\DFIR_GUY\\Downloads\\download.dat","rb") as file1:
    data1 = file1.read()

with open ("C:\\Users\\DFIR_GUY\\Downloads\\download(1).dat","rb") as file2:
    data2 = file2.read()

same_data_integers = []
#for end of cycle set the smaller file 
for i in range(0,len(data2)):
    if data1[i]==data2[i]:
        same_data_integers.append(data1[i])

print(bytes(same_data_integers).hex())