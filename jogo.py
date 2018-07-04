# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:51:14 2018

CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
PROGRAMAÇÃO FUNCIONAL OO - PYTHON
Projeto Integrador - Atividade 08 - DESAFIO
@author: Nelson de Campos Nolasco
"""

from crianca import Crianca
from crianca import Pegador

crianca1 = Crianca('Nelson', 8)
crianca2 = Crianca('Toninho', 9)
crianca3 = Pegador('Haroldinho', 10)

# Qual o nome e idade de vocês?
print('Meu nome é ' + crianca1.nome + ' e eu tenho ' + str(crianca1.idade) + ' anos.')
print('Meu nome é ' + crianca2.nome + ' e eu tenho ' + str(crianca2.idade) + ' anos.')
print('Meu nome é ' + crianca3.nome + ' e eu tenho ' + str(crianca3.idade) + ' anos.')

# Qual de vocês é o pegador?
print(crianca1.pegador)
print(crianca2.pegador)
print(crianca3.pegador)

## É hora do play:
crianca2.correr()
crianca3.correr()

crianca3.pegar(crianca2)
crianca2.correr()
crianca3.pegar(crianca2)
crianca1.salvar(crianca2)
crianca1.correr()
crianca1.salvar(crianca2)
crianca1.salvar(crianca2)
crianca3.salvar(crianca1)
