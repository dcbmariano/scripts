#!/usr/bin/python
#     Program: myIonPlugin.py
#    Function: Teste de criacao de plugins do Ion
# Description:
#      Author: Diego Mariano
#     Version: 1

  2 from ion.plugin import *

  3 class MyIonPlugin(IonPlugin):
  4     version='1.0'
  5     def launch(self):
  6         print "Testando a criacao de um plugin para torrent suite 3.0"
