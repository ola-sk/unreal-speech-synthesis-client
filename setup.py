from setuptools import setup

setup(
    name='unreal-speech-synthesis-client',
    version='1.0',
    description='Unreal Speech Client for handling requests for synthesis of text and download of speech audio',
    author='Ola Sokolek',
    author_email='50403262+ola-sk@users.noreply.github.com',
    install_requires=[
        'requests',
        'PyYAML',
    ],
    python_requires='>=3.6,<4.0',
)
