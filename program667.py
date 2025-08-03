def Strupr(data):
    
    icount = 0
    OutPut  = ""
    for ch in data:
        if (ch >= 'a'  and ch <= 'z'):
           OutPut = OutPut + chr(ord(ch)  - 32)    # ord is the function to convert char to the ASCII value   
        else:
           OutPut = OutPut + ch
    return OutPut
    
def main():
    print("Enter String:")
    str = input()
    strX = Strupr(str)
    print(f"updated String is {strX}")

if __name__ == "__main__":
    main()

