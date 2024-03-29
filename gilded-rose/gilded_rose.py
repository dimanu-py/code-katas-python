from abc import ABC, abstractmethod
from enum import StrEnum

MAX_QUALITY = 50
MIN_QUALITY = 0


class ItemType(StrEnum):
    SULFURES = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES = "Backstage passes"
    AGED_BRIE = "Aged Brie"
    CONJURED = "Conjured"


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


class BackstagePassesItemUpdater(ItemUpdater):
    """Backstage passes increase its quality by 1 each day. When the sell in day is less than 11, the quality increases by 2.
    When the sell in day is less than 6, the quality increases by 3. When the sell in day is negative, the quality is 0."""
    def update_quality(self, item: Item) -> None:
        increase_quality(item)
        if item.sell_in < 11:
            increase_quality(item)
        if item.sell_in < 6:
            increase_quality(item)
        if item.sell_in < 0:
            item.quality = MIN_QUALITY


class SulfuresItemUpdater(ItemUpdater):

    def update_quality(self, item: Item) -> None:
        """Sulfures do not update its quality because is a legendary item."""
        pass

    @staticmethod
    def update_sell_in(item: Item) -> None:
        """Sulfures do not update its sell in day because is a legendary item."""
        pass


class ConjuredItemUpdater(ItemUpdater):
    """Conjured items decrease their quality twice as fast as Normal Items, this means they decreased its quality by two every time, and
    also if sell in day has passed."""
    def update_quality(self, item: Item) -> None:
        decrease_quality(item, amount=2)
        if item.sell_in < 0:
            decrease_quality(item, amount=2)


class GildedRose(object):

    def __init__(self, items: list[Item]) -> None:
        self.items = items
        self.item_updater ={
            ItemType.AGED_BRIE: AgedBrieItemUpdater,
            ItemType.BACKSTAGE_PASSES: BackstagePassesItemUpdater,
            ItemType.SULFURES: SulfuresItemUpdater,
            ItemType.CONJURED: ConjuredItemUpdater
        }

    def update_quality(self) -> None:
        for item in self.items:
            self.update_item_state(item)

    def update_item_state(self, item: Item) -> None:

        item_updater = self.item_updater.get(item.name, NormalItemUpdater)()

        item_updater.update_sell_in(item)
        item_updater.update_quality(item)


def decrease_quality(item: Item, amount: int = 1) -> None:
    if item.quality > MIN_QUALITY:
        item.quality -= amount


def increase_quality(item: Item, amount: int = 1) -> None:
    if item.quality < MAX_QUALITY:
        item.quality += amount
