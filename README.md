Neuro-comma
This library was developed with the idea to help us to create punctuation restoration models to memorize trained parameters, data, training visualization, etc. The Library doesn't use any high-level frameworks, such as PyTorch-lightning or Keras, to reduce the level entry threshold.

Feel free to fork this repo and edit model or dataset classes for your purposes.

Prerequirements
Python 3.9 for training
Docker for production
Why development environment is Python 3.9 if production environment in Dockerfile is 3.8?

Our team always uses the latest version and features of Python. We started with Python 3.9, but realized, that there is no FastAPI image for Python 3.9. There is several PRs in image repositories, but no response from maintainers. So we decided to change code which we use in production to work with the 3.8 version of Python. In some functions we have 3.9 code, but we still use them, these functions are needed only for development purposes.
Installation
Option 1:
pip install -U pip wheel setuptools
pip install -r requirements.txt
Option 2:
sh scripts/installation.sh
Python module usage
