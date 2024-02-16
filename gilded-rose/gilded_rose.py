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
        decrease_quality(item)
        if item.sell_in < 0:
            decrease_quality(item)


class AgedBrieItemUpdater(ItemUpdater):
    """Aged Brie increases its quality by 1 each day. When the sell in day is negative, the quality increases by 2."""
    def update_quality(self, item: Item) -> None:
        increase_quality(item)
        if item.sell_in < 0:
            increase_quality(item)


class GildedRose(object):

    def __init__(self, items: list[Item]) -> None:
        self.items = items
        self.item_updater ={
            AGED_BRIE: AgedBrieItemUpdater,
        }

    def update_quality(self) -> None:
        for item in self.items:
            self.update_item_state(item)

    def update_item_state(self, item: Item) -> None:

        item_updater = self.item_updater.get(item.name, NormalItemUpdater)()

        if item.name == SULFURES:
            return

        item.sell_in = item.sell_in - 1
        item_has_expired = item.sell_in < 0

        if item.name == AGED_BRIE:
            item_updater.update_quality(item)
        elif item.name == BACKSTAGE_PASSES:
            increase_quality(item)
            if item.sell_in < 11:
                increase_quality(item)
            if item.sell_in < 6:
                increase_quality(item)
            if item_has_expired:
                item.quality = MIN_QUALITY
        else:
            decrease_quality(item)
            if item_has_expired:
                decrease_quality(item)


def decrease_quality(item: Item) -> None:
    if item.quality > MIN_QUALITY:
        item.quality -= 1


def increase_quality(item: Item) -> None:
    if item.quality < MAX_QUALITY:
        item.quality += 1
