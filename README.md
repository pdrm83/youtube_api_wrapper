[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)

# An Easy Wrapper for YouTube Data API 3.0
This module provides you an easy interface to extract YouTube video metadata including title, comments, and stats. You
must setup your **API KEY** before being able to use this module. If you have your Google API key, you can skip this
section; otherwise, check out this video: [Getting Started - Creating an API Key and Querying the API](https://www.youtube.com/watch?v=th5_9woFJmk).
You must enter the `API_KEY` when you want to initialize the `youtube-easy-api` module. Check out the examples below. 
For more detailed description, you can read this article: [An Easy Python Wrapper for YouTube Data API 3.0](https://towardsdatascience.com/an-easy-python-wrapper-for-youtube-data-api-3-0-a0f1b9f4c964)

## Library
The module requires the following libraries:

* google-api-python-client
* google-auth-oauthlib
* google

## Install

It can be installed using pip:
```python
pip3 install youtube-easy-api
```

Make sure the `pip` is upgraded to the latest version. 

## Usage

The module currently support the methods below.

* `search_videos`
* `get_metadata`

You can search YouTube service by passing a `search_keyword` to the `search_videos` method. You will 
receive an ordered lists of videos according to the search configs.

```python
from youtube_easy_api.easy_wrapper import *

easy_wrapper = YoutubeEasyWrapper()
easy_wrapper.initialize(api_key=API_KEY)
results = easy_wrapper.search_videos(search_keyword='python', order='relevance')
order_id = 1
video_id = results[order_id]['video_id']

print(video_id)
'_uQrJ0TkZlc'
```

You can also extract the metadata of a video by passing its `video_id` to the method `get_metadata`. 

```python
from youtube_easy_api.easy_wrapper import *

easy_wrapper = YoutubeEasyWrapper()
easy_wrapper.initialize(api_key=API_KEY)
metadata = easy_wrapper.get_metadata(video_id='rdjnkb4ONWk')

print(metadata['title']) 
'The Pink Panther Show Episode 59 - Slink Pink'

print(metadata['statistics']['likeCount'])
285373
```

And, that's pretty much it!
