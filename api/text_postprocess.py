import re
import os
import time
import sys
import string

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.constant import (  
    ACTION_HOTWORDS, ACTIONS
)  

# 去除標點符號並將文本轉換為小寫
def remove_punctuation_and_lowercase(transcription):
    """  Remove punctuation and convert text to lowercase  

    :param  
        ----------  
        transcription: str  
            The input text to be cleaned  
    :rtype  
        ----------  
        str: The cleaned text  
    """

    text = transcription.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    return text

# 比對熱詞並返回匹配的關鍵詞
def find_matched_hotwords(text, hotwords):
    """  Find matched hotwords in the text  

    :param  
        ----------  
        text: str  
            The input text to be searched  
        hotwords: list  
            The list of hotwords to match  
    :rtype  
        ----------  
        tuple: The index and matched hotword, or (None, -1) if no match found  
    """ 
 
    text = f" {text} "
    for index, word in enumerate(hotwords):
        if f" {word.lower()} " in text:
            matched_words = word.lower()
            matched_index = text.split().index(matched_words.split()[-1])
            return matched_index, matched_words
    return None, -1

# 比對熱詞只保留數字並返回關鍵數字
def check_numbers_hotwords(text, hotwords):
    """  Check for number hotwords in the text  

    :param  
        ----------  
        text: list  
            The input text split into words  
        hotwords: list  
            The list of number hotwords to match  
    :rtype  
        ----------  
        list or int: The list of matched number hotwords, or -1 if no match found  
    """ 

    matched_words = []
    for word in text:
        if word in hotwords:
            matched_words.append(word)
    return matched_words if matched_words else -1


# 將字母和數字分開
def separate_alphanumeric(text):
    """  This function separates letters and numbers in the given text.  
      
    :param  
        ----------  
        text: str  
            The input string containing alphanumeric characters.  
      
    :rtype  
        ----------  
        str:   
            The modified string with letters and numbers separated by spaces.  
    """ 
 
    pattern = re.compile(r'([a-zA-Z]+)(\d+)|(\d+)([a-zA-Z]+)')
    separated_text = pattern.sub(r'\1 \2\3 \4', text)
    return separated_text


def hotword_extract(spoken_text):
    """ This function identifies hotwords from the processed spoken text.  
      
    :param  
    ----------  
    spoken_text: str  
        The processed spoken text from which hotwords are to be identified.  
      
    :return  
    ----------  
    tuple:  
        A tuple containing a dictionary of hotwords and the spoken text.  
    """


    # find action type
    matched_action_index, matched_action_hotwords = find_matched_hotwords(spoken_text, ACTION_HOTWORDS)


    hotwords = {
        "action_code": matched_action_hotwords,
    }

    return hotwords, spoken_text

# 編碼函數
def encode_command(hotwords):
    """  This function encodes hotwords into corresponding command IDs.  
      
    :param  
        ----------  
        hotwords: dict  
            A dictionary containing identified hotwords.  
      
    :rtype  
        ----------  
        dict:   
            A dictionary with encoded command IDs.  
    """

    ids = {
        "action_code": -1,
    }

    ids['action_code'] = str(ACTIONS.get(hotwords['action_code'], -1))


    return ids

  
def extract_sensevoice_result_text(input_string: str) -> str:  
    """  
    Extract the text after the last '>' character in the input string.  
  
    Args:  
        input_string (str): The input string to process.  
  
    Returns:  
        str: The extracted text or an empty string if no match is found.  
    """  
    pattern = r'>([^<]+)$'  
    match = re.search(pattern, input_string)
    if match:  
        return match.group(1)  
    return ""
  