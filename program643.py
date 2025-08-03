def CountEvenOdd(Brr):
  iEven = 0
  iOdd = 0
  for no in Brr :
    if(no % 2 == 0):
      iEven = iEven + 1
    else:
      iOdd = iOdd + 1
    

  return iEven , iOdd   

def main():
  
 print("Enter the number of the element :")
 ilength = int(input())
 
 Arr = []

 for i in range(1 , ilength+1):
   no = int(input())
   Arr.append(no)

 iRet1 , iRet2 = CountEvenOdd(Arr)
   

 print(f" NUmber of even element : {iRet1} & odd element : {iRet2}")


  

if __name__ == "__main__":
    main()
