import psycopg2

import commands

from bitcoin import *

source_priv = 'privatekey'

pub = privtopub(source_priv)

addr = pubtoaddr(pub)

source_addr = addr

dest = 'publickey'

#get utxo
utxos = unspent(source_addr)

print 'history : ' + str(h)

#history_format = [{'output': u'd2949b5d8c62db9deeb06046273cbc1f77c3:1', 'block_height': 442236, 'value': 100000, 'address': u'publickey'}]

#get value of utxos
total_value = 0

for tx in utxos:
	total_value += access(tx, 'value')

print 'total : ' + str(total_value)


#set the fee here in Satoshis 100,000,000 satoshi is 1 bitcoin
fee = 34000

total_value -= fee


print 'total minus fee : ' + str(total_value)

outs = [{'value': total_value, 'address': dest}]

#outs = [{'value': total_value, 'address': addr}, {'value': send_value, 'address': dest}]

print 'outs : ' + str(outs)

#make txn
txn = mktx(utxos,outs)


txn = sign(txn,0,source_priv)


print txn