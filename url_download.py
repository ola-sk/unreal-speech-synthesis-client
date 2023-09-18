from urllib.error import HTTPError
import requests
import os
from urllib.request import urlretrieve

path = os.path.dirname(os.path.abspath(__file__))


def audio_download(url, audio_subdir='') -> bool:
    # example headers from https://unreal-tts-live-demo.s3-us-west-1.amazonaws.com/
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-NL,en;q=0.9,nl-NL;q=0.8,nl;q=0.7,en-GB;q=0.6,en-US;q=0.5,pl;q=0.4,de;q=0.3',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'unreal-tts-live-demo.s3-us-west-1.amazonaws.com',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    # if any method of downloading the audio file fails, return False
    if request_audio_download_method1h(url, headers, audio_subdir) \
            or request_audio_download_method1(url, audio_subdir) \
            or request_audio_download_method2h(url, headers, audio_subdir) \
            or request_audio_download_method2(url, audio_subdir) \
            or request_audio_download_method3(url, audio_subdir):
        return True
    else:
        return False


def request_audio_download_method1h(url, headers, audio_subdir) -> bool:
    try:
        print(f"Attempting to download MP# file with headers request using `requests` package with streaming.")
        audio_response = requests.get(url, headers=headers, stream=True)
        if audio_response.status_code == 200:
            print(f"OK: Downloading MP3 file to '{path + '/audio/' + audio_subdir + 'requests_stream.mp3'}'")
            with open(path + '/audio/' + audio_subdir + '/requests_stream.mp3', 'wb') as audio_output_stream:
                for chunk in audio_response.iter_content(chunk_size=1024):
                    if chunk:
                        audio_output_stream.write(chunk)
            if os.path.exists(path + '/audio/' + audio_subdir + '/requests_stream.mp3'):
                return True
        else:
            print(f"Failed to download MP3 files for method of requesting with `requests` package with streaming. "
                  f"Status code: {audio_response.status_code}")
            return False
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred and audio file could not be downloaded, you can still find the URL in the logs. '
              f'Error: {http_err}')
        return False


def request_audio_download_method1(url, audio_subdir) -> bool:
    try:
        print(f"Attempting to download MP3 file with no headers request using `requests` package with streaming.")
        audio_response = requests.get(url, stream=True)
        if audio_response.status_code == 200:
            print(f"OK: Downloading MP3 file to '{path + '/audio/' + audio_subdir + 'requests_stream.mp3'}'")
            with open(path + '/audio/' + audio_subdir + '/requests_stream.mp3', 'wb') as audio_output_stream:
                for chunk in audio_response.iter_content(chunk_size=1024):
                    if chunk:
                        audio_output_stream.write(chunk)
            if os.path.exists(path + '/audio/' + audio_subdir + '/requests_stream.mp3'):
                return True
        else:
            print(f"Failed to download MP3 files for method of requesting with `requests` package with streaming. "
                  f"Status code: {audio_response.status_code}")
            return False
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred and audio file could not be downloaded, you can still find the URL in the logs. '
              f'Error: {http_err}')
        return False


def request_audio_download_method2h(url, headers, audio_subdir) -> bool:
    try:
        print("Attempting to download MP3 file with headers request using `requests` package with no streaming.")
        audio_response = requests.get(url, headers=headers, stream=False)
        if audio_response.status_code == 200:
            print(f"OK: Downloading MP3 file to '{path + '/audio/' + audio_subdir + 'requests_no_stream.mp3'}'")
            with open(path + '/audio/' + audio_subdir + '/requests_no_stream.mp3', 'wb') as audio_output:
                audio_output.write(audio_response.content)
                if os.path.exists(path + '/audio/' + audio_subdir + '/requests_no_stream.mp3'):
                    return True
        else:
            print(f"Failed to download MP3 files for method of requesting with `requests` package with no streaming. "
                  f"Status code: {audio_response.status_code}")
            return False
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred and audio file could not be downloaded, you can still find the URL in the logs. '
              f'Error: {http_err}')
        return False


def request_audio_download_method2(url, audio_subdir) -> bool:
    try:
        print("Attempting to download MP3 file with no headers request using `requests` package with no streaming.")
        audio_response = requests.get(url, stream=False)
        if audio_response.status_code == 200:
            print(f"OK: Downloading MP3 file to '{path + '/audio/' + audio_subdir + 'requests_no_stream.mp3'}'")
            with open(path + '/audio/' + audio_subdir + '/requests_no_stream.mp3', 'wb') as audio_output:
                audio_output.write(audio_response.content)
                if os.path.exists(path + '/audio/' + audio_subdir + '/requests_no_stream.mp3'):
                    return True
        else:
            print(f"Failed to download MP3 files for method of requesting with `requests` package with no streaming. "
                  f"Status code: {audio_response.status_code}")
            return False
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred and audio file could not be downloaded, you can still find the URL in the logs. '
              f'Error: {http_err}')
        return False


def request_audio_download_method3(url, audio_subdir) -> bool:
    try:
        saved_in_file, audio_response = urlretrieve(url, audio_subdir + '/urllib_urlretrieve.mp3')
        print(saved_in_file, audio_response)
        return True
    except HTTPError as http_err:
        print(f'HTTP error occurred and audio file could not be downloaded, you can still find the URL in the logs. '
              f'Error: {http_err}')
        return False
