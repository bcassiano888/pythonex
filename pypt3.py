# -*- coding: utf-8 -*-
while True:
  linha = input().split()
  if linha[0] == '0' and linha[1] == '0':
      break
  a,b = linha
  s = int(a)+int(b)
  s = str(s).split("0")
  ns = "".join(s)
  print(ns)

