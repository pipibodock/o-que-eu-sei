# Operados lógicos

Um dos mais antigos operadores lógicos é o chamado dado booleano. Isso implica
que trabalharemos com Verdadeiro ou Falso,0 e 1, Sim ou Não, Aceso ou Apagado. Podemos
então, trabalhar e fazer operações com valores booleanos para entrada e saída.

---

## Tabela da Verdade AND

Na tabela and, teremos um True somente se os dois valores forem True. 

- Ex:
    
        False and False = False
        False and True = False
        True and False = False
        True and True = True

    > Podemos comparar o AND a um sinal de multiplicação.

## Tabela da Verdade OR

Na tabela OR, teremos um True somente se um dos operadores for True.

- Ex:

        False or False = False
        False or True = True
        True or False = True
        True or True = True

    > podemos comparar o OR a um sinal de adição.

## Tabela da Verdade NOT

O operador NOT é o único que recebe apenas um operador, e servirá para inverter
os nossos valores.

- Ex:

        Not True = False
        Not False = True

---

## Tabela da Verdade XOR

O operador XOR ou OR-Exclusivo, é um operador que tem como saída um True, somente
se os operadores forem **Diferentes**

- Ex:

        False xor False = False
        False xor True = True
        True xor False = True
        True xor True = False

## Tabela da Verdade NAND

O operador NAND é o inverso do AND, isso significa que ele terá como saída um
True se pelo menos um dos operadores for False.

- Ex:

        False nand False = True
        False nand True = True
        True nand False = True
        True nand True = False

## Tabela da verdade NOR

O operador NOR é o inverso do OR, isso significa que só teremos um True se os
dois operadores for False.

- Ex:

        False nor False = True
        False nor True = False
        True nor False = False
        True nor True = False

## Tabela da verdade XNOR

O operador 'NAO-OU-EXCLUSIVO' ou XNOR terá como saída um True somente se os dois
operadores forem iguais.

- Ex:

        False xnor False = True
        False xnor True = False
        True xnor False = False
        True xnor True = True
