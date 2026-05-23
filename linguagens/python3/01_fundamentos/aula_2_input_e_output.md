# Fundamentos em Python3

## Input e Output

---

## Conteudo

- Como usar **input** para inserir valores
- Como ver conteudos dentro de variaves/resultados com **print()**
- Personalização dos resultados imprimidos na tela/terminal com **"f" strings**
- Verificação de tipos primitivos com **type**
- Como fazer **Quebra de texto** ao imprimir valores/resultados
- Como **Juntar Linhas** ao imprimir valores/resultados
- Como **Incrementar, Decrementar, Multiplicar e Dividir** valores/resultados de variaveis e salvalas

## Resumo

- `input()` São comando utilizados para receber um valor do usuario pelo terminal
- `print()` Função do python para imprimir textos no terminal
- *"f" strings*: É um metodo que se utiliza junto ao print() para personalizar a saida de texto
- `type()` Função para verificar qual é o tipo primitivo da variavel
- `\n` syntax usado para delimitar uma sequencia de texto com uma quebra de linha
- `, end=""` syntax usado para juntar a proxima linha com o texto princiapl
- `+=`, `-=`, `*=`, `/=` usamos para acrementar ou diminuir valores de uma variavel

---

## Código Python

```python
nome = input("Nome: ")
idade = input("Idade: ")

print(f"Bem-vindo, {nome}.\nVocê tem {idade} anos de idade")

print(type(nome))
print(type(idade))

peso = float(input("Peso: "))

print(f"Seu peso é de {peso}, o tipo da variavel é {type(peso)}")
```

---

## input()

A função input em python é uma ferramenta que é utilizada para **receber uma informação vinda do usuario**, elá é personalizada para imprimir um texto junto de uma espera de um comando, seja numeros, simbolos, textos, qualquer coisas que tiver até apertar ENTER para confirmar.

Por padrão **todo valor inserido seja até nulo, é guardado em String `str()` seja numero ou texto, sempre o resultado do que colocar ao receber um input será transformado em string** e guardado em uma variavel

É uma maneira exelente caso você tenha que **amarzenar valores não fixo**, você "pergunta" o que quer salvar na variavel, como um *nome*

```python
nome = input()
nome = input("Insira qualquer valor: ")
```

Nesse exemplo podemos observar que o input le de qualquer forma, porem você pode insirir um texto acompanhdo adicionando "" dentro da função `input()`, ali você pode imprimir um texto junto com o input.

```python
idade = int(input("Insira sua idade: "))
print(idade)
```

Vemos aqui que nesse exemplo, o `input()` esta dentro da função `int()` que transforma o valor dentro dele em **número inteiro**, isso é uma maneira automatica de receber um valor e já transformalo, porém é **facil de dar erro nesses casos, já que ele pede em outras palavras um valor inteiro, se eu enviar uma letra o programa trava**, ficar atento a esses casos por agora, futuras aulas demonstrarei como evitar erros em seu código.

---

## type()

A função `type()` é usada para demonstrar qual **tipo primitivo** uma variavel armazena, se é *bool*, *int*, *float*, *str*... Ela é usada desta forma:

```python
notificacao = True
numero_notificacoes = 16

print(type(notificacao))
print(type(numero_notificacoes))
```

---

## "f" Strings

As chamas *f strings* são maneiras de imprimir um texto (String) só que com formatação "dinamica", diferente das String normais `"String"` temos a `f"String"`, vou explicar com alguns exemplos:

```python
primeiro_nome = "Rian"
sobrenome = "Batista"
idade = 19
peso = 46.65
maior_de_idade = True

print(f"Seja bem-vindo, {primeiro_nome + ' ' + sobrenome}!")
print(f"Sua idade atual é de {idade} com peso de {peso:.1f}")
print(f"Testando se {primeiro_nome} é maior de idade... {maior_de_idade}")
```

