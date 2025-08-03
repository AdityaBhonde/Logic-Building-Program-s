def Addition(Brr):
  iSum = 0
  no = 0
  for no in Brr :
    iSum = iSum + no

  return iSum   

def main():
  
 print("Enter the number of the element :")
 ilength = int(input())
 
 Arr = []

 for i in range(1 , ilength+1):
   no = int(input())
   Arr.append(no)

 iRet = Addition(Arr)  

 print(f"Addition of all the elements is {iRet}")


  

if __name__ == "__main__":
    main()
