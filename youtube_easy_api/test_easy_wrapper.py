from youtube_easy_api.easy_wrapper import *

PROJECT_PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
CREDENTIALS_PATH = PROJECT_PATH


def test_get_video_details_01():
    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(credentials_path=CREDENTIALS_PATH)
    video_id = easy_wrapper.extract_video_id(url='https://www.youtube.com/watch?v=LsK-xG1cLYA')
    metadata = easy_wrapper.get_video_details(video_id=video_id)
    assert metadata['comments'][0] == 'Your channel has saved me a looooooot of time. Thanks!'


def test_get_video_details_02():
    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(credentials_path=CREDENTIALS_PATH)
    metadata = easy_wrapper.get_video_details(video_id='rdjnkb4ONWk')
    assert metadata['title'] == 'The Pink Panther Show Episode 59 - Slink Pink'


def test_search_videos_by_keyword():
    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(credentials_path=CREDENTIALS_PATH)
    search_keyword = 'python'
    results = easy_wrapper.search_videos_by_keywords(q=search_keyword, part='id,snippet', type='video', order='relevance')
    order_id = 1
    video_id = results[order_id]['video_id']
    assert video_id == '_uQrJ0TkZlc'
