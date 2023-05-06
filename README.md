# Google TTS

Python TTS software using Google TextToSpeech
[API](https://cloud.google.com/text-to-speech).

You need to set `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

## Examples
``` python
from google_tts import Voice

text = 'Hello world!'
language_code = 'en-US'
name='en-US-Wavenet-C'

voice = Voice(language_code, name)
voice.tts(text, 'test.mp3')
```

``` python
from google_tts import Voice

text = '안녕하세요!'
language_code = 'ko-KR'
gender = 'female'

voice = Voice(language_code, gender=gender)
voice.tts(text, 'test.mp3')
```

## Supported voices and languages
[List](https://cloud.google.com/text-to-speech/docs/voices)

## Dependency
- google-cloud-texttospeech
