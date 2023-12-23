from message import send
from command import ai
from command import yy
from command import mrxw

def execute(c_type):
    # 转换为数组
    if c_type == "":
        return
    arr_type = c_type.split()
    if arr_type[0] == "help":
        send.group_msg("#ai img 提示词   #AI画图\n" +
                       "#ai chat 内容   #AI聊天(测试中", False)
    if arr_type[0] == "ai":
        if len(arr_type) >= 3:
            if arr_type[1] == "img":
                ai.ai_img(arr_type[2])
            if arr_type[1] == "chat":
                send.group_msg("未开放", False)
    if arr_type[0] == "一言":
        yy.yy()