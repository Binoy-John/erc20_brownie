from operator import index
from brownie import network, accounts, config

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["ganache-local", "development"]
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]


def get_account(id=None, index=None):
    account = network.show_active()
    if index:
        return accounts[index]
    if id:
        return accounts.load[id]
    if account in LOCAL_BLOCKCHAIN_ENVIRONMENT or account in FORKED_LOCAL_ENVIRONMENT:
        print("The active network is found in : ", account)
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
