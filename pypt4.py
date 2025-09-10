# -*- coding: utf-8 -*-
bolas = sum(map(int,input().split()))
renas = {
    1: "Dasher",
    2: "Dancer",
    3: "Prancer",
    4: "Vixen",
    5: "Comet",
    6: "Cupid",
    7: "Donner",
    8: "Blitzen",
    9: "Rudolph"
}
while bolas > 9:
  bolas -= 9
print(renas[bolas])

