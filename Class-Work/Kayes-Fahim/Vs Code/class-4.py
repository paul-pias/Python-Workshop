with open("movie_information.txt", "a") as f:
   # print(f.read())
    f.write("fahim")

with open("movie_information.txt") as f:
   print(f.read())


   print(type(f.read()))