def CountSmall(data):
    
    icount = 0
    for ch in data:
        if (ch >= 'a' and ch <= 'z'):
            icount += 1
    return icount

def main():
    print("Enter String:")
    str = input()
    iRet = CountSmall(str)
    print(f"Frequency of small char in '{str}' is {iRet}")

if __name__ == "__main__":
    main()

