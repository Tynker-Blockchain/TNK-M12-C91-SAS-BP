import hashlib
import json
from time import time
import random

def generateHash(input_string):
    hashObject = hashlib.sha256()
    hashObject.update(input_string.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue

class BlockChain():
    def __init__(self):
        self.chain = []

    def length(self):
        return len(self.chain)
        
    def addBlock(self, currentBlock):
        if(len(self.chain) == 0):
            self.createGenesisBlock()
        currentBlock.previousHash = self.chain[-1].currentHash
        # Comment the below line to mine the block
        currentBlock.currentHash = self.calculateHash()
        # Mine the currentBlock using mineBlock() method
        

        self.chain.append(currentBlock)
           
    
    def createGenesisBlock(self):
        genesisBlock = Block(0, time(), "No Previous Hash.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transactions", block.transactions)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    def validateBlock(self, currentBlock):
        previousBlock = self.chain[currentBlock.index - 1]
        if(currentBlock.index != previousBlock.index + 1):
            return False
        previousBlockHash = previousBlock.calculateHash()
        if(previousBlockHash != currentBlock.previousHash):
            return False
        
        return True
        
class Block:
    def __init__(self, index, timestamp, previousHash):
        self.index = index
        self.transactions = []
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
        self.isValid = None
        # Create self.difficulty number to set difficulty to 4 
        
       
    # Add a parameter randomString with default value " " 
    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp
        # Also concatenate randomString to create block string
        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transactions, default=str)
        return generateHash(blockString)
    
    # Define mineBlock() Method
    
        # Define target variable and set it to a string with number '0' and multiply with difficulty
        
        # Run the Loop until programme reaches the target
        
            # Generate a random string
            
            # Calculate hash for the block and  pass randomString to calculateHash() method
            
      

    def addTransaction(self, transaction):
        if transaction:
            self.transactions.append(transaction)
            if len(self.transactions) == 3:
                # Comment the below line
                self.currentHash = self.calculateHash()
                return "Ready"
            return "Add more transactions"


       
