import string

ch=input("enter string")
s=[]
for i in ch:
	if i>="A" and i=<"Z":
		s.append(i.lower())
	else:
		s.append(i.upper())
print(s)