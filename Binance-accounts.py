import os
import time
import uuid
import random
import json
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
import base64
import ddddocr
from PIL import Image
from loguru import logger
from faker import Faker
from curl_cffi import requests
import requests as requests1
import concurrent.futures
import threading
import cv2
from io import BytesIO
import numpy as np
import sys
import string
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
import onnxruntime as ort
import glob
import subprocess
import time
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

faker = Faker()
acts = []
i=0


# Replace the original model loading code (line 37) with:

try:
    model = ort.InferenceSession("binance.onnx")
    print("Model loaded successfully")
except Exception as e:
    print(f"Model loading failed: {e}")
    print("Using dummy model instead")
    model = None

# Then modify the predict_image function:
def predict_image(model, img_path, class_names):
    '''获取轨迹信息'''
    if model is None:
        # Return random class if model fails
        return random.choice(class_names)
    
    try:
        img_array = load_and_preprocess_image(img_path)
        input_name = model.get_inputs()[0].name
        output_name = model.get_outputs()[0].name
        result = model.run([output_name], {input_name: img_array})
        probabilities = result[0]
        predicted_index = np.argmax(probabilities)
        predicted_class = class_names[predicted_index]
        return predicted_class
    except Exception as e:
        print(f"Prediction error: {e}")
        return random.choice(class_names)
NODE = execjs.get()
with open('bcaptcha.js', 'r', encoding='utf-8') as f:  # 获取验证码参数
    js1 = f.read()
with open('bcaptcha2.js', 'r', encoding='utf-8') as f:  # 获取验证码参数
    js2 = f.read()
with open('get_token.js', 'r', encoding='utf-8') as f:  # 获取Fvideo-Token参数
    js3 = f.read()
with open('get_figer.js', 'r', encoding='utf-8') as f:  # 加密fingerprint参数
    js4 = f.read()
with open('cookie.js', 'r', encoding='utf-8') as f:  # 生成cookie
    js5 = f.read()

CTX1 = NODE.compile(js1)
CTX2 = NODE.compile(js2)
CTX3 = NODE.compile(js3)
CTX4 = NODE.compile(js4)
CTX5 = NODE.compile(js5)

# 读取配置文件数据
BASE_URL = 'https://accounts.binance.me'

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.loads(f.read())

with open('countries.json', 'r', encoding='utf-8') as f:
    COUNTRIES = json.loads(f.read())

with open('lat.json', 'r', encoding='utf-8') as f:
    COUNTRIES1 = json.loads(f.read())

with open('useragents.txt', 'r', encoding='utf-8') as file:
    useragentsnumber = [line.strip() for line in file.readlines()]


print(f"导入代理{len(useragentsnumber)}成功")

RESOLUTION = [
    [[720, 1280], [672, 1280], [551, 676], [500, 395], [640, 336]],  # 1920*1080 150%
    [[864, 1536], [816, 1536], [695, 816], [640, 443], [768, 348]],  # 1920*1080 125%
    [[1080, 1920], [1032, 1920], [911, 1030], [830, 570], [960, 455]],  # 1920*1080 100%
    [[700, 1120], [652, 1120], [531, 656], [436, 370], [560, 326]],  # 1680*1050 150%
    [[840, 1344], [792, 1344], [671, 792], [534, 448], [672, 396]],  # 1680*1050 125%
    [[1050, 1680], [1002, 1680], [881, 1000], [715, 555], [840, 501]],  # 1680*1050 100%
    [[600, 1067], [552, 1067], [431, 556], [408, 325], [533, 276]],  # 1600*900 150%
    [[900, 1600], [852, 1600], [731, 850], [680, 455], [800, 426]]  # 1600*900  100%
]

possible_resolutions = [
    {
        "width": 2560,
        "height": 1440,
    },
    {
        "width": 1920,
        "height": 1080,
    },
    {
        "width": 1280,
        "height": 1024,
    },
    {
        "width": 1400,
        "height": 1050,
    },
    {
        "width": 1600,
        "height": 1200,
    },
]

possible_glvd = [
    "Google Inc. (AMD)",
    "Google Inc. (NVIDIA)",
]


possible_glrd = {
    "Google Inc. (AMD)": [
        "ANGLE (AMD, AMD Radeon RX 6500 XT Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon RX 6600 XT Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon RX 6700 XT Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon RX 6800 XT Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon RX 6900 XT Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon(TM) RX Vega 11 Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon(TM) Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon RX 6700 Pro Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (AMD, AMD Radeon RX 6600 Direct3D11 vs_5_0 ps_5_0, D3D11)",
    ],
    "Google Inc. (NVIDIA)": [
        "ANGLE (NVIDIA, NVIDIA GeForce RTX 3090 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (NVIDIA, NVIDIA GeForce RTX 3070 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (NVIDIA, NVIDIA GeForce GTX 1060 6GB Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.9613)",
        "ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.5671)",
        "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "ANGLE (NVIDIA, NVIDIA GeForce GTX 1650 Super Direct3D11 vs_5_0 ps_5_0, D3D11)",
    ],
}


proxy_list = []
for proxy in config['proxies']:
    proxy_list.append(proxy)


