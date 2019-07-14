import re


# 整句聚合
def make_split(line):
    if re.match(r'.*([，…？！。.,?! ])$', ''.join(line)):
        return []
    return [",", line]


# 坏句子判断
def good_line(sen):
    if len(re.findall(r'a-zA-Z0-9', ''.join(sen))) > 2:
        return False
    return True


# 英文标点转中文标点
def regular(sen):
    sen = re.sub(r'\.{3,100}', '…', sen)
    sen = re.sub(r'…{3,100}', '…', sen)
    sen = re.sub(r'…{3,100}', '…', sen)
    sen = re.sub(r',{1,100}', '，', sen)
    sen = re.sub(r'\.{1,100}', '。', sen)
    sen = re.sub(r'\?{1,100}', '？', sen)
    sen = re.sub(r'!{1,100}', '！', sen)

    return sen
