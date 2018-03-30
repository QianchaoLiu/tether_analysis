# Description
Omni Layer is a bitcoin fork that enables smart contact on the bitcoin blockchain. Tether(USDT) is only kind of digit asset using Omni Layer whose property id is 31.

To parse omnicore raw data using Json-RPC, you should setup a [Omnicore](https://github.com/OmniLayer/omnicore) fullnode and start the json-rpc service.

Sample code for parsing transactions from block a to b is:

```python
parser = USDT_Parser(OMNI_URL, OMNI_RPC_USERNAME, OMNI_RPC_PW)
for txs in parser.get_block(a, b):
    print(txs)
```
