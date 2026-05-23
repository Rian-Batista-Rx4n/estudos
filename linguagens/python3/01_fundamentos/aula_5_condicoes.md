# Fundamentos em Python3

## Condições

---

## Conteudo

- Caso a condição seja verdadeira, fazer algo
- Caso essa não seja, e essa for, fazer algo
- Caso contrario, fazer isso
- Adicionar mais condições
- Alternar condições
- Fazer **Aninhamento**

## Resumo

- `if` Verificar uma condição
- `elif` Verificar outras condições caso a anterior não satisfaz
- `else` Se nenhuma satisfazer, essa será executada
- `and` Verificar se todas as condições são verdadeiras
- `or` verificar se alguma condição é verdadeira
- Aninhamento: Espaçamento com a margem lateral esquerda do editor de código para criar um bloco separado para execução de um determinado termo.

---

## Código Python

```python
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

# Exemplo 2
if nome == "rian" and senha == "1234":
    print(f"Olá {nome}")
else:
    print(f"Usuario não encontrado")

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

# Exemplo 4
if idade >= 18:
    maior_de_idade = True

if maior_de_idade:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

```

---

### Aninhamento

> [!IMPORTANT]
> É bom esclarecer que agora iremos começar usar *aninhamento* não é complicado é só imaginar blocos de código para executar uma função...

```python
# Bloco 1
se x é igual a 1:
    conta = 1+1
    resultado = conta
    mostrar(resultado)

# Bloco 2
se x é diferente de 1:
    conta = x + 1
    resultado = conta
    mostrar(resultado)
```

Vemos que construimos 2 blocos, blocos são esses códigos que estão 4 espaços a margem esquerda da tela, são nescessario para o código entender que aquilo faz parte de outro bloco, e evitar de executar, eles só devem executar se satisfazerem uma condição.

---

## if

`if` é de longe umas das principais funcionalidades para se usar dentro do python, é ela que no final vai trabalhar para verificar algumas condições onde o código toma rumos diferentes até um resultado.

```python
nome = input("Nome: ")

if nome == "Rx4n":
    print("Logado como admin")
if nome != "Rx4n":
    print("Logado como Convidado")
```

Aqui vemos que o metodo de usar `if` pode variar muito os resultados em python pela maneira que ele recebe os valores, nesse exemplo ele detecta se o nome de usuario é *Rx4n*, para saber se é ou não o admin

`==` Compara se *X é igual a Y*
`!=` Compara se *X é diferente de Y*
`>`  Compara se *X é maior que Y*
`>=` Compara se *X é maior ou igual Y*
`<`  Compara se *X é menor que Y*
`<=` Compara se *X é menor que Y*

Outro metodo de verificar algumas condições, é o uso de valores booleanos, no final todo `if` na verdade está retornando um valor booleano...

```python
nome = "Rx4n"
print(nome == "Rx4n") # True
```

Esse print mostra que ao comparar `nome` com a string `"Rx4n"` ele retorna True, isso significa que a condição é verdadeira.
O `if` só é executado o seu bloco quando a condição é verdadeira

```python
admin = True

if admin:
    print("Logado como Admin")

if admin == False:
    print("Logado como convidado")
```

Esse código demonstra bem que se você é ou não admin do sistema, ele detecta se é True ou False a condição, e executa um ou outro.

## else

`else` é uma condição quando a demais não são favorecidas, ela executa se o `if` anterior não conseguir executar.

```python
nivel = "convidado"

if nivel == "admin":
    print("Logado como Admin")
else:
    print("Logado como convidado")
```

Vemos que caso o primeiro bloco não execute pois seu nivel não é convidado, o bloco do `else` quem será executado.

## if, elif, else

Agora o uso de `elif` durante os blocos `if`, so pode ser usado dentro de condições onde o `if` é executado primeiro.

```python
tipo_inimigo = "water"
tipo_jogador = "grass"

if tipo_jogador == "fire":
    print(f"Jogador tem fraquesa quanto a {tipo_inimigo}")
elif tipo_jogador == "water":
    print(f"Jogador tem jogo equilibrado quanto a {tipo_inimigo}")
elif tipo_jogador == "grass":
    print(f"Jogador tem vantagem contra o tipo {tipo_inimigo}")
else:
    print(f"Erro, nenhuma tipagem foi escolhida!")
```

Nesse código acima observamos bem que usamos 2 metodos com `elif`, isso que dizer **caso a condição antetior não satisfaça, tentar esse, caso não tentar esse...** e isso até acabar as condições.
Usar `else` nesses momentos nem sempre é nescessario, *nesse caso usamos para evitar erros e imprimir que temos uma falta de tipagem no jogo*.
A sequencia em usar é sempre `if` >> `elif` >> `else` é a sequencia correta.

```python
tipo_inimigo = "water"
tipo_jogador = "grass"

if tipo_jogador == "fire":
    print(f"Jogador tem fraquesa quanto a {tipo_inimigo}")
if tipo_jogador == "water":
    print(f"Jogador tem jogo equilibrado quanto a {tipo_inimigo}")
if tipo_jogador == "grass":
    print(f"Jogador tem vantagem contra o tipo {tipo_inimigo}")
else:
    print(f"Erro, nenhuma tipagem foi escolhida!")
```

Tente executar esse código agora que não tem `elif` e nota-se alguns problemas.

> usar ou não um elif apos um if, não significa que está certo, alguns caso pode variar a forma que constroi o código, notaram com praticas e treinamento.

## if, elif, else, and, or

Vamos agora juntar mais de uma condição para retornar algumas coisas

```python
usuario = "Rx4n"
senha = 1234
nivel = "admin"

if usuario == "Rx4n" and senha == 1234:
    if nivel == "admin":
        print(f"Bem-vindo de volta {usuario}, você está logado como Admin!")
    else:
        print(f"Bem-vindo de votla {usuario}!")
elif usuario == "" or senha <= 0:
    print("Os campos não foram preenchidos!")
else:
    print("Convido Logado com Sucesso")
```

Nesse código eu pesso que para testar, tente mudar os valores das variveis `usuario`, `senha` e `nivel`, e com isso você notara o rumo que o código toma como verificar se todos os campos foram preenchidos, se é o Rx4n quem logou, se é admin ele ou não, e se por fim é só outro convidado que logou.

```python
usuario = "Zer0"
senha = 4321

if (usuario == "Rx4n" and senha == 1234) or (usuario == "Zer0" and senha == 4321):
    print(f"Logado como admin, bem vindo {usuario}")
else:
    print("Acesso negado!")
```

Nesse momento usamos combinações de condições, *esperamos que o primeiro `()` seja verdadeiro **ou** o segundo `()` seja verdadeiro*
