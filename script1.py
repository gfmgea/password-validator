def validar_senha(senha):
    """
    Função para validar a senha.
    Temos os dicionários contendo os caracteres (maiusculos, minusculos, numeros e especiais)
    E depois temos uma sequencia de ifs condicionando se atende aos requisitos ou não
    Como entrada temos o input do usuário e como retorno False ou True
    """

    #Dicionários contendo os caracteres   
    caracteres_maiusculos = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    caracteres_minusculos = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    numeros = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    caracteres_especiais = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?'}
    
    #Verifica se a senha tem pelo menos oito caracteres
    if len(senha) < 8:
        return False, "Faltando caracteres (pelo menos 8 caracteres necessários). Coloque pelo menos 8 caracteres, por favor!"
    
    #Verifica se a senha contém pelo menos uma letra maiúscula
    if not any(char in caracteres_maiusculos for char in senha):
        return False, "Faltando letra maiúscula. Coloque uma maiúscula, por favor!"
    
    #Verifica se a senha contém pelo menos uma letra minúscula
    if not any(char in caracteres_minusculos for char in senha):
        return False, "Faltando letra minúscula. Coloque uma minúscula, por favor!"
    
    #Verifica se a senha contém pelo menos um número
    if not any(char in numeros for char in senha):
        return False, "Faltando número. Coloque um número, por favor!"
    
    #Verifica se a senha contém pelo menos um caractere especial
    if not any(char in caracteres_especiais for char in senha):
        return False, "Faltando caractere especial. Coloque um, por favor!"
    
    #Se passou por todos acima, a senha é forte
    return True, "Senha forte! Pode usá-la!"

"""
Main
Onde temos o input para receber a senha do usuário e o print da mensagem caso ela atenda aos requisitos do código ou não
"""
print("As senhas que você digitar são apenas para verificar se ela é forte o suficiente ou não, fique tranquilo que não armazenamos elas em nenhum lugar! :)")
senha = input("Digite sua senha (não compartilhe com ninguém, ok?): ")
validade, mensagem = validar_senha(senha)
if validade:
    print(mensagem)
else:
    print(mensagem)

#print(validar_senha.__doc__)