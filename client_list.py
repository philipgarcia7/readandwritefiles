def main():

    infile = open("clients.txt", "r")

    n = 1
    for client in infile:
        print(n, ".", client.rstrip("\n"), sep="")
        n += 1


main()
