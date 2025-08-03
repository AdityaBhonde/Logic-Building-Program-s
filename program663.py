def Replace(data):
    
    icount = 0
    OutPut  = ""
    for ch in data:
        if (ch == 'a' ):
           OutPut = OutPut + 'a' 
        else:
           OutPut = OutPut + ch
    return OutPut
    
def main():
    print("Enter String:")
    str = input()
    strX = Replace(str)
    print("updated String is {strX}")

if __name__ == "__main__":
    main()

