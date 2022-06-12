import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        #Secure Hash Algorithm
        #HA-256 ハッシュオブジェクトを作る 多分ハッシュ値
        sha = hasher.sha256()
        #空に対して生成されるハッシュ値は以下の通り
        # print(sha.hexdigest())
        # e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()