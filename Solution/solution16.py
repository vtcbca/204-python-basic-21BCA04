#check string palimdrome or not
s=input("enter any string:")
l=len(s)
s1=(s[::-1])
if(s1==s):
    print("string is palimdrome")
else:
    print("string is not palimdrome")


