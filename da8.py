def searchFile(key, filename):
    try:
        fin = open(filename, "r")
        lines = fin.read().split("\n")
        fin.close()
        for line in lines:
            if line == key:
                return True
            else:
                return False
    except FileNotFoundError:
        print("File not found")


def get_config_value(key, path):
    config_filename = "app.config"
    complete_path = path + "\\" + config_filename
    try:
        fin = open(complete_path, "r")
        lines = fin.read().split("\n")
        fin.close()
        for line in lines:
            pair = line.split("=")
            if pair[0] == key:
                print(pair[1])
            else:
                print("Key not found")
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':
    f = input("Input directory for config file: ")
    k = input("Input key: ")
    get_config_value(k, f)
