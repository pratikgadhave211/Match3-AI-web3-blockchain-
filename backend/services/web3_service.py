from __future__ import annotations

from typing import Any

from web3 import Web3

from backend.config import CONTRACT_ABI, CONTRACT_ADDRESS, EXPECTED_CHAIN_ID, NETWORK_NAME, RPC_URL
from backend.utils.helpers import clean_user_record


def _normalize_chain_user(raw_user: Any) -> dict[str, Any]:
    # tuple from Solidity: (wallet, name, interests, goals, registeredAt, exists)
    if isinstance(raw_user, (list, tuple)):
        user = {
            "wallet": raw_user[0] if len(raw_user) > 0 else "",
            "name": raw_user[1] if len(raw_user) > 1 else "",
            "interests": raw_user[2] if len(raw_user) > 2 else [],
            "goals": raw_user[3] if len(raw_user) > 3 else [],
        }
        return clean_user_record(user)

    if isinstance(raw_user, dict):
        return clean_user_record(raw_user)

    return clean_user_record({})


def fetch_all_users_from_chain() -> list[dict[str, Any]]:
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not web3.is_connected():
        raise RuntimeError("Unable to connect to RPC URL")

    chain_id = int(web3.eth.chain_id)
    if chain_id != EXPECTED_CHAIN_ID:
        raise RuntimeError(f"Wrong chain id {chain_id}. Expected {NETWORK_NAME} ({EXPECTED_CHAIN_ID})")

    contract = web3.eth.contract(
        address=Web3.to_checksum_address(CONTRACT_ADDRESS),
        abi=CONTRACT_ABI,
    )

    raw_users = contract.functions.fetchAll().call()
    users = [_normalize_chain_user(item) for item in raw_users]

    # Keep only users with at least a name.
    return [user for user in users if user.get("name") and user.get("name") != "Unknown"]
