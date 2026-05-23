# Fundamentos em Python3

## Loops e Repetições

---

## Conteudo

- Criar estruturas para **Loops/Repetições** por parte do código
- Criar **Paradas** para o codigo
- Formas de criar **Loops**

## Resumo

- `for`/ `while` São funções para iniciar loops com execuçao diferente entre si
- `break` Metodo usado para quebrar/parar um loop
- `in range()`, `in *Lista*`, `in *Texto*` Formas para determinar como usar e receber valores de uma repetição

---

## Código Python

```python
lista = ["Python3", "JavaScrit", "Java", "MySQL", "Kotlin"]
texto = "Rian Batista"

# Loops For
# Usando Range
for i in range(0, 10):
    print(i)

print("="*40)

for i in range(0, 10, -1):
    print(i)

print("="*40)

for i in range(0, 10, 2):
    print(i)

print("_-"*20)

#Usando Listas e Texto (Funciona com tuplas e dicionarios também)
for i in lista:
    print(i)

for i in range(0, len(lista)-1):
    print(lista[i])

print("="*40)

for i in texto:
    print(i)

print("#"*40)

# Loops While
# Condição verdaderia
contador = 0
while True:
    print("Oi")
    if contador = 5:
        break
    else:
        contador += 1

print("="*40)

# Condição sendo falsa passando para true
opc = ""
while not "exit" in opc:
    opc = input("Digite exit para sair").lower().strip()

print("="*40)

# Condição de quantidade
numero = 0
while numero < 5:
    print("Adicionando +1")
    numero += 1
```

---

## FOR

