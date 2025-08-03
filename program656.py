
def CountVowels(data):
   icount = 0
   for ch in str:
     if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o'or ch == 'u'or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        icount =+ 1

   return icount    

 


def main():
  
 print("Enter String :")
 str = input()
 iRet = CountVowels(str)

 print("Frequency of a Vowels in {str} is {iRet}")
 
 
  

if __name__ == "__main__":
    main()
