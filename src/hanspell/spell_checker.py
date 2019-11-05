# -*- coding: utf-8 -*-
"""
Python용 한글 맞춤법 검사 모듈
"""

import requests
import json
import time
import sys
from collections import OrderedDict
import xml.etree.ElementTree as ET

from . import __version__
from .response import Checked
from .constants import base_url
from .constants import CheckResult

_agent = requests.Session()
PY3 = sys.version_info[0] == 3

def _remove_tags(text):

    text = u'<content>{}</content>'.format(text).replace('<br>','')
    if not PY3:
        text = text.encode('utf-8')


    result = ''.join(ET.fromstring(text).itertext())

    return result

def check(text):
    """
    매개변수로 입력받은 한글 문장의 맞춤법을 체크합니다.
    """
    if isinstance(text, list):
        result = []
        for item in text:
            checked = check(item)
            result.append(checked)
        return result

    # 최대 1000자까지 가능.
    if len(text) > 1000:
        return Checked(result=False)

    payload = {
        '_callback':'window.__jindo2_callback._spellingCheck_0',
        'q': text
    }

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'referer':'https://search.naver.com/'
    }


    start_time = time.time()
    r = _agent.get(base_url, params=payload, headers = headers)
    passed_time = time.time() - start_time

    r = r.text[42:-2]

    data = json.loads(r)
    html = data['message']['result']['html']
    result = {
        'result': True,
        'original': text,
        'checked': _remove_tags(html),
        'errors': data['message']['result']['errata_count'],
        'time': passed_time,
        'words': OrderedDict(),
    }

    return result['checked']
