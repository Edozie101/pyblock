class Blockchain(object):
    # THis is the class object used to contain the empty list which is the chain 
    # of transactions
    def init(self):
        self.chain = []
        self.current_transactions = []
    
    
    def new_block(self):
        # creates the new block and adds it to the chain
        pass
    
    def new_transaction(self):
        # Adds a new transaction  to the list of transactions
        pass
    
    @staticmethod
    def hash(block):
        # Hashes a Block 
        pass
    
    
    def lastblock(self):
        #Returns the last block in the chain 
        pass
    
    