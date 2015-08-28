import csv
import decimal
import sys

decimal_keys = ('Expected Bitcoin', 'Settled Amount',)

totals = { k: decimal.Decimal(0) for k in  decimal_keys}
lines = []
with open(sys.argv[1]) as fh:
    b = csv.DictReader(fh)
    for a in b:
        if a['Status'] == 'settled':
            for key in decimal_keys:
                if a[key]:
                    a[key] = decimal.Decimal(a[key])
                    totals[key] += a[key]
                else:
                    a[key] = decimal.Decimal(0)



            lines.append("{Creation Date} | {Expected Bitcoin:10f} btc | {Quoted Amount:10s} {Quoted Currency:3s} | {Customer Reference}\n".format(**a))


with open("donations/btc.txt", 'w') as fh:
    fh.writelines(lines)
    output = "Total {Expected Bitcoin:12f} btc ~ ".format(**totals)
    print(output)
