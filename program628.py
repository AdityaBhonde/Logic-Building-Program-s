def CountDigitX(iNo):
  iCount  = 0
  iDigit = 0 
  while(iNo != 0):
    iDigit = iNo % 10
    if(iDigit  == 5) :
     iCount = iCount + 1
     iNo = iNo // 10

  return iCount   

def main():
  print("Enter number :")
  iValue = int(input())

  iRet = 0
  iRet = CountDigitX(iValue)
  

  print(f" the Frequency of 5 in {iValue} is {iRet}")
  
if __name__ == "_main_":
 main()

