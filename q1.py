while(True):
    n=int(input("Enter the length of list between 3 and 12: "))
    if(n>3 and n<12):
        print("The list contains",n,"entries")
        break
    else:
        print("Invalid list length. Try again!\n")
print("\n")
print(25*"*"+"Section B"+25*"*")
i=0
li=[]
while(i<n):
    print("Enter the entry at index",i,": ",end="")
    x=int(input())
    if(x>0):
        li.append(x)
        i=i+1
    else:
        print("Invalid entry at index",i,".\n")
print("\n")
print(25*"*"+"Section C"+25*"*") #printing stars along with section C in it.
target=int(input("Enter your target value: ")) #asking for target value.
target_present=0
for j in range(0,n):
    for k in range(j+1,n):
        if(li[j]+li[k]==target):
            print("The entries ",li[j],li[k],"found at index",j,k,"sum to ",target,".")
            target_present=1
if(target_present==0): #checking for the invalid sum .
    print("No valid combination summing to",target," was found.")
print("\n")
