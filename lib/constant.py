from pydantic import BaseModel
import torch

#############################################################################

class ModlePath(BaseModel):
    paraformer: str = "models/speech_paraformer_asr-en-16k-vocab4199-pytorch"
    sensevoice: str = "models/SenseVoiceSmall"

#############################################################################
""" options for inference """
OPTIONS = {
    "language": "en",
    "hotword": "add, back, done, go payment, hi, home, next time, next, nfc, setting, show coupon, use coupon, use now",
    "itn": True,
    "ban_emo_unk": False,
}



#############################################################################
""" 示例 ACTION 熱詞列表 """
ACTION_HOTWORDS = [
    "add", "back", "done", "go payment", "hi", "home", "next time",
    "next", "nfc", "setting", "show coupon", "use coupon", "use now",

]

ACTIONS = {
    "add": 1, "back": 2, "done": 3, "go payment": 4, "hi": 5, "home": 6, "next time": 7,
    "next": 8, "nfc": 9, "setting": 10, "show coupon": 11, "use coupon": 12, "use now": 13
}

#############################################################################


""" command  """
COMMAND_DICTIONARY = [
    "add", "back", "done", "go", "hi", "home", "time", "next", 'payment',
    "nfc", "setting", "show", "use", "coupon", "now",
]

""" special case """
# to > two, for > four
CASE1 = ["tiger", "viper"]
# two > to, four > for
CASE2 = ["cleared"]
# the case we need to convert
CONVERSION_CASE = ["to", "two", "for", "four"]