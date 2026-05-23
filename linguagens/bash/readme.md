# 🐧 Bash — Documentação de Estudos

Esta pasta reúne toda a minha trilha de aprendizado em Bash (Bourne Again Shell), essencial para automação, administração de sistemas Linux e produtividade no terminal.

Aqui estão registradas anotações, scripts, exemplos práticos, conceitos fundamentais e avançados, além de automações reais utilizadas no dia a dia.

A estrutura foi organizada para acompanhar a evolução natural no uso do terminal:
do básico → comandos → manipulação de texto → scripts → automação → ferramentas avançadas.

---

## 📚 Objetivo da Trilha de Bash
- Dominar o terminal Linux
- Automatizar tarefas repetitivas
- Criar scripts úteis para uso real
- Melhorar produtividade no sistema
- Entender funcionamento do sistema via CLI

---

## 📂 Estrutura Completa do Conteúdo
```text
bash/
├── 00_introducao/
│   ├── aula_01_o_que_e_shell.md
│   ├── aula_02_bash_vs_sh_zsh.md
│   ├── aula_03_primeiros_comandos.md
│   └── aula_04_ajuda_man_help.md
|
├── 01_comandos_basicos/
│   ├── aula_01_navegacao_ls_cd_pwd.md
│   ├── aula_02_manipulacao_arquivos.md
│   ├── aula_03_copiar_mover_remover.md
│   ├── aula_04_permissoes_chmod_chown.md
│   ├── aula_05_visualizacao_cat_less_head.md
│   └── aula_06_redirecionamento_pipe.md
|
├── 02_texto_e_filtros/
│   ├── aula_01_grep.md
│   ├── aula_02_sed.md
│   ├── aula_03_awk.md
│   ├── aula_04_sort_uniq_cut.md
│   └── aula_05_wc_tr.md
|
├── 03_variaveis_e_ambiente/
│   ├── aula_01_variaveis.md
│   ├── aula_02_variaveis_ambiente.md
│   ├── aula_03_export_path.md
│   └── aula_04_arquivos_bashrc_profile.md
|
├── 04_controle_de_fluxo/
│   ├── aula_01_if_else.md
│   ├── aula_02_case.md
│   ├── aula_03_loops_for_while.md
│   ├── aula_04_break_continue.md
│   └── aula_05_test_conditions.md
|
├── 05_scripts_bash/
│   ├── aula_01_primeiro_script.md
│   ├── aula_02_shebang.md
│   ├── aula_03_argumentos.md
│   ├── aula_04_funcoes.md
│   ├── aula_05_input_usuario.md
│   └── aula_06_debug_set_x.md
|
├── 06_manipulacao_de_arquivos/
│   ├── aula_01_find.md
│   ├── aula_02_xargs.md
│   ├── aula_03_tar_zip.md
│   └── aula_04_backup_scripts.md
|
├── 07_processos_e_sistema/
│   ├── aula_01_ps_top_htop.md
│   ├── aula_02_kill_jobs_bg_fg.md
│   ├── aula_03_cron_agendamentos.md
│   └── aula_04_monitoramento_logs.md
|
├── 08_redes_e_api/
│   ├── aula_01_curl.md
│   ├── aula_02_wget.md
│   ├── aula_03_testes_http.md
│   └── aula_04_consumindo_api.md
|
├── 09_automacao_real/
│   ├── projeto_01_backup_automatico/
│   ├── projeto_02_monitoramento_sistema/
│   ├── projeto_03_organizador_arquivos/
│   └── projeto_04_deploy_script/
|
├── 10_customizacao_terminal/
│   ├── aula_01_alias.md
│   ├── aula_02_prompt_ps1.md
│   ├── aula_03_bashrc_custom.md
│   └── aula_04_plugins_e_temas.md
|
└── README.md
```

---

## Explicação dos Módulos

### 00 — Introdução
- Entendendo o terminal
- O que é shell
- Diferença entre bash, sh e zsh
- Primeiros comandos
- Como usar man e help

### 01 — Comandos Básicos
- Base do Linux na prática
- Navegação no sistema
- Manipulação de arquivos
- Permissões
- Visualização de conteúdo
- Pipes e redirecionamentos

### 02 — Texto e Filtros
- O verdadeiro poder do Bash
- grep → busca
- sed → edição
- awk → processamento
- sort / uniq → organização
- wc / tr → transformação

### 03 — Variáveis e Ambiente
- Configurando seu sistema
- Variáveis locais
- Variáveis de ambiente
- PATH
- .bashrc e .profile

### 04 — Controle de Fluxo
- Lógica dentro do Bash
- if / else
- case
- loops
- condições

### 05 — Scripts Bash
- Criando automações
- Scripts executáveis
- Argumentos
- Funções
- Entrada de dados
- Debug

### 06 — Manipulação de Arquivos
- Automação pesada
- find
- xargs
- compactação
- scripts de backup

### 07 — Processos e Sistema
- Controle do sistema
- processos
- jobs
- cron
- logs

### 08 — Redes e API
- Integração com o mundo externo
- curl
- wget
- requisições HTTP
- APIs

### 09 — Automação Real
- Projetos práticos
- Backup automático
- Monitoramento de CPU/RAM
- Organização de arquivos
- Script de deploy

### 10 — Customização do Terminal
- Seu ambiente, sua ferramenta
- alias
- prompt personalizado
- bashrc tunado
- produtividade

## 🎯 Objetivos Finais do Estudo de Bash
- Dominar completamente o terminal Linux
- Criar scripts reais e úteis
- Automatizar tarefas do dia a dia
- Trabalhar com servidores Linux
- Integrar Bash com projetos Python/Flask
- Pensar como um usuário avançado de Linux

### Nota

> Este material é autoral, criado para estudo próprio e evolução profissional, Conteúdo atualizado constantemente conforme avanço nos estudos e projetos.
