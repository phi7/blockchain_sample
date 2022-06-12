from cryptocurrency_block import *
import datetime as date

def create_genesis_block():
    #手動ｓで１つ目のブロックを作る
    return Block(0, date.datetime.now(), "Genesis Block", "0")