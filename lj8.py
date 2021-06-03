import json
import lj7


def load_json_file(file):
    try:
        fin = open(file)
        contents = fin.read()
        fin.close()
        return contents
    except FileNotFoundError:
        raise FileNotFoundError


def write_json_file(file, json_output):
    try:
        fout = open(file, "w")
        fout.write(json.dumps(json_output))
        fout.close()
        return True
    except IOError:
        print("Could not write file")
        return False


if __name__ == '__main__':
    inverted = lj7.invert_dict(json.loads(load_json_file("locations.json")))
    print(inverted)
    print(write_json_file("output.json", inverted))
