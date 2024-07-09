import sys
import json
import yaml
import xmltodict

def read_file(file_path):
    if file_path.endswith('.json'):
        return read_json(file_path)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return read_yaml(file_path)
    elif file_path.endswith('.xml'):
        return read_xml(file_path)
    else:
        print(f"Nieobsługiwany format pliku: {file_path}")
        sys.exit(1)

def write_file(data, file_path):
    if file_path.endswith('.json'):
        write_json(data, file_path)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        write_yaml(data, file_path)
    elif file_path.endswith('.xml'):
        write_xml(data, file_path)
    else:
        print(f"Nieobsługiwany format pliku: {file_path}")
        sys.exit(1)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print(f"Błąd dekodowania JSON z pliku {file_path}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Plik nie znaleziony: {file_path}")
        sys.exit(1)

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError:
        print(f"Błąd dekodowania YAML z pliku {file_path}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Plik nie znaleziony: {file_path}")
        sys.exit(1)

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def read_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = xmltodict.parse(file.read())
        return data
    except xmltodict.expat.ExpatError:
        print(f"Błąd dekodowania XML z pliku {file_path}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Plik nie znaleziony: {file_path}")
        sys.exit(1)

def write_xml(data, file_path):
    with open(file_path, 'w') as file:
        xml_string = xmltodict.unparse(data, pretty=True)
        file.write(xml_string)

def main():
    if len(sys.argv) != 3:
        print("Użycie: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_file(input_file)
    write_file(data, output_file)

    print(f"Dane pomyślnie skonwertowane z {input_file} do {output_file}")

if __name__ == "__main__":
    main()
