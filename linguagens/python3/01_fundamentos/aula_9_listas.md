# Fundamentos em Python3

## Listas

---

## Conteudo

- Como criar **Listas** e usalas
- Criar uma **Lista dentro de uma Lista**
- **Remover/Deletar e Adicionar** valores de uma lista
- **Ordenar** listas
- Como **Criar/Evitar** criar Copias/Mesclar listas

## Resumo

- `lista = []` ou `lista = list()`, são meios de declaras uma lista em python
- `lista[]...`, são maneiras de acessar valores em listas
- `.append()`, `.insert(,)`, é uma forma de insirir valores
- `del()`, `.pop()`, `.remove()`, são formas de remover valores
- `.sort()` & `.sort(reverse=True)`, são jeitos de ordenar os itens das listas

---

## Código Python

```python
# Lista e manipulação
lanche = ["pizza", "hamburguer", "bolo", "batata", "pepsi"]
print(lanche)
print(lanche[3])
lanche[3] = "picole"
print(lanche[3])

# Adicionando ao final da lista
lanche.append("feijoada")
print(lanche)

# Insirindo em uma posição algo
lanche.insert(0, "arroz")
print(lanche)

# Formas de deletar valores
del lanche[2] # Especificar posição para remover
print(lanche)
lanche.pop(2) # Mostrar qual será o valor removido e remover
print(lanche)
lanche.remove("pepsi") # Mostrar escrito qual valor remover
print(lanche)

# Gerando uma lista
numeros = list(range(0, 10)) # Criamos uma lista de 0 a 9

# Ordenagem
numeros.sort(reverse=True)       # Deixar ao contrario
print(numeros)
numeros.sort()                   # Organizar novamente
print(numeros)

print(lanche.sort(reverse=True))

# Contando
print(len(numeros))

# Criando listas
dados = []                       # Lista vazia ou `dados = list()`
# ou
dados = list()
dados.append(["Rian", 20])       # adicioanndo valores a lista
dados.append(["Zer0", 19])
dados.append(["House", 19])
print(dados)                     # Lista completa de dados
print(dados[0])                  # primeiro valor da lista
print(dados[0:1])                # primeiro e segundo valor
print(dados[0][0])               # primeiro valor e primeiro valor
print(dados[2][1])               # segundo valor do ultimo valor

# Criando copias (ATENÇÃO!)
num_0 = [1, 2, 3]
num_1 = num_0
num_1.append(4)
print(num_0)                     # num_0 virou a mistura de num_1 com num_0, se mesclam

# Evitar de mesclar/virar copia
num_a = [1,2,3]
num_b = num_a[:]                 # Ele ira cria uma lista com base na lista anterior e n mesclar
num_b.append(4)
print(num_a)
print(num_b)
```

---

## Listas

Listas são variaveis que armazenas varios valores em conjunto, diferente das tuplas elas sim são manipulaveis

```python
# Formas de escrever listas

# Listas vazias
lista = list()
lista = []

# Maneiras de formar listas
lista = ["Rx4n", "Zer0", "House"]
numeros = [1, 2, 3, 4, 5]
alf_num = ["Python3", 27, 69, "Linux", 7, "Hardware", "Backend"]
numeros = list(range(0, 100))     # Gerando numeros de 0 a 99
```

Assim como manipular texto, essas variaveis são acessadas da seguinte forma

**usando código anterior**

```python
lista = ["Rx4n", "Zer0", "House"]
alf_num = ["Python3", 27, 69, "Linux", 7, "Hardware", "Backend"]
numeros = list(range(0, 100))

print(lista)
print(alf_num)
print(numeros)

print(lista[0])
print(lista[0:1])
print(lista[:])
```

Podemos acessar o primeiro valor da lista usando `lista[0]`
Ou acessar de um ponto ao outro `lista[0:1]`

O uso de **`[]`** nas listas é importante entender

- **lista[inicio : fim : pulo]**
  - inicio, marca onde iniciar a procura
  - fim, onde parar de mostrar
  - pulo, de qual em qual (igual é em `for(range())`)

---

## Listas dentro de listas (tipo tabelas (colunas x linhas))

Listas podem agir para categorizar, organizar e criar tabelas de certo modo

```python
players = [["Rx4n", 2500], ["Zer0", 3000], ["House", 1800]]

print(players)
print(players[1])
print(players[0][1])
```

Vemos que criamos uma lista de jogadores e suas pontuações, para isso criamos uma lista usando `[]` dentro dela criamos mais listas

```text

PLAYERS = [["Rx4n", 2500], ["Zer0", 3000], ["House", 1800]]
________________________________________________
| jogador 1    | jogador 2     | jogador 3     |
|--------------+---------------+---------------|
|nome | pontos | nome | pontos | nome | pontos |
|-----+--------+------+--------+------+--------|
|Rx4n |   2500 |Zer0  |   3000 |House |   1800 |
+----------------------------------------------+

PLAYERS[ JOGADOR ][ REGISTRO ]
```

