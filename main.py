import requests
from config import *
import json
from audio_download_resolver import resolve_audio_download
import os


def get_response(input_text_file, config):
    return requests.post(
        'https://api.v6.unrealspeech.com/synthesisTasks',
        headers={
            'Authorization': 'Bearer ' + config.bearer_token
        },
        json={
            'Text': input_text_file.read(),
            'VoiceId': config.voice_id,
            'Bitrate': config.bitrate,
            'Speed': config.speed,
            'Pitch': config.pitch,
            'TimestampType': config.timestamp_type,
        }
    )


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    env = AppConfig()

    # process all text files in the texts_to_process directory
    for text_filename_for_synthesis in os.listdir(os.path.join(path, 'texts_to_process')):
        # open the text file and create a new entry in response log file
        flag_move_text_file = False
        next_text_file = os.path.join(path, 'texts_to_process', text_filename_for_synthesis)
        with open(next_text_file, 'r') as text_for_synthesis:
            response = get_response(text_for_synthesis, env)
            print(response.json())
            # if the response is OKAY, move text file to env.processed_texts_path
            if response.ok:
                flag_move_text_file = True
                print("OK: Response status code is 200.")
                current_text_file_path = os.path.join(path, 'texts_to_process', text_filename_for_synthesis)
                text_file_archive = os.path.join(path, 'processed_texts')
                archived_text_file_path = None
                if not os.path.exists(text_file_archive):
                    os.mkdir(text_file_archive)
                    archived_text_file_path = os.path.join(text_file_archive, text_filename_for_synthesis)
                # os.rename(current_text_file_path, new_text_file_path)
                print("OK: Text file moved to processed_texts directory.")
                # write the response to a log file
                log_filename = (os.path.splitext(text_filename_for_synthesis)[0]) + "_" + response.json().get(
                    'SynthesisTask').get('TaskId') + '.json'
                log_path = os.path.join(path, 'audio_synthesis_logs')
                if os.path.exists(log_path):
                    print("OK: Log directory exists.")
                    log_file_path = os.path.join(log_path, log_filename)
                else:
                    print("Log directory does not exist, creating...")
                    os.mkdir(log_path)
                    log_file_path = os.path.join(log_path, log_filename)
                with open(log_file_path, 'w+') as log_file:
                    processing_log = {
                        'AudioFilename': resolve_audio_download(text_filename_for_synthesis, response),
                        'TextFilename': text_filename_for_synthesis,
                        'RequestTime': response.json().get('SynthesisTask').get('CreationTime'),
                        'LengthOfText': response.json().get('SynthesisTask').get('RequestCharacters'),
                        'OutputUri': response.json().get('SynthesisTask').get('OutputUri'),
                        'TimestampsUri': response.json().get('SynthesisTask').get('TimestampsUri'),
                        'VoiceId': response.json().get('SynthesisTask').get('VoiceId'),
                        'Speed': env.speed,
                        'Bitrate': env.bitrate,
                        'Pitch': env.pitch,
                        'TimestampType': env.timestamp_type,
                        'SynthesisTaskID': response.json().get('SynthesisTask').get('TaskId'),
                    }
                    json.dump(processing_log, log_file)
                    print("OK: Log file written to " + log_file_path + ".")
            else:
                print("ERROR: Response status code indicates an error. Aborting...")
                continue
        if flag_move_text_file:
            print("OK: Text file processing complete. Moving to next text file...")
            if os.path.exists(text_file_archive):
                os.rename(current_text_file_path, archived_text_file_path)
            else:
                os.mkdir(text_file_archive)
                os.rename(current_text_file_path, archived_text_file_path)


if __name__ == '__main__':
    main()
