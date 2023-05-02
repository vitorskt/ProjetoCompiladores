vogais = "aeiou"
consoantes = "bcdfglmnprstvxz"
caracteres_validos = "123456789 "


def is_valid_token(token, posicao):
    """
    Validates all tokens (letters that make up the word)
    :param token: letter
    :return: Boolean value (True if token is valid)
    """

    if posicao == 0 and token in "xz":
        print("Palavras iniciadas com as consoantes X ou Z são palavras reservadas pelo sistema.")
        return False

    if posicao == 0 and token not in consoantes:
        return False

    if token not in vogais and token not in consoantes and token not in caracteres_validos:
        return False

    return True


def lexer(cadeia):
    print(f"cadeia inicial: {cadeia}")
    cadeia = cadeia.lower()
    if len(cadeia) > 10:
        cadeia = cadeia[:10]
        print(f"NOVA CADEIA: {cadeia}")
    for posicao, token in enumerate(cadeia):
        if not is_valid_token(token, posicao): # == False
            print(f"A cadeia é rejeitada. O token {token} não é válido.")
            return 0

        if len(cadeia) - 1 != posicao and token in caracteres_validos.strip():
            print("Cadeia Inválida 1")
            return 0

        elif len(cadeia) - 1 == posicao and token in caracteres_validos.strip():
            print("CADEIA ACEITA")
            return 0

        if not (cadeia[posicao] in consoantes and cadeia[posicao + 1] in vogais) and \
            not (cadeia[posicao] in vogais and cadeia[posicao + 1] in consoantes):

            if len(cadeia) - 1 == posicao + 1 and cadeia[posicao + 1] in caracteres_validos.strip():
                print("CADEIA ACEITA")
            else:
                print("Cadeia Inválida 2")
            return 0
    print("CADEIA ACEITA")
lexer("paralazemi dematis lll")
