import re
import pandas as pd 

def remove_chinese(text):
    if pd.isnull(text):
        return text
    
    chinese_pattern = re.compile('[\u4e00-\u9fff]+[^0-9]+')
    cleaned_text = re.sub(chinese_pattern, '', text)
    return cleaned_text

def has_chinese_pattern(text):
    if pd.isnull(text):
        return False
    
    chinese_pattern = re.compile('[\u4e00-\u9fff]+')
    return bool(chinese_pattern.search(text))