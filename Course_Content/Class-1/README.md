# PYTHON WORKSHOP 
by NSUCEC R&D on august 2019


### Instructors: Pias Paul & Moh. Anwar-Ul-Azim Bhuiya
***



## Class-1:

    * Basic concepts on Programming Language
    * Why Python as a Language?
    * Data Types
    * Operators
    * File
    * Assignment

***


## Class-1 Assignment:

**There is txt file named “movie_information.txt” which holds the following information.**
    *** Movie Name**
    *** Director name**
    *** Lead Actor Name**
    *** Releasing Year**
    *** Total earning of that movie**
**Read the file “movie_information.txt” and do the following tasks:-**
    **-> Display the information stored on the file**
    **-> First read the file line by line and split the information on the basis of “ : ” and store the Movie Name and the Lead Actor Name into two separate variable.**
    **-> Store the new information into another file named “Actor_Information.txt” using “Name of the Actor : Movie Name” this convention.**

#### Solution:

```python
with open("movie_Information.txt",'r') as f:
movies = f.read()

with open ("Actors_Information.txt",'a') as m:
    movies = movies.split("\n")

    for movie in movies:
        actor_name = (movie.split(":")[2])
        movie_name = (movie.split(":")[0])
        m.write(actor_name.strip() + " : " + movie_name.strip() + '\n')
```

***


