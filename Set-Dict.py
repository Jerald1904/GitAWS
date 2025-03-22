a={''} 
n=int(input("Enter the number -"))
for i in range(n):
  s=input("Enter the value -")
  a.add(s)
a.remove('')
print(a) 

j={}
n=int(input("Enter the number -"))
for i in range(n):
  s=input("Enter the Key -")
  k=input("Enter the item -")
  j.update({s:k})
print(j)
