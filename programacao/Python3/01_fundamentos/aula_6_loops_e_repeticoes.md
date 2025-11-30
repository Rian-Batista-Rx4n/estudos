# Fundamentos em Python3

## Loops e Repetições

---

## Conteudo

- Loops / Repetições
- Paradas
- Maneiras

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

## WHILE

Quando usamos o loop `while` é comum usar para quando não temos uma noção correta de repetições, como mostragem de menus, usamos para gerar repetições até que suas condições não os satesfazem mais
