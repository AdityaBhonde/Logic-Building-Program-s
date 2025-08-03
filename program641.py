def Maxium(Brr):
  iMax = 0
  i = 0
  iMax = Brr[0]
  for i in range(1 , len(Brr)):
    if(Brr[i] > iMax):
      iMax = Brr[i]
      

  return iMax  

def main():
  
 print("Enter the number of the element :")
 ilength = int(input())
 
 Arr = []

 for i in range(1 , ilength+1):
   no = int(input())
   Arr.append(no)

 iRet = Maxium(Arr)  

 print(f" the maxium number in the List is {iRet}")


  

if __name__ == "__main__":
    main()
