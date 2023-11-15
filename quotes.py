print("################### YOUR QUOTE BUCKET #################")

lists=[]

add=1
while add:
    quote=input("Enter your quote: ")
    lists.append(quote)
    print(" Quote added successfully....")
    temp=input("Do you want to add another quote? y/n :\n")
    if temp=='n':
        add=0


#sleep 1
#clear

ans=input("Do you want to list all quotes? y/n :\n")

if ans=='y':
    for quotes in lists:
        print(quotes)
        print('\n')
else:
    print("Come back anytime to add/read your quotes")
        

