import hashlib
import json 
from flask import Flask
from time import time 
from hashlib import sha256

class Blockchain(object):
    # THis is the class object used to contain the empty list which is the chain 
    # of transactions
    def init(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1,proof=100)
    
        
    def new_block(self,proof,previous_hash=None):
        """ 
        The all important creation of a new block
        
        param proof: is an integer representing the proof from the POW algorithm
        param previous_hash: is a string representing the hash of the previous block
        :return <dict> of a new block
        """
        block = {
            
            'index':  len(self.chain) + 1,
            'timestamp': time(),
            'transactions':self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        self.current_transactions = []
        # create empty transactions list
        
        self.chain.append(block)
        #append the block to the last on the chain
        
        return block
    
    def new_transaction(self, sender,recipient,amount):
        # Adds a new transaction  to the list of transactions
        """ 
        The transaction is created and with the sender and the recipient 
        to go into the next minde Block
        
        :param sender: is a string of the address of the sender
        :param recipient: is a  string of the address of the recipient
        :param amount: is an integer of the amount 
        
        :return <int> The index of the block that will hold the transaction 
        
        
        """
        
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }
            
            )
        
        # This is the index of the next block that will contain the new transaction 
        
        return self.last_block['index'] + 1 
    
    @staticmethod
    def hash(block):
        # Hashes a Block 
        
        """ 
        creates a 256 hash of a block
        :param block <dict> block
        return string hash
        
        """
        # We must make sure that the Dict is ordered or we will have in consistent hashes
        block_string = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    @property 
    def last_block(self):
        #Returns the last block in the chain 
        return self.chain[-1]
    

    # a block will contian a few key factors 
    # a timestamp , index, proof, previous hash 
    # and  transactions list



