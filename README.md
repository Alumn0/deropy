# DEROPY

Deropy is a toolbox for creating, managing and testing DERO smart contracts.

# Roadmap

As I am actively using deropy to work on my own smart contracts, I will be adding features as I need them. If you have any suggestions or requests, feel free to open an issue.

> Info: I am also open to suggestion regarding the repo itself, if you have any suggestion on how to improve the repo, feel free to open an issue.

**Version 0.0.x**
- [x] Generate python class for smart contract
  - [x] Each public function have a corresponding `scinvoke` request
  - [x] Each public function have a corresponding `transfer2` request (to manually specify the fee)

- [x] Deploy the smart contract to:
  - [x] The simulator
  - [ ] The testnet
  - [ ] The mainnet

**Version 0.1.x**
- (30%) Full DVM simulator in pure python
  - [ ] Implement all the DVM standard functions
  - [x] Add compute gaz and storage gaz calculation

**Version 1.0**
- (50%) Full python to DVM Transpiler :rocket:
  - [x] Function definition
  - [x] Fuction call
  - [x] Variable declaration
  - [x] Variable assignement
  - [x] Mathematic operator
  - [x] Comparison operator
  - [x] If block
  - [ ] While loop :fire:
  - [ ] For loop ?

## Installation

```bash
pip install deropy
```

## Quick Start

**If the simulator is running** the followin
the following command will:
- Deploy your smart contract to the simulator
- Create a new SC.py file in the current directory with the correct SCID.
- A new tests/test_sc.py file in the current directory.

**If the simulator is not running** the Smart Contract will not be deployed

SC.py will contain a class that allow you to call every function implemented in your smart contract
test_sc.py will contain a test class that provide you with a basic test skeleton for every function implemented in your smart contract

```bash
deropy deploy -g path/to/sc.bas
```

## Commands

| Command | Description |
| --- | --- |
| `deropy init` | Initialize a new DERO project |
| `deropy deploy` | Compile a DERO smart contract |
| `deropy generate` | Test a DERO smart contract |


