girisler=[]
count=0
while count<5:
    giris=input("Enter a value:")
    if giris.isdigit():
     girisler.append(int(giris))       
    
    else:
     girisler.append(giris)
    count+=1
    continue

print("1.girişin veri tipi: {}".format(type(girisler[0])))
print("2.girişin veri tipi: {}".format(type(girisler[1])))
print("3.girişin veri tipi: {}".format(type(girisler[2])))
print("4.girişin veri tipi: {}".format(type(girisler[3])))
print("5.girişin veri tipi: {}".format(type(girisler[4])))
