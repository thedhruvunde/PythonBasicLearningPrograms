while True:
    try:
        var = int(input("Enter a number: "))
        print(var)
        break
    except Exception as e:
        print(e)
        print("Input invalid try again!!!")
        continue
print("Exiting Program")
exit()
