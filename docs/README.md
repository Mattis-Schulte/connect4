**Vier Gewinnt – Mattis Schulte, Sajan Sivapatham | [GitHub](https://github.com/Mattis-Schulte/connect4/)**

## Aufgabenstellung
Am Anfang hat der Lehrer das Vier Gewinnt-Spiel erklärt. Dabei hatte ein Schüler ein Protokoll angefertigt wo alle nötigen Methoden und deren Erklärungen festgehalten wurde. Als das Protokoll fertigestellt wurde haben die Schüler die noch leeren Methoden übernommen die man für das Spiel benötigt. Die Schüler hatten dann nur die notwedigen leeren Methoden und die dazugehörigen Erklärungen parat um das Spiel zu entwickeln.

- Die vorgegebenen leeren Methoden des Lehrers mussten benutzt werden.
- Unten Links muss der Startpunkt sein (x=0/y=0)(wie im Koordinatensystem).
- EXTRA: Als extra kann man neben der Auswahl zum Zweispielermodus auch ein KI-Modus einbauen sodass man allein gegen ein Computerspieler spielt.


## Liste der verwendeten Ausstattung 
- Computer mit Windows 10 (Version 21H1) / macOS Big Sur 11.6 (20G165) 
- [PyCharm 2021.2.3](https://www.jetbrains.com/pycharm/) (Professional Edition)
- Python 3.9 
- [Replit](https://replit.com/) (Webseite mit einer Online-IDE, Editor, Compiler und Interpreter) 

## Spielregeln
Um das Spiel zu spielen muss man zuerst wissen wie es gespielt wird
## Programm
### Benutzeranleitung:
Wenn man das Spiel gestartet hat kommt man in das Spielmenü wo der Benutzer auswählen kann im welchen Spielmodus er spielen will:
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




### (1) Einzelspieler (KI-Modus)
Wenn der Benutzer den Einzelspielermodus (also gegen denn Computergegner) wählt muss der Benutzer sein Benutzernamen eingeben:
````
Bitte geben Sie ihren Benutzernamen ein!
>>
````
Nachdem der Benutzer sein Benutzernamen eingegeben hatte wird man zur Farbauswahl gebeten:
````
Bitte wählen Sie ihre Farbe (Rot, Grün oder Gelb)!
>> 
````
Der Benutzer muss dann eines der drei Farben die zur Auswahl stehen eingeben.
Nachdem der Spieler eine Farbe ausgewählt hat wird er zum Spielfeld weitergeleitet wo der Benutzer denn ersten Spielstein setzen darf. Dabei darf er nur die Spalte auswählen (A-G) wo er denn Spielstein einwerfen möchte.

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
Nachdem der Benutzer die Spalte eingegeben hat wird der Spielstein gesetzt und der Computergegner setzt dann sein Spielstein auch automatisch ein (In diesem Fall ist der Computergegner Gelb):
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
Danach geht das Spiel weiter bis Spielbrett voll ist oder jemand gewonnen hat:

#### Der Benutzer hat gewonnen:
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


#### Die primitive KI hat gewonnen:
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
|  🟡  |  🟡  |  🟡 |  🟡  |  🔴  |  🔴 |  🔴  |
+------+------+------+------+------+------+------+
    A      B      C      D      E      F      G  

Die Primitive KI (Gelb) hat mit folgenden Steinen gewonnen: (1|0) (2|0) (3|0) (4|0)
````

### (2) Zweispieler
Der Zweispielermodus ist so ähnlich aufgebaut wie der Einzelspielermodus.
Wenn der Benutzer denn Zweispielermodus gewählt hat gibt dieser 
### Programmteile erklärt:
#### Klasse und Variablen anlegen 
````python

````
In diesem Teil des Codes wird unsere Klasse `Cipher`, sowie alle für die Ver- und Entschlüsselung benötigten Variablen angelegt bzw. übernommen. Außerdem wird hier auch schon die CRC32 Prüfsumme des Passwortes gebildet, geteilt und der Zufalls-Seed mit einem Teil dieser Prüfsumme initialisiert. Zudem wird auch die benötigte Pseudozufallszahl generiert.

#### Erklärung der einzelnen Methoden:
````python

````
> Hier findet die eigentliche Verschlüsselung statt. Falls jedoch kein Dateipfad zur Ausgabedatei angegeben wurde, muss zuerst noch einer generiert werden. Dies geschieht, indem zuerst der Dateipfad zum Ordner der Eingabedatei bestimmt und dann mit dem Standardnamen der Ausgabedatei kombiniert wird. Der Standardname ist wie folgt aufgebaut: `cip + (die Länge der Dateiendung der Eingabedatei) + (die Dateiendung der Eingabedatei)`, als Dateiendung wird `.cip` benutzt. Beispiel: "cip3gif.cip"

Wenn der Dateipfad zur Ausgabedatei klar ist, wird die Eingabedatei im binären Lesemodus und die Ausgabedatei im binären Schreibmodus geöffnet – `with open(self.input_file_, 'rb') as r, open(self.output_file_, 'wb') as w:`. Als Nächstes wird eine Schleife ausgeführt, diese Schleife erhält mithilfe der `enumerate` Funktion die Variablen `i` und `x`, `i` zählt die Anzahl der Bytes und `x` enthält den Wert des jeweiligen Bytes. 

Mithilfe von `i` wird die Unicode-Nummer eines Zeichen des Passworts bestimmt (in der nächsten Iteration immer das nächst weitere Zeichen), diese Nummer wird dann mit einem Teil der CRC32 Prüfsumme, der vorher bestimmten Pseudozufallszahl und mit `x ` (also dem Wert des jeweiligen Byte der Iteration) addiert. Falls das Ergebnis größer als 255 ist, wird von 0 weiter gezählt, so wird jedes Byte der Datei nach und nach verändert und in die Ausgabedatei geschrieben.

#### Entschlüsselung
````python

````
Das Entschlüsselungsverfahren unterscheidet sich kaum von der Verschlüsselung, es wird lediglich nicht mehr zum Byte addiert, sondern subtrahiert. Zudem wird der Dateipfad zur Ausgabedatei, wenn dieser nicht angegeben wurde, anders generiert.

> Diese Generation geschieht, indem jeglich die Dateiendung des Pfads der Eingabedatei verändert wird. Dazu trennen wir den Dateipfad am Punkt und benutzten nur den vordern Teil und fügen noch die Dateiendung an, die wir aus denn Dateiname der Eingabedatei auslesen – `self.output_file_ = self.input_file_.split('.')[0] + '.' + self.input_file_.split('/')[-1][4:-4]`

#### Hauptteil und Argumente
````python

````
In diesem Teil bzw. im Hauptteil fügen wir die benötigten Argumente sowie die Logik hinter diesen hinzu. 
> Nennenswerte Ausschnitte sind: 
> 
> `args = parser.parse_args()` – hier werden die Argument in der `args` Variable gespeichert über die wir sie später auslesen können
> 
> `mycipher = Cipher(args.inputfile, args.outputfile, args.password)` – hier werden mit denn durch die Argumente eingegeben Daten ein Objekt mit unser Klasse `Cipher` erstellt
> 
> `mycipher.encode_with_caesar()` oder `mycipher.decode_with_caesar()` – nun rufen wir mit unserem Objekt die Methode zum Ver- oder Entschlüsseln auf

## Fazit
Abschließend kann man sagen, dass das Projekt "Vier Gewinnt" eine ziemliche Herausforderung war, da wir keine richtige Aufgabenstellung vom Lehrer erhalten haben und wir uns am Protokoll des Schülers orientieren mussten. Auch gab es Missverständnisse und wurden zu philosophischen Gedankengänge verleitet, weil wir manchmal nicht genau wussten, warum eine Methode genau genutzt werden sollte und manche dieser Methoden uns überflüssig erschienen sind. Jedoch ist uns beim Nachfragen des Lehrers und der Definitionserklärung der Methoden von den Schülern uns gelungen, das Projekt fertigzustellen.