from gilded_rose import Item, GildedRose


class TestNormalItem:

    def test_item_name_does_not_change(self) -> None:
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert "foo" == items[0].name

    def test_item_quality_decreases(self) -> None:
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_item_sell_in_decreases(self) -> None:
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_item_quality_decreases_twice_as_fast_when_sell_in_is_negative(self) -> None:
        items = [Item("foo", -1, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_item_quality_is_never_negative(self) -> None:
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].quality >= 0


class TestAgedBrieItem:

    def test_item_quality_increases_with_age(self) -> None:
        items = [Item("Aged Brie", 1, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 2 == items[0].quality

    def test_item_sell_in_decreases(self) -> None:
        items = [Item("Aged Brie", 1, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].sell_in

    def test_item_quality_increases_twice_as_fast_when_sell_in_is_negative(self) -> None:
        items = [Item("Aged Brie", -1, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 3 == items[0].quality

    def test_item_quality_is_never_greater_than_50(self) -> None:
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality


class TestBackstagePassesItem:

    def test_item_quality_increases_with_age(self) -> None:
        items = [Item("Backstage passes", 15, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 21 == items[0].quality

    def test_item_quality_increases_twice_faster_when_sell_in_is_lower_than_10(self) -> None:
        items = [Item("Backstage passes", 8, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 22 == items[0].quality

    def test_item_quality_increases_thrice_faster_when_sell_in_is_lower_than_5(self) -> None:
        items = [Item("Backstage passes", 4, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 23 == items[0].quality

    def test_item_quality_drops_to_zero_when_sell_in_is_0(self) -> None:
        items = [Item("Backstage passes", 0, 20)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 0 == items[0].quality

    def test_item_quality_is_never_greater_than_50(self) -> None:
        items = [Item("Backstage passes", 1, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 50 == items[0].quality


class TestGildedRose:

    def test_sulfuras_does_not_decrease_quality(self) -> None:
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 80 == items[0].quality

    def test_sulfuras_dos_not_decrease_sell_in(self) -> None:
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert 1 == items[0].sell_in