country_to_language = {
    'AO': 'pt-AO',  # 安哥拉，使用葡萄牙语
    'AF': 'ps-AF',  # 阿富汗，使用普什图语
    'AL': 'sq-AL',  # 阿尔巴尼亚，使用阿尔巴尼亚语
    'DZ': 'ar-DZ',  # 阿尔及利亚，使用阿拉伯语
    'AS': 'en-AS',  # 美属萨摩亚，使用英语
    'AD': 'ca-AD',  # 安道尔，使用加泰罗尼亚语
    'AG': 'en-AG',  # 安提瓜和巴布达，使用英语
    'AR': 'es-AR',  # 阿根廷，使用西班牙语
    'AM': 'hy-AM',  # 亚美尼亚，使用亚美尼亚语
    'AU': 'en-AU',  # 澳大利亚，使用英语
    'AT': 'de-AT',  # 奥地利，使用德语
    'AZ': 'az-AZ',  # 阿塞拜疆，使用阿塞拜疆语
    'BH': 'ar-BH',  # 巴林，使用阿拉伯语
    'BD': 'bn-BD',  # 孟加拉国，使用孟加拉语
    'BB': 'en-BB',  # 巴巴多斯，使用英语
    'BY': 'be-BY',  # 白俄罗斯，使用白俄罗斯语
    'BE': 'nl-BE',  # 比利时，使用荷兰语
    'BZ': 'en-BZ',  # 伯利兹，使用英语
    'BJ': 'fr-BJ',  # 贝宁，使用法语
    'BT': 'dz-BT',  # 不丹，使用宗喀语
    'BO': 'es-BO',  # 玻利维亚，使用西班牙语
    'BA': 'bs-BA',  # 波斯尼亚和黑塞哥维那，使用波斯尼亚语
    'BW': 'en-BW',  # 博茨瓦纳，使用英语
    'BR': 'pt-BR',  # 巴西，使用葡萄牙语
    'BN': 'ms-BN',  # 文莱，使用马来语
    'BG': 'bg-BG',  # 保加利亚，使用保加利亚语
    'BF': 'fr-BF',  # 布基纳法索，使用法语
    'BI': 'fr-BI',  # 布隆迪，使用法语
    'KH': 'km-KH',  # 柬埔寨，使用高棉语
    'CM': 'fr-CM',  # 喀麦隆，使用法语
    'CA': 'en-CA',  # 加拿大，使用英语和法语
    'CV': 'pt-CV',  # 佛得角，使用葡萄牙语
    'CF': 'fr-CF',  # 中非共和国，使用法语
    'TD': 'fr-TD',  # 乍得，使用法语
    'CL': 'es-CL',  # 智利，使用西班牙语
    'CN': 'zh-CN',  # 中国，使用汉语
    'CO': 'es-CO',  # 哥伦比亚，使用西班牙语
    'KM': 'ar-KM',  # 科摩罗，使用阿拉伯语
    'CD': 'fr-CD',  # 刚果（金），使用法语
    'CG': 'fr-CG',  # 刚果（布），使用法语
    'CR': 'es-CR',  # 哥斯达黎加，使用西班牙语
    'CI': 'fr-CI',  # 科特迪瓦，使用法语
    'HR': 'hr-HR',  # 克罗地亚，使用克罗地亚语
    'CU': 'es-CU',  # 古巴，使用西班牙语
    'CY': 'el-CY',  # 塞浦路斯，使用希腊语
    'CZ': 'cs-CZ',  # 捷克，使用捷克语
    'DK': 'da-DK',  # 丹麦，使用丹麦语
    'DJ': 'fr-DJ',  # 吉布提，使用法语
    'DM': 'en-DM',  # 多米尼加，使用英语
    'DO': 'es-DO',  # 多明尼加共和国，使用西班牙语
    'EC': 'es-EC',  # 厄瓜多尔，使用西班牙语
    'EG': 'ar-EG',  # 埃及，使用阿拉伯语
    'SV': 'es-SV',  # 萨尔瓦多，使用西班牙语
    'GQ': 'es-GQ',  # 赤道几内亚，使用西班牙语
    'ER': 'ti-ER',  # 厄立特里亚，使用提格利尼亚语
    'EE': 'et-EE',  # 爱沙尼亚，使用爱沙尼亚语
    'SZ': 'en-SZ',  # 斯威士兰，使用英语
    'ET': 'am-ET',  # 埃塞俄比亚，使用阿姆哈拉语
    'FJ': 'en-FJ',  # 斐济，使用英语
    'FI': 'fi-FI',  # 芬兰，使用芬兰语
    'FR': 'fr-FR',  # 法国，使用法语
    'GA': 'fr-GA',  # 加蓬，使用法语
    'GM': 'en-GM',  # 冈比亚，使用英语
    'GE': 'ka-GE',  # 格鲁吉亚，使用格鲁吉亚语
    'DE': 'de-DE',  # 德国，使用德语
    'GH': 'en-GH',  # 加纳，使用英语
    'GR': 'el-GR',  # 希腊，使用希腊语
    'GD': 'en-GD',  # 格林纳达，使用英语
    'GT': 'es-GT',  # 危地马拉，使用西班牙语
    'GN': 'fr-GN',  # 几内亚，使用法语
    'GW': 'pt-GW',  # 几内亚比绍，使用葡萄牙语
    'GY': 'en-GY',  # 圭亚那，使用英语
    'HT': 'fr-HT',  # 海地，使用法语和海地克里奥尔语
    'HN': 'es-HN',  # 洪都拉斯，使用西班牙语
    'HU': 'hu-HU',  # 匈牙利，使用匈牙利语
    'IS': 'is-IS',  # 冰岛，使用冰岛语
    'IN': 'hi-IN',  # 印度，使用印地语和英语
    'ID': 'id-ID',  # 印度尼西亚，使用印度尼西亚语
    'IR': 'fa-IR',  # 伊朗，使用波斯语
    'IQ': 'ar-IQ',  # 伊拉克，使用阿拉伯语和库尔德语
    'IE': 'en-IE',  # 爱尔兰，使用英语和爱尔兰语
    'IL': 'he-IL',  # 以色列，使用希伯来语
    'IT': 'it-IT',  # 意大利，使用意大利语
    'JM': 'en-JM',  # 牙买加，使用英语
    'JP': 'ja-JP',  # 日本，使用日语
    'JO': 'ar-JO',  # 约旦，使用阿拉伯语
    'KZ': 'kk-KZ',  # 哈萨克斯坦，使用哈萨克语
    'KE': 'sw-KE',  # 肯尼亚，使用斯瓦希里语和英语
    'KI': 'en-KI',  # 基里巴斯，使用英语
    'KP': 'ko-KP',  # 朝鲜，使用朝鲜语
    'KR': 'ko-KR',  # 南朝鲜，使用朝鲜语
    'KW': 'ar-KW',  # 科威特，使用阿拉伯语
    'KG': 'ky-KG',  # 吉尔吉斯斯坦，使用吉尔吉斯语
    'LA': 'lo-LA',  # 老挝，使用老挝语
    'LV': 'lv-LV',  # 拉脱维亚，使用拉脱维亚语
    'LB': 'ar-LB',  # 黎巴嫩，使用阿拉伯语
    'LS': 'st-LS',  # 莱索托，使用塞索托语
    'LR': 'en-LR',  # 利比里亚，使用英语
    'LY': 'ar-LY',  # 利比亚，使用阿拉伯语
    'LI': 'de-LI',  # 列支敦士登，使用德语
    'LT': 'lt-LT',  # 立陶宛，使用立陶宛语
    'LU': 'lb-LU',  # 卢森堡，使用卢森堡语
    'MG': 'mg-MG',  # 马达加斯加，使用马尔加什语和法语
    'MW': 'ny-MW',  # Malawi, uses Chewa
    'MY': 'ms-MY',  # Malaysia, uses Malay
    'MV': 'dv-MV',  # Maldives, uses Divehi
    'ML': 'fr-ML',  # Mali, uses French
    'MT': 'mt-MT',  # Malta, uses Maltese
    'MH': 'en-MH',  # Marshall Islands, uses English
    'MQ': 'fr-MQ',  # Martinique, uses French
    'MR': 'ar-MR',  # Mauritania, uses Arabic
    'MU': 'en-MU',  # Mauritius, uses English
    'YT': 'fr-YT',  # Mayotte, uses French
    'MX': 'es-MX',  # Mexico, uses Spanish
    'FM': 'en-FM',  # Micronesia, uses English
    'MD': 'ro-MD',  # Moldova, uses Romanian
    'MC': 'fr-MC',  # Monaco, uses French
    'MN': 'mn-MN',  # Mongolia, uses Mongolian
    'ME': 'sr-ME',  # Montenegro, uses Serbian
    'MS': 'en-MS',  # Montserrat, uses English
    'MA': 'ar-MA',  # Morocco, uses Arabic
    'MZ': 'pt-MZ',  # Mozambique, uses Portuguese
    'MM': 'my-MM',  # Myanmar, uses Burmese
    'NA': 'en-NA',  # Namibia, uses English
    'NR': 'na-NR',  # Nauru, uses Nauruan
    'NP': 'ne-NP',  # Nepal, uses Nepali
    'NL': 'nl-NL',  # Netherlands, uses Dutch
    'NC': 'fr-NC',  # New Caledonia, uses French
    'NZ': 'en-NZ',  # New Zealand, uses English
    'NI': 'es-NI',  # Nicaragua, uses Spanish
    'NE': 'fr-NE',  # Niger, uses French
    'NG': 'en-NG',  # Nigeria, uses English
    'NU': 'en-NU',  # Niue, uses English
    'NF': 'en-NF',  # Norfolk Island, uses English
    'MK': 'mk-MK',  # North Macedonia, uses Macedonian
    'NO': 'no-NO',  # Norway, uses Norwegian
    'OM': 'ar-OM',  # Oman, uses Arabic
    'PK': 'ur-PK',  # Pakistan, uses Urdu
    'PW': 'en-PW',  # Palau, uses English
    'PS': 'ar-PS',  # Palestinian Territories, uses Arabic
    'PA': 'es-PA',  # Panama, uses Spanish
    'PG': 'en-PG',  # Papua New Guinea, uses English
    'PY': 'es-PY',  # Paraguay, uses Spanish
    'PE': 'es-PE',  # Peru, uses Spanish
    'PH': 'en-PH',  # Philippines, uses English
    'PN': 'en-PN',  # Pitcairn Islands, uses English
    'PL': 'pl-PL',  # Poland, uses Polish
    'PT': 'pt-PT',  # Portugal, uses Portuguese
    'PR': 'es-PR',  # Puerto Rico, uses Spanish
    'QA': 'ar-QA',  # Qatar, uses Arabic
    'RE': 'fr-RE',  # Réunion, uses French
    'RO': 'ro-RO',  # Romania, uses Romanian
    'RU': 'ru-RU',  # Russia, uses Russian
    'RW': 'rw-RW',  # Rwanda, uses Kinyarwanda
    'BL': 'fr-BL',  # Saint Barthélemy, uses French
    'SH': 'en-SH',  # Saint Helena, uses English
    'KN': 'en-KN',  # Saint Kitts and Nevis, uses English
    'LC': 'en-LC',  # Saint Lucia, uses English
    'MF': 'fr-MF',  # Saint Martin, uses French
    'PM': 'fr-PM',  # Saint Pierre and Miquelon, uses French
    'VC': 'en-VC',  # Saint Vincent and the Grenadines, uses English
    'WS': 'sm-WS',  # Samoa, uses Samoan
    'SM': 'it-SM',  # San Marino, uses Italian
    'ST': 'pt-ST',  # São Tomé and Príncipe, uses Portuguese
    'SA': 'ar-SA',  # Saudi Arabia, uses Arabic
    'SN': 'fr-SN',  # Senegal, uses French
    'RS': 'sr-RS',  # Serbia, uses Serbian
    'SC': 'en-SC',  # Seychelles, uses English
    'SL': 'en-SL',  # Sierra Leone, uses English
    'SG': 'en-SG',  # Singapore, uses English
    'SX': 'nl-SX',  # Sint Maarten, uses Dutch
    'SK': 'sk-SK',  # Slovakia, uses Slovak
    'SI': 'sl-SI',  # Slovenia, uses Slovene
    'SB': 'en-SB',  # Solomon Islands, uses English
    'SO': 'so-SO',  # Somalia, uses Somali
    'ZA': 'en-ZA',  # South Africa, uses English
    'GS': 'en-GS',  # South Georgia & South Sandwich Islands, uses English
    'SS': 'en-SS',  # South Sudan, uses English
    'ES': 'es-ES',  # Spain, uses Spanish
    'LK': 'si-LK',  # Sri Lanka, uses Sinhala
    'SD': 'ar-SD',  # Sudan, uses Arabic
    'SR': 'nl-SR',  # Suriname,
    'SU': 'nl-SR',  # 苏里南，使用荷兰语
    'SJ': 'no-SJ',  # 斯瓦尔巴和扬马延，使用挪威语
    'SE': 'sv-SE',  # 瑞典，使用瑞典语
    'CH': 'de-CH',  # 瑞士，使用德语、法语和意大利语
    'SY': 'ar-SY',  # 叙利亚，使用阿拉伯语
    'TW': 'zh-TW',  # 台湾，使用汉语
    'TJ': 'tg-TJ',  # 塔吉克斯坦，使用塔吉克语
    'TZ': 'sw-TZ',  # 坦桑尼亚，使用斯瓦希里语
    'TH': 'th-TH',  # 泰国，使用泰语
    'TL': 'pt-TL',  # 东帝汶，使用葡萄牙语
    'TG': 'fr-TG',  # 多哥，使用法语
    'TK': 'en-TK',  # 托克劳，使用英语
    'TO': 'en-TO',  # 汤加，使用英语
    'TT': 'en-TT',  # 特立尼达和多巴哥，使用英语
    'TN': 'ar-TN',  # 突尼斯，使用阿拉伯语
    'TR': 'tr-TR',  # 土耳其，使用土耳其语
    'TM': 'tk-TM',  # 土库曼斯坦，使用土库曼语
    'TC': 'en-TC',  # 特克斯和凯科斯群岛，使用英语
    'TV': 'ty-TV',  # 图瓦卢，使用图瓦卢语
    'UG': 'sw-UG',  # 乌干达，使用斯瓦希里语和英语
    'UA': 'uk-UA',  # 乌克兰，使用乌克兰语
    'AE': 'ar-AE',  # 阿拉伯联合酋长国，使用阿拉伯语
    'GB': 'en-GB',  # 英国，使用英语
    'US': 'en-US',  # 美国，使用英语
    'UY': 'es-UY',  # 乌拉圭，使用西班牙语
    'UZ': 'uz-UZ',  # 乌兹别克斯坦，使用乌兹别克语
    'VU': 'bi-VU',  # 瓦努阿图，使用比斯拉马语
    'VA': 'it-VA',  # 梵蒂冈，使用意大利语
    'VE': 'es-VE',  # 委内瑞拉，使用西班牙语
    'VN': 'vi-VN',  # 越南，使用越南语
    'VG': 'en-VG',  # 英属维尔京群岛，使用英语
    'VI': 'en-VI',  # 美属维尔京群岛，使用英语
    'WF': 'fr-WF',  # 瓦利斯和富图纳，使用法语
    'EH': 'ar-EH',  # 西撒哈拉，使用阿拉伯语
    'YE': 'ar-YE',  # 也门，使用阿拉伯语
    'ZM': 'en-ZM',  # 赞比亚，使用英语
    'ZW': 'en-ZW'  # 津巴布韦，使用英语
}


