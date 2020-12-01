from youtube_easy_api.easy_wrapper import *

PROJECT_PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
CREDENTIALS_PATH = '../../../Secrets/YouTube'

f = open(os.path.join(CREDENTIALS_PATH, 'api.txt'), "r")
API_KEY = f.read()


def test_get_metadata_01():
    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(api_key=API_KEY)
    metadata = easy_wrapper.get_metadata(video_id='f3lUEnMaiAU')
    print(metadata['comments'][0])


def test_get_metadata_02():
    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(api_key=API_KEY)
    metadata = easy_wrapper.get_metadata(video_id='rdjnkb4ONWk')
    print(metadata['statistics']['likeCount'])
    assert metadata['title'] == 'The Pink Panther Show Episode 59 - Slink Pink'


def test_get_metadata_03():
    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(api_key=API_KEY)
    metadata = easy_wrapper.get_metadata(video_id='BW4fYZHVhfk')
    print(metadata['statistics']['commentCount'])


def test_search_videos_01():
    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(api_key=API_KEY)
    results = easy_wrapper.search_videos(search_keyword='python', order='relevance')
    order_id = 1
    video_id = results[order_id]['video_id']
    assert video_id == '_uQrJ0TkZlc'


def test_search_videos_02():
    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(api_key=API_KEY)
    results = easy_wrapper.search_videos(search_keyword='python', order='relevance')
    order_id = 1
    print(results[order_id]['video_id'])
