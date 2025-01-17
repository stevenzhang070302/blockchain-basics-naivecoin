# Naivecoin: a tutorial for building a cryptocurrency

## Chapter 1 - Minimal working blockchain

Simply put think of a blockchain as a distributed database that continuously grows as a list of records.
Basic functionalities of blockchain are:
- Block and Blockchain structure
- Add new blocks to the blockchain
- Blockchain nodes that communicate and sync the blockchain with other nodes
- HTTP API to control node

First the block structure contains the following fields:
- index
- data
- timestamp
- hash 
- previousHash

The hash is calculated over all data in the block - so if anything in the block changes the
original hash is no longer valid. 

The genesis block is the first block in the blockchain and is hardcoded.

The generate a block needs the following
- previousBlock
- nextIndex
- nextTimestamp
- nextHash
- returns newBlock initialization

Validate the integrity of blocks
- the index of the block must be one number larger than the previous
- the previousHash of the block must match the hash of the previous block
- the hash of the block itself must be valid

Also validate that the structure of the block is valid as well.

So to validate that this is a valid chain -
- validate genesis block
- validate each block in the chain (for loop over all blocks)

Note: choose the longest chain in case of conflicts like two nodes generate the 
block number 72. Choose the chain with the longest number of blocks.

Communicating with other nodes - nodes need to share and sync the blockchain with
other nodes. 
- when a node generates a new block - broadcast to the network
- when a node connects a new peer it queries for the latest block
- when a node encounters a block that has a index larger than the current known block
it either adds the block to the current chain or queries for the full blockchain

Use websockets for p2p communication. 

User can control the node - setting up HTTP server
- /blocks to get blockchain
- /mineBlock to generate next block
- /peers to get sockets
- /addPeer to connect to peer

Basically user can list all blocks, create a new block with user content, and list/add peers

We have two servers - one for user HTTP controlling the node, and one for websocket communication between the nodes




