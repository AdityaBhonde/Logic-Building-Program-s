def DisplayFactrors(iNo):
   print(f"Factors of {iNo} is :")
   for i in range(1 , (iNo // 2)+1):
      if(iNo % i == 0):
         print(i)
      


def main():
  print("Enter the Number :")
  iValue = int(input())

  DisplayFactrors(iValue)

if __name__ == "__main__":
    main()
