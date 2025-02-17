from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from web3 import Web3
import os


INFURA_URL = os.getenv("INFURA_API_KEY")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY") 

@api_view(['GET'])
def sample_api(request):
    return Response({"message" : "Hello from Django API!"})


web3 = Web3(Web3.HTTPProvider(INFURA_URL)) ## In here we connect to the Ethereum network using Web3.py library.

def get_transactions(request):
    transactions = None  
    address = request.GET.get("address", "").strip() 
    if address:  
        transactions = fetch_transactions(address)
    return render(request, "transaction.html", {"transactions": transactions, "address": address})




def fetch_transactions(address):
    etherscan_api_url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(etherscan_api_url)
    data = response.json()

    #if the API response isn't in the right format.
    if "result" not in data or not isinstance(data["result"], list):
        print("API -> false format: ", data) #error catching
        return[]
    
    tx_list = []
    for tx in data["result"][:10]:  
        tx_list.append({
            "hash": tx.get("hash", "N/A"),
            "from": tx.get("from", "N/A"),
            "to": tx.get("to", "N/A"),
            "value": str(int(tx.get("value", 0)) / 10**18) + " ETH", 
        })
    return tx_list