# 封装请求
def core_request(url, headers=None, proxies=None, json=None, type='GET',timeout=10):

    try:
        if type == 'POST':
            response = requests.post(url, headers=headers, proxies=proxies, json=json,timeout=timeout,impersonate="chrome110", verify=False)
        if type == 'GET':
            response = requests.get(url, headers=headers, proxies=proxies, json=json,timeout=timeout, verify=False)
        response.raise_for_status()
        return response
    except Exception as e:
        print(f"Request failed for {url}: {e}")
        return None

def generate_random_mac():
    mac = [0x00, 0x16, 0x3E,
           random.randint(0x00, 0x7F),
           random.randint(0x00, 0xFF),
           random.randint(0x00, 0xFF)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

def get_language_by_country_code(country_code):
    return country_to_language.get(country_code, "en-US")


def get_random_base36_string():
    # 生成一个随机浮点数
    random_number = random.random()
    # 将浮点数转换为36进制的字符串表示
    base36_string = ''
    while random_number > 0:
        random_number *= 36
        digit = int(random_number)
        base36_string += (string.digits + string.ascii_lowercase)[digit]
        random_number -= digit
        if len(base36_string) >= 10:  # 确保生成的字符串足够长
            break
    return base36_string[:8]  # 取从第2位开始的8个字符

def get_device_info(headers, timezone_str,utc_offset_minutes,gmt_offset,systemlang, screen_resolution, available_screen_resolution,proxies):
    resolution = random.choice(possible_resolutions)
    screen = f"{resolution['width']},{resolution['height']}"
    glvd = random.choice(possible_glvd)
    glrd = random.choice(possible_glrd[glvd])

    ip=getIp(proxies)


    data = {
        "screen_resolution": screen,
        "available_screen_resolution": screen,
        "system_version": 'Windows 11',
        "brand_model": "unknown",
        "system_lang": systemlang,
        "timezone": gmt_offset,
        "timezoneOffset": -utc_offset_minutes,
        "user_agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) y8-browser/1.0.10 Chrome/73.0.3683.121 Electron/5.2.13 Safari/537.36',
        "list_plugin": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
        "canvas_code": get_random_base36_string(),
        "webgl_vendor": glvd,
        "webgl_renderer": glrd,
        "audio": str(random.uniform(123, 125)),
        "platform": "Win32",
        "web_timezone": timezone_str,
        "device_name": 'Electron V5.2.13 (Windows)',

    }

    a = [str(data[key]) for key in sorted(data.keys())]
    keyparam = ''.join(a)
    data['fingerprint'] = CTX4.call('x64hash128', keyparam, 32)
    data['device_id'] = ""
    data['related_device_ids'] = ""
    data['login_ip'] = ip
    data['mac_address'] = generate_random_mac()
    print(data['mac_address'])
    data['app_install_date'] = int(time.time())
    device_info = base64.b64encode(json.dumps(data, ensure_ascii=False).encode('utf-8')).decode('utf-8')

    return device_info

def uuidv4():
    return ''.join(
        '0123456789abcdef'[
            random.randint(0, 15) if c == 'x'
            else (random.randint(0, 15) & 0x3 | 0x8)
        ]
        for c in 'xxxxxxxx-xxxx-4xxx-bxxx-xxxxxxxxxxxx'
    )

def get_session(headers, device_info, proxies):
    '''获取fvideo-id参数-dfp'''

    url = 'https://www.binance.info/fvideo/dt/sign/web?en=CXU&t=binance'
    #headers['referer'] = 'https://accounts.binance.info/en/login'

    res = requests.post(url, headers=headers, data=device_info, proxies=proxies,timeout=10, verify=False)
    res_json = res.json()

    dfp = res_json.get('dfp')
    dt = res_json.get('dt')
    if res == None or res.status_code != 200:
        return None

    if res_json['message']:
        return None
    return dfp, dt



def precheck(bizId, callingCode, mobile, mobileCode, dt, headers, proxies):
    data = {
        "bizType": "login",
        "mobile": mobile,
        "callingCode": callingCode,
        "mobileCode": mobileCode
    }
    url = f'{BASE_URL}/bapi/accounts/v1/public/account/security/request/precheck'
    try:
        res = core_request(url, headers=headers, json=data, proxies=proxies,type='POST')
        if res is None:
            print(f"Precheck failed: No response for {callingCode}{mobile}")
            return None
        res_json = res.json()
        print(f"第一次请求{res_json}")
        if res_json['code'] != '000000':
            print(f"Precheck failed: Error code {res_json['code']} for {callingCode}{mobile}")
            return None
        return res_json['data']
    except Exception as e:
        print(f"Precheck exception for {callingCode}{mobile}: {e}")
        return None



def getCaptcha(bizId, dt, ret, headers, proxies,systemlang):
    '''获取验证码'''
    url = f'{BASE_URL}/bapi/composite/v1/public/antibot/getCaptcha'
    if ret['captchaType'] == 'bCAPTCHA' or ret['captchaType'] == 'bCAPTCHA2':
        data = 'bizId=login'
        headers['content-type'] = 'text/plain'
        headers['captcha-sdk-version'] = '1.0.2'

    res = requests.post(url, headers=headers, data=data, proxies=proxies,timeout=10, verify=False)
    res_json = res.json()

    if res is None or res.status_code != 200:
        return None
    if res_json['data']:
        return res_json['data']
    else:
        return None


def split_image_by_width(image_bytes, specified_width=60):
    '''裁剪图片'''
    img = Image.open(BytesIO(image_bytes))  # 将字节数据转换为文件对象
    img_width, img_height = img.size
    if specified_width > img_width:  # 检查指定宽度是否大于图片宽度
        raise ValueError("指定宽度大于图片宽度")
    right_start_x = specified_width  # 计算右边图片的起始位置
    left_img = img.crop((0, 0, specified_width, img_height))  # 裁剪左半部分
    right_img = img.crop((right_start_x, 0, img_width, img_height))  # 裁剪右半部分
    left_img_bytes = BytesIO()  # 将裁剪后的图片转换为字节数据
    right_img_bytes = BytesIO()
    left_img.save(left_img_bytes, format=img.format)
    right_img.save(right_img_bytes, format=img.format)
    # 返回裁剪后的图片字节数据
    return left_img_bytes.getvalue(), right_img_bytes.getvalue()


def get_distance(bg_bytes, slider_bytes):
    '''获取滑块距离'''
    ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    distance = ocr.slide_match(bg_bytes, slider_bytes, simple_target=True)
    return distance['target'][0]


def load_and_preprocess_image(img_path, target_size=(110, 110)):
    '''处理图片信息'''
    if isinstance(img_path, str):  # 如果是字符串（文件路径）
        img = Image.open(img_path)
    elif isinstance(img_path, bytes):  # 如果是字节数据
        img = Image.open(BytesIO(img_path))
    else:
        raise ValueError('img_path 参数必须是图片路径或字节')
    img = img.resize(target_size)  # 调整大小
    img = np.array(img).astype(np.float32)  # 将图片转换为 NumPy 数组
    # 如果是单通道灰度图像，转为三通道
    if len(img.shape) == 2:
        img = np.stack([img] * 3, axis=-1)
    # 归一化: 如果模型需要图像数据在 [0, 1] 范围内（通常是 rescale=1./255）
    img = img / 255.0
    # 添加 batch 维度: 模型通常期望输入形状为 (batch_size, height, width, channels)
    img_array = np.expand_dims(img, axis=0)
    return img_array
    # img_array = image.img_to_array(img)
    # img_array = np.expand_dims(img_array, axis=0)  # 增加批次维度
    # img_array = img_array / 255.0  # 缩放到 [0, 1]
    # return img_array


def predict_image(model, img_path, class_names):
    '''获取轨迹信息'''
    img_array = load_and_preprocess_image(img_path)
    # 推理
    input_name = model.get_inputs()[0].name
    output_name = model.get_outputs()[0].name
    result = model.run([output_name], {input_name: img_array})
    # 获取预测的概率分布
    probabilities = result[0]
    # 找到概率最高的类别索引
    predicted_index = np.argmax(probabilities)
    # 根据索引获取类别名称
    predicted_class = class_names[predicted_index]
    return predicted_class

    # # img_array = load_and_preprocess_image(img_path)
    # # predictions = model.predict(img_array)
    # # predicted_class_index = np.argmax(predictions)
    # # predicted_class = class_names[predicted_class_index]
    # return predicted_class


def split_image(img_bytes, tag):
    # 类别名称列表
    class_names = ['airplane', 'bicycle', 'bird', 'bus', 'car', 'cat', 'dog', 'elephant', 'fish', 'panda', 'ship']
    index = 0
    pil_image = Image.open(BytesIO(img_bytes))
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    # 检查图像是否成功读取
    if image is None:
        raise ValueError(f"无法读取图像文件")
    # 获取图像尺寸
    height, width = image.shape[:2]
    # 计算每个小格子的尺寸
    cell_height = height // 3
    cell_width = width // 3
    results = []
    # 遍历图像并切割
    for row in range(3):
        for col in range(3):
            cell = image[row * cell_height:(row + 1) * cell_height, col * cell_width:(col + 1) * cell_width]
            # 将图像数组转换为字节
            retval, buffer = cv2.imencode('.png', cell)
            byte_data = buffer.tobytes()
            predicted_class = predict_image(model, byte_data, class_names)
            if predicted_class == tag:
                results.append(index)
            index += 1
    return results


def get_dist(img_bytes, tag):
    '''返回9宫格验证结果'''
    results = split_image(img_bytes, tag)
    return results


def get_data(bizId, validateId, captchaType, data, client_info, available_screen_resolution, slide_coordinate,
             center_coordinate, proxies):
    '''获取验证码图片、进行识别及生成验证码验证参数'''
    path2 = data['path2']
    url = 'https://bin.bnbstatic.com' + path2 if 'binance' in BASE_URL else 'https://static-file-1306379396.file.myqcloud.com' + path2

    headers = {
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.5',
        'referer': BASE_URL.replace('accounts', 'www') + '/',  # 少/请求不到数据
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    res = requests.get(url, headers=headers, data={}, proxies=proxies,timeout=10, verify=False)  # 下载验证码图片

    client_interHeight = client_info[0]  # 浏览器内高
    client_outerHerght = client_info[1]  # 浏览器外高
    platform = 'Win32'
    if 'SLIDE' in path2:
        slider_bytes, bg_bytes = split_image_by_width(res.content)
        distance = get_distance(bg_bytes, slider_bytes)
        slide_x = slide_coordinate[0]  # 滑块起点坐标
        slide_y = slide_coordinate[1]
        param = CTX1.call('jt', distance, bizId, data, headers['user-agent'], platform, client_interHeight,
                          client_outerHerght, slide_x, slide_y)
    else:
        tag = data['tag']
        client_w = available_screen_resolution[0]  # 浏览器内宽
        client_h = available_screen_resolution[1]  # 浏览器内高
        center_x = center_coordinate[0]  # 9宫格中心点坐标
        center_y = center_coordinate[1]
        dist = get_dist(res.content, tag)
        if dist == []:
            return []
        param = CTX2.call('jt', dist, bizId, data, headers['user-agent'], platform, validateId, client_interHeight,
                          client_outerHerght, client_w, client_h, center_x, center_y)

    return param


def validateCaptcha(captchaType, data, headers, proxies):
    '''验证验证码，获取token参数'''
    url = f'{BASE_URL}/bapi/composite/v1/public/antibot/validateCaptcha'
    res = requests.post(url, headers=headers, data=data, proxies=proxies,timeout=10, verify=False)
    headers['captcha-sdk-version']="1.0.2"
    headers['content-type'] = "text/plain"
    if res is None or res.status_code != 200:
        token = ''
        return token


    res_json = res.json()
    print(res_json)
    token = res_json['data']['token']
    return token




def result(sessionId, dt, validateCodeType, headers, proxies, token=None):
    url = f'{BASE_URL}/bapi/accounts/v1/public/account/security/check/result'
    print(sessionId)
    print(validateCodeType)
    print(proxies)
    data = {
        'sessionId': sessionId,
        'validateCodeType': validateCodeType
    }
    data['bCaptchaToken'] = token
    try:
        res = requests1.post(url, headers, json=data, proxies=proxies, verify=False)
        print(f"res={res.text}")
        if res is None:
            return False
        res_json = res.json()
        if res_json['code'] != '000000':
            return False
        else:
            return True
    except:
        return False


def bizCheck(bizId, callingCode, mobileCode, mobile, sessionId, dt, headers, proxies):
    print("发起第三次请求")
    '''判断账号是否注册'''
    url = f'{BASE_URL}/bapi/accounts/v1/public/account/security/bizCheck'
    data = {
        "bizType": "login",
        "mobile": mobile,
        "callingCode": callingCode,
        "mobileCode": mobileCode,
        "sessionId": sessionId
    }


    if headers['clienttype'] == 'android':
        data['bizId'] = 'login'
    if bizId == 'register':
        if headers['clienttype'] != 'android':
            data['deviceInfo'] = headers['device-info']
        data['bizType'] = 'register'
        data['registerationMethod'] = 'MOBILE'
    try:
        res = requests.post(url, json=data, impersonate="chrome110", headers=headers, proxies=proxies, verify=False)
        if res is None:
            print(f"BizCheck failed: No response for {callingCode}{mobile}")
            return None
        res_json = res.json()
        print(f"最后验证{res_json}")
        if res_json['code'] !='000000':
            print(f"BizCheck failed: Error code {res_json['code']} for {callingCode}{mobile}")
            return None
        valid = res_json['data']['valid']  # 返回valid=True表示存在账号，否则不存在
        return valid
    except Exception as e:
        print(f"BizCheck exception for {callingCode}{mobile}: {e}")
        return None

def send_tls(url, method="POST", proxy='', headers=None, payload=""):
        tls = '2'
        print(proxy, tls)
        header_str = '|*|'.join([str(key) + ' = ' + str(value) for key, value in headers.items()])
        cscscscs = {
                "key": "48988AB995894132ACB3FFC495D3D8C8",
                "tls": tls,
                "url": url,
                "method": method,
                "proxy": proxy,
                "data": payload,
                "header": header_str,
            }
        urlcs = f"http://170.106.179.60:1235/TLS"
        response = requests.request("POST", urlcs, json=cscscscs,proxies=proxy,data=payload, timeout=20)
        print(response.text)
        return response



def init_cookies(userAgent, cookies, screen_resolution,language):
    '''初始化cookies'''
    screen_height, screen_width = screen_resolution[0], screen_resolution[1]
    cookies['theme'] = 'dark'
    time_stamp = int(time.time())
    cookies['_ga'] = 'GA1.2.{}.{}'.format(int(random.random() * 1000000000), time_stamp)
    cookies['_gid'] = 'GA1.2.{}.{}'.format(int(random.random() * 1000000000), time_stamp)
    cookies['bnc-uuid'] = uuid.uuid4().__str__()
    cookies['sajssdk_2015_cross_new_user'] = '1'
    sensorsdata2015jssdkcross = CTX5.call('sensorsdata2015jssdkcross', screen_height, screen_width, userAgent)
    cookies['sensorsdata2015jssdkcross'] = sensorsdata2015jssdkcross
    cookies['_gat'] = '1'
    cookies['lang'] = language


def parse_cookies(cookies):
    result = []
    for k, v in cookies.items():
        result.append('='.join([k, v]))
    return '; '.join(result)


def generate_session_id(length=8):
    """生成指定长度的随机字符串，默认长度为8"""
    all_characters = string.ascii_letters + string.digits  # 包含字母和数字的字符集
    return ''.join(random.choice(all_characters) for _ in range(length))
def get_proxies(proxies):
    if proxies['name'] == 'luna':
        username = proxies["username"]
        password = proxies["password"]
        tunnel = proxies["tunnel"]
        
        # Simplified proxy format with basic authentication
        proxy_dict = {
            "http": f"http://{username}:{password}@{tunnel}",
            "https": f"http://{username}:{password}@{tunnel}"
        }

    elif proxies['name'] == 'cherry':
        username = proxies["username"]
        password = proxies["password"]
        tunnel = proxies["tunnel"]
        proxy_dict = {
            "http": f"http://{username}:{password}@{tunnel}",
            "https": f"http://{username}:{password}@{tunnel}"
        }
    return proxy_dict

def save(file, callingCode, mobile, valid):
    if valid == True:
        with open(file, 'a') as f:
            f.write(f"{callingCode + mobile}\n")
            # print('写入成功')
        acts.remove(callingCode + mobile)
        print(f'任务队列剩余{len(acts)}个')
        # print(f'{callingCode + mobile}已移除')
    if valid == False:
        with open(file, 'a') as f:
            f.write(f"{callingCode + mobile}\n")
            # print('写入成功')
        acts.remove(callingCode + mobile)
        print(f'任务队列剩余{len(acts)}个')


def verify(bizId, clientType, timezone_str, utc_offset_minutes, gmt_offset, language, systemlang, callingCode, mobile,
           mobileCode):
    try:
        print(f"Starting verification for {callingCode}{mobile}")
        # Add small random delay to avoid overwhelming the service
        time.sleep(random.uniform(0.5, 2.0))
        
        proxietype = random.choice(proxy_list)
        proxies = get_proxies(proxietype)
        chrome = random.choice(useragentsnumber)
        # 验证码处理-------------------
        screen_info = random.choice(RESOLUTION)
        screen_resolution = screen_info[0]  # 屏幕大小
        available_screen_resolution = screen_info[1]  # 屏幕可用区域(浏览器内高和宽)
        client_info = screen_info[2]  # 客户端内高和外高
        slide_coordinate = screen_info[3]  # 滑块的起点坐标
        center_coordinate = screen_info[4]  # 9宫格中心点坐标
        # -----------------------------------------

        headers = process_headers(clientType,language,systemlang)  # 根据平台生成headers
        clienttype = headers['clienttype']




        device_info = get_device_info(headers, timezone_str, utc_offset_minutes, gmt_offset, systemlang, screen_resolution,
                                    available_screen_resolution,proxies)  # 添加随机device_info
        if clienttype != 'android':
            # 安卓特殊处理
            cookies = {}


        dfp=""
        dt=""
        #dfp,dt=get_session(headers,device_info,proxies)
        headers['device-info'] = device_info
        #headers['fvideo-id'] = dfp
        #headers['fvideo-token'] = dt
        # 第一次请求 ---
        ret = precheck(bizId, callingCode, mobile, mobileCode, dt, headers, proxies)

        if ret is not None:
            captchaType = ret.get('captchaType')

            if captchaType == 'random':
                token = "123"
            if captchaType == 'reCAPTCHA':
                print(f"reCAPTCHA encountered for {callingCode}{mobile}")
                return False

            elif captchaType == 'turnstile':
                print(f"Turnstile encountered for {callingCode}{mobile}")
                return False

            elif captchaType == 'bCAPTCHA' or captchaType == 'bCAPTCHA2':

                data = getCaptcha(bizId, dt, ret, headers, proxies, systemlang)
                if data == None:
                    print(f"Failed to get captcha for {callingCode}{mobile}")
                    return False
                # 验证码请求处理-----拿到轨迹加密后的data
                params = get_data(bizId, ret['validateId'], captchaType, data, client_info, available_screen_resolution,
                                  slide_coordinate, center_coordinate, proxies)
                if params == []:
                    print(f"Failed to get captcha params for {callingCode}{mobile}")
                    return False
                token = validateCaptcha(captchaType, params, headers, proxies)
            if token == '':
                logger.error(f'BC验证失败|{clienttype}|{bizId}|{captchaType}|{mobileCode}-{callingCode}-{mobile}')
                return False            # BC1 BC2最终验证号码信息
            if captchaType == 'bCAPTCHA' or captchaType == 'bCAPTCHA2':
                msg = result(ret['sessionId'], dt, captchaType, headers, proxies, token=token)
                print(f"第二次请求的{msg}")
                if msg == True:
                    print("daozheli")
                    res = bizCheck(bizId, callingCode, mobileCode, mobile, ret['sessionId'], dt, headers, proxies)
                    if res == True:
                        save('已激活/result.txt', callingCode, mobile, valid=True)
                        logger.success(f'{clienttype}|{bizId}|{captchaType[0:2]}|已注册：{mobileCode}-{callingCode}-{mobile}')
                        return {'号码': '\t' + callingCode + mobile, '是否注册': '是'}
                    elif res == False:
                        save('未注册/result.txt', callingCode, mobile, valid=False)
                        logger.warning(f'{clienttype}|{bizId}|{captchaType[0:2]}|未注册：{mobileCode}-{callingCode}-{mobile}|{headers}')
                        return {'号码': '\t' + callingCode + mobile, '是否注册': '否'}
                    else:
                        logger.error(f'{clienttype}|{bizId}|{captchaType[0:2]}|Failed bizCheck for {callingCode}{mobile}')
                        return False
                else:
                    logger.error(f'{clienttype}|{bizId}|{captchaType[0:2]}|Failed result validation for {callingCode}{mobile}')
                    return False
            else:
                res = bizCheck(bizId, callingCode, mobileCode, mobile, ret['sessionId'], dt, headers, proxies)
                if res == True:
                    save('已激活/result.txt', callingCode, mobile, valid=True)
                    logger.success(f'{clienttype}|{bizId}|{captchaType[0:2]}|已注册：{mobileCode}-{callingCode}-{mobile}')
                    return {'号码': '\t' + callingCode + mobile, '是否注册': '是'}
                elif res == False:
                    save('未注册/result.txt', callingCode, mobile, valid=False)
                    logger.warning(f'{clienttype}|{bizId}|{captchaType[0:2]}|未注册：{mobileCode}-{callingCode}-{mobile}')
                    return {'号码': '\t' + callingCode + mobile, '是否注册': '否'}
                else:
                    logger.error(f'{clienttype}|{bizId}|{captchaType[0:2]}|Failed bizCheck for {callingCode}{mobile}')
                    return False
        else:
            print(f"Precheck returned None for {callingCode}{mobile}")
            return False
    except Exception as e:
        print(f"Exception in verify function for {callingCode}{mobile}: {e}")
        return False


def process_headers(clientType, language, systemlang):
    random_key = random.choice(list(country_to_language.keys()))

    # 使用随机键提取对应的值
    random_value = country_to_language[random_key]
    syslang = random_value.split("-")[0]


    f=uuidv4()
    '''根据不同的平台生成不同的headers'''
    headers = {
        'clienttype':'electron',
        #'accept': '*/*',
        #'accept-language': f'{random_value},{syslang};q=0.9,{syslang};q=0.8',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'content-type': 'application/json',
        'versionname': '1.58.9',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'x-ui-request-trace':f,
        'x-trace-id': f,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Binance/1.54.5 Chrome/116.0.5845.228 Electron/26.6.10 Safari/537.36 (electron 1.54.4)'
    }
    return headers


def pre_check(accounts: list) -> bool:
    check_list = []
    '''检验输入数据'''
    if type(accounts) != list:
        raise ValueError('传入参数必须为列表')
    
    print(f"Processing {len(accounts)} accounts...")
    for i in accounts:
        print(f"Checking account: {i}")
        found_match = False
        for code in COUNTRIES:
            if i.startswith(code):
                mobile_number = str(i)[len(str(code)):]
                print(f"Found match: country code {code}, mobile: {mobile_number}")
                check_list.append([code, mobile_number])
                found_match = True
                break
        if not found_match:
            print(f"No country code match found for: {i}")

    print(f"Successfully processed {len(check_list)} accounts with valid country codes")
    if len(check_list) == 0:
        print("没有找到该国家，程序将退出。")
        print("Available country codes:", list(COUNTRIES.keys())[:10], "...")  # Show first 10
        sys.exit()  # 退出程序

    return check_list


def check(max_workers):
    # 检查号码
    accounts = pre_check(acts)
    logger.debug('开始运行，共{}条数据，正在导入任务，请稍后...'.format(len(accounts)))
    QUHAO = COUNTRIES[accounts[0][0]]['code']
    #QUHAO1='GB'
    language = get_language_by_country_code(QUHAO)
    systemlang = language
    dt1 = COUNTRIES1[QUHAO]
    longitude = float(dt1.split(',')[0])
    latitude = float(dt1.split(',')[1])
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=latitude, lng=longitude)
    timezone = pytz.timezone(timezone_str)
    dt_now = datetime.utcnow()
    dt_now = pytz.utc.localize(dt_now)
    dt_tz = dt_now.astimezone(timezone)
    utc_offset_minutes = int(dt_tz.utcoffset().total_seconds() / 60)
    offset_hours = utc_offset_minutes // 60
    gmt_offset = "GMT{:+03d}:00".format(offset_hours)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for account in accounts:
            callingCode = str(account[0])  # 前缀
            mobile = str(account[1])  # 用户电话号码
            mobileCode = COUNTRIES[callingCode]['code']  # 查询号码前缀对应的手机区号（英文字母）
            clientType = random.choice(['electron'])  # 随机客户端类型
            bizId = random.choice(['login'])  # ,'register'
            future = executor.submit(verify, bizId, clientType, timezone_str, utc_offset_minutes, gmt_offset, language,
                                     systemlang, callingCode, mobile, mobileCode)
            futures.append(future)
        concurrent.futures.wait(futures)

    if acts:
        accounts1 = pre_check(acts)
        with open(f'检测失败/fail-{i + 1}.txt', 'a') as f:
            f.writelines([f"{account[0] + account[1]}\n" for account in accounts1])

        logger.error(f"这一批失败检测 {len(accounts1)} 个账号.")
    else:
        logger.success('这一小批全部完毕')


def split_list(lst, group_size):
    return [lst[i:i + group_size] for i in range(0, len(lst), group_size)]


def process_file(file_path, acts,max_workers):
    # 读取文本文件
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    # 打乱列表

    result = split_list(lines, 50000)
    for i in result:
        acts.clear()
        for row in i:
            phone = str(row)
            acts.append(phone)
        check(max_workers)  # 多线程
def getIp(proxies):
    try:
        response2 = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10, verify=False)
        response2.raise_for_status()
        ip = response2.json()['origin']
        return ip
    except Exception as e:  # Fix this line
        print(f"Proxy error: {str(e)}")
        return None
