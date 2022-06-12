from numpy import block
from cryptocurrency_genesis import *
from cryptocurrency_new_block import *

#ブロックチェーンをリストで定義し，初期値として１つ目のブロックを入れておく
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

#ブロックチェーンのブロックの数
num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    #これからブロックチェーンに加えるブロックを作る
    blocks_to_add = next_block(previous_block)
    #加える
    blockchain.append(blocks_to_add)
    #今追加したブロックを次作るブロックからみて１つ前のブロックとする
    previous_block = blocks_to_add
    print("Block {} has been added to the blockchain!".format(blocks_to_add.index))
    print("Hash: {}\n".format(blocks_to_add.hash))
