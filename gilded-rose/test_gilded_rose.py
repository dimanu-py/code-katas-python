from gilded_rose import Item, GildedRose


class TestGildedRose:
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