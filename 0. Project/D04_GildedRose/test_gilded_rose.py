import pytest
from gilded_rose import Item, GildedRose

def test_foo():
    items = [
             Item(name='+5 Dexterity Vest', sell_in=10, quality=20),
             Item(name='Aged Brie', sell_in=2, quality=0),
             Item(name='Elixir of the Mongoose', sell_in=5, quality=7),
             Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80),
             Item(name='Sulfuras, Hand of Ragnaros', sell_in=-1, quality=80),
             Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=20),
             Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=8, quality=30),
             Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=3, quality=40),
             Item(name='+8 Dexterity Vest', sell_in=0, quality=20),
             Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=0, quality=10),
             Item(name='Aged Brie', sell_in=0, quality=10),
    ]
    items_answer = [
        Item(name='+5 Dexterity Vest', sell_in=9, quality=19),
        Item(name='Aged Brie', sell_in=1, quality=1),
        Item(name='Elixir of the Mongoose', sell_in=4, quality=6),
        Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80),
        Item(name='Sulfuras, Hand of Ragnaros', sell_in=-1, quality=80),
        Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=14, quality=21),
        Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=7, quality=32),
        Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=2, quality=43),
        Item(name='+8 Dexterity Vest', sell_in=-1, quality=18),
        Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=-1, quality=0),
        Item(name='Aged Brie', sell_in=-1, quality=12),
    ]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for i in range(len(items)):
        assert str(items[i]) == str(items_answer[i])
