from celery import shared_task
import requests
import json
from .models import *
import time

@shared_task
def check_wallets():
    bonuses = (1,5)
    users = CustomUser.objects.all()
    for user in users:
        print(f"Checking {user.username}")
        try:
            wallet = Wallet.objects.get(user=user)
            wallet_address = wallet.address
        except Wallet.DoesNotExist:
            print(f"No wallet of {user.username}")
            continue

        response = requests.get(f"https://fcd.terra.dev/v1/txs?offset=0&limit=100&account={wallet_address}")

        try:
            responseJson = json.loads(response.content)
            txs = responseJson['txs']
        except Exception as e:
            print(e, response.content)

        balance_of_terra = 0
        for i in txs:
            value = i['tx']['value']['msg'][0]['value']
            amount = value['amount'][0]
            denom = amount['denom']
            amount_of_coin = int(amount['amount']) / 1000000
            addressTo = value['to_address']

            if wallet_address == addressTo and denom == "uusd":
                balance_of_terra += amount_of_coin
        user_balance = user.balance_for_withdraw
        apy = user.apy
        last_updated_time = int(user.balance_last_updated_time * 1000)
        diff = time.time()*1000 - last_updated_time
        calculated_balance = calculate_balance_after_n_ms(
            balance=user_balance,
            apy=apy, 
            ms=int(diff)
        )

        if balance_of_terra != 0 and user_balance != balance_of_terra:
            last_updated_time = int(user.balance_last_updated_time * 1000)
            diff = time.time()*1000 - last_updated_time
            calculated_balance = calculate_balance_after_n_ms(
                balance=user_balance,
                apy=apy, 
                ms=int(diff)
            )
            if user.usertype == "TESTER" and user_balance in bonuses:
                balance_diff = abs(balance_of_terra) 
                user.balance_for_withdraw = calculated_balance + balance_diff
            elif user_balance not in bonuses:
                balance_diff = abs(balance_of_terra - user_balance) 
                user.balance_for_withdraw = calculated_balance + balance_diff
            user.balance_last_updated_time = time.time()
            user.save()
            print(f"Balance: {user.balance_for_withdraw} of {user.username}")
        time.sleep(0.5)


def calculate_balance_after_n_ms(balance, apy, ms):
    N = 365 * 24 * 60 * 60 * 1000
    x = N * (pow(apy / 100 + 1, 1 / N) - 1)
    balance = balance * pow(1 + x / N, ms)
    return balance
