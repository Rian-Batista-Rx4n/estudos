# Fundamentos em Python3

## Dicionarios

---

## Conteudo

- Como são e o que é **Dicionarios**.
- Como **acessar** os valores dentro de dicionarios.
- Como **adicionar** e **remover** valores em Dicionarios.
- O que são **items**, **Keys** e **Values** e acessando.
- Criando **Dicionarios dentro de Listas** e acessando.
- Criando **Dicionarios dentro de Dicionarios** e acessando.
- Criando **Dicioanrios com Listas dentro** e acessando.

## Resumo

- `dict()` or `dict = {}`, criando variaveis com tipagem de **dicionario**
- `.items()`, itens são o conjunto de ***chaves*** e ***valores***
- `.keys()`, chaves são as **"variaveis"** do dicionario criado
- `.values()`, valores são os **dados dentro das "variaveis"** dos dicionarios

---

## Código Python

```python
dados = dict()
# ou
dados = {"nome": "Rx4n", "idade": 20}
print(dados)           # {'nome': 'Rx4n', 'idade': 20}
print(dados['nome'])   # 'Rx4n'
print(dados['idade'])  # 20

dados['sexo'] = "M"  # Adicionando mais uma "Variavel" no dicionario
print(dados)         # {'nome': 'Rx4n', 'idade': 20, 'sexo': 'M'}

dados['nome'] = "Zer0"  # Substituindo uma "Variavel" no dicionario
print(dados['nome'])    # Zer0

dados['idade'] += 5  # Adicionando +5 a idade
print(dados)         # {'nome': 'Zer0', 'idade': 25}

del dados['idade']
print(dados)         # {'nome': 'Zer0'}

filme = {
    'titulo': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f"O {k} é {v}")

# Dicionarios dentro de Dicionario
alunos = {
    "Rx4n":{
        "cuida": "backend",
        "linguagens": ["Python", "JavaScript", "Bash"],
        "nivel": "junior"
    },
    
    "Zer0":{
        "cuida": "frontend",
        "linguagens": ["html", "css", "react", "typescript"],
        "nivel": "senior"

    },

    "House":{
        "cuida": "marketing",
        "linguagens": ["markdown", "python"],
        "nivel": "pleno"
    }
}

# Lista de Dicionários (Estrutura idêntica a um Array de Objetos JSON)
usuarios_api = [
    {
        "id": 101,
        "nome": "Rx4n",
        "ativo": True,
        "permissoes": ["admin", "editor"]
    },
    {
        "id": 102,
        "nome": "House",
        "ativo": False,
        "permissoes": ["user"]
    },
    {
        "id": 103,
        "nome": "Zer0",
        "ativo": True,
        "permissoes": ["moderador", "user"]
    }
]

print(usuarios_api[2])
print(usuarios_api[1]['nome'])
```

---

## Dicionarios

Os dicionários em Python são estruturas de dados mutáveis e flexíveis que armazenam informações no formato chave-valor. Eles são ideais para mapear, organizar e buscar dados de forma rápida e intuitiva, já que cada valor é recuperado por meio de uma chave de identificação única.

para criar um dicionario utilizamos "`{}`" ou definimos uma variavel como `dicionario = dict()`. Assim como nas listas, temos essas formas de criar dicionarios

```python
dados = dict()

# ou

dados = {"nome": "Rx4n", "idade": 20}

print(dados)           # {'nome': 'Rx4n', 'idade': 20}
print(dados['nome'])   # 'Rx4n'
print(dados['idade'])  # 20
```

A estrutura para entender dicionario é facil vamos pensar que o "dicionario" (`dados`), fosse um conjunto de variaveis, temos o nome dela `idade` e ela vai armazenar um valor `20`.

|Dicionario|"Variavel"|"Valor"|
|:--------:|:--------:|:-----:|
|dados     |nome      |Rx4n   |
|dados     |idade     |20     |

Dicionarios são excelente para armazenas valores e manter uma organização exepcional!
Seus valores são faceis de acessar em dicionarios grandes e tendo mais deles.
Lembrando que a estrutura para montar dicionarios é extamente esse:

```text
DICIONARIO = { "VARIAVEL" : "VALOR", ... }
```

E para acessar esses valores, você pede qual dicionario usar e qual valor você quer

```python
dicionario = {"nome_1": "nome_x", "nome_2": "nome_y", "nome_3": "nome_z"}

print(dicionario['nome_3'])
print(f"Bem vindo {dicionario['nome_3']}")
```

---

## Adicionando e removendo valores

Existem 2 formas de "adicionar" valores em dicionarios

### Acrescentando valor ao Dicionario

