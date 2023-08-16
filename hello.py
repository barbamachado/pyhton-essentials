#!/usr/bin/env python

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
# __*__ => dunder
__version__ = "0.8.1" 
__author_ = "lucas machado"
__license__ = "unlicensed"

# indentifica a variável name e executa caso "main" (feio)
# if __name__ == "__main__": 

# seta a linguagem atual
current-language = "en_US"

# armazena texto na var
msg = "hello world"

# condicional linguagem
if current-language == "pt_BR":
    msg = "olá mundo"


# imprime a var
print(msg)







