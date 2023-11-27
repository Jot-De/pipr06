# PIPR LAB 6-7 - 23Z

## PRZED LABORATORIUM:

* stworzyć repo i wrzucić do niego zawartość katalogu [receipts_starter/](receipts_starter) - **1 takie repo per prowadzona grupa**
* wysłać do studentów prośbę o zalogowanie się do gitlaba wydziałowego i upewnienie się, że działa

## ROZGRZEWKA - `@property`

Demonstrujemy enkapsulację w Pythonie na przykładzie dekoratora `@property` w pliku [property.py](property.py). Wg uznania można tu pomachać palcem, że w C++ i w Javie takiego dekoratora nie ma i na 100% należy pisać gettery jak na filmiku. Następnie można powiedzieć, że Python to nie C++ ani Java i tutaj używa się innych idiomów.

## PROBLEM

Jesteśmy właścicielami małego sklepiku.
Dużo czasu zajmuje nam rachunkowość, którą prowadzimy w papierowym zeszycie.
Chcemy usprawnić działanie naszego sklepu tworząc program w języku Python do zarządzania naszym sklepem.
Program ma pomagać w gromadzeniu danych z paragonów.
Na paragonie mamy informacje o:

* nazwie produktu
* cenie
* ilości
* podatku

Takich produktów może być na paragonie dowolnie dużo.
Chcemy by nasz kod był łatwy w utrzymaniu i modyfikacji, dlatego stworzymy obiektową wersję programu.

## SCENARIUSZ LABORKI

### 1. Dyskusja

**czas:** ok. 15min

Wrzucamy treść problemu i rozpoczynamy dyskusję o tym jakie klasy można by było wydzielić w ramach tego zadania. Prawdopodobnie będą to:

* Paragon
* Pozycja na paragonie
* Przedmiot
* Cena
* Klient

> Czy interfejs powinien być klasą? A może raczej zestawem funkcji? Tak czy siak, dzisiaj nie implementujemy interfejsu.

Dostarczony jest plik `main.py`, który na kolorowo wyświetla kolejne rzeczy które będą działać. Nie musimy go omawiać. Po zaimplementowaniu wszystkich klas, plik powinien odpalić się poprawnie i wykonać do końca. Odpalamy go np. za pomocą `python3 -m receipts.main` z katalogu nadrzędnego.

Wspólnie omawiamy które klasy będą ze sobą gadać, a które nie.

### 2. Praca w grupach

**czas:** ok. 45min

Dzielimy ludzi na grupy (1 grupa - 1 klasa): są 4 rzędy na środku lab 09, rząd przy ścianie dzielimy na 2 grupy = w sumie 6 grup. Wysyłamy link do stworzonego wcześniej repo, wszyscy robią `git clone`.

#### Nowości w kodzie do omówienia:

* w `Price` metoda klasy zwraca nowy obiekt tej samej klasy tzn. `Price` - nieoczywiste dla wielu osób!
* nowe type hinty (`Sequence`, `Tuple` etc.)
* `__eq__`, `__str__`, `__add__`, `__mul__` itp.
* struktura folderów z plikami `__init__.py`
* `@classmethod` (w `Price` jako zapewnienie dodatkowej metody inicjalizacji)
* `@property` (wszędzie)
* `__iter__` (w `Receipt`)
* `__len__` (w `Receipt`)
* `__repr__` pisany według standardowego szablonu (jak w `Price`)
* opcjonalnie: list comprehensions

Każda klasa ma dodatkowe funkcje na dole modułu. Służą one do generowania losowych obiektów danej klasy - gdyby któraś grupa wyrobiła się bardzo szybko ze swoim kodem i się nudziła, to niech napisze też te funkcje.


#### Organizacja:

* w każdej grupie ma być kierownik, któremu nadamy prawa do pushowania do repo
* na ogół to kierownik pisze kod, a reszta mu pomaga (ważne, żeby każda grupa wybrała osobę, która nie pisze w tempie 10wpm)
* każda grupa pisze testy i implementację swojej klasy i commituje swoje zmiany do lokalnego repo

### 3. Omawianie i próba integracji rozwiązań

**czas:** do końca laborki

Po przedstawieniu rozwiązań na forum, kierownik danej grupy robi `push`, reszta robi `pull --rebase --autostash`.

Wspólnie podejmujemy finalną próbę połączenia pracy wszystkich grup w działający program i odpalenia `main.py` :)
