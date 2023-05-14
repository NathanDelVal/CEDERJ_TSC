binary = input("Digite um número binário para começar \n")

counter = 0

for x in binary:
    if x != "1" and x != "0":
        print(binary, " não está codificado em binário")
        counter = 1
        break

if counter == 0:
    print("A soma de ", binary, " por 1 é:")
    for x in range(len(binary) - 1, -1, -1):
        if binary[x] == "0":
            binary[x] = "1"
            break
    print(binary)
