from brownie import interface, accounts
from web3 import Web3

LINK_ADDRESS = "0x514910771AF9Ca656af840dff83E8264EcF986CA"

def get_contract_link_balance(holder_address):
    link_contract = interface.Link(LINK_ADDRESS)
    print(link_contract.balanceOf(holder_address))
    holder = accounts.at(holder_address, force = True)
    #holder = accounts(holder_address)
    #holder = interface.Contract(holder_address)
    balance = holder.balance()/ 10**18
    print(balance)
    #print(web3.eth.getBalance(holder_address))
    #balance = accounts.at(holder_address, force=True).balance()
    #print(f"The balance of {holder_address} is {balance} ETH")
    account = accounts[0]
    amount = 10 * 10 ** 18
    account.transfer(holder_address, amount)
    balance = holder.balance()/ 10**18
    print(balance)

BINANCE_ADDRESS = "0xF977814e90dA44bFA03b6295A0616a897441aceC"

def main():
    print("hi")
    get_contract_link_balance(BINANCE_ADDRESS)