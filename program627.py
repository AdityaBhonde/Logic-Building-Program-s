def Reverse(iNo):
  iDigit = 0
  iReverse = 0

  while(iNo != 0):
    iDigit = iNo % 10 
    iReverse = iReverse * 10 + iDigit
    iNo = iNo // 10


  return iReverse


def main():
  print("Enter number :")
  iValue = int(input())
  iRet = 0

  iRet = Reverse(iValue)

  print(f"The Reverse of the {iValue} is {iRet}")
 
  
  
if __name__ == "_main_":
 main()
