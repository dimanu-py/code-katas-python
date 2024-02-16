from abc import ABC, abstractmethod

MAX_QUALITY = 50
MIN_QUALITY = 0
SULFURES = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes"
AGED_BRIE = "Aged Brie"


class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater(ABC):
    """Model the behavior to update the quality and sell in day of an item."""

    @abstractmethod
    def update_quality(self, item: Item) -> None:
        """Update the quality of an item."""
        pass

    @staticmethod
    def update_sell_in(item: Item) -> None:
        """Update the sell in day of an item."""
        item.sell_in = item.sell_in - 1


class NormalItemUpdater(ItemUpdater):
    """Normal items decrease their quality by 1 each day. When the sell in day is negative, the quality decreases by 2."""
    def update_quality(self, item: Item) -> None:
        if item.quality > MIN_QUALITY:
            item.quality = item.quality - 1
        if item.sell_in < 0:
            item.quality = item.quality - 1


class GildedRose(object):

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            self.update_item_state(item)

    def update_item_state(self, item: Item) -> None:

        if item.name == SULFURES:
            return

        item.sell_in = item.sell_in - 1
        item_has_expired = item.sell_in < 0

        if item.name == AGED_BRIE:
            self.increase_quality(item)
            if item_has_expired:
                self.increase_quality(item)
        elif item.name == BACKSTAGE_PASSES:
            self.increase_quality(item)
            if item.sell_in < 11:
                self.increase_quality(item)
            if item.sell_in < 6:
                self.increase_quality(item)
            if item_has_expired:
                item.quality = MIN_QUALITY
        else:
            self.decrease_quality(item)
            if item_has_expired:
                self.decrease_quality(item)


def decrease_quality(item: Item) -> None:
    if item.quality > MIN_QUALITY:
        item.quality -= 1


def increase_quality(item: Item) -> None:
    if item.quality < MAX_QUALITY:
        item.quality += 1
