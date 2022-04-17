from operator import index
from urllib.parse import urlencode
import json

"walletAddressesData=%7B%27coins%27%3A+%7B%27UST%27%3A+%7B%27address%27%3A+%27terra1jp0vljxnc4h3jhp6l2mfs9vplfgdrwpjh0euyu%27%2C+%27addressAdditionalData%27%3A+%27123456%27%7D%7D%7D"
#custom index.js
"walletAddressesData=%7B%22coins%22%3A%7B%22UST%22%3A%7B%22address%22%3A%22terra1fu8mnxz7mauahlujcf4au97k5ghrcnyfh54wvz%22%2C%22addressAdditionalData%22%3A%22123456%22%7D%7D%7D"
class Transak():
    # https://global.transak.com/?apiKey=db70aca0-ca84-4344-8dcc-036f470414fc&fiatCurrency=KZT&fiatAmount=15000&walletAddressesData=%7B%22coins%22%3A%7B%22UST%22%3A%7B%22address%22%3A%22terra1jp0vljxnc4h3jhp6l2mfs9vplfgdrwpjh0euyu%22%2C%22addressAdditionalData%22%3A%22USERNAME%22%7D%7D%7D&cryptoCurrencyList=UST,LUNA&defaultCryptoCurrency=UST&networks=terra
    
    def generate_url(self, username, amount_in_kzt, wallet_address, def_crypto="UST", is_visible=True, data=None):
        link = f"https://global.transak.com/?apiKey=db70aca0-ca84-4344-8dcc-036f470414fc&fiatCurrency=KZT&fiatAmount={amount_in_kzt}&walletAddressesData=%7B%22coins%22%3A%7B%22UST%22%3A%7B%22address%22%3A%22{wallet_address}%22%2C%22addressAdditionalData%22%3A%22{username}%22%7D%7D%7D&cryptoCurrencyList=UST,LUNA&defaultCryptoCurrency={def_crypto}&networks=terra"
        
        if not is_visible:
            link += "&disableWalletAddressForm=true"

        if data:
            link += f"userData=%7B%22first_name%22%3A%22Satoshi%22%2C%22last_name%22%3A%22Nakamoto%22%2C%22email%22%3A%22somegoodmans@gmail.com%22%2C%22mobileNumber%22%3A%22%2B19692154942%22%2C%22dob%22%3A%221994-11-26%22%2C%22address%22%3A%7B%22addressLine1%22%3A%22170%20Pine%20St%22%2C%22addressLine2%22%3A%22San%20Francisco%22%2C%22city%22%3A%22San%20Francisco%22%2C%22state%22%3A%22CA%22%2C%22postCode%22%3A%2294111%22%2C%22countryCode%22%3A%22US%22%7D%7D"
        
        return link

t = Transak()
print(t.generate_url("f0opy", 20000, "terra1jp0vljxnc4h3jhp6l2mfs9vplfgdrwpjh0euyu", is_visible=False))