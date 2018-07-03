from .general_functions import _fulfill_transaction, _send_transaction
from .global_vars import BDB

def _create(asset, metadata, user):
    transaction = _prepare_create_transaction(asset, metadata, user.public_key)
    signed_transaction = _fulfill_transaction(transaction, user.private_key)
    receipt = _send_transaction(signed_transaction)
    if signed_transaction == receipt:
        return receipt.get('id')

def _prepare_create_transaction(asset, metadata, key):
    prepared_creation_tx = BDB.transactions.prepare(
        operation='CREATE',
        signers=key,
        asset=asset,
        metadata=metadata,
    )
    return prepared_creation_tx
