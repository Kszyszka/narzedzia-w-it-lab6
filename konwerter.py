"""Program do konwersji danych w formatach .xml, .json, .yml."""
import argparse
import json
from xml.parsers.expat import ExpatError
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
import xmltodict
import yaml

def arguments():
    """Funkcja obsługująca parsowanie argumentów przy uruchomieniu programu."""
    parser = argparse.ArgumentParser(
        prog="konwerter.py | konwerter.exe",
        description="Program do konwersji plików .xml, .json, .yml.",
        epilog="Made by Krzysztof Hager 52687 'Kszyszka' @ DSW."
    )
    try:
        parser.add_argument('source_file',
                            metavar='source_file',
                            type=open)
        parser.add_argument('destination_file',
                            metavar='destination_file',
                            type=argparse.FileType('w', encoding='UTF-8'))
        argumenty = parser.parse_args()
    except FileNotFoundError:
        print("Plik źródłowy nie istnieje.")
        return 0
    except PermissionError:
        print("Brak wymaganych uprawnień do obsługi wskazanych plików.")
        return 0
    return argumenty

def parse_data(source_file):
    """Funkcja do odczytywania danych z plików i konwersji do słownika."""
    try:
        if source_file.name[-4:] == 'json':
            content_dict = json.loads(source_file.read())
        elif source_file.name[-3:] == 'xml':
            content_dict = xmltodict.parse(source_file.read())
        elif source_file.name[-3:] == 'yml':
            content_dict = yaml.load(source_file.read(), Loader=yaml.SafeLoader)[0]
        else:
            print("Nieobsługiwany format pliku źródłowego.")
            return 0
    except json.JSONDecodeError:
        print("Plik źródłowy .json posiada niepoprawną składnię pliku.")
        return 0
    except ExpatError:
        print("Plik źródłowy .xml posiada niepoprawną składnię pliku.")
        return 0
    except yaml.scanner.ScannerError:
        print("Plik źródłowy .yml posiada niepoprawną składnię pliku.")
        return 0
    return content_dict

def dump_data(destination_file, content_dict):
    """Funkcja do zapisywania danych ze słownika do pliku źródłowego (json, xml, yml)."""
    if destination_file.name[-4:] == 'json':
        destination_file.write(json.dumps(content_dict, indent=4))
    elif destination_file.name[-3:] == 'xml':
        parsed_content = parseString(dicttoxml(content_dict, return_bytes=False)).toprettyxml()
        destination_file.write(parsed_content)
    elif destination_file.name[-3:] == 'yml':
        destination_file.write(yaml.dump(content_dict, allow_unicode=True))
    else:
        print("Nieobsługiwany format pliku źródłowego.")
        return 0
    return 1

def main():
    """Główna funkcja programu."""
    argumenty = arguments()
    if argumenty:
        zawartosc = parse_data(argumenty.source_file)
        if zawartosc:
            dump_data(argumenty.destination_file, zawartosc)
        else:
            print("Wystąpił problem ze składnią pliku źródłowego, wstrzymywanie programu.")
            return 0
    else:
        print("Wystąpił problem z plikiem źródłowym, wstrzymywanie programu.")
        return 0
    return 1

if __name__ == "__main__":
    main()
