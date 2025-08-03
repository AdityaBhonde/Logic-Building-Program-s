
def CountVowels(data):
   
   pattern = "aeiouAEIOU"
   icount = 0
   for ch in str:
      if(ch in pattern):
        icount =+ 1

   return icount    

 


def main():
  
 print("Enter String :")
 str = input()
 iRet = CountVowels(str)

 print("Frequency of a Vowels in {str} is {iRet}")
 
 
  

if __name__ == "__main__":
    main()
