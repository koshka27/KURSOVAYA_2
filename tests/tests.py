import unittest

from utils import get_posts_by_user
from main import app

class MyTestCase(unittest.TestCase):
    def test_get_posts_by_user(self):
        result = [{'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
                   'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
                   'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.',
                   'views_count': 376, 'likes_count': 154, 'pk': 1},
                  {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
                   'pic': 'https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
                   'content': 'Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.',
                   'views_count': 287, 'likes_count': 99, 'pk': 5}]

        assert get_posts_by_user('leo') == result

    def test_api_1(self):
        result = app.test_client().get("/api/posts").json

        assert isinstance(result, list)

        for item in result:
            assert "poster_name" in item.keys()
            assert "poster_avatar" in item.keys()

    def test_api_2(self):
        result = app.test_client().get("/api/posts/1/").json

        assert isinstance(result, dict)

        assert "poster_name" in result.keys()
        assert "poster_avatar" in result.keys()

if __name__ == '__main__':
    unittest.main()
