d = {}
INPUT = "input.txt"

def main():
    with open(INPUT,"r") as f:
        for line in f:
            for word in line.strip().split(" "):
                if word not in d:
                    d[word] = 1
                else:
                    d[word] = d[word] + 1

    print(d)
    print(f"{len(d)} különböző szó van az állományban.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
