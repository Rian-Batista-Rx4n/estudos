# Fundamentos em Python3

## Operadores Aritmeticos

---

## Conteudo

- Como calcular e fazer somas ou juntar valores **(Adição)**
- Como remover/diminuir valores **(Subtração)**
- Como multiplicar valores **(Multiplicação)**
- Como separar/dividir valores **(Divisão)**
- Como fazer potenciação **(Potencia)**
- Pegar valores por inteiro na divisão **(Divisão por inteiros)**
- Pegar o restante da divisão **(Resto da Divisão)**

## Resumo

- `+` Adição, simbolo usado para determinar uma soma / junção em python (acrescentar)
- `-` Subtração, simbolo usado para determinar uma remoção / subtrair em python (decrementar)
- `*` Multiplicação, usado para multiplicar / repetir em python (multiplicar)
- `/` Divisão, usado para dividir / separar em python (separação)
- `**` Potencia, usado para fazer calculos como raizes (exponecial)
- `//` Divisão inteira, retorna somente um valor completo para divisão
- `%` Restante, usado para obter o valor restante de uma divisão simples

---

## Código Python

```python
valor_1 = 5
valor_2 = 3
valor_3 = 0
valor_4 = -7
valor_5 = 0.5
valor_personalizado = float(input("Digite um valor: "))

print("=-" * 15)
print(5 + 3)                # 5 + 3     = 8
print(valor_2 - valor_5)    # 3 - 0.5   = 2.5
print(5 * valor_2)          # 5 * 3     = 15
print(5 + 3 * 0)            # 5 + 3 * 0 = 5
print(valor_2 / valor_3)    # 3 / 0     = Erro
print(9 ** valor_5)         # 9 ** 0.5  = 3
print(27 ** 1/valor_2)      # 27 ** 0.3 = 3
print(5 // 3)               # 5 // 3    = 1
print(5 % 2)                # 5 % 2     = 2
print(8 * valor_personalizado)
print("=" * 30)
```

---

## Operadores Aritmetico

São simbolos/formas que construimos o código ao usar uma syntex que indica que queremos fazer algum calculo no python desde dos calculos mais simples até a re-construção de uma formula mais complexa como Bhaskara.

> [!TIP]
> Lembre-se assim como na manematica **1º** vem os calculos entre `()`, **2º** calculos com `**`, **3º** Calculos com `/` e `*`, dai então seguir com os outros, mas sempre lendo da esquerda para direita, só seguir a ordem das propriedades

### Operador: +

Além de usar o simbolo de **adicição** para adicionar valores a uma conta, tambpem usamos para juntar strings

```python
nome = "Rian"
sobrenome = "Batista"
idade = 19

print(nome + " " + sobrenome)
print(f"Daqui a 5 anos você terá, {idade + 5} anos")
print(f"idade atual: {idade}")
```

Vemos que usamos o simbolo *+* para juntar duas strings, e ao mesmo tempo usamos depois para adicionar 5 a idade sem trocar o valor orignal

---

### Operador: -

Usamos para remover valores a uma variavel.

```python
municao = 30
print(f"Você tem {municao} de munição")

municao = municao - 5
print(f"Você deu 5 tiros, agora vc tem {municao}")
```

Nesses exemplo mostramos que munição agora será atualizada para ter menos 5, *munição é igual a ela so que 5 a menos*.
Podemos usar `-=` ou `+=` e até `*=` se quisermos multiplar de uma vez

---

### Operador: *

Usado para realizar calculos de multiplicação

```python
preco = 1.25
doce = 6
print(f"Se eu comprar 6 doces restantes que custam 1.25,\n eu gastaria ao todo: R${doce * preco:.2f}")
print("-" * 30)
```

POdemos ver que alem das contagem, podemos usar para repitir algumas coisas.

---

### Operador: /

Usamos para dividir algo por alguma quantia ou partes e também para reaizar calculos de frações

```python
torta = 8
pessoas = 4

print(f"Tenho {torta} pedações de torta, e quero dividir para {pessoas} pessoas, ficaria {torta / pessoas} pedaços para cada um.")
```

> lembre-se de se atentar a possiveis divisões por 0, qualquer coisas dividida por zero pode gerar erro.

---

### Operador: **

Potencias e expoentes, vamos analisar como usar potencias para algumas coisas

```python
valor_1 = 9
valor_2 = 8
valor_3 = 3

print(f"Raiz quadrada: {valor_1 ** (1/2)}")       # 9**(1/2) =  3
print(f"Raiz Cubica: {valor_2 ** (1/3)}")         # 8**(1/3) =  2
print(f"3 elevado a {valor_3} = {3 ** valor_3}")  # 3**3     = 27
```

Vimos que podemos combinar com fração para relizar raizes, na matematica pura é isso mesmo, raizes quadras são um valor elevedo a uma fração, isso gera sua raiz

> notar que usamos *()* na hora de realizar raizes, pois queriamos o valor da fração primeiro, lembre-se sempre da regra das **ordem de prioridade**! se não gera valor errado.

---

### Operador: //

Usado para recebermos um valor exato de quantias.

```python
valor = 130.00

print(f"para pagar 130 reais, eu consigo dar {130 // 50} notas de R$50.00\ne {130 // 20} de R$20.00")
```

---

### Operador: %

Usado para descobrir o valor que restou para continuar a divisão, boa caso queira valores especificos e evitar virgular, bom para arredondamentos.

```python
valor_1 = 26
valor_2 = 97

print(valor_1 % 2)
print(valor_2 % 2)

print("Dica, você pode usar o resultado de % com 2 para ver se da 0, se sim significa que ele é par! caso contrio impar!")
```

> Você pode usar o resultado de % com 2 para ver se da 0, se sim significa que ele é par! caso contrio impar!
