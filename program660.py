def CountNonVowels(data):
    pattern = "aeiouAEIOU"
    icount = 0
    for ch in data:
        if ch  not in pattern:
            icount += 1
    return len(data) - icount

def main():
    print("Enter String:")
    user_input = input()
    iRet = CountNonVowels(user_input)
    print(f"Frequency of Non-Vowels in '{user_input}' is {iRet}")

if __name__ == "__main__":
    main()
