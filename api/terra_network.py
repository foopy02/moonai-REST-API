import asyncio
from msilib.schema import Error
from terra_sdk.client.lcd.api.tx import CreateTxOptions
from terra_sdk.client.lcd import AsyncLCDClient, LCDClient
from terra_sdk.key.mnemonic import MnemonicKey
from terra_sdk.core import Coins, Coin
from terra_sdk.core.bank import MsgSend
from terra_sdk.core.market import MsgSwap
import requests

class TerraNetwork:
    denominator = 1000000
    #TESTNET
    #TODO: Change to Mainnet link
    terra = LCDClient("https://bombay-lcd.terra.dev", "bombay-12")

    def __init__(self, ):
        pass

    def create_wallet(self):
        mk = MnemonicKey()
        return (mk.acc_address, mk.mnemonic)
    
    def check_balance(self, address):
        return self.terra.bank.balance(address)
    
    def _estimate_gas_fee(self, token):
        fees = requests.get(
                "https://fcd.terra.dev/v1/txs/gas_prices"
                ).json()
        try:
            fee = str(float(fees[token]) ) + token
        except:
            raise KeyError(f"There is no {token} in list.")
        return fee
    

    def send(self, mnemonic, from_address, to_address, memo, amount, denom):
        wallet = self.terra.wallet(mnemonic)
        coin = Coin(denom, int(amount*self.denominator)).to_data()
        coins = Coins.from_data([coin])
        tx = wallet.create_and_sign_tx(
            CreateTxOptions(
                msgs=[MsgSend(from_address, to_address, coins)],
                memo=memo,
                gas_prices=self._estimate_gas_fee(denom),
                gas_adjustment="1.5",
                fee_denoms=[denom]
            )
        )
        return self.terra.tx.broadcast(tx)
    
    def get_memo(self, tx_hash):
        info = self.terra.tx.tx_info(tx_hash)
        return info.__dict__['tx'].__dict__['body'].__dict__['memo']
    
    def get_last_transactions(self, limit, address):
        response = requests.get(f"https://fcd.terra.dev/v1/txs?offset=0&limit={limit}&account={address}").json()
        txs = response['txs']
        return txs
    
    def get_memo_from_txhash(self, txhash):
        info = self.terra.tx.tx_info(txhash)
        return info.__dict__['tx'].__dict__['body'].__dict__['memo']


def test():
    tn = TerraNetwork()
    test_mk = MnemonicKey("cruise income fiction era cook media budget farm key laundry satoshi pitch rude proof enforce toward once very engage feed discover board sand naive")
    
    mk2 = MnemonicKey("deal used situate replace truck spray brief shoe movie language another horror portion comic blind merit bargain sand mix live diamond link envelope lunar")
    mk = MnemonicKey("ask engage entry curve race equip garment shield front pulp chapter useless grass build name gesture beef evil enrich outdoor miss negative shop tent")
    tx = tn.send(mk, mk.acc_address, mk2.acc_address, "Hello this is test", 10, "uusd")
    info  = tn.terra.wallet(mk)
    print(tn.get_last_transactions(10,"terra16vkuarckk3fjfk0fnag70au4ywsgyfsr7zhvzr"))








