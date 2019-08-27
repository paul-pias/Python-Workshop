with open("Actors_Information.txt", "r") as f1:
    #print(f1.read())
    with open("new.txt", "w") as f2:
    #print(f2.read())
        f2.write(f1.read())
    with open("new.txt", "r") as f3:
        print(f3.read().split(":"))