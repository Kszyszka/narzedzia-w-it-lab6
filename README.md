# narzedzia-w-it-lab6
### Projekt na zaliczenie ćwiczenia Narzędzi w branży IT 6-8 (Projekt)

## Funkcjonowanie
Program przyjmuje dowolny (poprawny) plik w formatach: .json, .xml, .yml oraz konwertuje go do dowolnego innego formatu (.json, .xml, .yml).

## Użycie
### .exe (Automatyczny build ./artefacts/konwerter.exe)
Należy pobrać automatycznie zbuildowany plik .exe, który dostępny jest z poziomu:
- Repozytorium [./artefacts/konwerter.exe](https://github.com/Kszyszka/narzedzia-w-it-lab6/tree/main/artefacts)
- Build runtime (https://github.com/Kszyszka/narzedzia-w-it-lab6/actions)
- Release (https://github.com/Kszyszka/narzedzia-w-it-lab6/releases)
#### Plik może być rozpoznawany jako wirus przez Windows Update, można dodać go do wyjątku, lub postąpić z własnoręczym buildem wskazanym poniżej.

### .py (Manualny build)
1. Sklonowanie repozytorium lub pobranie
    ```
    git clone git@github.com:Kszyszka/narzedzia-w-it-lab6.git
    cd narzedzia-w-it-lab6
    ```
2. Pobranie zależności (oraz opcjonalny automatyczny build do .exe)
    ```
    pip install -r requirements.txt
    python konwerter.py [-h] source_file destination_file
    ```
    lub
    ```
    powershell.exe .\buildme.ps1
    cd artefacts
    .\konwerter.exe [-h] source_file destination_file
    ```