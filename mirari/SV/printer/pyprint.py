# -*- coding: latin1 -*-
#!usr/bin/env/ python
from escpos import printer
import sys, json
Epson = printer.Usb(0x04b8,0x0e15)
for data in sys.stdin:
    ticketLine = json.loads(data)
    for t in ticketLine:
        try:
            if t[0] == 'image':
                Epson.image(t[1])
            if t[0] == 'qr':
                Epson.qr(t[1], size=8)
            if t[0] == 'text':
                Epson.text(t[1].encode("latin1", "surrogateescape").decode("latin1"))
            if t[0] == 'set':
                Epson.set(t[1][0],t[1][1],t[1][2],t[1][3],t[1][4])
            if t[0] == 'cut':
                Epson.cut()
        except:
            pass