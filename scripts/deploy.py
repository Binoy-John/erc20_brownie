from brownie import OurToken, network, config, Contract
from eth_utils import to_wei
from scripts.helpful_scripts import get_account
from web3 import Web3


def deploy_token():
    initial_supply = to_wei(69, "ether")
    account = get_account()
    token = OurToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Token Deployed!")
    return token


def main():
    deploy_token()
