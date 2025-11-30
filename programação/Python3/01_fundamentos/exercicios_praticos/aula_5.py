# Registrando inputs
nome = input("Nome: ")
senha = input("Senha: ")
idade = int(input("Idade: "))



# Exemplo 1
if nome == "rian":
    if senha == "1234":
        print(f"Olá {nome}!")
    else:
        print("Usuario não encontrado")
else:
    print("Usuario não encontrado")



# ===----- Separador de Exemplos -----===
print("="*45)
# ===----- Separador de Exemplos -----===



# Exemplo 2
if nome == "rian" and senha == "1234":
    print(f"Olá {nome}")
else:
    print(f"Usuario não encontrado")



# ===----- Separador de Exemplos -----===
print("="*45)
# ===----- Separador de Exemplos -----===



# Exemplo 3
print("Vamos jogar Pedra Papel e Tesoura")
print("[1] Pedra, [2] Papel, [3] Tesoura")

escolha = int(input(">> "))

if escolha > 3 or escolha < 1:
    print("Jogada Invalida!")
else:
    if escolha == 1:
        print(f"{nome} Jogou: Pedra!")
    elif escolha == 2:
        print(f"{nome} Jogou: Papel!")
    else:
        print(f"{nome} Jogou: Tesoura!")



# ===----- Separador de Exemplos -----===
print("="*45)
# ===----- Separador de Exemplos -----===



# Exemplo 4
if idade >= 18:
    maior_de_idade = True

if maior_de_idade:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
