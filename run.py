from multiprocessing import Pool, TimeoutError
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import time



rpc_user="bitcoin"
rpc_password="local321"
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(rpc_user, rpc_password))

lines = [line.rstrip('\n') for line in open('addresses')]

def f(line):
    txids = rpc_connection.getaddresstxids(line);
    for idd in txids:
		  rpc_connection.getrawtransaction(idd)


while True:

	start = time.time()
	pool = Pool(processes=4)              # start 4 worker processes
	pool.map(f, lines)

	end = time.time()
	sec = (end - start)
	persec = float(len(lines))/sec
	print(persec)

