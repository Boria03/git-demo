#!/usr/bin/env python
import sys

sys.stdin = open("duom_full.txt","r")
sys.stdout = open("mapout.txt","w")


for line in sys.stdin:
    line = line.strip()
    line = line[2:len(line)-2]
    susstring = line.split('}}{{')
    for stopas in susstring:
      grupe = None
      svoris = None
      parstrings = stopas.split('}{')

      for parstring in parstrings: 
        (vardas, reiksme) = parstring.split('=')
        if(reiksme != ''):
          if(vardas == 'svoris'):
            svoris = float(reiksme)
          if(vardas == 'svorio grupe'):
            grupe = str(reiksme)
          if(vardas == 'siuntu skaicius'):
            siuntu_skaicius = int(reiksme)

      if(grupe != None and svoris != None):
        print('%s\t%s\t%s' % (grupe, svoris, siuntu_skaicius))