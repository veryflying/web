import requests
import re

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
    r = requests.get('http://tool.manmanbuy.com/history.aspx?&url=%s' % url)
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

if __name__ == '__main__':
    print get_from_mmm('https://detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.85.wStIhm&id=40486085357')