## ENGETO-Python-3-projekt
Třetí projekt na Python Akademii od Engeta.

## Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

### Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuálníprostředí s nainstalovaným manažerem spustit následovně:

    $ pip3 --version			# ověřím verzi manažeru
    $ pip install -r requirements.txt	# nainstaluje knihovny

### Spuštění projektu
Spuštění souboru Projekt_3_Elections_Scraper.py v rámci příkazového řádku požaduje dva povinné argumenty.
python soubor.py URL adresu: "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205" a název souboru "vysledky_Most.csv"

    python Projekt_3_Elections_Scraper.py <odkaz-uzemniho-celku> <vysledny-soubor.csv>
Následně se vám stáhnou výsledky jako .csv soubor.

### Ukázka projektu
Výsledky hlasování pro okres Most:
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205
2. argument: vysledky_Most.csv

python Projekt_3_Elections_Scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205" "vysledky_Most.csv"

### Spuštění programu:
    python Projekt_3_Elections_Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205' 'vysledky_Most.csv'

### Průběh stahování:
    $ WELCOME TO THE APP ELECTION SCRAPER$
    $ DATA ARE DOWNLOADING FROM SELECTED URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205
    $ THE DATA WAS DOWNLOADED TO A FILE:
    $ <user_file_adress>\vysledky_Most.csv
    $ FILE SIZE:
    $ 2898 bytes

### Částečný výstup:
    ...
    code, location, registered, enveloped, valid, Občanská demokratická strana,...
    567043, Bečov, 1286, 489, 486, 29, 2, 0, 42, 12, 66, 2, 5, 5, 1, 1, 18 , 0 , 8, 211, 0, 3, 5, 0, 0, 0, 1, 74, 1
    567027, Most, 52759, 24735, 24620, 2139, 60, 7, 1720, 698, 2471, 419, 168, 317, 20, 37, 1843, 34, 748, 9832, 7, 100, 246, 11, 143, 26, 150, 3345, 79
    ...