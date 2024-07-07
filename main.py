"""Program do konwersji danych w formatach .xml, .json, .yml."""
import argparse

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

def main():
    """Główna funkcja programu."""
    print(arguments().source_file.name)
    return 0

if __name__ == "__main__":
    main()
