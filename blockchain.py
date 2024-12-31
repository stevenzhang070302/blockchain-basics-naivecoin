from block import Block
import hashlib
import time
import json

class Blockchain:
    def __init__(self):
        """
        Initializes the blockchain with the genesis block.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Adjust as needed for mining difficulty

    def create_genesis_block(self):
        """
        Creates the genesis (first) block in the blockchain.
        """
        genesis_block = Block(
            index=0,
            timestamp=int(time.time()),
            data="my genesis block!!",
            previous_hash="0"
        )
        return genesis_block

    def get_latest_block(self):
        """
        Retrieves the latest block in the blockchain.
        """
        return self.chain[-1]

    def generate_next_block(self, block_data):
        """
        Generates the next block with the provided data.
        """
        previous_block = self.get_latest_block()
        next_index = previous_block.index + 1
        next_timestamp = int(time.time())
        next_hash = self.calculate_hash(next_index, previous_block.hash, next_timestamp, block_data)
        new_block = Block(next_index, next_timestamp, block_data, previous_block.hash)
        new_block.hash = self.proof_of_work(new_block)
        return new_block

    def calculate_hash(self, index, previous_hash, timestamp, data):
        """
        Calculates the hash for a block based on its contents.
        """
        block_string = json.dumps({
            "index": index,
            "timestamp": timestamp,
            "data": data,
            "previous_hash": previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, block):
        """
        Simple Proof of Work algorithm:
        - Increment the nonce until the hash starts with a certain number of zeros (difficulty)
        """
        while not block.hash.startswith('0' * self.difficulty):
            block.timestamp = int(time.time())
            block.hash = block.calculate_hash()
        print(f"Block mined: {block.hash}")
        return block.hash

    def add_block(self, new_block):
        """
        Adds a new block to the blockchain after verification.
        """
        if self.is_valid_new_block(new_block, self.get_latest_block()):
            self.chain.append(new_block)
        else:
            print("Invalid block. Block not added to the chain.")

    def is_valid_new_block(self, new_block, previous_block):
        """
        Validates a new block before adding it to the chain.
        """
        if previous_block.index + 1 != new_block.index:
            print("Invalid index")
            return False
        elif previous_block.hash != new_block.previous_hash:
            print("Invalid previous hash")
            return False
        elif new_block.calculate_hash() != new_block.hash:
            print("Invalid hash")
            return False
        return True

    def is_valid_chain(self, chain):
        """
        Validates the entire blockchain.
        """
        if chain[0].hash != self.chain[0].hash:
            print("Genesis block doesn't match")
            return False

        for i in range(1, len(chain)):
            if not self.is_valid_new_block(chain[i], chain[i - 1]):
                return False

        return True

    def replace_chain(self, new_chain):
        """
        Replaces the current chain with a new one if it's valid and longer.
        """
        if self.is_valid_chain(new_chain) and len(new_chain) > len(self.chain):
            self.chain = new_chain
            print("Blockchain replaced with the new longer chain.")
            return True
        else:
            print("Received blockchain invalid or shorter than the current chain.")
            return False
