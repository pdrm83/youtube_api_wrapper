# An Easy Wrapper for Youtube API 3.0
YouTube is one of the main sources of education, entertainment, advertisement, and much more. This service has so much 
data that one can use to run data science projects or build machine learning products. For example, YouTube video 
comments can be an excellent source of NLP projects. YouTube API enables you to search for videos matching specific 
search criteria but it might be a bit confusing for some people. This library provides you a very easy interface to 
extract Youtube video metadata including title, comments, and stats. Hope you enjoy it. 

**Note-** You must setup your **credentials** before being able to use this library. To learn how to setup credentials, 
read the link below. This is an excellent post about Youtube API service, and help you step-by-step configure the 
credentials. You need to pass the FOLDER_PATH of the credentials when you initialize this library.

[Extracting YouTube Comments with YouTube API & Python](https://python.gotrained.com/youtube-api-extracting-comments/) 


## Library
The library requires the following libraries:

* os
* pickle
* urllib
* googleapiclient
* google_auth_oauthlib
* google

## Install

It can be installed using pip:
```python
pip install youtube_api_wrapper
```

## Usage
```python
from youtube_api_wrapper.easy_wrapper import *

easy_wrapper = YoutubeEasyWrapper()
easy_wrapper.initialize(credentials_path=CREDENTIALS_PATH)
search_keyword = 'python'
results = easy_wrapper.search_videos_by_keywords(q=search_keyword, part='id,snippet', type='video', order='relevance')
video_id = results[1][0]

print(video_id)
'_uQrJ0TkZlc'
```

You can also extract the metadata of a video by passing its video_id. 

```python
from youtube_api_wrapper.easy_wrapper import *

easy_wrapper = YoutubeEasyWrapper()
easy_wrapper.initialize(credentials_path=CREDENTIALS_PATH)
metadata = easy_wrapper.get_video_details(video_id='rdjnkb4ONWk')

print(metadata['title']) 
'The Pink Panther Show Episode 59 - Slink Pink'
```


And, that's pretty much it!
