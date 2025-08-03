def Strupr(data):
    
    icount = 0
    OutPut  = ""
    for ch in data:
        if (ch >= 'a'  and ch <= 'z'):
           OutPut = OutPut + (ch  - 32)  #Error
        else:
           OutPut = OutPut + ch
    return OutPut
    
def main():
    print("Enter String:")
    str = input()
    strX = Strupr(str)
    print("updated String is {strX}")

if __name__ == "__main__":
    main()

