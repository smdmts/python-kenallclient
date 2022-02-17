import pytest

EXAMPLE = """\
{
  "version": "2020-11-30",
  "data": [
    {
      "jisx0402": "13101",
      "old_code": "100",
      "postal_code": "1008105",
      "prefecture_kana": "",
      "city_kana": "",
      "town_kana": "",
      "town_kana_raw": "",
      "prefecture": "東京都",
      "city": "千代田区",
      "town": "大手町",
      "koaza": "",
      "kyoto_street": "",
      "building": "",
      "floor": "",
      "town_partial": false,
      "town_addressed_koaza": false,
      "town_chome": false,
      "town_multi": false,
      "town_raw": "大手町",
      "corporation": {
        "name": "チッソ　株式会社",
        "name_kana": "ﾁﾂｿ ｶﾌﾞｼｷｶﾞｲｼﾔ",
        "block_lot": "２丁目２－１（新大手町ビル）",
        "block_lot_num": "2-2-1",
        "post_office": "銀座",
        "code_type": 0
      }
    }
  ]
}
"""

SEARCH_EXAMPLE = """\
{
  "version": "2021-02-26",
  "query": "神奈川県 AND 日本郵便",
  "count": 3,
  "offset": 0,
  "limit": 100,
  "facets": [
    [
      "/神奈川県", 3
    ]
  ],
  "data": [
    {
      "jisx0402": "14131",
      "old_code": "210",
      "postal_code": "2108797",
      "prefecture_kana": "",
      "city_kana": "",
      "town_kana": "",
      "town_kana_raw": "",
      "prefecture": "神奈川県",
      "city": "川崎市川崎区",
      "town": "榎町",
      "koaza": "",
      "kyoto_street": "",
      "building": "",
      "floor": "",
      "town_partial": false,
      "town_addressed_koaza": false,
      "town_chome": false,
      "town_multi": false,
      "town_raw": "榎町",
      "corporation": {
        "name": "日本郵便　株式会社　南関東支社",
        "name_kana": "ニツポンユウビン　カブシキガイシヤ　ミナミカントウシシヤ",
        "block_lot": "１－２",
        "block_lot_num": "1-2",
        "post_office": "川崎港",
        "code_type": 0
      }
    },
    {
      "jisx0402": "14131",
      "old_code": "210",
      "postal_code": "2108796",
      "prefecture_kana": "",
      "city_kana": "",
      "town_kana": "",
      "town_kana_raw": "",
      "prefecture": "神奈川県",
      "city": "川崎市川崎区",
      "town": "榎町",
      "koaza": "",
      "kyoto_street": "",
      "building": "",
      "floor": "",
      "town_partial": false,
      "town_addressed_koaza": false,
      "town_chome": false,
      "town_multi": false,
      "town_raw": "榎町",
      "corporation": {
        "name": "日本郵便　株式会社　神奈川監査室",
        "name_kana": "ニツポンユウビン　カブシキガイシヤ　カナガワカンサシツ",
        "block_lot": "１－２",
        "block_lot_num": "1-2",
        "post_office": "川崎港",
        "code_type": 0
      }
    },
    {
      "jisx0402": "14131",
      "old_code": "210",
      "postal_code": "2108793",
      "prefecture_kana": "",
      "city_kana": "",
      "town_kana": "",
      "town_kana_raw": "",
      "prefecture": "神奈川県",
      "city": "川崎市川崎区",
      "town": "榎町",
      "koaza": "",
      "kyoto_street": "",
      "building": "",
      "floor": "",
      "town_partial": false,
      "town_addressed_koaza": false,
      "town_chome": false,
      "town_multi": false,
      "town_raw": "榎町",
      "corporation": {
        "name": "日本郵便　株式会社　南関東支社　郵便事業本部　（三種）",
        "name_kana": "ニホンユウビン　カブシキガイシヤ　ミナミカントウシシヤ　ユウビンジギヨウホンブ　（サンシユ）",
        "block_lot": "１－２",
        "block_lot_num": "1-2",
        "post_office": "川崎港",
        "code_type": 0
      }
    }
  ]
}
"""

@pytest.fixture
def dummy_json():
    import json

    return json.loads(EXAMPLE)


@pytest.fixture
def dummy_search_json():
    import json

    return json.loads(SEARCH_EXAMPLE)
