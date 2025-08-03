def SumationFactrors(iNo):
   iSum = 0
   print(f"Factors of {iNo} is :")
   for i in range(1 , (iNo // 2)+1):
      if(iNo % i == 0):
         iSum = iSum + i
   return iSum  


def main():
  print("Enter the Number :")
  iValue = int(input())

  iRet = SumationFactrors(iValue)
  print(f"The sum of the Factor is {iRet}")

if __name__ == "__main__":
    main()
