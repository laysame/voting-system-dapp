# Election DApp Client

TODO: Introduction

## Prerequisites

Before using the Election DApp Client, ensure you have the following:
- The contract address 
- The wallet address
- The wallet-private-key

## Installation

### Install Dependencies

This project uses Poetry for dependency management. To install the required dependencies, follow these steps:

1. Install Poetry if it's not already installed. You can find the instructions at [Poetry's official website](https://python-poetry.org/docs/#installation).
2. Navigate to the root directory of the project.
3. Run the following command to install the dependencies:

```bash
$ cd client
$ poetry install
```

## Usage

### Cast a Vote

To cast a vote for a candidate, use the following command:

```bash
$ python client/client.py \
    --contract-address CONTRACT_ADDRESS \
    --wallet-address WALLET_ADDRESS \
    --wallet-private-key WALLET_PRIVATE_KEY \
    cast-vote CANDIDATE_INDEX
```

### Get Candidate Details

To retrieve details of a specific candidate by their index, use the command:

```
$ python client/client.py \
    --contract-address CONTRACT_ADDRESS \
    --wallet-address WALLET_ADDRESS \
    --wallet-private-key WALLET_PRIVATE_KEY \
    get-candidate-by-index CANDIDATE_INDEX
```

### Get Vote Counts

To fetch the current vote counts for all candidates, execute:

```
$ python client/client.py \
    --contract-address CONTRACT_ADDRESS \
    --wallet-address WALLET_ADDRESS \
    --wallet-private-key WALLET_PRIVATE_KEY \
    get-vote-counts
```