```python
dados = {"nome": "Rx4n", "idade": 20}

print(dados)         # {'nome': 'Rx4n', 'idade': 20}

dados['sexo'] = "M"  # Adicionando mais uma "Variavel" no dicionario

print(dados)         # {'nome': 'Rx4n', 'idade': 20, 'sexo': 'M'}
```

Desta forma acrementamos mais um valor em nosso dados, agora o "Rx4n" tem um genero definido como "M" (masculino), assim é possivel criamos varios valores e um dicionario.

Caso o valor já exista a "Variavel" o valor nela será substituido:

```python
dados = {"nome": "Rx4n", "idade": 20, "sexo": "M"}

print(dados)            # {'nome': 'Rx4n', 'idade': 20, 'sexo': 'M'}

dados['nome'] = "Zer0"  # Substituindo mais uma "Variavel" no dicionario

print(dados['nome'])    # Zer0
```

> [!IMPORTANT]
> **Lembre-se sempre!**
> `DICIONARIO['VARIAVEL'] = 'VALOR'`
> Ou ira **Adicionar novos valores** ou ira **Substituir valores atuais**

Você pode fazer ajustes automaticas também elas são mutaveis!

```python
dados = {"nome": "Rx4n", "idade": 20}

print(dados)         # {'nome': 'Rx4n', 'idade': 20}

dados['idade'] += 5  # Adicionando +5 a idade

print(dados)         # {'nome': 'Rx4n', 'idade': 25}
```

Tudo que aprendeu até agora você pode usar

### Removendo Valores

Para remover valores indesejados também segue a mesma logica aqui vamos udar **`del`**

```python
dados = {"nome": "Rx4n", "idade": 20}

print(dados)         # {'nome': 'Rx4n', 'idade': 20}

del dados['idade']

print(dados)         # {'nome': 'Rx4n'}
```

Ele remove a "variavel" que mensionou nos dados, mesma coisa que Acrementar/Adicionar você também remove.

---

## Itens, Chaves e Valores

Para o python, dicionarios tem um comportamento diferente, esses fatores são exenciais para a organização do código e syntax do python

```python
filme = {
    'titulo': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

print(filme.values())
print(filme.keys())
print(filme.items())
```
> [!TIP]
> Se até então não foi explicado, até fechar com `""` ou `()` ou `[]` ou `{}` tudo pode ser aninhado para não ficar uma linha comprida.

Diferença entre os novos comandos `.items()`, `.keys()` e `.values()`:

### `.items()`

São a junção de `.keys()` com `.values()`:

```python
filme = {
    'titulo': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

print(filme.items()) 
# dict_items([('titulo', 'star wars'), ('ano', '1977'), ('diretor', 'george lucas')])
```

### `.keys()`

São os identificadores únicos (como palavras em um dicionário de idiomas). Você usa a chave para pesquisar um valor. Devem ser tipos de dados imutáveis (strings, números, etc.).

```python
filme = {
    'titulo': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

print(filme.keys())
# dict_keys(['titulo', 'ano', 'diretor'])
```

> [!WARNING]
> Toda **KEY** (Chaves) podem ser qualquer objeto imutável (strings, números, e até tuplas).

### `.values()`

É o conteúdo ou dado associado à chave (como o significado da palavra). Aceitam qualquer tipo de dado (listas, números, textos ou até outros dicionários).

```python
filme = {
    'titulo': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

print(filme.values())
# dict_values(['star wars', '1977', 'george lucas'])
```

> [!NOTE]
> #### Resumo da "opera":
> |              | .KEYS()   | .VALUES()      |
> |:------------:|:---------:|:--------------:|
> | **.ITEMS()** | 'titulo'  | 'Star Wars'    |
> | **.ITEMS()** | 'ano'     | '1977'         |
> | **.ITEMS()** | 'diretor' | 'george Lucas' |

---

**Para acessar esses valores você pode fazer por exemplo:**

```python
for k,v in filme.items():
    print(f"O {k} é {v}")

# O titulo é star wars
# O ano é 1977
# O diretor é george lucas
```

---

## EXTRAS

### Usando Dicionarios com Listas

```python
aluno = {
    "nome": "Ana",
    "idade": 22,
    "disciplinas": ["Matemática", "Física", "Programação"]
}

# Acessando a segunda disciplina
print(aluno["disciplinas"][1])  # Output: Física
``` 

Dentro do **dicionario `aluno`** temos uma *chave* chamada `disciplinas` que é uma *lista* e podemos acessar do `aluno` suas `disciplinas` tendo 3 até o momento

---

### Usando Dicionarios dentro de Dicionarios (com listas)

