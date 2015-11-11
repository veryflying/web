import requests
import re

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) ' \
              'AppleWebKit/537.36 (KHTML, like Gecko) ' \
              'Chrome/44.0.2403.125 Safari/537.36'


def get_tm_prices_from_third(tmall_id):
    try:
        r = requests.get('http://www.xitie.com/tmall.php?no=%s'%tmall_id)
        prices = re.search(r'data: \[([\d,.]+)\]', r.content).group(1).split(',')
        times = re.search(r'categories: \[(.*?)\]', r.content).group(1).split(',')
        result = {}
        for i in xrange(len(times)):
            each = times[i]
            result['%s'%each.strip('\'').replace('.','')] = prices[i].strip()
    except:
        result = {}
    finally:
        return result

def get_from_mmm(url):
    r = requests.get('http://tool.manmanbuy.com/history.aspx?w=950&h=580&h2=360&m=1&e=1&tofanli=1&url=%s'%url, headers={'referer':'http://tool.manmanbuy.com/historyLowest.aspx?url=%s'%url,
                     'user-agent':USER_AGENT})
    ptn = re.search('chart\("(.*)"\)', r.content)
    result = {}
    try:
        s = ptn.group(1)
        for each in s.split('],['):
            p = re.search('Date.UTC\(([\d,.]+)\),([\d,.]+)', each)
            result[p.group(1)] = p.group(2)
    except:
        pass
    return result


def short_url_tb(primary_url):
    r = re.compile(
        'https?://(item|detail|ershou|shuziitem|game|wt|baoxian|waimai|kezhan.trip|meal|chaoshi|chaoshi.detail|temai.detail|d.life|2|mdetail|detail.ju)\.(taobao|tmall)\.(com|hk)/.*\?(|((?!item_id).)*&)(id|item_id|itemId|mallstItemId|default_item_id|item_num)=(\d+).*'
    )
    mth = r.search(primary_url)
    return 'http://' + mth.group(1).__str__() + '.' + mth.group(2).__str__() + '.' + mth.group(3).__str__() + '/item.htm?' + mth.group(6).__str__() + '=' + mth.group(7).__str__()

if __name__ == '__main__':
    print get_from_mmm('https://detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.85.wStIhm&id=40486085357')