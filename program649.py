def Revers(Brr):
  iStart = Brr[0]
  iEnd = len(Brr)-1
  iTemp = 0
  while(iStart < iEnd) :
    iTemp  = Brr[iStart]
    Brr[iStart] = Brr[iEnd]

    iStart += 1
    iEnd -= 1
     
     

     

def main():
  
 print("Enter the number of the element :")
 ilength = int(input())
 
 Arr = []

 for i in range(1 , ilength+1):
   no = int(input())
   Arr.append(no)

Revers(Arr)
print(Arr)

   

 


  

if __name__ == "__main__":
    main()
