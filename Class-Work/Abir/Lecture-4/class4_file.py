with open("Actors_Information.txt") as f:
    print(f.read())
    
with open("Actors_Information.txt", "a") as f:
    f.write("hello")