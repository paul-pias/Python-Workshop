# PYTHON WORKSHOP 
by NSUCEC R&D on august 2019


### Instructors: Pias Paul & Moh. Anwar-Ul-Azim Bhuiya
***



## Class-2:

* **Data Structure**
* **List**
* **Loop**
* **Dictionaries**
* **Control Flow**
* **Assignment**


***


## Class-2 Assignment:
```python
nominated = {
    2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']
}
winners = {
    2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']
}

```
1.	**Create a dictionary that includes the count of Oscar nominations for each director in the nominations list.**
2.	**Provide a dictionary with the count of Oscar wins for each director in the winners list.**


#### Solution:
```python
nominated = {
    2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'],
    2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'],
    2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'],
    2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'],
    2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'],
    2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'],
    2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'],
    2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'],
    2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'],
    2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'],
    2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']
}
winners = {
    2000: ['Steven Soderbergh'],
    2001: ['Ron Howard'],
    2002: ['Roman Polanski'],
    2003: ['Peter Jackson'],
    2004: ['Clint Eastwood'],
    2005: ['Ang Lee'],
    2006: ['Martin Scorsese'],
    2007: ['Ethan Coen', 'Joel Coen'],
    2008: ['Danny Boyle'],
    2009: ['Kathryn Bigelow'],
    2010: ['Tom Hooper']
}

### 1A: Create dictionary with the count of Oscar nominations for each director
nom_count_dict = {}

for year, name in nominated.items():
    for director in name:
        if director not in nom_count_dict:
            nom_count_dict[director] = 1
        else:
            nom_count_dict[director] +=1


print("nom_count_dict = {}\n".format(nom_count_dict))

### 1B: Create dictionary with the count of Oscar wins for each director
win_count_dict = {}

for year, name in winners.items():
    for director in name:
        if director not in win_count_dict:
            win_count_dict[director] = 1
        else:
            win_count_dict[director] +=1


print("win_count_dict = {}".format(win_count_dict))
```

***