Vemos nesse exemplo que quando vamos imprimir um texto com `print()` alem de usamos as `" "` aspas, usamos também a letra *f* antes das aspas, isso indiga para o interpretador do python que a string a seguir pode ser **formatada**.
A formatação é quando você molda algo para sair como planejado, igual vimos nos 3 *prints* que usamos acima.

---

### print(f"Seja bem-vindo, {primeiro_nome + ' ' + sobrenome}!")

Aqui usamos as variaveis `primeiro_nome` combinando com a variavel `sobrenome` usando o sinal de *+* para juntar as strings delas, para evitar que a saida seja *RianBatista* adicionamos entre as variaveis uma espaçamento `' '`.
Você deve ter notado que usamos agora `' '` invez de `" "`, vou explicar o porque, por costume eu uso para output sempre "", porem imaginasse se que quero escrever algo "ironico" igual fiz aqui, o python lê o que esta entre abrir e fchar aspas, assim com os parenteses, ent se tiver um `print("Ola "rian"")` ele vai entender que a string acaba em ola e começa vazio depois, o *rian* ele entende como parte do codigo do *console* para evitar isso você deve começar por '' caso queria usar "" dentro, se usar "" vc deve usar '' dentro.
Outro detalhe é que dentro das {} do f-string, você pode executar qualquer coisa que o python entende como parte do console, pode fazer contas, comandos, etc... ele lê como comando e executa, e ja mostra o resultado formatado exemplo:

```python
num1 = 2
num2 = 2
print(f"Soma do primeiro numero mais o segundo é de {num1 + num2}")
```

Aqui ele ja faz o calculo sem presisar declarar mais uma variavel.

---

### print(f"Sua idade atual é de {idade} com peso de {peso:.1f}")

O uso de `:.1f` dentro de {} ao lado da variavel, significa que :. inicia a interpretação do python para entender que quero formatar essa variavel, 1 ou qualquer outro valor significa quantas casas decimais vou querer como saida, e o f indica que é um numero float ou seja tem casas decimas.

Aqui vai mais exemplos usando `print(f'{varivavel:}')` no python3:

```python
nome = "Rx4n"

print(f'Olá {nome}!')     # Normal

print(f'Olá {nome:20}!')  # Espaçamento de 20 caracteres
print(f'Olá {nome:>20}!') # alinhas 20 caracteres para direita
print(f'Olá {nome:<20}!') # alinhar 20 caracteres para esquerda 
print(f'Olá {nome:^20}!') # Alinha ao centro usando 20 caracteres como referencia
print(f'Olá {nome:=^20}!')# Alinhar ao centro usando 20 caracteres personalizados, no caso "="
```

---

## Quebrar Linhas: `\n`

Usado durante uma string numa função `print()`, o `\n` serve como quebra de linha para pular o texto a frente em novas linhas.

```python
print("Olá Rx4n,\nSeja bem vindo!\n    >> Versão 1.0")
print("\n Gostaria de reiniciar?")
input("[S/N]\n>> ")
```

## Manter a mesma linha: `, end=""`

Utilizado também em função de imprimir texto, diferente do `\n` ele junta a proxima linha com a anterior.

```python
print("Atualizando o sistema", end="")
print(".", end="")
print(".", end="")
print(".", end="   ")
print("PRONTO!")
print("Tudo atualizado.")
```

## Adicionar, Remover, Multiplicar, Dividir... valores: `+=` `-=` `*=` `/=` 

É facil de usar, significa que queremos adicionar a uma variavel ou diminuir os valores dela, podendo ser usadas para multiplicalas ou dividilas entre outros operadores numericos.

```python
contador = 0
cooldown = 15

contador += 1
print(contador)
contador += 5
print(contador)

cooldown -= 10
print(cooldown)
cooldown -= 5
print(cooldown)

cooldown *= 10
print(cooldown)
cooldown /= 5
print(cooldown)
```
