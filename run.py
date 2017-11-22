from multiprocessing import Pool, TimeoutError
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import time

def chunk(l, n, i):
    return l[i*n:(i+1) * n]

rpc_user="bitcoin"
rpc_password="local321"
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))

lines = [line.rstrip('\n') for line in open('addresses')]

def f(line):
  txids = rpc_connection.getaddresstxids(line);
  for idd in txids:
    rpc_connection.getrawtransaction(idd)
  return len(txids)

i = 0
while True:
  mychunk = chunk(lines, 100, i)
  i+1

  start = time.time()
  pool = Pool(processes=40)              # start 40 worker processes
  all = sum(pool.map(f, mychunk))

  end = time.time()
  sec = (end - start)
  persec = float(all)/sec
  print(str(persec) + " txs/sec")

