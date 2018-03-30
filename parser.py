import requests
from requests.auth import HTTPBasicAuth
import json

USDT_PROPERTYID = 31
OMNI_URL = 'http://localhost:8332'
OMNI_RPC_USERNAME = 'xxx'
OMNI_RPC_PW = 'xxx'

class USDT_Parser(object):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        
    def __rpcRequest(self, method, params):
        """Make an RPC request to geth on port 8332."""
        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
        }
        res = requests.post(
              self.url,
              data=json.dumps(payload),
              auth=HTTPBasicAuth(self.username, self.password),
              headers={"content-type": "application/json", }).json()
        return res['result']

    def __getTx(self, txid):
        tx = self.__rpcRequest("omni_gettransaction", [txid])
        return tx if tx['propertyid'] == USDT_PROPERTYID else None
        
    def __getTxsByBlock(self, block):
        txs = self.__rpcRequest("omni_listblocktransactions", [block])
        return txs
    
    def get_block(self, start=0, end=None):
        assert end >= start
        if not end:
            end = self.__rpcRequest('omni_getinfo', [])['block']
        for block in range(start, end+1):
            txids = self.__getTxsByBlock(block)
            tx_details = []
            for txid in txids:
                tx_detail = self.__getTx(txid)
                if tx_detail:
                    tx_details.append(tx_detail)
            yield tx_details
                
        
parser = USDT_Parser(OMNI_URL, OMNI_RPC_USERNAME, OMNI_RPC_PW)
for txs in parser.get_block(438072):
    print(txs)