response = int(input("Pick a lucky number:  "))
try:
    if response > 1000:
        print("Greater than 1000")
    elif response  % 2 != 0:
        print("Odd numbers aren't lucky")
    else:
        print("Lucky number")