import numpy as np
from lexico_utils import *

def le_arquivo(caminho):
    # Lê o arquivo e garante que será fechado automaticamente
    with open(caminho, "r") as arquivo:
        return processar_arquivo(arquivo)

def processar_arquivo(arquivo):
    # Dicionário para armazenar os tokens e lexemas
    tokens_lexemas = {
        1: "while",
        2: "var",
        3: "to",
        4: "then",
        5: "string",
        6: "real",
        7: "read",
        8: "program",
        9: "procedure",
        10: "print",
        11: "nreal",
        12: "nint",
        13: "literal",
        14: "integer",
        15: "if",
        16: "ident",
        17: "for",
        18: "end",
        19: "else",
        20: "do",
        21: "const",
        22: "begin",
        23: "vstring",
        24: ">=",
        25: ">",
        26: "=",
        27: "<>",
        28: "<=",
        29: "<",
        30: "+",
        31: ";",
        32: ":=",
        33: ":",
        34: "/",
        35: ".",
        36: ",",
        37: "*",
        38: ")",
        39: "(",
        40: "{",
        41: "}",
        42: "-"
    }
    
    lexemas_array = list(tokens_lexemas.values())

    tokens = []
    lexemas = []
    linha_atual = []
    in_comment = False

    for linha_numero, linha in enumerate(arquivo, start=1):
        lexema = ''
        i = 0

        while i < len(linha):
            if in_comment:
                # Dentro do comentário de bloco, ingora os caracteres até encontrar a sequencia '*/'
                if linha[i:i+2] == '*/':
                    in_comment = False
                    i += 2
                else:
                    i += 1
                continue

            if linha[i:i+2] == '//':
                # Comentário de linha, ignora o restante da linha
                break

            if linha[i:i+2] == '/*':
                # Inicio do comentário de bloco
                in_comment = True
                i += 2
                continue

            if linha[i] in lexemas_array:
                lexema = linha[i]
            elif linha[i] != ' ':
                lexema = lexema + linha[i]
            else:
                lexema = ''

            if lexema in lexemas_array:
                # Verifica se o próximo caractere forma um operador composto. Casos do tipo <> :=
                if i + 1 < len(linha) and lexema + linha[i + 1] in lexemas_array:
                    lexema += linha[i + 1]
                    token = lexemas_array.index(lexema) + 1
                    i += 2
                    adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                    lexema = ''
                    continue

                token = lexemas_array.index(lexema) + 1
                adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                lexema = ''
            else:
                # Verifica se é uma string
                if verificar_string(lexema):
                    validar_string(linha_numero, lexema)
                    token = lexemas_array.index('vstring') + 1
                # Verifica se é um número
                elif verificar_numero_inteiro(lexema):
                    while i + 1 < len(linha) and verificar_numero_inteiro(linha[i + 1]):
                        lexema += linha[i + 1]
                        i += 1
                    # Verifica se é real
                    if linha[i + 1] == '.':
                        lexema += linha[i + 1]
                        i += 1
                        while i + 1 < len(linha) and verificar_numero_inteiro(linha[i + 1]):
                            lexema += linha[i + 1]
                            i += 1
                        if verificar_numero_real(lexema):
                            validar_numero_real(linha_numero, lexema)
                            token = lexemas_array.index('nreal') + 1
                    else:          
                        validar_numero_inteiro(linha_numero, lexema)
                        token = lexemas_array.index('nint') + 1
                # Verifica se é um literal
                elif lexema == '"':
                    while i + 1 < len(linha):
                        lexema += linha[i + 1]
                        i += 1
                        if linha[i] == '"' and not lexema == '"':
                            break
                    validar_literal(linha_numero, lexema)
                    token = lexemas_array.index('literal') + 1
                else:
                    token = ''

                if token != '':
                    adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha_numero, linha_atual)
                    lexema = ''

            i += 1

    exibir_tokens_e_lexemas(tokens, lexemas, linha_atual) # Apenas para entendimento, não é necessário para o funcionamento
    tokens = np.array(tokens)
    return tokens

def adicionar_token_e_lexema(tokens, lexemas, token, lexema, linha, linha_atual):
    tokens.append(token)
    lexemas.append(lexema)
    linha_atual.append(linha)

def exibir_tokens_e_lexemas(tokens, lexemas, linha_atual):
    for token, lexema, linha in zip(tokens, lexemas, linha_atual):
        print(f'Token: {token} - Lexema: {lexema} - Linha: {linha}')
    print(tokens) # [array de tokens] Apenas para entendimento, não é necessário para o funcionamento

