class simplehash:
    def __init__(self, size=1000):
        self.size=size
        self.table=[None]*size

    def hash_function(self,key):
        return sum(ord(c) for c in key)% self.size
    
    def insert(self,key,value):
        index=self.hash_function(key)
        self.table[index]=value

    def get(self,key):
        index=self.hash_function(key)
        return self.table[index]

hash_table=simplehash()
hash_table.insert("name","priya")
print(hash_table.get("name"))
    
