a = int(input())
s = str(a)
a = int(input())
while a:
    s += "_" + str(a)
    a = int(input())

print(s)
'''from requests import get
import json

gif_url = "http://api.giphy.com/v1/gifs/search/"

params = {
    "api_key": GIF_TOKEN,
    "q": "железный человек",
    "limit": "3"
}
data = get(url, params=params).json()

print(json.dumps(data, sort_keys=True, indent=4))
# k = get("https://speller.yandex.net/services/spellservice.json/checkText?text=синхрафазатрон+в+дубн").json()
# print(k)
{'head': {}, 'def': [{'text': 'естественно', 'pos': 'adverb', 'tr': [
    {'text': 'разумеется', 'pos': 'parenthetic', 'fr': 1, 'syn': [{'text': 'вестимо', 'pos': 'parenthetic', 'fr': 1}]},
    {'text': 'конечно', 'pos': 'adverb', 'fr': 1,
     'syn': [{'text': 'конечно же', 'pos': 'adverb', 'fr': 1}, {'text': 'понятно', 'pos': 'adverb', 'fr': 1},
             {'text': 'наверняка', 'pos': 'adverb', 'fr': 1}, {'text': 'обязательно', 'pos': 'adverb', 'fr': 1},
             {'text': 'натурально', 'pos': 'adverb', 'fr': 1}, {'text': 'известно', 'pos': 'adverb', 'fr': 1},
             {'text': 'без всяких', 'pos': 'adverb', 'fr': 1}]}, {'text': 'безусловно', 'pos': 'adverb', 'fr': 1,
                                                                  'syn': [
                                                                      {'text': 'несомненно', 'pos': 'adverb', 'fr': 1},
                                                                      {'text': 'закономерно', 'pos': 'adverb', 'fr': 1},
                                                                      {'text': 'без сомнения', 'pos': 'adverb',
                                                                       'fr': 1},
                                                                      {'text': 'вне всякого сомнения', 'pos': 'adverb',
                                                                       'fr': 1},
                                                                      {'text': 'не иначе', 'pos': 'adverb', 'fr': 1},
                                                                      {'text': 'безоговорочно', 'pos': 'adverb',
                                                                       'fr': 1},
                                                                      {'text': 'неподдельно', 'pos': 'adverb',
                                                                       'fr': 1}]},
    {'text': 'понятное дело', 'pos': 'noun', 'fr': 1},
    {'text': 'обычно', 'pos': 'adverb', 'fr': 1, 'syn': [{'text': 'нормально', 'pos': 'adverb', 'fr': 1}]},
    {'text': 'просто', 'pos': 'particle', 'fr': 1}, {'text': 'бесспорно', 'pos': 'parenthetic', 'fr': 1},
    {'text': 'непринужденно', 'pos': 'adverb', 'fr': 1,
     'syn': [{'text': 'свободно', 'pos': 'adverb', 'fr': 1}, {'text': 'раскованно', 'pos': 'adverb', 'fr': 1}]},
    {'text': 'непосредственно', 'pos': 'adverb', 'fr': 1, 'syn': [{'text': 'элементарно', 'pos': 'adverb', 'fr': 1}]},
    {'text': 'природно', 'pos': 'noun', 'fr': 1}, {'text': 'без всякого сомнения', 'pos': 'adverb', 'fr': 1,
                                                   'syn': [{'text': 'вне сомнения', 'pos': 'adverb', 'fr': 1}]}]}]}

{
    "data": [
        {
            "analytics": {
                "onclick": {
                    "url": "https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX2lkPUFnUTU1SGhpMFdBdzAmZXZlbnRfdHlwZT1HSUZfU0VBUkNIJmNpZD1hNzU5NWY5YWp4cHNwZnJ2dGgycGIwdThoNWx1M2JzbWQyaXluYjdnZWNkcWFrcWMmY3Q9Z2lm&action_type=CLICK"
                },
                "onload": {
                    "url": "https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX2lkPUFnUTU1SGhpMFdBdzAmZXZlbnRfdHlwZT1HSUZfU0VBUkNIJmNpZD1hNzU5NWY5YWp4cHNwZnJ2dGgycGIwdThoNWx1M2JzbWQyaXluYjdnZWNkcWFrcWMmY3Q9Z2lm&action_type=SEEN"
                },
                "onsent": {
                    "url": "https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX2lkPUFnUTU1SGhpMFdBdzAmZXZlbnRfdHlwZT1HSUZfU0VBUkNIJmNpZD1hNzU5NWY5YWp4cHNwZnJ2dGgycGIwdThoNWx1M2JzbWQyaXluYjdnZWNkcWFrcWMmY3Q9Z2lm&action_type=SENT"
                }
            },
            "analytics_response_payload": "e=Z2lmX2lkPUFnUTU1SGhpMFdBdzAmZXZlbnRfdHlwZT1HSUZfU0VBUkNIJmNpZD1hNzU5NWY5YWp4cHNwZnJ2dGgycGIwdThoNWx1M2JzbWQyaXluYjdnZWNkcWFrcWMmY3Q9Z2lm",
            "bitly_gif_url": "http://gph.is/17BQ86W",
            "bitly_url": "http://gph.is/17BQ86W",
            "content_url": "",
            "embed_url": "https://giphy.com/embed/AgQ55Hhi0WAw0",
            "id": "AgQ55Hhi0WAw0",
            "images": {
                "480w_still": {
                    "height": "480",
                    "size": "551832",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/480w_s.jpg?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=480w_s.jpg&ct=g",
                    "width": "480"
                },
                "downsized": {
                    "height": "170",
                    "size": "551832",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy.gif&ct=g",
                    "width": "170"
                },
                "downsized_large": {
                    "height": "170",
                    "size": "551832",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy.gif&ct=g",
                    "width": "170"
                },
                "downsized_medium": {
                    "height": "170",
                    "size": "551832",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy.gif&ct=g",
                    "width": "170"
                },
                "downsized_small": {
                    "height": "150",
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy-downsized-small.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy-downsized-small.mp4&ct=g",
                    "mp4_size": "79100",
                    "width": "150"
                },
                "downsized_still": {
                    "height": "170",
                    "size": "551832",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy_s.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy_s.gif&ct=g",
                    "width": "170"
                },
                "fixed_height": {
                    "height": "200",
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200.mp4&ct=g",
                    "mp4_size": "281625",
                    "size": "741259",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200.gif&ct=g",
                    "webp": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200.webp?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200.webp&ct=g",
                    "webp_size": "443444",
                    "width": "200"
                },
                "fixed_height_downsampled": {
                    "height": "200",
                    "size": "154093",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200_d.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200_d.gif&ct=g",
                    "webp": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200_d.webp?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200_d.webp&ct=g",
                    "webp_size": "93218",
                    "width": "200"
                },
                "fixed_height_small": {
                    "height": "100",
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/100.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=100.mp4&ct=g",
                    "mp4_size": "60487",
                    "size": "184326",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/100.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=100.gif&ct=g",
                    "webp": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/100.webp?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=100.webp&ct=g",
                    "webp_size": "124922",
                    "width": "100"
                },
                "fixed_height_small_still": {
                    "height": "100",
                    "size": "7612",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/100_s.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=100_s.gif&ct=g",
                    "width": "100"
                },
                "fixed_height_still": {
                    "height": "200",
                    "size": "26687",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200_s.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200_s.gif&ct=g",
                    "width": "200"
                },
                "fixed_width": {
                    "height": "200",
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200w.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200w.mp4&ct=g",
                    "mp4_size": "281625",
                    "size": "741259",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200w.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200w.gif&ct=g",
                    "webp": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200w.webp?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200w.webp&ct=g",
                    "webp_size": "443444",
                    "width": "200"
                },
                "fixed_width_downsampled": {
                    "height": "200",
                    "size": "154093",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200w_d.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200w_d.gif&ct=g",
                    "webp": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200w_d.webp?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200w_d.webp&ct=g",
                    "webp_size": "93218",
                    "width": "200"
                },
                "fixed_width_small": {
                    "height": "100",
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/100w.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=100w.mp4&ct=g",
                    "mp4_size": "49089",
                    "size": "184326",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/100w.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=100w.gif&ct=g",
                    "webp": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/100w.webp?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=100w.webp&ct=g",
                    "webp_size": "124922",
                    "width": "100"
                },
                "fixed_width_small_still": {
                    "height": "100",
                    "size": "7612",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/100w_s.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=100w_s.gif&ct=g",
                    "width": "100"
                },
                "fixed_width_still": {
                    "height": "200",
                    "size": "26687",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/200w_s.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=200w_s.gif&ct=g",
                    "width": "200"
                },
                "looping": {
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy-loop.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy-loop.mp4&ct=g",
                    "mp4_size": "4732097"
                },
                "original": {
                    "frames": "31",
                    "hash": "a7c6a0dce2d419bb99c1f924d2e2f3bf",
                    "height": "170",
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy.mp4&ct=g",
                    "mp4_size": "1477829",
                    "size": "551832",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy.gif&ct=g",
                    "webp": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy.webp?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy.webp&ct=g",
                    "webp_size": "373868",
                    "width": "170"
                },
                "original_mp4": {
                    "height": "480",
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy.mp4&ct=g",
                    "mp4_size": "1477829",
                    "width": "480"
                },
                "original_still": {
                    "height": "170",
                    "size": "24311",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy_s.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy_s.gif&ct=g",
                    "width": "170"
                },
                "preview": {
                    "height": "150",
                    "mp4": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy-preview.mp4?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy-preview.mp4&ct=g",
                    "mp4_size": "44795",
                    "width": "150"
                },
                "preview_gif": {
                    "height": "76",
                    "size": "47884",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy-preview.gif?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy-preview.gif&ct=g",
                    "width": "76"
                },
                "preview_webp": {
                    "height": "104",
                    "size": "35360",
                    "url": "https://media3.giphy.com/media/AgQ55Hhi0WAw0/giphy-preview.webp?cid=a7595f9ajxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc&rid=giphy-preview.webp&ct=g",
                    "width": "104"
                }
            },
            "import_datetime": "2013-11-04 14:18:07",
            "is_sticker": 0,
            "rating": "pg",
            "slug": "wizard-of-oz-scarecrow-AgQ55Hhi0WAw0",
            "source": "http://fyeah-wizard-of-oz.tumblr.com/post/19331115285",
            "source_post_url": "http://fyeah-wizard-of-oz.tumblr.com/post/19331115285",
            "source_tld": "fyeah-wizard-of-oz.tumblr.com",
            "title": "Wizard Of Oz Dorothy GIF",
            "trending_datetime": "1970-01-01 00:00:00",
            "type": "gif",
            "url": "https://giphy.com/gifs/wizard-of-oz-scarecrow-AgQ55Hhi0WAw0",
            "username": ""
        }
    ],
    "meta": {
        "msg": "OK",
        "response_id": "jxpspfrvth2pb0u8h5lu3bsmd2iynb7gecdqakqc",
        "status": 200
    },
    "pagination": {
        "count": 1,
        "offset": 0,
        "total_count": 667
    }
}
'''
