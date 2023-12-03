import click
from web3 import Web3

GANACHE_DEFAULT_ENDPOINT_URI = "http://127.0.0.1:7545"
CONTRACT_ABI_DEFAULT_FILE_PATH = "./client/contracts/Election.abi.json"


class Client:
    def __init__(self, endpoint_uri, contract_address, contract_abi_path, wallet_address, wallet_private_key):
        self._web3 = Web3(Web3.HTTPProvider(endpoint_uri))
        self._contract = self._web3.eth.contract(
            address=contract_address,
            abi=self._load_contract_abi(contract_abi_path),
        )

        self._wallet_address = wallet_address
        self._wallet_private_key = wallet_private_key

    def is_connected(self):
        return self._web3.is_connected()

    def cast_vote(self, candidate_index):
        tx_hash = self._contract.functions.castVote(candidate_index).transact({
            "from": self._wallet_address,
        })

        return self._web3.eth.wait_for_transaction_receipt(tx_hash)

    def get_candidate_by_index(self, candidate_index):
        return self._contract.functions.getCandidateByIndex(candidate_index).call({
            "from": self._wallet_address,
        })

    def get_vote_counts(self):
        return self._contract.functions.getVoteCounts().call({
            "from": self._wallet_address,
        })

    def _load_contract_abi(self, filepath):
        with open(filepath, "r") as input_file:
            return input_file.read()


@click.group()
@click.option('--endpoint-uri', help='The blockchain endpoint URI', default=GANACHE_DEFAULT_ENDPOINT_URI, show_default=True)
@click.option('--contract-address', help='The contract address', required=True)
@click.option('--contract-abi-path', help='The contract ABI file path', default=CONTRACT_ABI_DEFAULT_FILE_PATH)
@click.option('--wallet-address', help='The wallet address', required=True)
@click.option('--wallet-private-key', help='The wallet private key', required=True)
@click.pass_context
def cli(ctx, endpoint_uri, contract_address, contract_abi_path, wallet_address, wallet_private_key):
    ctx.obj = client = Client(
        endpoint_uri,
        contract_address,
        contract_abi_path,
        wallet_address,
        wallet_private_key,
    )

    if not client.is_connected():
        click.echo("Error: unable to connect!", err=True)


@cli.command()
@click.argument('candidate-index', type=int)
@click.pass_obj
def cast_vote(client, candidate_index):
    output = client.cast_vote(candidate_index)
    click.echo(f"TX Hash: {output['transactionHash'].hex()} / Block: #{output['blockNumber']}")


@cli.command()
@click.argument('candidate-index', type=int)
@click.pass_obj
def get_candidate_by_index(client, candidate_index):
    output = client.get_candidate_by_index(candidate_index)
    click.echo(output)


@cli.command()
@click.pass_obj
def get_vote_counts(client):
    output = client.get_vote_counts()
    click.echo(output)


if __name__ == "__main__":
    cli()