Aqui vamos criar um database dos alunos da escola e seus detalhes:

```python
# Dicionário onde os valores são listas de disciplinas
alunos = {
    "Rx4n":{
        "cuida": "backend",
        "linguagens": ["Python", "JavaScript", "Bash"],
        "nivel": "junior"
    },
    
    "Zer0":{
        "cuida": "frontend",
        "linguagens": ["html", "css", "react", "typescript"],
        "nivel": "senior"

    },

    "House":{
        "cuida": "marketing",
        "linguagens": ["markdown", "python"],
        "nivel": "pleno"
    }
}
```

> [!TIP]
> Experimente ficar usando (`print()`, `.items()`, `.values()`, `.keys()`, `for` e `[]`) para ir vendo e praticando seus valores

Agora vamos destrinchar

- **print(alunos)**
  - Vamos obter **todos os dados** dos `alunos`
- **print(alunos['Rx4n'])**
  - Vamos obter os dados do aluno `Rx4n`
- **print(alunos['Rx4n']['linguagens'])**
  - Vamos obter os dados das `linguagens` do aluno `Rx4n`
- **print(alunos['Rx4n']['linguagens'][1])**
  - Vamos obter a segunda `linguagens` do aluno `Rx4n`

Experimente agora usando essa DATABASE de ALUNOS os seguintes comandos:

```python
# Vendo todos dados para cada Aluno
for k,v in alunos.items():
    print(f"| {k} | {v} |")

# Vendo todos os dados detalhados dos dados de cada aluno
for k,v in alunos.items():
    print(f"| {k} | {v} |")
    for k2, v2 in v.items():
        print(f"< {k2} >< {v2} >")
```

> [!WARNING]
> #### Nivel Avançado
> **Usando tecnicas que vimos anté o momento**
> Criando um sistema de pesquisa por Alunos com menu bonito:
> ```python
> while True:
>     nome = input("\nDigite o NOME do aluno (ou 'sair' para fechar): ").strip()
>    
>     if nome.lower() == 'sair':
>         print("Encerrando o programa...")
>         break
>        
>     aluno_encontrado = None
>     
>     # For tradicional para buscar o aluno ignorando maiúsculas/minúsculas
>     for chave in alunos:
>         if chave.lower() == nome.lower():
>             aluno_encontrado = alunos[chave]
>             break # Interrompe o loop assim que encontra
>            
>     if aluno_encontrado:
>         linguagens_str = ", ".join(aluno_encontrado["linguagens"])
>        
>         print(f"\n--- Dados de {nome} ---")
>         print(f"Cuida de: {aluno_encontrado['cuida'].capitalize()}")
>         print(f"Usa:      {linguagens_str}")
>         print(f"Nível:    {aluno_encontrado['nivel'].capitalize()}")
>     else:
>         print("Aluno não encontrado! Tente novamente.")
>```

---

### Usando Dicionarios dentro de listas

Como fazer dicionarios dentro de listas e usar dados!

> [!NOTE]
> O formato de lista de dicionários no Python é a representação idêntica de um JSON (JavaScript Object Notation) contendo uma lista de objetos

```python
# Lista de Dicionários (Estrutura idêntica a um Array de Objetos JSON)
usuarios_api = [
    {
        "id": 101,
        "nome": "Rx4n",
        "ativo": True,
        "permissoes": ["admin", "editor"]
    },
    {
        "id": 102,
        "nome": "House",
        "ativo": False,
        "permissoes": ["user"]
    },
    {
        "id": 103,
        "nome": "Zer0",
        "ativo": True,
        "permissoes": ["moderador", "user"]
    }
]
```

Para acessar podemos usar:

```python
# Percorrendo a lista de usuários
for usuario in usuarios_api:
    # Verifica uma condição dentro do dicionário
    if usuario["ativo"]:
        status = "Ativo"
    else:
        status = "Inativo"
        
    # Formatando a exibição dos dados
    print(f"Usuário: {usuario['nome']} | Status: {status}")
    print(f"Permissões: {', '.join(usuario['permissoes'])}")
    print("-" * 30)

# Ou pegando um dicionario em alguma posição e seu valor
print(usuarios_api[2])
print(usuarios_api[1]['nome'])
```

---

> [!IMPORTANT]
> ## Encerramento do Modulo
> Com isso terminamos o **Modulo_01 (Fundamentos em Python3)**
> Sempre revise conteudos e treine bem, pegue exemplos e desafios para praticarem e sempre se organizem.
> 
> ***Código simples é melhor do que complexo.***
>
> As coisas começaram a ficar dificeis de entender mas praticando se entende melhor, coisas uteis virão e desafios piores chegaram :).