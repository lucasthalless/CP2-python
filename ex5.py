string = input("Digite uma string: ")
invertedString = ""

for x in range (1, string.__len__()+1):
  invertedString += string[string.__len__()-x]

print(f"String invertida: {invertedString}")