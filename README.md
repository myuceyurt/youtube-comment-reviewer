# YouTube Comment Reviewer
YouTube Comment Reviewer is a Python program that analyzes comments for a video on YouTube and generates an overall score. The program uses Natural Language Processing (NLP) techniques to evaluate the sentiment of each comment and assign a score between 0 and 100. The overall score is calculated as the average of all comment scores.

# Installation
To use the YouTube Comment Reviewer, you will need to have Python 3 installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

In addition, you will need to install the following Python packages:

googletrans

google-api-python-client

textblob

You can install these packages using pip, the Python package manager, by running the following command:

`pip install googletrans google-api-python-client textblob`

# Usage
To use the YouTube Comment Reviewer, you will need to create a Google API key and enable the YouTube Data API. You can follow the instructions in the [Google API Console documentation](https://developers.google.com/youtube/registering_an_application) to create an API key and enable the YouTube Data API.


Once you have your API key, you can run the program by opening a terminal or command prompt and navigating to the directory where you have saved the main.py file. Then, run the following command:

`python main.py [API_KEY]`


Replace **[API_KEY]** with your Google API key. 


**For example;** 

`python main.py "123456789"`

The program will retrieve the comments for the specified video and analyze them using NLP techniques. It will then output the overall score for the video.


# Contributing
If you find any issues with the YouTube Comment Reviewer, or if you have suggestions for new features, please open an issue on the GitHub repository. Pull requests are also welcome!
