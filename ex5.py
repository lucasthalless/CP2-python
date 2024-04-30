string = input("Digite uma string:\n")
invertedString = ""

for x in range (1, string.__len__()+1):
  invertedString += string[string.__len__()-x]

print(invertedString)