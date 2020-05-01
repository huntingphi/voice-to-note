from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
import io

def fetch_and_recognize(link_to_audio):
    """
    Performs synchronous speech recognition on an audio file

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1p1beta1.SpeechClient()

    # The language of the supplied audio
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 16000

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.OGG_OPUS
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    audio = {"uri": link_to_audio}


    response = client.recognize(config, audio)
    transcript = ""
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        transcript+=(u"Transcript: {}".format(alternative.transcript))
    return transcript
