from __future__ import annotations

import os
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE_PATH = DATA_DIR / "users.json"

RPC_URL = os.getenv("RPC_URL", "https://sepolia.infura.io/v3/e0147d99ceeb41e1835d2e09f4d4ce27")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "0x1D67D3511BEDd04208D419fcf559CC5f5975edEf")
EXPECTED_CHAIN_ID = int(os.getenv("EXPECTED_CHAIN_ID", "11155111"))
NETWORK_NAME = os.getenv("NETWORK_NAME", "Sepolia Test Network")

CONTRACT_ABI: list[dict[str, Any]] = [
    {
        "inputs": [
            {"internalType": "string", "name": "_name", "type": "string"},
            {"internalType": "string[]", "name": "_interests", "type": "string[]"},
            {"internalType": "string[]", "name": "_goals", "type": "string[]"},
        ],
        "name": "register",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "wallet",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "name",
                "type": "string",
            },
            {
                "indexed": False,
                "internalType": "string[]",
                "name": "interests",
                "type": "string[]",
            },
            {
                "indexed": False,
                "internalType": "string[]",
                "name": "goals",
                "type": "string[]",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "registeredAt",
                "type": "uint256",
            },
        ],
        "name": "UserRegistered",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "address", "name": "_user", "type": "address"}],
        "name": "fetch",
        "outputs": [
            {"internalType": "address", "name": "wallet", "type": "address"},
            {"internalType": "string", "name": "name", "type": "string"},
            {"internalType": "string[]", "name": "interests", "type": "string[]"},
            {"internalType": "string[]", "name": "goals", "type": "string[]"},
            {"internalType": "uint256", "name": "registeredAt", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "fetchAll",
        "outputs": [
            {
                "components": [
                    {"internalType": "address", "name": "wallet", "type": "address"},
                    {"internalType": "string", "name": "name", "type": "string"},
                    {"internalType": "string[]", "name": "interests", "type": "string[]"},
                    {"internalType": "string[]", "name": "goals", "type": "string[]"},
                    {
                        "internalType": "uint256",
                        "name": "registeredAt",
                        "type": "uint256",
                    },
                    {"internalType": "bool", "name": "exists", "type": "bool"},
                ],
                "internalType": "struct EventUsers.User[]",
                "name": "",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
]


def get_runtime_settings() -> dict[str, Any]:
    return {
        "network": NETWORK_NAME,
        "rpc_url": RPC_URL,
        "contract": CONTRACT_ADDRESS,
        "chain_id": EXPECTED_CHAIN_ID,
        "data_file": str(DATA_FILE_PATH),
    }
