# coding:utf-8

import os
import re
import requests

dest_url = 'http://www.new1.uestc.edu.cn/?n=UestcNews.Front.Document.ArticlePage&Id=62297'
save_dir = ''
INF = 1e6


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    }
    html = requests.get(url, header)
    html.encoding = 'utf-8'
    return html.text


def remove_redundance(html):
    r = re.compile(r'''<head.*?</head>''', re.I | re.M | re.S)
    s = r.sub('', html)
    r = re.compile(r'''<footer.*?</footer>''', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''<script.*?</script>''', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''<style.*?</style>''', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''<!--.*?-->''', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''<meta.*?>''', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''<ins.*?</ins>''', re.I | re.M | re.S)
    s = r.sub('', s)

    # r = re.compile(r'''^\s+$''', re.M | re.S)
    # s = r.sub('', s)
    # r = re.compile(r'''\n+''', re.M | re.S)
    # s = r.sub('\n', s)
    r = re.compile(r'''\s+''', re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''\n+''', re.M | re.S)
    s = r.sub('\n', s)
    return s


def remove_image(s, n=0):
    image = 'a' * n
    r = re.compile(r'''<img.*?>''', re.I | re.M | re.S)
    s = r.sub(image, s)
    return s


def remove_video(s, n=0):
    video = 'a' * n
    r = re.compile(r'''<embed.*?>''', re.I | re.M | re.S)
    s = r.sub(video, s)
    r = re.compile(r'''<video.*?</video>''', re.I | re.M | re.S)
    s = r.sub(video, s)
    return s


# def remove_any_tag_but_a(s):
#     text = re.findall(r'''<a[^r][^>]*>(.*?)</a>''', s, re.I | re.S | re.S)
#     s = re.sub(r'''<[^>]+>''', '', s)
#     text_b = s.strip()
#     return len(''.join(text)), len(text_b)


def get_content(clean_html, k=1):
    if not clean_html:
        print("Can not get the clean_html!")
        exit()
    s = re.sub(r'''<[^>]+>''', '\n', clean_html)
    tmp = s.split('\n')
    group_value = []
    ovthresh = 8
    for i in range(0, len(tmp)):
        group = '\n'.join(tmp[i:i + k])
        group = remove_image(group)
        group = remove_video(group)
        temp = len(group) - ovthresh
        group_value.append(temp)
    cur_max = 0
    glo_max = -INF
    left, right = 0, 0
    for index, value in enumerate(group_value):
        cur_max += value
        if (cur_max > glo_max):
            glo_max = cur_max
            right = index
        elif (cur_max < 0):
            cur_max = 0

    for i in range(right, -1, -1):
        glo_max -= group_value[i]
        if abs(glo_max < 0.00001):
            left = i
            break
    right += 1
    tmp = '\n'.join(tmp[left:right])
    tmp = re.sub(r'''<[^>]+>''', '', tmp)
    tmp = re.sub(r'''<img(.|\n)*?>''', '', tmp)
    tmp = re.sub(r'''<embed.*?/>''', '', tmp)
    content = re.sub(r'''<video.*?</video>''', '', tmp)
    return content


def save_content(content):
    with open(save_dir, 'w') as f:
        f.writelines(content)


if __name__ == '__main__':
    html = get_html(dest_url)
    clean_html = remove_redundance(html)
    content = get_content(clean_html)
    save_content(content)
