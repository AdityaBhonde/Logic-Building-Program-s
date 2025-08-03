def ReverseArray(Brr):
  i = 0
  Crr = []
  for i in range(len(Brr)-1 ,-1 , -1):
    if(Brr[i] % 2 == 0):
     Crr.append(Brr[i])
  return Crr   
     
     

     

def main():
  
 print("Enter the number of the element :")
 ilength = int(input())
 
 Arr = []

 for i in range(1 , ilength+1):
   no = int(input())
   Arr.append(no)

 Data = ReverseArray(Arr)

 print(Data)

   

 


  

if __name__ == "__main__":
    main()
