# PYTHON WORKSHOP 
by NSUCEC R&D on august 2019


### Instructors: Pias Paul & Moh. Anwar-Ul-Azim Bhuiya
***



## Class-2:

    * Data Structure
    * List
    * Loop
    * Dictionaries
    * Control Flow
    * Assignment


***


## Class-2 Assignment:

    **
    nominated = {2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper’]}

    winners = {2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper’]}

    A.	Create a dictionary that includes the count of Oscar nominations for each director in the nominations list.
    B.	Provide a dictionary with the count of Oscar wins for each director in the winners list.
    **

#### Solution:

    "cells": [
    {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Assignment - 2"
    ]
    },
    {
    "cell_type": "code",
    "execution_count": 16,
    "metadata": {},
    "outputs": [
        {
        "name": "stdout",
        "output_type": "stream",
        "text": [
        "nom_count_dict = {'Stephen Daldry': 3, 'Ang Lee': 2, 'Steven Soderbergh': 2, 'Ridley Scott': 2, 'Robert Altman': 1, 'Peter Jackson': 2, 'David Lynch': 1, 'Ron Howard': 2, 'Rob Marshall': 1, 'Martin Scorsese': 3, 'Pedro Almodovar': 1, 'Roman Polanski': 1, 'Fernando Meirelles': 1, 'Sofia Coppola': 1, 'Peter Weir': 1, 'Clint Eastwood': 3, 'Taylor Hackford': 1, 'Alexander Payne': 1, 'Mike Leigh': 1, 'Bennett Miller': 1, 'Paul Haggis': 1, 'George Clooney': 1, 'Steven Spielberg': 1, 'Alejandro Gonzaalez Inarritu': 1, 'Stephen Frears': 1, 'Paul Greengrass': 1, 'Julian Schnabel': 1, 'Jason Reitman': 2, 'Tony Gilroy': 1, 'Paul Thomas Anderson': 1, 'Joel Coen': 2, 'Ethan Coen': 2, 'David Fincher': 2, 'Gus Van Sant': 1, 'Danny Boyle': 1, 'James Cameron': 1, 'Quentin Tarantino': 1, 'Lee Daniels': 1, 'Kathryn Bigelow': 1, 'Darren Aronofsky': 1, 'David O. Russell': 1, 'Tom Hooper': 1}\n",
        "\n",
        "win_count_dict = {'Steven Soderbergh': 1, 'Ron Howard': 1, 'Roman Polanski': 1, 'Peter Jackson': 1, 'Clint Eastwood': 1, 'Ang Lee': 1, 'Martin Scorsese': 1, 'Ethan Coen': 1, 'Joel Coen': 1, 'Danny Boyle': 1, 'Kathryn Bigelow': 1, 'Tom Hooper': 1}\n"
        ]
        }
    ],
    "source": [
        "nominated = {2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'],\n",
        "2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], \n",
        "2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'],\n",
        "2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], \n",
        "2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], \n",
        "2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], \n",
        "2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], \n",
        "2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], \n",
        "2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], \n",
        "2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], \n",
        "2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']\n",
        "}\n",
        "winners = {2000: ['Steven Soderbergh'],\n",
        "2001: ['Ron Howard'],\n",
        "2002: ['Roman Polanski'],\n",
        "2003: ['Peter Jackson'], \n",
        "2004: ['Clint Eastwood'], \n",
        "2005: ['Ang Lee'], \n",
        "2006: ['Martin Scorsese'], \n",
        "2007: ['Ethan Coen', 'Joel Coen'], \n",
        "2008: ['Danny Boyle'], \n",
        "2009: ['Kathryn Bigelow'], \n",
        "2010: ['Tom Hooper']}\n",
        "### 1A: Create dictionary with the count of Oscar nominations for each director \n",
        "nom_count_dict = {}\n",
        "# Add your code here\n",
        "for year, name in nominated.items():\n",
        "    for director in name:\n",
        "        if director not in nom_count_dict:\n",
        "            nom_count_dict[director] = 1\n",
        "        else:\n",
        "            nom_count_dict[director] +=1\n",
        "\n",
        "\n",
        "print(\"nom_count_dict = {}\\n\".format(nom_count_dict))\n",
        "\n",
        "\n",
        "### 1B: Create dictionary with the count of Oscar wins for each director\n",
        "win_count_dict = {}\n",
        "# Add your code here\n",
        "for year, name in winners.items():\n",
        "    for director in name:\n",
        "        if director not in win_count_dict:\n",
        "            win_count_dict[director] = 1\n",
        "        else:\n",
        "            win_count_dict[director] +=1\n",
        "        \n",
        "\n",
        "\n",
        "print(\"win_count_dict = {}\".format(win_count_dict))"
    ]
    }
    ]
 

***


