def palindrome(string):
    if text.lower()[::-1] == text.lower():
        print("text is palindrome")
    else:
        print("text is not a palindrome")


if __name__ == "__main__":
    text = input("input text: ")
    palindrome(text)
