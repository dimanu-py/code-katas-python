SULFURES = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes"
AGED_BRIE = "Aged Brie"


class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            self.update_item_state(item)

    def update_item_state(self, item: Item) -> None:
        if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
            if item.quality > 0:
                if item.name != SULFURES:
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                self.increase_quality(item)
                if item.name == BACKSTAGE_PASSES:
                    if item.sell_in < 11:
                        if item.quality < 50:
                            self.increase_quality(item)
                    if item.sell_in < 6:
                        if item.quality < 50:
                            self.increase_quality(item)
        if item.name != SULFURES:
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != AGED_BRIE:
                if item.name != BACKSTAGE_PASSES:
                    if item.quality > 0:
                        if item.name != SULFURES:
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    self.increase_quality(item)

    @staticmethod
    def increase_quality(item: Item) -> None:
        item.quality = item.quality + 1
