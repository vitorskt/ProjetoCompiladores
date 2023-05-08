vogais = "aeiou"
consoantes = "bcdfglmnprstvxz"
caracteres_validos = "123456789"
flag = False


def is_valid_token(token, posicao, tam):
    global flag

    if posicao == 0 and token in "xz":
        print("Palavras iniciadas com as consoantes X ou Z são palavras reservadas pelo sistema.")
        return False

    if posicao == 0 and token not in consoantes:
        return False

    if token not in vogais and token not in consoantes and token not in caracteres_validos:
        return False

    if tam - 1 != posicao and token in caracteres_validos.strip():
        return False

    if tam - 1 == posicao and token in caracteres_validos.strip():
        return True

    if token in consoantes and flag == False:
        flag = True
    elif token in vogais and flag == True:
        flag = False
    else:
        return False

    return True


def lexer(cadeia):
    print(f"cadeia inicial: {cadeia}")
    cadeia = cadeia.lower()
    if len(cadeia) > 10:
        cadeia = cadeia[:10]
        print(f"NOVA CADEIA: {cadeia}")

    tam = len(cadeia)

    for posicao, token in enumerate(cadeia):
        if not is_valid_token(token, posicao, tam):  # == False
            print(f"A cadeia é rejeitada. A cadeia não obedece uma de nossas regras.")
            return 0

    print("CADEIA ACEITA")


lexer("paralazeme dematis lll")