Visualizando de outra forma:

|INDEX|nome         |       pontos|
|-----|------------:|------------:|
|0    |Rx4n         |         2500|
|1    |Zer0         |         3000|
|2    |House        |         1800|
|     |0            |1            |

- **PLAYERS[Y][X]**
  - `[Y]` - Qual Linha você quer (index)
  - `[X]` - Qual Coluna você quer (Nome/Pontos)

Isso serve para listas maiores também

```python
filmes = ["Zootopia", ["Animação", "Comedia"]], ["John Wick", ["Ação", "Aventura"]], ["Mario", ["Animação", "Jogo"]]

filmes[Y]        # Qual filmes
filmes[Y][X]     # Nome ou Generos
filmes[Y][1][Z]  # Dos generos, qual quer ver?
```

> [!TIP]
> Assim começa ficar complicado de analisar e entender, por enquanto vamos manter somente `LISTA[]` ou `LISTA[][]`

---

## Adicionando/Substituindo Valores

É possivel adicionar e susbituir valores ja existentes em listas, servem muito para atualziar ou ajustar valores em algumas situações

digamos que tenhamos um restaurante com comidas simples e poucas combinações

```python
comidas = ["arroz", "feijão", "batata"]
```

agora queremos adicionar um elemento principal

```python
comidas = ["arroz", "feijão", "batata"]

comidas.append("macarrão")

print(comidas)
```

vemos que agora no nosso menu de alimentos temos mais opções para escolha.
Digamos que mudamos batata para outra aliemnto

```python
comidas = ["arroz", "feijão", "batata"]

comidas.append("macarrão")

comidas.insert(2, "bolo")

print(comidas)
```

agora no lugar de batata temos bolo mas ainda temos batata no menu, so a ordem que ta diferente

- **.insert(X, Y)**
  - Inserir na posição de um alimento
  - X, posição
  - Y, item
- **.append()**
  - Adiciona no final da lista algum item

digamos que não quero mais batata no menu quero outro

```python
comidas = ["arroz", "feijão", "batata"]

comidas.append("macarrão")

comidas.insert(2, "bolo")

comidas[3] = "pizza"

print(comidas)
```

temos pizza no lugar de batata (substituido)

---

## Removendo/Deletando valores de uma lista

Para remover valores temos algumas opções para escolher

### Usando **`del()`**

```python
comidas = ['arroz', 'feijão', 'bolo', 'pizza', 'macarrão']

del comidas[2] # Deletando bolo

print(comidas)
```

### Usando **`.pop()`**

```python
comidas = ['arroz', 'feijão', 'bolo', 'pizza', 'macarrão']

comidas.pop()  # Deletando Ultimo valor
comidas.pop(0) # Deletando valor expecifico

print(comidas)
```

### Usando **`.remove()`**

Desta forma ele removera o primeiro valor que encontrar que combine com o que foi setado

```python
comidas = ['arroz', 'feijão', 'bolo', 'pizza', 'macarrão']

comidas.remove('pizza')  # Removendo o valor inserido

print(comidas)
```

---

## Ordenando

Semelhante a aula anterior, temos um comando para ordenar as coisas em listas

Diferente de TUPLAS **`.sort()`** pode alterar valores e mantelos alterados

```python
comidas = ['arroz', 'feijão', 'bolo', 'pizza', 'macarrão']
comidas.sort()
print(comidas)
```

Aqui vemos que não precisamos adicionar ao print a condição até o final do codigo ele se mantem organizado

funciona inversamente também

```python
comidas = ['arroz', 'feijão', 'bolo', 'pizza', 'macarrão']
comidas.sort(reverse=True)
print(comidas)
```

> [!TIP]
> Caso queira fazer uma lista que adicione valores conforme execute imagine que queria registrar 5 pessoas novas
> ```python
> registro = list()
> for pessoa in range(0, 5):
>     registro.append(input("Nome: "))
> print(registro)

## Cuidado ao usar listas!

> [!WARNING]
> Listas podem ser facilmente mescladas/copiadas
> exemplo bem comum:
> ```python
> n1 = [1, 2, 3]
> n2 = n1
> n2[2] = 100
> print(n1)

é bem comum valores se misturares para evitar isso é importante manter o código assim

```python
n1 = [1,2,3]
n2 = n1[:]
n2[2] = 100
print(n1)
```

Assim evitamos de criar copias/mesclar conteudos sem querer

> [!TIP]
> Listas são muito usadas em BigData para analise de dados como tabelas usandas com colunas e linhas
