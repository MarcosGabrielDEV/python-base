#!/usr/bin/env python3


"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente O
programa exibe a msg correspondente.

Como usar: 

Tenha a variavel LANG devidamente configurada ex:
   export LANG=PT_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__="0.0.1"
__author__="Marcos Gabriel"
__license__="Unlicense"

#Dunder __

import os

current_language = os.getenv("LANG","en_US")[:5]

msg = "Hello,world"
if current_language == "pt_BR":
    msg = "Olá,mundo"
elif current_language=="it_IT":
    msg="ciao"

elif current_language=="es_SP"
    msg="hola"
else:
    msg="hi"
 

print(msg) # built in
 
