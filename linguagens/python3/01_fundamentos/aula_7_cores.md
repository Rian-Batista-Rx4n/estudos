# Fundamentos em Python3

## Cores

---

## Conteudo

- Customização ao imprimir, cores e estilizar

## Resumo

- `\033[m`: usar a tabela de ANSI para gerenciar e organizar cores no terminal python

---

## Código Python

```python
print("\033[4;36;41m Rian Batista \033[m")
print("\033[34;107m Rian Batista \033[m")
print("\033[41m Rian Batista \033[m")
print("\033[7;36;41m Rian Batista \033[m")
print("\033[1;35m Rian Batista \033[m")
```

---

## Explicação Rápida

Usar cores e estilizar texto no python é muito simples e não é nescessario muita explicação.

### Código principal
**`\033[m`** esse é seu código principal, ele quem diz o que seu texto será **daqui para frente**

> [!WARNING]
> O código `\033[m` transforma os textos apos ele, se n quiser seu código inteiro modificado lembrese sempre de fechar a area que n quer mais pinta com ele **exatamente** assim **`\033[m`**


### Syntax e Funcionamento

- **`\033[E;CT;CFm`**
  - **`\033[`** Parte Principal
  - **`E`** Estilização (0, 1, 4, 7)
  - **`CT`** Cor do Texto (30, 31, 32, 33, 34, 35, 36, 37 e 97)
  - **`CF`** Cor do Fundo (40, 41, 42, 43, 44, 45, 46, 47 e 107)
  - **`;`** Separar Funções
  - **`m`** Finalizar Customização

---

## Tabela de Códigos ANSI

Disponibilizando um guia em tabelas para se organizar qual formatação usar para customizar

### Reset

|Python    |Função  |
|:--------:|:-------|
|`\033[0m` |Resetar |

---

### Cores Texto

|Python    |Cor     |
|:--------:|:-------|
|`\033[30m`|Preto   |
|`\033[31m`|Vermelho|
|`\033[32m`|Verde   |
|`\033[33m`|Amarelo |
|`\033[34m`|Azul    |
|`\033[35m`|Magenta |
|`\033[36m`|Ciano   |
|`\033[37m`|Cinza   |
|`\033[97m`|Branco  |

---

### Cores Fundo

|Python     |Cor     |
|:---------:|:-------|
|`\033[40m` |Preto   |
|`\033[41m` |Vermelho|
|`\033[42m` |Verde   |
|`\033[43m` |Amarelo |
|`\033[44m` |Azul    |
|`\033[45m` |Roxo    |
|`\033[46m` |Ciano   |
|`\033[47m` |Cinza   |
|`\033[107m`|Branco  |

---

### Estilizar

|Python   |Estilo    |
|:-------:|:---------|
|`\033[1m`|Negrito   |
|`\033[4m`|Sublinhado|
|`\033[7m`|Invertido |

---

## Extra

você pode criar variaveis para customizar texto automaticamente, exige espaço e nescessidade, caso realmente queira fazer algo puro no terminal

```python
# 1. Definição das variáveis de cores (Estilo;Cor do Texto)
VERMELHO = '\033[31m'
VERDE = '\033[32m'
AZUL = '\033[34m'
AMARELO = '\033[33m'
NEGRITO = '\033[1m'

# 2. Variável de reset (obrigatório para voltar ao normal)
RESET = '\033[m'

# 3. Utilizando as variáveis com f-string
nome = "Ana"
pontos = 95

print(f"{NEGRITO}{AZUL}Olá, {nome}!{RESET} Sua pontuação é {VERDE}{pontos} pontos{RESET}!")
print(f"{VERMELHO}Atenção:{RESET} {AMARELO}Você precisa melhorar!{RESET}")
```

> [!NOTE]
> Não é nescessario fazer essas customização, a não ser que queria um programa inteiro no python, cores ajuda a usuarios identificar o que estão fazendo só de analisar cores, fica bonito no terminal, mas somente caso queira um Aplicativo que use o terminal como fonte do programa.