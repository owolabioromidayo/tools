import sys

def main(fpath):
    count = 0
    with open(fpath) as f:
        for line in f.readlines():
            for char in range(len(line)-1):
                if line[char] == ' ' and line[char+1] != ' ':
                    count += 1
    count += 1
    print(f"Count of file {fpath} is {count}")

if __name__ == "__main__":
    main(sys.argv[1])
