**Vier Gewinnt – Mattis Schulte, Sajan Sivapatham | [GitHub](https://github.com/Mattis-Schulte/connect4/)**

## Aufgabenstellung
Am Anfang hat der Lehrer das "Vier Gewinnt"-Spiel erklärt. Dabei hatte ein Schüler ein Protokoll angefertigt, wo alle benötigten Methoden und deren Erklärungen festgehalten wurden. Als das Protokoll fertiggestellt wurde, haben die Schüler die noch leeren Methoden übernommen, die man für das Spiel benötigt. Die Schüler hatten dann nur die notwendigen leeren Methoden und die dazugehörigen Erklärungen parat, um das Spiel zu entwickeln.

- Die vorgegebenen leeren Methoden des Lehrers mussten benutzt werden.
- Unten Links muss der Startpunkt sein (x=0/y=0)(wie im Koordinatensystem).
- EXTRA: Als extra kann man neben der Auswahl zum Zweispielermodus auch ein KI-Modus einbauen, sodass man allein gegen ein Computerspieler spielt.


## Liste der verwendeten Ausstattung 
- Computer mit Windows 10 (21H2) / macOS Monterey 12.2.1 (21D62)
- [PyCharm 2021.3.2](https://www.jetbrains.com/pycharm/) (Professional Edition)
- Python 3.10
- [Replit](https://replit.com/) (Webseite mit einer Online-IDE, Editor, Compiler und Interpreter)
- Das Protokoll des Schülers

## Spielregeln
Die Spielregeln von "Vier Gewinnt", sind sehr einfach erklärt. Der Spieler kann gewinnen, indem er mit seinen zugehörigen Spielsteinen abwechselnd eine Reihe mit mindestens 4 Spielsteinen legt. Er kann diese Reihe vertikal, horizontal oder diagonal verlegen. Das Einzige, was man beachten muss, ist, dass diese vierer Reihe nicht durch einen gegnerischen Spielstein belegt wird. So kann man das Spiel spielen, bis man selbst gewonnen hat, der Gegner gewonnen hat oder bis das Spielbrett voll ist.

## Programm
### Benutzeranleitung:
Wenn man das Spiel gestartet hat, kommt man in das Spielmenü, wo der Benutzer auswählen kann, in welchen Spielmodus er spielen will:
````

              ██╗   ██╗██╗███████╗██████╗   
              ██║   ██║██║██╔════╝██╔══██╗  
              ╚██╗ ██╔╝██║█████╗  ██████╔╝  
               ╚████╔╝ ██║██╔══╝  ██╔══██╗  
                ╚██╔╝  ██║███████╗██║  ██║  
                 ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝  

 ██████╗ ███████╗ ██╗       ██╗██╗███╗  ██╗███╗  ██╗████████╗
██╔════╝ ██╔════╝ ██║  ██╗  ██║██║████╗ ██║████╗ ██║╚══██╔══╝
██║  ██╗ █████╗   ╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║   ██║   
██║  ╚██╗██╔══╝    ████╔═████║ ██║██║╚████║██║╚████║   ██║   
╚██████╔╝███████╗  ╚██╔╝ ╚██╔╝ ██║██║ ╚███║██║ ╚███║   ██║   
 ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚══╝   ╚═╝   
    
Wählen Sie einen Spielmodus:
(1) Einzelspieler (KI-Modus)
(2) Zweispieler
>> 
````
Dabei hat er die Auswahl zwischen einem primitiven Computergegner oder er kann das Spiel mit einem menschlichen Gegenspieler starten.




#### (1) Einzelspieler (KI-Modus)
Wenn der Benutzer den Einzelspielermodus (also gegen denn Computergegner) wählt, muss der Benutzer seinen Benutzernamen eingeben:
````
Bitte geben Sie ihren Benutzernamen ein!
>>
````
Nachdem der Benutzer seinen Benutzernamen eingegeben hat, wird man zur Farbauswahl gebeten:
````
Bitte wählen Sie ihre Farbe (Rot, Grün, Gelb oder Blau)!
>> 
````
Der Benutzer muss dann seine gewünschte Spielsteinfarbe eingeben.
Nachdem der Spieler eine Farbe ausgewählt hat, wird er zum Spielfeld weitergeleitet, wo der Benutzer denn ersten Spielstein setzen darf. Dabei darf er nur die Spalte auswählen (A-G), wo er denn Spielstein einwerfen möchte.

````
VIER GEWINNT

+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Spieler 1 (Rot) ist am Zug >> a
````
Nachdem der Benutzer die Spalte eingegeben hat, wird der Spielstein gesetzt und der Computergegner setzt dann sein Spielstein auch automatisch ein (Der Computergegner hat nach Zufallsprinzip die Farbe Gelb ausgewählt):
````
VIER GEWINNT

+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|  🔴  |      |      |  🟡  |      |      |      |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Spieler 1 (Rot) ist am Zug >> 
````
Danach geht das Spiel weiter, bis Spielbrett voll ist oder jemand gewonnen hat:

##### Der Benutzer hat gewonnen:
````
VIER GEWINNT

+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|  🔴  |  🔴  |  🔴 |  🔴  |  🟡  |  🟡 |  🟡  |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Spieler 1 (Rot) hat mit folgenden Steinen gewonnen: (1|0) (2|0) (3|0) (4|0)
````


##### Die primitive KI hat gewonnen:
````
VIER GEWINNT

+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |  🔴  |      |      |
+------+------+------+------+------+------+------+
|  🟡  |  🟡  |  🟡 |  🟡 |  🔴  |  🔴 |  🔴  |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Primitive KI (Gelb) hat mit folgenden Steinen gewonnen: (1|0) (2|0) (3|0) (4|0)
````


##### Unentschieden:
````
VIER GEWINNT

+------+------+------+------+------+------+------+
|  🟡  |  🔴  |  🔴  |  🔴  |  🟡  |  🟡  |  🔴  |
+------+------+------+------+------+------+------+
|  🟡  |  🔴  |  🟡  |  🟡  |  🔴  |  🔴  |  🔴  |
+------+------+------+------+------+------+------+
|  🟡  |  🟡  |  🔴  |  🔴  |  🔴  |  🟡  |  🟡  |
+------+------+------+------+------+------+------+
|  🔴  |  🔴  |  🔴  |  🟡  |  🟡  |  🔴  |  🔴  |
+------+------+------+------+------+------+------+
|  🟡  |  🟡  |  🔴  |  🔴  |  🔴  |  🟡  |  🟡  |
+------+------+------+------+------+------+------+
|  🟡  |  🟡  |  🟡  |  🔴  |  🟡  |  🔴  |  🟡  |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G

Das Spiel ist unentschieden!
````

#### (2) Zweispieler
Der Zweispielermodus ist so ähnlich aufgebaut wie der Einzelspielermodus.
Wenn der Benutzer denn Zweispielermodus gewählt hat, wird dieser gebeten, denn Namen des ersten Spielers zu wählen.


````
Spieler 1:
Bitte geben Sie ihren Benutzernamen ein!
>>
````
Auch hier wird abgefragt, welche Farbe der Spieler möchte.

````
Spieler 1:
Bitte wählen Sie ihre Farbe (Rot, Grün, Gelb oder Blau)!
>> 
````

#### Beim zweiten Spieler sind die Abfragen identisch außer bei der Wahl der Farbe. Denn die Farbe, die der erste Spieler gewählt hat, wird dann dem zweiten Spieler nicht mehr zur Verfügung stehen.

Nachdem beide Spieler ihren Benutzernamen und Farben ausgewählt haben, wird das Spiel gestartet und das Spielbrett erscheint.

````
VIER GEWINNT

+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Spieler 1 (Rot) ist am Zug >> 
````
Danach werden abwechselnd zwischen den zwei Spielern die Spielsteine eingeworfen, bis jemand gewonnen hat oder das Spiel unterschieden verläuft bzw. das Spielbrett voll ist.

##### Der Spieler 1 hat gewonnen:

````
VIER GEWINNT

+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|  🔴  |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|  🔴  |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|  🔴  |      |      |      |      |      |  🟡  |
+------+------+------+------+------+------+------+
|  🔴  |      |      |      |      |  🟡  |  🟡  |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Spieler 1 (Rot) hat mit folgenden Steinen gewonnen: (0|0) (0|1) (0|2) (0|3) 
````

##### Der Spieler 2 hat gewonnen:

````
VIER GEWINNT

+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+
|  🔴  |  🔴  |      |     |      |      |      |
+------+------+------+------+------+------+------+
|  🔴  |  🔴  |      | 🟡  |  🟡  |  🟡  |  🟡 |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Spieler 2 (Gelb) hat mit folgenden Steinen gewonnen: (3|0) (4|0) (5|0) (6|0)
````

##### Unentschieden bzw. das Spielbrett ist voll:


````
VIER GEWINNT

+------+------+------+------+------+------+------+
|  🟡  |  🟡  |  🟡  |  🔴  |  🟡  |  🟡  |  🟡  |
+------+------+------+------+------+------+------+
|  🔴  |  🔴  |  🔴  |  🟡  |  🔴  |  🔴  |  🔴  |
+------+------+------+------+------+------+------+
|  🟡  |  🟡  |  🟡  |  🔴  |  🟡  |  🟡  |  🟡  |
+------+------+------+------+------+------+------+
|  🔴  |  🔴  |  🔴  |  🟡  |  🔴  |  🔴  |  🔴  |
+------+------+------+------+------+------+------+
|  🟡  |  🟡  |  🟡  |  🔴  |  🟡  |  🟡  |  🟡  |
+------+------+------+------+------+------+------+
|  🔴  |  🔴  |  🔴  |  🟡  |  🔴  |  🔴  |  🔴  |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Das Spiel ist unentschieden!
````



### Programmteile erklärt:
#### Hauptteil (main.py)
````python
exec(clear_cmd)
usr_name = 'Spieler 1'
print('Bitte geben Sie ihren Benutzernamen ein!')
usr_input = input('>> ')
if usr_input != '':
    usr_name = usr_input
exec(clear_cmd)

# Select color
print(f'Bitte wählen Sie ihre Farbe ({" oder ".join([", ".join(color_helper[key] for key in valid_colors.colors[:-1]), color_helper[valid_colors.colors[-1]]])})!')
usr_input = input('>> ')
while True:
    try:
        if usr_input.upper() in dict((v.upper(), k) for k, v in color_helper.items()):
            usr_input = dict((v.upper(), k) for k, v in color_helper.items())[usr_input.upper()]
            if usr_input not in valid_colors.colors:
                raise WrongColError('Duplicated color!')
        else:
            raise WrongColError('Invalid color!')
          
        p1 = Player(usr_name, usr_input)
        valid_colors.colors.remove(usr_input)
        p2 = Player('Primitive KI', choice(valid_colors.colors))
        Game = ConnectFourGame(p1, p2, Board, 1)
        break
    except WrongColError:
        print('Fehlerhafte Auswahl!')
        usr_input = input('>> ')
````
In diesem Teil des Codes wird der Benutzer nach seinem Namen und seiner Farbe gefragt, falls der Benutzer keinen Namen angegeben hat, wird der Standardname also hier z. B. Spieler 1 gewählt. Außerdem kann der Benutzer nur zwischen den erlaubten Farben `valid_colors` wählen, wenn er eine korrekte Farbe ausgewählt hat, wird dann eine Spieler-Instanz für den Benutzer und eine für die KI erstellt – der Name der KI lautet "Primitive KI" und die Farbe der KI wird zufällig gewählt. Aufgrund dessen entfernen wir auch vorher die vom Benutzer gewählte Farbe aus der Liste der erlaubten Farben, damit die KI nicht dieselbe Farbe wählen kann. Außerdem erstellen wir hier auch schon die Instanz für das eigentliche Spiel, der wir die beiden Spieler-Instanzen, das Board und den Spielmodus (1 oder 2) übergeben: `Game = ConnectFourGame(p1, p2, Board, 2)`

````python
# Running the actual game
while not (Board.is_board_full()) and not (Board.get_winning_positions(Board.field)):
    Game.play()
else:
    Board.print_board(p1.color, p2.color)
    if Board.get_winning_positions(Board.field):
        winner_token_owner = Board.get_token(Board.get_winning_positions(Board.field)[0][0], Board.get_winning_positions(Board.field)[0][1])
        exec('winner_name = p' + str(winner_token_owner) + '.name')
        exec('winner_color = p' + str(winner_token_owner) + '.color')
        winner_color = color_helper[winner_color]
        print(f'{winner_name} ({winner_color}) hat mit folgenden Steinen gewonnen: ', end='')
        [print(f'({"|".join(str(x) for x in item)})', end=' ') for item in Board.get_winning_positions(Board.field)]
        print()
    elif Board.is_board_full():
        print('Das Spiel ist unentschieden!')
````
In diesem Abschnitt wird, solange bis das Spielbrett voll ist oder jemand gewonnen hat, das eigentliche Spiel laufen gelassen. Dafür rufen wir die Methode `play` der `Game` Instanz auf und übergeben dieser die Instanzen der beiden Spieler. Zudem geben wir in diesem Teil auch falls jemand gewonnen hat, den Namen des Gewinners, seine Farbe und die Steine aus, mit denen er gewonnen hat. Falls das Spiel unentschieden ist, wird das ebenfalls hier ausgegeben.

#### Die Spiele-Klasse (connect_four_game.py)
In dieser Klasse findet das eigentliche Spiel statt, so werden in dieser Klasse die Spielzüge durchgeführt, bestimmt wer am Zug ist und der Algorithmus der KI ist ebenfalls in dieser Klasse.
````python
def set_ai(self):
    """ The AI algorithm, it wants to either win or avoid losing if neither is possible it will put the token in a random column """
    valid_columns = [x for x in range(0, len(self.board.field)) if 0 in self.board.field[x]]

    # Check if the game can be won or a loss avoided
    for win in reversed(range(0, 2)):
        for column in sample(valid_columns, len(valid_columns)):
            test_board = deepcopy(self.board.field)
            # Prioritize winning over avoiding losing
            if win:
                test_board[column][self.board.field[column].index(0)] = 2
            else:
                test_board[column][self.board.field[column].index(0)] = 1

            if self.board.get_winning_positions(test_board):
                self.board.set_token(column, 2)
                self.active_player = 1
                return
        
    # Check to prevent a random token from being placed in the opponent's favour
    for random_column in sample(valid_columns, len(valid_columns)):
        test_board = deepcopy(self.board.field)
        test_board[random_column][self.board.field[random_column].index(0)] = 2
        if 0 in test_board[random_column]:
            test_board[random_column][self.board.field[random_column].index(0) + 1] = 1
            if not self.board.get_winning_positions(test_board):
                self.board.set_token(random_column, 2)
                self.active_player = 1
                return
        else:
            self.board.set_token(random_column, 2)
            self.active_player = 1
            return

    # Choose random column
    self.board.set_token(choice(valid_columns), 2)
    self.active_player = 1
````
Dies ist die Methode des KI-Algorithmus, als Erstes werden alle möglichen Spalten ermittelt. Im ersten Abschnitt prüft die KI dann mit der Methode `get_winning_positions` der "Board-Klasse" ob es eine Spalte gibt, die die KI nutzen könnte, um zu gewinnen oder den Nutzer zumindest am Gewinnen zu hindern (dabei, wird der Sieg natürlich bevorzugt). Gibt es keine Spalte, in der dies der Fall ist, wird eine zufällige Spalte ausgewählt. Es wird vorher allerdings noch geprüft, ob der Zug vorteilhaft für den Gegner ist, also ob man durch seinen Zug den Gegner es ermöglicht vier nebeneinander zulegen (dafür ist der zweite Abschnitt da), falls dies nicht der Fall ist oder es keine andere Möglichkeit gibt, legt die KI.
````python
def play(self):
    color_helper = {'RED': 'Rot', 'GREEN': 'Grün', 'YELLOW': 'Gelb', 'BLUE': 'Blau'}
    self.board.print_board(self.p1.color, self.p2.color)
    if self.active_player == 1:
        # Player one's turn
        while True:
            try:
                self.set_player1(input(f'{self.p1.name} ({color_helper[self.p1.color]}) ist am Zug >> '))
                break
            except(ValueError, IndexError):
                print('Fehlerhafte Auswahl!')
            except ColumnFullError:
                print('Diese Spalte ist schon voll!')
    elif self.active_player == 2 and self.game != self.AI:
        # Player two's turn
        while True:
            try:
                self.set_player2(input(f'{self.p2.name} ({color_helper[self.p2.color]}) ist am Zug >> '))
                break
            except(ValueError, IndexError):
                print('Fehlerhafte Auswahl!')
            except ColumnFullError:
                print('Diese Spalte ist schon voll!')
    elif self.active_player == 2 and self.game == self.AI:
        # AI's turn
       self.set_ai()
````
Dies ist die Spiele Methode, in dieser werden die eigentlichen Spielzüge durchgeführt oder die KI aufgerufen. Zudem werden hier auch Fehler wie eine fehlerhafte Eingabe der Spalte oder die Eingabe einer vollen Spalte behandelt und eine Fehlermeldung für den Benutzer ausgegeben.

#### Die Spielfeld-Klasse (connect_four_board.py)
Dies ist die Klasse für das Spielfeld, sie enthält Methoden zum Setzten und Auslesen von Spielsteinen, zum Ausgeben des Spielfelds, zum zurücksetzten des Spielfelds und zum überprüfen 
In dieser Klasse findet das eigentliche Spiel statt, so werden in dieser Klasse die Spielzüge durchgeführt, bestimmt wer am Zug ist und der Algorithmus der KI ist ebenfalls in dieser Klasse.

## Fazit
Abschließend kann man sagen, dass das Projekt "Vier gewinnt" eine ziemliche Herausforderung war, da wir keine richtige Aufgabenstellung vom Lehrer erhalten haben und wir uns am Protokoll des Schülers orientieren mussten. Auch gab es Missverständnisse und wurden zu philosophischen Gedankengänge verleitet, weil wir manchmal nicht genau wussten, warum eine Methode genau genutzt werden sollte und manche dieser Methoden uns überflüssig erschienen sind. Jedoch ist uns beim Nachfragen des Lehrers und der Definitionserklärung der Methoden von den Schülern uns gelungen, das Projekt fertigzustellen.
