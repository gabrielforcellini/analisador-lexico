# lexico_utils.py
import re

# Funções para verificar os erros léxicos
def validar_literal(linha_numero, lexema):
    if not lexema.startswith('"') or not lexema.endswith('"'):
        print(f"Erro léxico: Literal mal formatado na linha {linha_numero}.")

def validar_string(linha_numero, lexema):
    if not (lexema.startswith('"') and lexema.endswith('"')) or len(lexema) > 258:
        print(f"Erro léxico: String mal formatada na linha {linha_numero}.")

def validar_numero_inteiro(linha_numero, lexema):
    try:
        num = int(lexema)
        if num < 0 or num > 500000:
            print(f"Erro léxico: Número inteiro fora do intervalo na linha {linha_numero}.")
    except ValueError:
        print(f"Erro léxico: Número inteiro mal formatado na linha {linha_numero}.")

def validar_numero_real(linha_numero, lexema):
    try:
        num = float(lexema)
        if num < 0 or num > 500000 or not lexema.count('.') == 1 or len(lexema.split('.')[1]) != 2:
            print(f"Erro léxico: Número real mal formatado ou fora do intervalo na linha {linha_numero}.")
    except ValueError:
        print(f"Erro léxico: Número real mal formatado na linha {linha_numero}.")

def validar_identificador(linha_numero, lexema):
    if len(lexema) > 20 or any(c.isdigit() for c in lexema):
        print(f"Erro léxico: Identificador mal formatado na linha {linha_numero}.")

# Funções Regex

# Função para validar se um lexema é uma string
def verificar_string(lexema):
    return re.match(r"^'.*'", lexema)

# Função para validar se um lexema é um número inteiro
def verificar_numero_inteiro(lexema):
    return re.match(r'^[-+]?\d+$', lexema)

# Função para validar se um lexema é um número real
def verificar_numero_real(lexema):
    return re.match(r'^[-+]?\d+\.\d{2}$', lexema)

# Função para validar se um lexema é um literal
def verifica_literal(string):
    return re.match(r'^"([^"]*)"$', string)


