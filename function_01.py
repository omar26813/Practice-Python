def pt():
 n=int(input("Enter a number:"))
 for i in range(n,0,-1):
   print("*"*i)
   
   
pt()   

def pt2(n):
 #n=int(input("Enter a number:"))
 if (n==0):
   return
 print("*"*n)

 pt2(n-1)


pt2(5)   