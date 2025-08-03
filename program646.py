def ReverseArray(Brr):
  i = 0

  for i in range(len(Brr)-1 ,-1 , -1):
    print(Brr[i])

     

     

def main():
  
 print("Enter the number of the element :")
 ilength = int(input())
 
 Arr = []

 for i in range(1 , ilength+1):
   no = int(input())
   Arr.append(no)

 ReverseArray(Arr)
   

 


  

if __name__ == "__main__":
    main()
