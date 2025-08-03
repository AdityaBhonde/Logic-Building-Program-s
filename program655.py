def CountFrequnecy(data):
   icount = 0
   for ch in str:
     if(ch == 'a'):
        icount =+ 1

   return icount    

 


def main():
  
 print("Enter String :")
 str = input()
 iRet = CountFrequnecy(str)

 print("Frequency of a in {str} is {iRet}")
 
 
  

if __name__ == "__main__":
    main()
