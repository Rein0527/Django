from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request, tvno = 0):
    tv_list = [{'name':'幽閉星光', 'tvcode':'WcNIJldE7U8'},
        {'name':'グラブル', 'tvcode':'M8iOTfwYqvw'},
        {'name':'Worlds End', 'tvcode':'1Jh8KQVkwm4'},
        {'name':'皿ハンド', 'tvcode':'2lfKWxcjOs0'},]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())
    # 如果要傳遞的變數比較多，能將字典形式改使用Python的locals()函數

def engtv(request, tvno = '0'):
    tv_list = [{'name':'0', 'tvcode':'WcNIJldE7U8'},
        {'name':'1', 'tvcode':'M8iOTfwYqvw'},
        {'name':'2', 'tvcode':'skgV4ItYyzo'},]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    return render(request, 'engtv.html', locals())