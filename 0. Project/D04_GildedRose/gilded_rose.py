from dataclasses import dataclass
from abc import ABC, abstractmethod

SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
CONJURED = "Conjured"


@dataclass
class Item:
    name: str
    sell_in: int
    quality: int

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRoseItem(ABC):
    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update_quality(self):
        pass

    def update_sell_in(self):
        if self.item.name != SULFURAS:
            self.item.sell_in -= 1


class ItemAgedBrie(GildedRoseItem):
    def update_quality(self):
        self.item.quality = min(50, self.item.quality + (1 if self.item.sell_in >= 0 else 2))


class ItemSulfuras(GildedRoseItem):
    def update_quality(self):
        pass


class ItemBackstagePass(GildedRoseItem):
    def update_quality(self):
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 6:
            self.item.quality = min(50, self.item.quality + 3)
        elif self.item.sell_in < 11:
            self.item.quality = min(50, self.item.quality + 2)
        else:
            self.item.quality = min(50, self.item.quality + 1)


class ItemNormal(GildedRoseItem):
    def update_quality(self):
        self.item.quality = max(0, self.item.quality - (1 if self.item.sell_in >= 0 else 2))


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            gilded_rose_item = self.gilded_rose_item_creator(item)
            gilded_rose_item.update_sell_in()
            gilded_rose_item.update_quality()

    def gilded_rose_item_creator(self, item):
        if item.name == SULFURAS:
            return ItemSulfuras(item)
        elif item.name == AGED_BRIE:
            return ItemAgedBrie(item)
        elif item.name == BACKSTAGE_PASS:
            return ItemBackstagePass(item)
        else:
            return ItemNormal(item)
