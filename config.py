import yaml
import os


class AppConfig:
    def __init__(self):
        self._config_content = self.load_configuration()
        if self._config_content.get('authorisation_bearer_token') is None:
            print("No authorisation_bearer_token was specified in the config.yaml file. Please specify it and try "
                  "again.")
            exit()
        else:
            self._bearer_token = self._config_content.get('authorisation_bearer_token')
            print("Bearer token loaded from config.yaml file.")
        if self._config_content.get('mp3_output_path') is None:
            self._mp3_output_path = os.path.dirname(os.path.abspath(__file__)) + '/audio/'
            print(
                "No mp3_output_path was specified in the config.yaml file. Using default path: " + self._mp3_output_path + "")
        else:
            self._mp3_output_path = self._config_content.get('mp3_output_path')
            print("Using mp3_output_path: " + self._mp3_output_path + "")
        if self._config_content.get('text_input_path') is None:
            self._text_input_path = os.path.dirname(os.path.abspath(__file__)) + '/texts_to_process/'
            print(
                "No text_input_path was specified in the config.yaml file. Using default path: " + self._text_input_path + "")
        else:
            self._text_input_path = self._config_content.get('text_input_path')
            print("Using text_input_path: " + self._text_input_path + "")
        if self._config_content.get('processed_texts_path') is None:
            self._processed_texts_path = os.path.dirname(os.path.abspath(__file__)) + '/processed_texts/'
            print(
                "No processed_texts_path was specified in the config.yaml file. Using default path: " + self._processed_texts_path + "")
        else:
            self._processed_texts_path = self._config_content.get('processed_texts_path')
            print("Using processed_texts_path: " + self._processed_texts_path + "")
        if self._config_content.get('voice_id') is None:
            self._voice_id = 'Liv'
            print("No voice_id was specified in the config.yaml file. Using default voice_id: " + self._voice_id + "")
        else:
            self._voice_id = self._config_content.get('voice_id')
        if self._config_content.get('bitrate') is None:
            self._bitrate = '192k'
            print("No bitrate was specified in the config.yaml file. Using default bitrate: " + self._bitrate + "")
        else:
            self._bitrate = self._config_content.get('bitrate')
        if self._config_content.get('speed') is None:
            self._speed = '+0.3'
            print("No speed was specified in the config.yaml file. Using default speed: " + self._speed + "")
        else:
            self._speed = self._config_content.get('speed')
        if self._config_content.get('pitch') is None:
            self._pitch = '1'
            print("No pitch was specified in the config.yaml file. Using default pitch: " + self._pitch + "")
        else:
            self._pitch = self._config_content.get('pitch')
        if self._config_content.get('timestamp_type') is None:
            self._timestamp_type = 'sentence'
            print("No timestamp_type was specified in the config.yaml file. Using default timestamp_type: " + self._timestamp_type + "")
        else:
            self._timestamp_type = self._config_content.get('timestamp_type')

    @property
    def mp3_output_path(self):
        return self._mp3_output_path

    @property
    def text_input_path(self):
        return self._text_input_path

    @property
    def processed_texts_path(self):
        return self._processed_texts_path

    @property
    def bearer_token(self):
        return self._bearer_token

    @property
    def voice_id(self):
        return self._voice_id

    @property
    def bitrate(self):
        return self._bitrate

    @property
    def speed(self):
        return self._speed

    @property
    def pitch(self):
        return self._pitch

    @property
    def timestamp_type(self):
        return self._timestamp_type

    @staticmethod
    def load_configuration():
        project_config_path = os.path.dirname(os.path.abspath(__file__)) + '/config.yaml'
        print("Loading configuration from " + project_config_path + '...')
        with open(project_config_path, 'r') as config_file:
            config_content = yaml.safe_load(config_file)
            # if config_content is None, get data from the user in the terminal
            if config_content is None or type(config_content) is not dict:
                # else if the config_content's type is not dict, but string,
                # inform the user that there is a problem with the config file,
                # like a syntax error and get data from the user in the terminal
                print('There is a problem with your config.yaml file. Please check it and try again. /n'
                      'Press any key to terminate...')
                input()
                exit()
            return config_content