Ao usarmos o loop `for` é como se tiversimos valores "fixos" para repetir o código (recomendado sempre que possivel usar o `for`

- `for` Significa que estamos dando inicio a uma Repetição for
- `i` É uma sigla qualquer usado como *INDEX* para indicar uma variavel do `for`, pode ser qualquer item ex. `letra`, `i`, `numero`, `amo_python` todas serão variaveis do `for`
- `in` quer dizer dentro, ela vai usar alguma maneira de executar esses *loops* até parar, seja por tamanho ou outra coisa
- `range()` usamos *range* quando queremos uma distancia, um numero de repetições, não nescessariamentente é preciso ser numero, podem ser funções ou variaveis que retornam ou são número, ex. `for numero in range(inicio, fim):` se tivermos uma variavel `inicio = 1` e `fim = 11` nosso programa vai contar de 1 a 10. **Sempre o final é considerado 1 a menos, mais facil de entender, se o "*fim*" é considerado como 10, logo seu valor de parada será 9.**
  - `range(x, y)` >> é de incio a fim
  - `range(x, y, z)` >> se *z* é -1, logo é feito reverso, se z é positivo/negativo logo terá um valor de pulo
- `lista`, `tuplas` e `dicionarios` são memlhores maneiras de correr por muitos valores procurando algo que quer, quando usamos uma dessas formas de armazenar muitas informações, é muito bom usar `for` nessas situações
- `texto` quando usamos uma *string* no `for i in texto:` dividimos cada caracter em um *index* para ela

### `for numero in range(0, 10):`

> Para cada, numero, em, uma distancia de, 0 a 10...

### `for letra in nome:`

> para cada, letra, em, nome...

### `for numero in lista_numero:`

> para cada, numero, em, uma lista de números...

esses valores `numero`e `letra` pode ser acessador pelo nome de sua variaveis, que são `numero` e `letra`

---

## WHILE

Quando usamos o loop `while` é comum usar para quando não temos uma noção correta de repetições, como mostragem de menus, usamos para gerar repetições até que suas condições não os satesfazem mais

```python
while True:
    # Exibir um menu simples com print()
    print("""\n[1] HelloWorld
[2] Rian Batista
[0] Exit""")

    opc = int(input(">> "))   # Anotando opição escolhida

    if opc == 1:
        print("HelloWorld")   # Caso digitar 1, ele imprime helloworld
    elif opc == 2:
        print("Rian Batista") # Caso digitar 2, ele imprime Rian Batista
    elif opc == 0:
        break                 # Caso digitar 0, ele para a execução do loop
    else:
        print("\nPor favor insir valor coerente") # Caso digitar qualquer coisa
```

Aqui por exemplo vemos um **loop while infinito**, ele fica repetindo um "menu" até digitar o valor **0** para parar o comando com **break**. Loops while são exelentes nessas ocasiões onde você de algo repetindo um numero de vezes que você não saiba o quão nescessario, para isso while foi introduzido para exibir um menu de opções para executar ações

Existem varias formas de usar `While` durante o código vamos ver algumas funcionalidades

### while not 'exit' in comando:

Como parar um bloco de código ao digitar uma palavra especifica.

```python
comando = ""

while not 'exit' in comando:      # Enquanto comando não for exit, repetir...
    comando = input("Digite EXIT para fechar...").lower().strip()

print("fim")
```

nesse exemplo ele está "verificando" quando for digitado **exit** para parar, passamos o seguinte entendimento:
- **comando**, está vazio
- **while**, iniciar um loop
- **not 'exit'**, passando uma condição para invertela
  - **comando = ''** está vazio ou outro valor
  - **not 'exit' in comando**, o valor é exit? não, então FALSE, porem estamos negando NOT, logo invertemos de FALSE para TRUE, o `in` serve para vere se tem 'exit' em comando, caso sim TRUE, como NOT inverte, FALSE.
  - enquanto não for EXIT a palavra a condição de while é TRUE, ficar ativado
- **comando = input()...** insirindo um novo valor para comando
- fim da linha de while, vamos repetir, se ainda for TRUE a condição ele continuara, se for FALSE ele ira parar o loop, logo proximo passo é...
- **print("fim")**, acabamos com o loop e seguimos até finalizar o código.

Ainda não entendeu? vamos seguir para algo diferente...

### while True:

```python
while True:    # Loop infinito (não temos nada para mudar seu valor)
    opc = input("Digite 'SAIR' para parar").strip().lower()
    if opc == 'sair':
        break
```

Agora sim você vai entender como funcionar o loop while.
**while** é em outras palavras está fazendo o seguinte *`Enquanto...`*
O while só é executado enquanto for **VERDADEIRO** sua condição por isso `True`
Significa que while vai ficar "ATIVO" vai executar seu bloco sempre que for VERDADEIRO, se for FALSO ele para (`false` faz o while parar)

>[!IMPORTANT]
> **break**
> como nossa condição só é `True` não temos nada que altere quando for `false` já que demos VERDADEIRO como condição, para isso usamos o BREAK para parar instantaneamente o loop, sempre use break para condições INFINITAMENTE VERDADEIRO onde nada possa mudar.

>[!NOTE]
> Use while somente para loops sem um valor expecifico para terminar, como MENUs, caso contrario se for usar `while True` lembre-se de colocar algo para dar BREAK se não seu comando nunca para, e dependendo até trave por não conseguir parar.

### while not idade >= 18:

Verificando se você tem idade nescessaria para usar o programa.

```python
idade = 0                 # Idade padrão para executar o loop.

while not idade >= 18:    # Enquanto idade não for maior ou igual 18, repetir...
    print("Esse sistema usa dados pessoais, para registrar qual sua idade?")
    idade = int(input(">> "))    # Insirir idade atual

    if idade <= 17:       # Um aviso extra e opcional, não nescessario.
        print("Idade insuficiente!")

print("Carregando sistema...")   # Executado apos o loop detectar FALSE
```

Vamos analisar melhor o seguinte... `not idade >= 18`
se definimos um input de `idade = 0`, logo verificando ela com `idade >= 18` o python daria um output de `False`, como passamos a instrução `not` logo ele inverte valores booleans, traznedo `False` para `True` assim deixando o while como true.
Teste o seguinte no terminal e vc verá

```python
>>> idade = 0
>>> idade >= 18
>>> False            # Output
>>> not idade >= 18
>>> True             # Output
```

> [!NOTE]
> Tudo que o `not` vier antes, ele negara a condição seguinte, se for TRUE ele traz FALSE, se for FALSE ele traz TRUE.

## Extra

Teste esse comando, você nunca sabe quando ele vai fechar, mas ele pode terminar cedo ou tarde

```python
from random import randint

soma = 0

print('Digite "exit", para fechar...\n')

while soma < 21:
    soma += randint(1, 10)

    print(f"Você tem {soma}.")
    opc = input("Comprar mais? [Y/n]: ").strip().lower()

    if soma == 21:
        print("VOCÊ GANHOU!")
        soma = 0
    elif soma > 21:
        print("VOCÊ PERDEU!")
        soma = 0
    elif opc == 'n':
        print("ok...")
        soma = 0
    elif opc == 'exit':
        break

print("Fim...")
```

