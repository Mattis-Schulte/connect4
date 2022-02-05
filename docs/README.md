**Vier Gewinnt – Mattis Schulte, Sajan Sivapatham | [GitHub](https://github.com/Mattis-Schulte/connect4/)**

## Aufgabenstellung
Am Anfang hat der Lehrer das Spiel erklärt. Dabei hatte ein Schüler ein Protokoll angefertigt wo alle nötigen Methoden und deren Erklärungen festgehalten wurde. Als das Protokoll fertigestellt wurde haben die Schüler die noch leeren Methoden übernommen die man für das Spiel benötigt. Die Schüler hatten dann nur die notwedigen leeren Methoden und die dazugehörigen Erklärungen parat.

- Die vorgegebenen leeren Methoden des Lehrers mussten benutzt werden
- Unten Links muss der Startpunkt sein (x=0/y=0)(wie im Koordinatensystem)
- 


## Liste der verwendeten Ausstattung 
- Computer mit Windows 10 (Version 21H1) / macOS Big Sur 11.6 (20G165) 
- [PyCharm 2021.2.3](https://www.jetbrains.com/pycharm/) (Professional Edition)
- Python 3.9 
- [Replit](https://replit.com/) (Webseite mit einer Online-IDE, Editor, Compiler und Interpreter) 

## Programm
### Benutzeranleitung:
Um das P

### Programmteile erklärt:
#### Klasse und Variablen anlegen 
````python

````
In diesem Teil des Codes wird unsere Klasse `Cipher`, sowie alle für die Ver- und Entschlüsselung benötigten Variablen angelegt bzw. übernommen. Außerdem wird hier auch schon die CRC32 Prüfsumme des Passwortes gebildet, geteilt und der Zufalls-Seed mit einem Teil dieser Prüfsumme initialisiert. Zudem wird auch die benötigte Pseudozufallszahl generiert.

#### Verschlüsselung
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
Zusammenfassend kann man sagen, dass das Projekt "Verschlüsselung" eine Herausforderung war, uns aber auch viel gelehrt hat. Besonders schwierig war es, sicherzustellen, dass die Verschlüsselung genau wie gewünscht funktioniert. Da man schnell eine Verschlüsselungsmethode geschrieben hatte, die scheinbar funktioniert, jedoch bei genauerem Hinsehen die Dateien nicht wie beabsichtigt verschlüsselt. Nichtsdestotrotz haben wir einiges dazugelernt und hoffen, dass wir das Gelernte in Zukunft weiter vertiefen können.