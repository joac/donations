import sys
import csv
import decimal

decimal_keys = ('Importe',)

total = 0
lines = []

with open(sys.argv[1]) as fh:
    b = csv.DictReader(fh)
    for a in b:
        importe = decimal.Decimal(a["Importe"].replace('.','').replace(',','.'))
        total += importe
        lines.append("{Fecha Origen} | {importe:10} | {Concepto}\n".format(importe=importe, **a))

with open("donations/wire.txt", 'a') as fh:
    fh.writelines(lines)
    print(total)
