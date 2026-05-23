# Bash - Introdução

## Bash | sh | zsh

---

## Conteudo

- O que é **sh**
- O que é **bash**
- O que é **zsh**
- Diferenças entre shells
- Compatibilidade
- Qual usar

## Resumo

- **sh** >> Shell mais antigo e básico
- **bash** >> Shell padrão mais usado (Linux)
- **zsh** >> Shell moderno e altamente customizável
- *bash* é compatível com *sh*
- *zsh* é compatível com bash (em muitos casos)
- Cada shell tem suas próprias funcionalidades

---

## Código Bash

```bash
#!/bin/bash
echo "Olá mundo!"
echo "Executando Bash!"
# Sábia que isso aqui é um comentário? é igual ao Python!
```

---

## Conceito

Existem vários tipos de Shells, cada um com características próprias.

### Os mais comuns são:
  - **sh** (*Bourne Shell*)
  - **bash** (*Bourne Again Shell*)
  - **zsh** (*Z Shell*)

### Mas diferem em:
  - funcionalidades
  - compatibilidade
  - usabilidade

> **Todos eles fazem a mesma coisa:**
> ***interpretar comandos***

---

### sh (Bourne Shell)

O **sh** é o shell mais antigo e simples.
- Base para outros shells
- Poucas funcionalidades
- Alta compatibilidade
- Usado em scripts mais universais

```bash
#!/bin/sh
echo "Executando com sh"
```

### Bash (Bourne Again Shell)

O **bash** é o shell mais comum no Linux.

- Mais poderoso que sh
- Suporte a funções, loops e recursos avançados
- Compatível com scripts sh
- Padrão em muitas distribuições

```bash
#!/bin/bash
echo "Executando com bash"
```

### Zsh (Z Shell)

O **zsh** é um shell mais moderno.

- Altamente customizável
- Melhor autocomplete
- Suporte a plugins e temas
- Muito usado com *frameworks* como **Oh My Zsh**

```bash
#!/bin/zsh
echo "Executando com zsh"
```
--- 

## Principais Diferenças

| Shell | Característica                              |
| ----- | ------------------------------------------- |
| sh    | Simples e universal                         |
| bash  | Equilíbrio entre compatibilidade e recursos |
| zsh   | Produtividade e personalização              |

> [!WARNING] 
> ### Compatibilidade
> Nem todo script funciona igual em todos os shells.
> ```bash
> [[ 1 -eq 1 ]] && echo "OK"
> ```
> - Funciona no bash e zsh
> - Pode não funcionar no sh

>[!TIP]
> ### Qual usar?
> Depende do objetivo:
> - Scripts simples e compatíveis >> sh
> - Uso geral e scripts >> bash
> - Produtividade no terminal >> zsh

---

### Verificando seu shell atual
```bash
echo $SHELL
```

### Mudando de shell
```bash
chsh -s /bin/zsh
```

---

> [!NOTE]
> O **shebang** (`#!/bin/bash`) define qual shell executa o script
> Nem sempre `/bin/sh` é o mesmo shell em todos sistemas
> Em algumas distros, *sh* aponta para *bash* ou *dash*

> [!TIP]
> #### Se você está começando:
> use bash
> #### Se quiser produtividade depois:
> experimente zsh