# Fundamentos em Python3

## Tuplas

---

## Conteudo

- O que são e como usar **Tuplas**
- Como **Contar** valores
- Como **Ordenar** valores
- Como indentificar **Posição** de um valor
- Como **remover/deletar** Tuplas

## Resumo

- `tupla = ()` Variaveis que são imutaveis / possui valores imutaveis (Não mudam de jeito nenhum) 
- `.count()`, função para contar items dentro de uma "variavel"
- `.sorted()` e `.sorted( ,reverse=True)` usado para re-ordenar de crescente e decrescente os resultados
- `.index()`, usamos para identificar a INDEX do item
- `del()` para remover tuplas

---

## Código Python

```python
lanche = ("hamburguer")
comidas = ("arroz", "feijão", "batata", "macarrão")

# Verificando as tuplas
print(lanche)
print(comidas[2])

# Verificando tamanho
print(len(lanche))
print(len(comidas))

# Mostrando cada item de uma tupla
for comida in comidas:
    print(comida)

# Ordenando
print(sorted(comidas))
print(sorted(comidas, reverse=True))

# Acrescentando valores a uma tupla
numeros_0 = (1, 3, 5, 2, 54)
numeros_1 = (2, 75, 2445, 24, 2)
numeros = numeros_0 + numeros_1
print(numeros)
print(numeros_0)
del(numeros_0)
print(numeros_0)
print(numeros)

print(numeros.count(2))

tupla = ("Rian")
print(tupla)

print(tupla[0] = ("Rx4n"))
```

---

## Tuplas

O que são tuplas? São variaveis conhecidas como:
- Variaveis Compostas
- Variaveis Imutaveis

> [!NOTE]
>São chamadas assim por que seus valores não podem ser alterados assim que o código é executado, diferente das variaveis normais onde falamos o que são ou podem ser, aqui nas tuplas variaveis definidas são elas até o final do cídigo

```python
tupla = ("Rian")
print(tupla)

print(tupla[0] = ("Rx4n")) # Erro, tuplas são imutaveis
print(tupla[0])            # 'Rian'

tupla = ("1", "2", "3")    # Tupla anterior é apagada, e criada essa nova
tupla[1] = ("Dois")        # Erro, não posso mudar o valor de "2" para "dois"
print(tupla[1])            # '2'

# Outras formas de fazer tuplas
tupla = 1, 2, 3
tupla = "1", "2", "3"
tupla = (123, 456, 789)
tupla = (1, "2", 3, "4")
tupla = (1, 2) + (3, 4)   # Output (1, 2, 3, 4)
```

> Tuplas são semelhante a **LISTAS** (veremos na próxima aula)

> [!NOTE]
>pode parecer que elas são mutaveis sim, porem lembre-se, ao colocar a mesma variavel com outros valores, você está criando uma nova e apagando a antiga, tuplas agem como forma de gaurdar varios valores, porem não podendendo alteras depois é como escrever senhas num papel a caneta, não tem como apagar sem trocar o papel ou rabiscando senhas antigas e rescrevendo elas.

## Ordenagem

é possivel organizar o resultado de um print de tupla

```python
numeros = 3, 4, 1, 5, 7

print(sorted(numeros)) # [1, 3, 4, 5, 7]
print(sorted(numeros, reverse=True)) # [7, 5, 4, 3, 1]
```

Usamos **`sorted()`** para colocarmos em ordem **crescente**
Usamos **`sorted(, reverse=True)`** para invertemos e ficar em **decrescente**

## Contando valores

Podemos contar quantas vezes um valor aparece dessa forma:

```python
numeros = (1, 3, 5, 2, 54, 2, 75, 2445, 24, 2)
palavra = "Rian Batista"
print(numeros.count(2)) # 3
print(palavra.count("a")) # 3
```

Usamos **`.count()`** para contar valores, podem ser texto, palavras, caracteres, numeros qualquer valor que queira contar

## Indentificando posição de valores

Podemos receber a posição do **INDEX** do valor que estamos procurando

```python
numeros = (1, 3, 5, 2, 54, 2, 75, 2445, 24, 2)
print(numeros.index(54)) # 4

# |  1|  3|  5|  2| 54|  2|...|   VALORES DA TUPLA
# |---|---|---|---|---|---|...|   -----------------
# |  0|  1|  2|  3|  4|  5|...|   INDEX DOS VALORES
```

Nesse caso estavamos procurando o valor `54` dentro da tupla e foi achada na *posição 4*.

podemos identificar volores apos outros:

```python
numeros = (1, 3, 5, 2, 54, 2, 75, 2445, 24, 2)
print(numeros.index(2, 6)) # 9
```

Aqui estamos procurando o valor `2` apos o INDEX `6`, depois dele ele vai procurar o primeiro `2` que encontrar.

> [!TIP]
> Caso pedir um valor que não esteja na lista, você será recebido com um erro pois não foi possivel encontrar ele, caso queira evitar isso faça o seguinte
> ```python
> numeros = 1,2,3,4,5,6
> opc = int(input("Valor desejado: ")) # Digite um numero inteiro para achar ex. 7
> if opc in numeros:                   # Verificando existencia
>     print(f"Foi encontrado na posição: {numeros.index(opc)}") # Mostrando index
> else:                                # Caso não exista
>     print(Não existe)
> ```
> Assim evitamos erros.

## Deletando tuplas

Podemos deletar tuplas não mais usadas

```python
n1 = 1,2,3,4,5
n2 = 6,7,8,9,0
n3 = n1+n2

print(n1)
del(n1)        # Deletamos n1
print(n1)      # Erro, não existe n1
print(n3)      # Calculo antes de ter deletado
```

Usamos **`del()`** para deletarmos valores especificos até variaveis

> [!IMPORTANT]
> Lembrando que não possivel deletar valores dentro da tupla por tuplas serem o que são, **imutaveis**.