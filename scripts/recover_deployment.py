import json,re
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];e=(R.parents[3]/'accounts.env').read_text();k=re.search(r'^ACCOUNT_4_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',e,re.M).group(1).strip();c=create_client(chain=studionet,account=create_account(account_private_key=k));tx='0x08dcfe936ba7ec6c3cb510df613f6fa46d49f41b14bce8bffa81c32ab7520dc1';q=c.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True);l=(q.get('consensus_data',{}).get('leader_receipt')or[{}])[0];print(json.dumps({'contract':q.get('data',{}).get('contract_address')or q.get('to_address'),'deploymentTx':tx,'consensus':q.get('result_name'),'execution':l.get('execution_result')},default=str),flush=True)
