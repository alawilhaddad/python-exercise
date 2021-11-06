if __name__ == "__main__":
    second = int(input("input seconds: "))
    minute = second // 60
    hour = second / 3600
    print(f"{second} seconds is equivalent to:")
    print(f"{minute} Minutes")
    print(f"{hour} Hours")