def CountEventDigits(iNo):
  iCount  = 0
  iDigit = 0 
  while(iNo != 0):
    iDigit = iNo % 10
    if(iDigit % 2 == 0) :
     iCount = iCount + 1
     iNo = iNo // 10

  return iCount   

def main():
  print("Enter number :")
  iValue = int(input())

  iRet = 0
  iRet = CountEventDigits(iValue)

  print(f"The number of the digit is {iRet}")
  
if __name__ == "_main_":
 main()
