# Fundamentos em Python3

## Transformação de Strings

---

## Conteudo

- Fatiamento
- Contagem de caracteres
- Procurar caracteres
- Verificar existencia
- Reposicionamento
- Maiusculas e Minusculas
- Capitalizar
- Titular palavras
- Remover espaços, multi direcional
- Dividir em palavras
- Juntar palavras

## Resumo

- `frase[index]`, Todas as strings podem ser identificadas cada caracter por uma index
- `.count("")` & `len()`, Contar caracteres especificos e tamanho de uma string
- `.find("")`, procurar uma caracter especifico, retornar uma index
- `in`, verificar se já existe as caracteres na string
- `.replace("", "")`, converter caracteres em outras
- `.upper()` & `.lower()`, Deixa a string em maiuscula ou minuscula
- `.capitalize()`, serve para deixar a primeira letra da primeira letra maiuscula
- `.title()`, serve para deixar todas as primeiras letras maiusculas
- `.strip()` & `.rstrip()` & `.lstrip()`, Remover espaços vazios em multidireções
- `.split()`, dividir as palavras em listas
- `"".join()`, adicionar caracterer para juntar

---

## Código Python

```python
frase = "Rian Batista"
frase_2 = input("Insira uma frase qualquer: ")

print(len(frase))                           # 12

print(frase[6])                             # a
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
```

---

## Manipulação_De_Texto[x:y:z]

Um texto pode ser manipulado para mostrar ou selecionar determinadas partes delas, vamos entender:

```python
frase = 'Rian Batista'
print(frase[6])                             # a
print(frase[5:11])                          # Batist
print(frase[0:11:2])                        # Ra ait
print(frase[:5])                            # Rian
print(frase[5:])                            # Batista
print(frase[5::11])                         # B
```

a manipulação de strings são determinadas em 3 caracteristicas **[Inicio : Fim : Pulos ]**.
Quando usamos `frase[6]` estamos pegando a frase no **index 6**, se separarmos a frase em pequenos espaços pre-locados notaremos isso melhor...

```bash
| R| i| a| n|  | B| a| t| i| s| t| a|
+--+--+--+--+--+--+--+--+--+--+--+--+
| 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|
```

Aqui vemos bem a separação de cada caracter da string em pequenas posições já alocadas, cada um sendo acessada por um valor.

### [Inicio] - [X] - []

Assim que usamos `frase[6]` estamos pegando a 7ª letra da string em questão, lembrando que **todos os index começam no 0**.
Outro exemplo é usando `frase[0]` estarimos selecionando a letra *"R"*.

> Podemos usar [-2], [-1] e até [-5] para pegarmos a penultima, ultima e a 5 letra de tras para frente em python

### [Inicio:Fim] - [X:Y] - [:]

Continue usando a tabela acima, vamos usar agora **[X:Y]**.
Se usarmos o `frase[5:11]` estariamos pedindo para o python selecionar a 5 até a penultima letra.
**Vamos entender melhor, sendo que a ultima letra é *a-11* e mesmo assim só saiu *batist*?**

Quando mandamos usar de *5 a 11* o python enterpreta assim:
*Começar no 5, parar no 11. "B-a-t-i-s-t"... (parar no 11)*
O Certo ent para mostrar tudo seria colocar *12 no Y* `frase[5:12]`

Uma outra dica agora, usando *[X:Y]*, se você pegar o inicio mesmo da frase, ou até o fim dela você pode!
`frase[:4]` significa ao python para ele que ele que **pegar do começo da frase até a 4ª posição**, sempre deixe um espaço vazio para isso, o resultado será `Rian`, mas você também pode fazer para pegar o resto da frase.
`frase[5:]` isso dirá ao python selecionar da **5ª posição até o final dela**.

> Podemos usar [:-2] para pegarmos do começo até a penultima letra e -1 para ultima letra, [-3:] da antepenultima até o fim

### [Inicio:Fim:Pulo] - [X:Y:Z] - [::]

Quando usamos `frase[0:12:3]` digamos ao python para **selecionar da posição 0 a 12, dando pulos de 3 caracteres...**, vamos entender melhor, *R-i-a-n- -B-a-t-i-s-t-a* se pularmos de 3, significa > *1-R, ok, 2-i, ok, 3-a, não!, 1-n, ok, 2- , ok, 3-B, não!...* e continua até acabar, ele faz esse contagem, quando der o valor do pulo, ele ignora aquela caracter

> Podemos usar `[::-1]` para mostrar e controlar a **reversidade** da string.

## Contagem len(), .count("")

Em python a função `len()` usa em seu interior uma string ou valores (listas, tuplas...) para analisar quantas caracteres ou valores existem atribuidas a ele

### len()

```python
lista = ["Rx4n", "Zer0", "House"]
nome = "Rian Batista"
nome_sem_espaco = nome.replace(" ", "")

print(len(lista))
print(len(nome))
print(len(nome_sem_espaco))
```

Vemos aqui que em **lista** ele conta os conteudos, e no resto ele conta as caracteres

### .count("")

É a função usado para contar uma caracter especifica em determinados espaços.

se usarmos `.count("i")` em algo, ele vai contar quantas vezes aparece aquele caracter

```python
nome = "Rian Batista"
print(nome.count("i"))
print(nome.count("a", 0, 5))
```

Vemos também aqui o uso de `.count("Z", X, Y)` onde *procuramos uma caracter Z indo de X a Y*.

## .find("")

Usamos esse metodo `.find("")` para procurar a primeira aparição de alguma caracter, ele rotornara o *INDEX*.

```python
frase = "Hello World"

print(frase.find("W"))
print(frase.find("Q"))
```

> Se retornar -1 significa que ele não pode encontrar a caracter especificada.

## .replace("", "")

Essa função é usada para reformular algo em uma string

```python
arquivo = input("Insira o nome do arquivo: ")

arquivo.replace(" ", "_")
print(arquivo)
print(arquivo.replace("_", "-"))
```

Ele faz a trocas dos caracteres mensionados por outra coisa que você desejar

## .upper(), .lower()

Mudar tamnho das caracteres por completo, pegamos uma string e modificamos completamente

```python
email = input("Email: ")
nome = input("Nome: ").upper()

print(f"Olá {nome}")
print(f"Seu email atual: {email}")
print(f"Será salvo assim: {nome.lower()} em seu {email.upper()}")
```

Vimos que podemos usar de 2 formar, seja para salvar ja modificado ou modificar mais tarde
`.upper()` deixa tudo maiusculo
`.lower()` deixa tudo minusculo

## .captalize(), .title()

São funções em python que ajudam a deixar as primeiras letras da string em letras maiusculas, e o resto minusculas.

### .captalize()

Usado para deixar a primeira letra maiuscula da primeira palavra, o restante minusculo.

### .title()

Usado para deixar as primeiras letras de cada palavra maiusculas.

## .strip(), .rstrip(), .lstrip()

São forma de remover espaços nulos contidos nas strings, porem só as que não estão entre as palavras.

```python
frase = "   Rian Batista   "

print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
```

`.strip()` remove os espaços em branco de ambos os lados
`.rstrip()` remove os espaços em branco do lado direito da string
`.lstrip()` remove os espaço em branco do lado esquerdo da string

## .split(), "".join()

Funções usadas para dividir string em espaços, e juntalas novamente.

### .split()

Divide a string em partes.

```python
frase = "Senhor dos Aneis"

print(frase.split())
```

### "".join()

Usado para juntar novamente as string

```python
frase = "Senhor dos Aneis"
frase.split()
print("-".join(frase))
```
