from receipts import receipt

sample = [
    {'amount': 2, 'item': {'name': 'ser', 'price': 220}},
    {'amount': 1, 'item': {'name': 'szynka', 'price': 2220}},
    {'amount': 2, 'item': {'name': 'ogór', 'price': 1220}}
    ]


def test_positions_empty():
    rec = receipt.Receipt([])
    assert rec.positions == []


def test_positions_notempty():
    rec = receipt.Receipt(sample)
    assert rec.positions == sample


def test_total_price():
    rec = receipt.Receipt(sample)
    assert rec.total_price.value_gr == 2 * 1220 + 2220 + 220 * 2


def test_iter():
    rec = receipt.Receipt(sample)
    try:
        iter(rec)
        return True
    except TypeError:
        return False


def test_len():
    rec = receipt.Receipt(sample)
    assert len(rec) == 3

def test_test():
    rec = receipt.Receipt(sample)
    print(rec)