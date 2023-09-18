from url_download import *


def resolve_audio_url(response):
    output_uri = response.json().get('SynthesisTask').get('OutputUri')
    return output_uri


def generate_audio_filename(text_filename_for_synthesis, response):
    audio_filename = text_filename_for_synthesis[:250] + '_' + str(
        response.json().get('SynthesisTask').get('TaskId')) + '.mp3'
    return audio_filename


def generate_audio_directory(text_filename_for_synthesis, response):
    audio_filename = text_filename_for_synthesis[:250] + '_' + str(
        response.json().get('SynthesisTask').get('TaskId'))
    return audio_filename


def resolve_audio_download(text_filename_for_synthesis, response) -> str:
    output_uri = resolve_audio_url(response)
    if output_uri is not None and output_uri != '':
        audio_dir = generate_audio_directory(text_filename_for_synthesis, response)
        if audio_download(output_uri, audio_dir):
            return audio_dir
        else:
            return ""

