from app.client.cats_client import CatClient
cat_client = CatClient()


def test_get_all_tags():
    res = cat_client.get_all_tags()
    assert res != None
    assert len(res) > 0
    print(res)


if __name__ == "__main__":
    test_get_all_tags()
