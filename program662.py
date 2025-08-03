def Replace(data):
    
    icount = 0
    OutPut  = ""
    for ch in data:
        if (ch == 'a' ):
           OutPut.append('a')
        else:
           OutPut.append(ch)
        
def main():
    print("Enter String:")
    str = input()
    strX = Replace(str)
    print("updated String is {strX}")

if __name__ == "__main__":
    main()

