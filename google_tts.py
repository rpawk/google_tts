from google.cloud import texttospeech
import google_voices


class Voice():
    def __init__(self,language_code,name=None,gender='male',kind='Wavenet',verbose=True):
        self.client = texttospeech.TextToSpeechClient()
        self.language_code = language_code
        if name:
            self.name = name
        else: # select voice using gender
            self.name = google_voices.select_voice(self.language_code,gender,kind)
        self.verbose = verbose

        self.voice = texttospeech.VoiceSelectionParams(
                language_code=self.language_code, name=self.name)
        # Select the type of audio file you want returned
        self.audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    def tts(self,text,output):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )

        with open(output, "wb") as out:
            out.write(response.audio_content)

        if self.verbose:
            print(f'Audio content written to file "{output}"')


if __name__ == '__main__':

    text='안녕하세요, 이것은 연습용 TTS 입니다'
    language_code='ko-KR'
    gender='female'

    voice_kr = Voice(language_code,gender='female')
    voice_kr.tts(text, f'test1.mp3')


    text='Hello world! I am a speaking machine!'
    language_code='en-US'
    name='en-US-Wavenet-C'

    voice_us = Voice(language_code,name)
    voice_us.tts(text, f'test2.mp3')
