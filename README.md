# Description
Omni Layer is a bitcoin fork that enables smart contact on the bitcoin blockchain. Tether(USDT) is one kind of digit assets using Omni Layer whose property id is 31.

To parse omnicore raw data using Json-RPC, you should setup a [Omnicore](https://github.com/OmniLayer/omnicore) fullnode and start the json-rpc service.

Sample code for parsing transactions from block a to b is:

```python
from parser import USDT_Parser

OMNI_URL = 'http://localhost:8332' # json-rpc usl
OMNI_RPC_USERNAME = 'xxx' # json-rpc authentication username
OMNI_RPC_PW = 'xxx' # json-rpc authentication password

a = 438072
b = 438082

parser = USDT_Parser(OMNI_URL, OMNI_RPC_USERNAME, OMNI_RPC_PW)
for txs in parser.get_block(a, b):
    print(txs)
```
