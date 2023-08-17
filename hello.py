#!/usr/bin/env python3

"""hello world multi línguas

escolhe linguagem dependendo da linguagem do ambiente

como usar:

    - configure devidamente a variável LANG, ex:
        export LANG=pt_BR
    
    - execução:
        python hello.py
        ou
        ./hello.py
"""
# __*__ => variáveis under
__version__ = "0.8.1" 
__author_ = "lucas machado"
__license__ = "unlicensed"

# importar pacote
import os

# indentifica a variável name e executa caso "main" (feio)
# if __name__ == "__main__": 

# seta a linguagem atual
current_language = os.getenv("LANG", "pt_BR")[:5]

# armazena texto na var
msg = "hello world"

# condicional linguagem
if current_language == "pt_BR":
    msg = "olá mundo"
elif current_language == "it_IT":
    msg = "ciao, mondo"
elif current_language == "es_SP":
    msg = "hola mundo"
elif current_language == "fr_FR":
    msg = "bonjour monde"


# imprime a var
print(msg)







