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

    **There is txt file named “movie_information.txt” which holds the following information.
        * Movie Name
        * Director name
        * Lead Actor Name
        * Releasing Year
        * Total earning of that movie
    Read the file “movie_information.txt” and do the following tasks:-
        -> Display the information stored on the file
        -> First read the file line by line and split the information on the basis of “ : ” and store the Movie Name    and the Lead Actor Name into two separate variable.
        -> Store the new information into another file named “Actor_Information.txt” using “Name of the Actor :         Movie Name” this convention.**

#### Solution:

    "cells": [
    {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Assignment -1"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 1,
    "metadata": {},
    "outputs": [
        {
        "name": "stdout",
        "output_type": "stream",
        "text": [
        "Braveheart : Mel Gibson : Mel Gibson : 1995 : $75.60M\n",
        "The Terminal : Steven Spielberg : Tom Hanks : 2004 : $77.87M\n",
        "The Green Mile : Frank Darabont : Tom Hanks : 1999 : $136.80M\n",
        "The Hateful Eight : Quentin Tarantino : Samuel L. Jackson : 2015 : $155.8M\n",
        "The Godfather : Francis Ford Coppola : Al Pacino : 1972 : $134.97M\n",
        "The Shawshank Redemption : Frank Darabont : Morgan Freeman : 1994 : $28.34M\n",
        "Schindler's List : Steven Spielberg : Liam Neeson : 1993 : $96.07M\n",
        "Vertigo : Alfred Hitchcock : James Stewart : 1958 : $3.20M\n",
        "Forrest Gump : Robert Zemeckis : Tom Hanks : 1994 : $330.25M\n",
        "12 Angry Men : Sidney Lumet :  Henry Fonda : 1957 : $4.36M\n",
        "The Silence of the Lambs : Jonathan Demme : Anthony Hopkins  : 1991 : $130.74M\n",
        "It's a Wonderful Life : Frank Capra :  James Stewart: 1946 : $5.05M\n",
        "Amadeus : Milos Forman : F. Murray Abraham : 1984 : $51.97M\n",
        "Gladiator : Ridley Scott :  Russell Crowe: 2000 : $187.71M\n",
        "Titanic : James Cameron : Leonardo DiCaprio : 1997 : $659.33M\n",
        "Saving Private Ryan : Steven Spielberg : Tom Hanks: 1998 : $216.54M\n",
        "An American in Paris : Vincente Minnelli : Gene Kelly : 1951 : $4.50M\n",
        "The Best Years of Our Lives : William Wyler : Myrna Loy : 1946 : $23.65M\n",
        "A Clockwork Orange : Stanley Kubrick : Malcolm McDowell : 1971 : $26.5M\n",
        "Doctor Zhivago : David Lean : Omar Sharif : 1965 : $111.72M\n",
        "Jaws : Steven Spielberg : Roy Scheider : 1975 : $260.00M\n",
        "Patton : Franklin J. Schaffner : George C. Scott : 1970 : $61.70M\n",
        "A Streetcar Named Desire : Elia Kazan : Vivien Leigh : 1951 : $8.00M\n",
        "Rocky : John G. Avildsen : Sylvester Stallone : 1976 : $117.24M\n",
        "Raiders of the Lost Ark : Steven Spielberg : Harrison Ford : 1981 : $248.16M\n",
        "Unforgiven : Clint Eastwood : Clint Eastwood : 1992 : $101.16M\n",
        "From Here to Eternity : Fred Zinnemann : Burt Lancaster : 1953 : $30.50M\n",
        "The Lord of the Rings- The Return of the King : Peter Jackson: Elijah Wood: 2003 : $377.85M\n",
        "Apocalypse Now : Francis Ford Coppola : Martin Sheen : 1979 : $83.47M\n",
        "Dances with Wolves : Kevin Costner : Kevin Costner : 1990 : $184.21M\n",
        "On the Waterfront : Elia Kazan : Marlon Brando : 1954 : $9.60M\n",
        "Ben-Hur : William Wyler : Charlton Heston : 1959 : $74.70M\n",
        "Singin' in the Rain : Stanley Donen : Gene Kelly : 1952 : $8.82M\n",
        "The Bridge on the River Kwai : David Lean : William Holden : 1957 : $44.91M\n",
        "Chinatown : Roman Polanski : Jack Nicholson : 1974 : $29.20M\n",
        "E.T. the Extra-Terrestrial : Steven Spielberg : Henry Thomas : 1982 : $435.11M\n",
        "A Space Odyssey : Stanley Kubrick : Keir Dullea : 1968 : $56.95M\n",
        "West Side Story : Jerome Robbins : Natalie Wood : 1961 : $43.66M\n",
        "The Sound of Music : Robert Wise : Julie Andrews : 1965 : $163.21M\n",
        "Psycho : Alfred Hitchcock : Anthony Perkins : 1960 : $32.00M\n",
        "Lawrence of Arabia : David Lean : Peter O'Toole : 1962 : $44.82M\n",
        "One Flew Over the Cuckoo's Nest : Milos Forman : Jack Nicholson : 1975 : $112.00M\n",
        "Gone with the Wind : Victor Fleming : Clark Gable : 1939 : $198.68M\n",
        "Citizen Kane : Orson Welles : Orson Welles: 1941 : $1.59M\n",
        "Casablanca : Michael Curtiz : Humphrey Bogart : 1942 : $1.02M\n",
        "Raging Bull : Martin Scorsese : Robert De Niro : 1980 : $23.38M\n",
        "The Good, the Bad and the Ugly : Sergio Leone : Clint Eastwood: 1966 : $6.10M\n",
        "Platoon : Oliver Stone : Charlie Sheen: 1986 : $138.53M\n",
        "High Noon : Fred Zinnemann : Gary Cooper : 1952 : $9.45M\n",
        "Jurassic Park : Steven Spielberg : Sam Neill: 1993 : $402.45M\n"
        ]
        }
    ],
    "source": [
        "with open(\"movie_Information.txt\",'r') as f:\n",
        "    movies = f.read()\n",
        "    \n",
        "    with open (\"Actors_Information.txt\",'a') as m:\n",
        "        movies = movies.split(\"\\n\")\n",
        "        \n",
        "        for movie in movies:\n",
        "            actor_name = (movie.split(\":\")[2])\n",
        "            movie_name = (movie.split(\":\")[0])\n",
        "            m.write(actor_name.strip() + \" : \" + movie_name.strip() + '\\n')"
    ]
    }
    ]


***


