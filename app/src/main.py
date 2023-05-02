def is_valid_token(token):
    """
    Validates all tokens (letters that make up the word)
    :param token: letter
    :return: Boolean value (True if token is valid)
    """
    valid_chars = "abcdefgilmnoprstuvxz0123456789 "
    invalid_chars = "jwkyçhq/()&%$#@!"
    if len(token) > 1:
        return False
    if token in invalid_chars:
        return False
    if token not in valid_chars:
        return False
    return True


def is_valid_word(word):
    """
    checks if the input word is valid
    :param word: word typed by the user
    :return: Boolen value (True if is a valid world)
    """
    vogais = "aeiou"
    consoantes_validas = "bcdfglmnprstvxz"

    if word[0] in "xz":
        print("Palavras iniciadas com as consoantes X ou Z são palavras reservadas pelo sistema.")
        return False
    if not word.isalnum(): # verifica se é alfanumerico (não aceita caracteres especiais) - regra 3
        return False
    if word[0].lower() in vogais: # não pode começar com vogais. regra 5
        return False
    for i in range(len(word) - 1): #sempre alternar entre consoante e vogal - regra 5.1
        if word[i].lower() in vogais and word[i + 1].lower() in vogais:
            return False
    return True


def lexer(input_string):
    print(f"cadeia inicial: {input_string}")
    if len(input_string) > 10:
        print("Cadeia com mais de 10 tokens, pegamos apenas os 10 primeiros.")
        input_string = input_string[:10]
    for token in input_string:
        # print(token)
        if not is_valid_token(token): # == False
            return f"A cadeia é rejeitada. O token {token} não é válido."
    #if not is_valid_word(word):
    #    print("QQQ")
    #    return f"A cadeia é rejeitada. A palavra {word} não é válida."
    """if words[0][0].lower() in "aeiou":
        return "A cadeia é rejeitada. A primeira palavra deve começar com uma consoante válida."
    if words[-1][-1].isdigit():
        return "A cadeia é aceita."
    else:
        return "A cadeia é rejeitada. A última palavra deve terminar com um algarismo numérico."
    """
lexer("zaralhei demais kkk")
