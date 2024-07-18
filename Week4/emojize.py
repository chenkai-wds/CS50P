# 先安装emoji库  ->  pip install emoji
from emoji import emojize

print("Output:", emojize(input("Input: "), language = "alias"))