if __name__ == '__main__':

    # Create output directories if they don't exist
    output_dirs = ['已激活', '未注册', '检测失败']
    for dir_name in output_dirs:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"Created directory: {dir_name}")

    try:
        max_workers = int(input("请输入线程数 (建议1-10): "))
        if max_workers <= 0 or max_workers > 100:  # Reduced max limit
            print("线程设置错误，建议使用1-10个线程")
            sys.exit()

    except ValueError as e:
        print(f"输入值错误 只能数字: {e}")
        sys.exit()

    print(f"线程设置为{max_workers}")
    print("正在进行本机外网测试")
    proxy1 = random.choice(proxy_list)
    proxies1 = get_proxies(proxy1)
    print(proxies1)
    a = getIp(proxies1)
    if a is None:
        print("请检查本机节点网络或者代理池是否停机")
    else:
        print(f"网络测试通过{a}")
    folder_path = "待检测"  # '待检测'  # 文件夹路径
    fail_path = "检测失败"  # '待检测'  # 文件夹路径
    # 获取文件夹中所有文件的路径
    falg = True
    file_paths = glob.glob(os.path.join(folder_path, '*.txt'))
    for file_path in file_paths:
        print(f'正在处理文件: {file_path}')
        process_file(file_path, acts, max_workers)

    while os.path.isfile(os.path.join(fail_path, f'fail-{i + 1}.txt')):
        i = i + 1
        process_file(f'检测失败/fail-{i}.txt', acts, max_workers)






