# Batch Synthesise to Speech any Text File in specific directory.

This client helps with converting programmatically all files from a given directory, by sending them within payload of requests to [unrealspeech.com](https://unrealspeech.com/) infrastructure which synthesises the speech from text and responds with links to resources hosted online: mp3 file and timestamp annotation for specific speech file. Each file can hold up to 500,000 characters to be submitted for synthesis. Client then downloads the Speech Audio for Offline use. 

## Setup
### Python dependencies
Make sure you have python 3.6 or higher installed. Install the dependencies by running:
```bash
pip install -r requirements.txt
```
in the project directory, or run:
```bash
pip install .
```
which will use the setup.py file to install the dependencies. 
### API Key
To get the token to access the API, login to [unrealspeech.com](https://unrealspeech.com/) website or register. Then go to your account and copy the API token.
#### Provide the Bearer token in the `config.yaml` file
In the `config.yaml` file at the root of this project, you will find an `authorisation_bearer_token: ` attribute after which you should paste API token for your account obtained from your account on the unreal speech website.

### Paths configuration for Text files for synthesis and for saving the results
#### Text files for synthesis
In the `config.yaml` file at the root of this project, you will find an `text_input_path: ` attribute after which you should paste the path to the directory with text files to be synthesised. This is optional and a sensible default is used for that path: you can place plain text files in the `./texts_to_process/` directory to have them synthesised.
#### Processed text files
By default, the processed text files are saved in the `./processed_texts/` directory. You can change that by changing the `processed_texts_path: ` attribute in the `config.yaml` file at the root of this project.
#### Output path for the logs & links
All the logs from text generation processing and outputs are kept in the `audio_synthesis_logs` directory. One log per generated speech synthesis. They are marked with filenames as the name of a text file that was synthesised + underscore + Id of the Synthesis task on the server. The logs contain the links to the generated speech audio and the timestamp annotation for the speech audio. The logs also contain name of the text file that was synthesised and the name of the output file with the speech audio. The logs are in the JSON format.
It is important to know where the logs are kept, because the client at the current version is not able to actually download the speech audio files. The links to the speech audio files are provided in the logs. The client is able to download the logs and parse them to get the links to the speech audio files. The client is also able to download the timestamp annotations for the speech audio files. The client is not able to download the speech audio files themselves, and it needs to be done by visiting the links in the browser and clicking download button.
#### Output path for the speech audio files
In the `config.yaml` file at the root of this project, you will find an `mp3_output_path: ` attribute after which you should paste the path to the directory where the results of the synthesis will be saved. This is optional and a sensible default is used for that path: you can find the results in the `./audio/` directory.