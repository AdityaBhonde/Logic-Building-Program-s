def CheckPerfect(iNo):
   iSum = 0
   print(f"Factors of {iNo} is :")
   for i in range(1 , (iNo // 2)+1):
      if(iNo % i == 0):
         iSum = iSum + i
    
   if(iSum == iNo):
      return True
   else :
      return False


def main():
  print("Enter the Number :")
  iValue = int(input())

  iRet = CheckPerfect(iValue)
  if(iRet == True):
     print(f"The {iValue} is the perfect Number")
  else:
     print(f"The {iValue} is not the perfect Number ")   

  

if __name__ == "__main__":
    main()
