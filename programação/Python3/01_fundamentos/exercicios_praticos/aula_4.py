frase = "Rian Batista"
frase_2 = input("Insira uma frase qualquer: ")

print(len(frase))                           # 12

print(frase[-6])                             # a
print(frase[5:11])                          # Batist
print(frase[0:11:2])                        # Ra ait
print(frase[:5])                            # Rian
print(frase[5:])                            # Batista
print(frase[5::11])                         # B

print(frase.count("i"))                     # 2
print(frase.count("i", 0, 5))               # 1

print(frase.find("Bat"))                    # 5
print(frase.find("Hobbit"))                 # -1

print(frase.replace("Batista", "Valfenda")) # Rian Valfenda
print(frase.upper() + " " + frase.lower())  # RIAN BATISTA rian batista
print(frase.capitalize())                   # Rian batista
print(frase.title())                        # Rian Batista

print(frase_2.strip())
print(frase_2.rstrip())
print(frase_2.lstrip())
print(frase_2.split())

print("-".join(frase_2))
