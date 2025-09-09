# -*- coding: utf-8 -*-
while True:
    try:
        t = input()
        tl = list(t)
        x = 1
        z = 3
        txt = []
        for i in range(len(tl)):
        
          if(tl[i] == "_"):
            if x == 1:
              txt.append("<i>")
              x = 2
            elif x == 2:
              txt.append("</i>")
              x = 1
          elif (tl[i] == "*"):
            if z == 3:
              txt.append("<b>")
              z = 4
            elif z == 4:
              txt.append("</b>")
              z = 3
          else:
              txt.append(tl[i]) 

        t = "".join(txt)
        print(t)
    except EOFError:
        break
