# Bash - Introdução

## O que é Shell?

---

## Conteudo

- O que é **Shell**
- O que é **Terminal**
- Interface **CLI**
- Comunicação com o sistema operacional
- Execução de comandos
- **Shell** como interpretador

## Resumo

- **Shell** é um interpretador de comandos
- Permite interação com o sistema via linha de comando (**CLI**)
- *Recebe comandos >> processa >> executa no sistema*
- **Bash** é um tipo de **shell**
- **Terminal** é onde o **shell** roda

---

## Primeiro Script Bash
> [!IMPORTANT]
> Crie um arquivo shell `introducao.sh`
> torne-o executavel `chmod +x introducao.sh`
> Para executa-lo escreva no *Terminal* `./introducao.sh` (*é nescessario ter na primeira linha do arquivo* `#!/bin/bash`)

```bash
#!/bin/bash
echo "Olá mundo"
```

---


## Conceito

O **Shell** é um programa que permite ao usuário interagir com o sistema operacional através de comandos.

Diferente de *interfaces gráficas* (**GUI**), onde usamos mouse e janelas, no **Shell** utilizamos texto para executar ações no sistema.

## Como funciona

Quando você digita um comando no terminal, acontece o seguinte:

1. O Shell recebe o comando
2. Interpreta o que foi digitado
3. Executa o comando no sistema operacional
4. Retorna o resultado na tela

### Exemplos:
```bash
echo "Olá mundo"
# output: Olá mundo
```

---

## Terminal vs Shell

É comum confundir os dois, mas são coisas diferentes:

- **Terminal** >> Interface onde você digita comandos
- **Shell** >> Programa que interpreta esses comandos

> #### Exemplo:
> Você abre o **terminal** >> o **Bash** roda dentro dele

### Tipos de Interface
  - **GUI** (Interface Gráfica)
  - Usa janelas
  - Usa mouse
  - Mais intuitiva
### **CLI** (Linha de Comando)
  - Usa texto
  - Mais poderosa
  - Mais rápida para automação

---

## Shell como interpretador

O **Shell** funciona como um intermediário entre você e o sistema.

```shell
ls
```

1. Recebe `ls`
2. Entende que é um comando de listagem
3. Executa no sistema
4. Retorna os arquivos

---

> [!NOTE]
>Você pode imaginar o **Shell** como:
>Um tradutor entre você e o sistema operacional
> 1. Você fala:
>   `ls`
> 2. O **shell** traduz:
>   "listar arquivos desse diretório"
> 
> Tudo no **Bash** é baseado em texto
> Comandos podem ser combinados
> O **Shell** é essencial para automação
> Muito usado em *servidores Linux*

> [!TIP]
> No começo pode parecer difícil usar só texto, mas com o tempo você percebe que:
> **CLI** é muito mais rápida que interface gráfica