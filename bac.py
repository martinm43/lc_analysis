# coding: utf-8
"""
short 'how drunk are you' script, easily editable drinks and hours
"""
import sys
ndrinks=int(sys.argv[1])
hours=int(sys.argv[2])
alcgrams=ndrinks*14
bw=95*1000
r=.68
bac=alcgrams/(bw*r)*100 - hours*0.015
print bac
