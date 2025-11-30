# MarkDown

Resumo completo de MarkDown, aqui mostra tudo o que da para fazer e escrever usando a sintaxe para arquivos `markdown.md`

## **Títulos**

### ===----- Texto -----===

```markdown
# Titulo 1
## Titulo 2
### Titulo 3
#### Titulo 4
##### Titulo 5
###### Titulo 6
```

### ===----- MarkDown -----===

# Titulo 1
## Titulo 2
### Titulo 3
#### Titulo 4
##### Titulo 5
###### Titulo 6

---

## **Enfases (Negrito, Italico, Riscar)**

### ===----- Texto -----===

```markdown
*itálico*     ou   _itálico_
**negrito**   ou   __negrito__
***negrito     e   itálico***
~~texto riscado~~
```

### ===----- MarkDown -----===

*itálico*
_itálico_

**negrito**
__negrito__

~~texto riscado~~

---

## **Listas**

### ===----- Texto -----===

```markdown
- Item
- Outro item
  - Subitem
    - Subitem 2

1. Primeiro
2. Segundo
   1. Subitem
   2. Subitem
```

### ===----- MarkDown -----===

- Item
- Outro item
  - Subitem
    - Subitem 2

1. Primeiro
2. Segundo
   1. Subitem
   2. Subitem

---

## **Links e Imagens**

### ===----- Texto -----===

```markdown
[Texto do link](https://example.com)
![Descrição da imagem](caminho/imagem.png)
```

### ===----- MarkDown -----===

[Texto do link](https://example.com)
![Descrição da imagem](caminho/imagem.png)

---

## **Código (inline e bloco)**

### ===----- Texto -----===

```markdown
Use o comando `ls -la` no terminal.

    ```python
    print("Hello, Markdown!")
    ```

```

### ===----- MarkDown -----===

Use o comando `ls -la` no terminal.

```python
print("Hello, Markdown!")
```

---

## **Citação (Quote)**

### ===----- Texto -----===

```markdown
> Isso é uma citação.

> Linha 1  
> Linha 2  
> Linha 3
```

### ===----- MarkDown -----===

> Isso é uma citação.

> Linha 1  
> Linha 2  
> Linha 3

---

## **Separadores (Linha horizontal)**

### ===----- Texto -----===

```markdown
---

ou

***
```

### ===----- MarkDown -----===

---

ou

***

---

## **Tabelas**

### ===----- Texto -----===

```markdown
| Nome    | Idade | Cargo     |
|---------|-------|-----------|
| João    | 20    | Dev       |
| Maria   | 25    | Designer  |
| Carlos  | 30    | Engenheiro|
```

### ===----- MarkDown -----===

| Nome    | Idade | Cargo     |
|---------|-------|-----------|
| João    | 20    | Dev       |
| Maria   | 25    | Designer  |
| Carlos  | 30    | Engenheiro|

---

## **Checklists (Caixas de tarefa)**

### ===----- Texto -----===

```markdown
- [ ] A fazer
- [x] Concluído
- [ ] Outro item
```

### ===----- MarkDown -----===

- [ ] A fazer
- [x] Concluído
- [ ] Outro item

---

## **Avisos / Blocos tipados (GitHub Flavored)**

### ===----- Texto -----===

```markdown
> [!NOTE]
> Isso é uma nota.

> [!WARNING]
> Isso é um aviso.

> [!IMPORTANT]
> Informação essencial.

> [!TIP]
> Dica útil.
```

### ===----- MarkDown -----===

> [!NOTE]
> Isso é uma nota.

> [!WARNING]
> Isso é um aviso.

> [!IMPORTANT]
> Informação essencial.

> [!TIP]
> Dica útil.

---

## **Abas e Spoilers (GitHub)**

### ===----- Texto -----===

```markdown
<details>
<summary>Clique para expandir</summary>

Conteúdo oculto aqui…

</details>
```

### ===----- MarkDown -----===

<details>
<summary>Clique para expandir</summary>

Conteúdo oculto aqui…

</details>

---

## Listas de definição**

### ===----- Texto -----===

```markdown
Termo
:   Definição do termo

Markdown
:   Linguagem simples de formatação
```

### ===----- MarkDown -----===

Termo
:   Definição do termo

Markdown
:   Linguagem simples de formatação

---

## **Tabelas com alinhamento**

### ===----- Texto -----===

```markdown
| Esquerda | Centro | Direita |
|:---------|:------:|--------:|
| a        | b      | c       |
| d        | e      | f       |
```

### ===----- MarkDown -----===

| Esquerda | Centro | Direita |
|:---------|:------:|--------:|
| a        | b      | c       |
| d        | e      | f       |

---

## **Emoji**

### ===----- Texto -----===

```markdown
🔥 🚀 🐺 💙

:fire:
:rocket:
```

### ===----- MarkDown -----===

:fire:
:rocket:

---

## **Cores (limitado, depende da plataforma)**

### ===----- Texto -----===

```markdown
<span style="color:blue">Texto azul</span>
```

### ===----- MarkDown -----===

<span style="color:blue">Texto azul</span>

---

## **HTML dentro do Markdown**

### ===----- Texto -----===

```markdown
<p align="center">Texto centralizado</p>

<img src="imagem.png" width="300px">
```

### ===----- MarkDown -----===

<p align="center">Texto centralizado</p>

<img src="imagem.png" width="300px">

---

## **Comentários (não aparecem no render)**

### ===----- Texto -----===

```markdown
<!-- Esse texto não aparece no arquivo renderizado -->
```

### ===----- MarkDown -----===

<!-- Esse texto não aparece no arquivo renderizado -->

---

## **Referências (links no rodapé)**

### ===----- Texto -----===

```markdown
Esse é um link de referência [clique aqui][link1]

[link1]: https://example.com
```

### ===----- MarkDown -----===

Esse é um link de referência [clique aqui][link1]

[link1]: https://example.com

---

## **Blocos de citação com código**

### ===----- Texto -----===

```markdown
> Exemplo de comando:
>
> ```bash
> sudo pacman -S firefox
> ```
```

### ===----- MarkDown -----===

> Exemplo de comando:
>
> ```bash
> sudo pacman -S firefox
> ```

---

## Markdown para READMEs (GitHub)

- O GitHub reconhece automaticamente:
  - README.md
  - CONTRIBUTING.md
  - LICENSE
  - CHANGELOG.md