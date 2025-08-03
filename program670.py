#input 4
# 4 3 3 1 2 3 4
def Display(iNo):
    i = 0
    for i in range(iNo , 0 , -1):
        print(i , end = "\t")

    for i in range(2 , iNo + 1 , 1):
        print(i , end = "\t")   
    

def main(): 
   print("Enter the value :")
   iValue = int(input())

if __name__ == "__main__":
    main()

