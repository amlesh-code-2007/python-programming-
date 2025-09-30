def main():
    try:
        a = int(input("HEy, Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    

    finally:
        print("Hey, i am Inside of finally ")


main()