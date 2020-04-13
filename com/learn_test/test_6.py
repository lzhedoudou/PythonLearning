import collections
from random import choice

# rank是花色 suit是大小
Card = collections.namedtuple('Card', ['rank', 'suit']) # 这是一种带命名的tuple

class FrenchDeck:
    # 所有的花色
    suits = '黑桃 方片 梅花 红桃'.split() # 将字符串切分成list
    
    # ranks结果 ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    # 也就代表了所有的牌面大小
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    # 纸牌数量
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

# 类实例化
rst = FrenchDeck()
print(choice(rst)) # 随机抽取一个list元素
print(rst.__getitem__(6))
print(rst[6])



