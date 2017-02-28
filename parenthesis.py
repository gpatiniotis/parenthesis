sm=0
print"to escape just press enter"
i=raw_input("give us the parenthesis")
if (i=="("):
        sm=sm+1
elif (i==")"):
        sm=sm-1
while i=="(" or i==")":
    i=raw_input("give us the parenthesis")
    if (i=="("):
        sm=sm+1
    elif (i==")"):
        sm=sm-1
if sm==0:
    print ("TRUE")
else:
    print("FALSE")
