# Fundamentos em Python3

## Variaveis e Tipos primitivos

---

## Conteudo

- Variaveis
- str
- int
- float
- bool
- Tipos

## Resumo

- Variaveis: são items que podem receber e armazenar valores, para serem utilizados posteriormente.
- `str()` são textos, qualquer textos que queira escrever ou converter, conhecido como 'Strings'
- `int()` são números inteiros, qualquer número sendo [-1, -14, 0, 20, 27...] conhecido como 'Inteiros' e pode ser usado para converter em inteiro
- `float()` são números com casas decimais [1.27, -23.223, 0.1, 27.777...] conhecido como 'Números Flutuantes' e pode ser usado para converter em Números Flutuante
- `bool()` são valores lógicos, sendo [True & False] conhecido como 'Valores Boleanos', também pode ser usado para converter valores em valores lógicos
- Tipos: vamos observar as funções [`isspace()`, `isnumeric()`, `isalpha()`, `isalnum()`, `isupper()`, `islower()` e `istitle()`]

---

## Código Python

```python
nome = 'Rian Batista'
idade = 19
peso = 46.65
maior_de_idade = True
```

---

## Variaveis

## `nome`, `idade`, `peso` e `maior_de_idade`

São variaveis declaras, que podem funcionar com a analogia a gavetas.

Imagine que numa gaveta chamada `nome` você quer guardar o nome do usúario, então você insere o comando: `nome =`.

O simbolo de "igual" em `=` significa que a variavel `nome` estará recebendo um valor, o valor adjacente é nescessario uma tipagem especifica para o **Python** identificar o que tem dentro dele, se são números, textos, valores lógicos ou números decimais

## Praticas recomendadas ao declarar uma variavel

### nomenclaturas

- **snake_case**: Você utiliza `_` para separar os nomes grandes.
  - `nome_cliente =`
  - `maior_de_idade? =`
  - `cidade_estado_pais =`
- **camelCase**: Você utiliza letras maiusculas ao iniciar uma palavra nova nas variaveis.
  - `nomeCompleto =`
  - `idadeAtual =`
  - `placaDeVideo =`
- **PascalCase**: Cada palavra começa com maiúscula.
  - `CorFavorita =`
  - `TemaSelecionado =`
  - `IdiomaSelecionado =`
- **UPPER_CASE**: Todas as letras maiúsculas, palavras separadas por `_`.
  - `NUMERO_MAXIMO_PESSOAS =`
  - `MAIOR_NUMERO =`
  - `NUMERO =`
- **kebab-case**: Palavras separadas por `-` (Não usado em python erro de syntax)
  - `nome-completo =`
  - `numero-total-de-arquivos =`
  - `numero-de-paginas =`
- **mixedCase**: Prefixos indicando tipo ou contexto (não é mais utilizado hoje).
  - `strNome = "Rx4n"`   > // string
  - `nContador = 0`      > // number
  - `pUsuario = ...`     > // pointer

## Regras para nomes de variáveis

- Permitido:
  - Letras minúsculas e maiúsculas;
  - Números (desde que não no início);
  - Underscore (_).

- Não permitido:
  - Espaços, acentos ou símbolos especiais;
  - Palavras reservadas (if, for, while, etc.).

## Dica

> Sempre de nomes descritivos as variaveis, que ao ler elas você sabera o que ela armazena, porem não colocar nome gigantes, poderar gerar fadiga de ficar lendo algo imenso para dizer algo simples.

---

## Tipos primitivos - `'Rian Batista'`, `19`, `46.65` e `True`

São valores que as nossas recentes variaveis criadas recebem, são informações, imagine que as gavetas com adesivos nomeando o que guardar, receberam um nome como **Rian Batista**, sabe algo peculiar que pode se notar aqui? uso de `''`, `.` e `True`.

---

### Str, Strings

Quando falamos de **Strings** ou **Textos** para que o **Python** entenda o que deve ser lido como um texto é nescessario envolver a informação entre `''` ou `""`, escrever uma variavel dessa forma `nome_completo = Rian Batista` resultara em um erro de *syntax*

Você pode converter também algum valor em string usando str(), o que tiver dentro dela sera alterado para texto...

```python
idade = 19
idade_texto = str(idade)
print(idade_texto)
```

---

### Int, Inteiros, Números

Aqui entra os **número inteiros**, exemplos: `17, -14, 0, 1, 127...`. Quando é declarado uma variavel onde se coloca um numero que não tenha casas decimais, são considerados número inteiros, aqui vai alguns exemplos:

```python
idade = 19
paginas = 65
y = -25
print(idade, paginas, y)
```

Podemos também transformar strings em números caso a string seja sómente númerica (composta por números e nada alem):

```python
conquistas_texto = "27"
conquistas_int = int(conquistas_texto)
print(conquistas_int)
```

---

### Float

Números Flutuantes ou números com casas decimais, são número onde utilizamos um `.` para separar as casas **lembrando, como códigos normalmente são criados e interpetrados usando o INGLES como referencia, os decimais que dividimos em `,`, no ingles é utilizado `.`. Aqui vai alguns exemplos:

```python
altura = 1.69
peso = 45.6
restantes = -23.754
print(altura, peso, restantes)
```

---

### Bool

Valores booleanos, são valores que representam um sistema "binario" [True ou False], [Verdadeiro ou Falso], [0 ou 1]... essa é a lógica dele, representar quando algo é `True` ou `False` (lembrando que o python só interpreta se a primeira letra estiver em maiuscula).

```python
permitir_notificacoes = True
usuario_logado = False
novas_mensagens = 1
```

Notace que em `novas_mensagens = 1` usamo o numero 1, em **bool** qualquer valor diferente de nulo e maior que 0 é considerado como *VERDADEIRO*, mesmo se colocarmos `987` nessa varivel, se passarmos ela no `bool(novas_mensagens = 987)` ele retornaram como `True`, experimente com:

```python
novas_mensagens = 987
print(bool(novas_mensagens))
```

---

## Verificar Tipagem

### isspace()

Usado nas variaveis para verificar se a variavel é somente *espaços*

```python
variavel = "Testar Variavels String 2.0"
print(varivavel.isspace())
```

---

### isnumeric()

Usado nas variaveis para verificar se a variavel é composta somente por números

```python
variavel = "Testar Variavels String 2.0"
print(varivavel.isnumeric())
```

---

### isalpha()

Usado nas variaveis para verificar se a variavel é composta somente por letras

```python
variavel = "Testar Variavels String 2.0"
print(varivavel.isalpha())
```

---

### isalnum()

Usado nas variaveis para verificar se a variavel é composta por letras combinadas com números somente

```python
variavel = "Testar Variavels String 2.0"
print(varivavel.isalnum())
```

---

### isupper()

Usado nas variaveis para verificar se a variavel está com as caracteres maiusculas

```python
variavel = "Testar Variavels String 2.0"
print(varivavel.isupper())
```

---

### islower()

Usado nas variaveis para verificar se a variavel está com as caracteres minusculas

```python
variavel = "Testar Variavels String 2.0"
print(varivavel.islower())
```

---

### istitle()

Usado nas variaveis para verificar se a variavel está com as caracteres inicias maiusculas

```python
variavel = "Testar Variavels String 2.0"
print(varivavel.istitle())
```
