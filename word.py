#coding=gbk
import requests
import BeautifulSoup as bs

YOUDAO_API = 'http://dict.youdao.com/search?q=%s&keyfrom=dict.index'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/46.0.2490.71 Safari/537.36'
YOUDAO = 'http://dict.youdao.com/'
INPUT_FILE = 'in.txt'
OUTPUT_FILE = 'op.txt'

def get_interp(word):
    result = []
    r = requests.get(YOUDAO_API % word,
                             headers={
                                 'referer': YOUDAO,
                                 'user-agent': USER_AGENT
            })
    b = bs.BeautifulSoup(r.content)
    lis = b.find('div', {'class':'trans-container'})
    if lis is not None:
        for i in lis.findAll('li'):
            result.append(i.text)
    return result


def file_itp(input_file, output_file):
    with open(input_file, 'r') as f:
        for each in f.readlines():
            word, count = each.split('	')

            result = get_interp(word)

            with open(output_file, 'a') as fi:
                fi.write('\n%s\t��Ƶ��%s' % (word, count))
                if len(result) == 0:
                    fi.write('\t��δ�ҵ�')
                    continue
                for i in xrange(len(result)):
                    try:
                        fi.write('\t%d. %s\n' % (i+1, result[i].encode('gbk')))
                    except Exception as e:
                        print word, e.message
                        fi.write('\t��δ�õ�')


if __name__ == '__main__':
    file_itp(INPUT_FILE, OUTPUT_FILE)

# import requests
# from Crypto.Hash import MD5
#
#
# if __name__ == '__main__':
#     url = 'http://www.sei.ecnu.edu.cn/Data/View/1617'
#     r = requests.get(url)
#     h = MD5.new(r.content)
#     temp = bytearray(100000)
#     with open('t2', 'r') as f:
#         f.readinto(temp)
#         # print temp
#         h.update(temp)
#     print h.hexdigest()

