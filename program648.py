def Updated(Brr):
  i = 0
  Crr = []
  for i in range(len(Brr)-1 ,-1 , -1):
    if(Brr[i] % 2 == 0):
     Brr[i] = Brr[i] + 1
 
     
     

     

def main():
  
 print("Enter the number of the element :")
 ilength = int(input())
 
 Arr = []

 for i in range(1 , ilength+1):
   no = int(input())
   Arr.append(no)

   Updated(Arr)

 print(Arr)

   

 


  

if __name__ == "__main__":
    main()
