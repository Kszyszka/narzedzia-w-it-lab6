"""Program do konwersji danych w formatach .xml, .json, .yml."""
import argparse
import dicttoxml
import xmltodict
import json
import yaml

def arguments():
    """Funkcja obsługująca parsowanie argumentów przy uruchomieniu programu."""
    parser = argparse.ArgumentParser(
        prog="main.py",
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
    except FileNotFoundError:
        print("Plik źródłowy nie istnieje.")

    argumenty = parser.parse_args()
    return argumenty

def parse_data(source_file):
    """Funkcja do odczytywania danych z plików i konwersji do słownika."""
    if source_file.name[-4:] == 'json':
        content_dict = json.loads(source_file.read())
    elif source_file.name[-3:] == 'xml':
        content_dict = xmltodict.parse(source_file.read())
    elif source_file.name[-3:] == 'yml':
        content_dict = yaml.load(source_file.read(), Loader=yaml.SafeLoader)[0]
    else:
        print("Nieobsługiwany format pliku źródłowego.")
        return 0
    return content_dict

def main():
    """Główna funkcja programu."""
    argumenty = arguments()
    parse_data(argumenty.source_file)
    return 0

if __name__ == "__main__":
    main()
