from __future__ import annotations
from fake_useragent import UserAgent
import sys
import requests 
import json
import subprocess
from telegram.ext import Application
from bs4 import BeautifulSoup
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


# Настройка опций Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")

# Генерация случайного User-Agent


# Заголовки с вашими cookies
headers = {
    'User-Agent'
    'Cookie': 'Device-id=5XLYQg3h1xbAeZTJjVRZ; Locale-Supported=ru; game=csgo; session=1; csrf_token=I',
}

def collect_data():
    urls = [
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=35073&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.16&_=1742141952772',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=35220&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.18&_=1742141868991',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=35220&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.18&max_paintwear=0.21&_=1742156144508',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=35354&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.17&_=1742155735028',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=36052&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.01&max_paintwear=0.02&_=1742155998781',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=34409&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.09&_=1742156815822',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=34409&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.01&_=1742156815822',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=34409&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.01&_=1742156815822',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=35221&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.09&_=1742157061584',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=887070&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.0&max_paintwear=0.01&_=1742157185274',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=887070&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.01&max_paintwear=0.02&_=1742157185274',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=34399&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.02&_=1742157284537',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=779275&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1742157332985',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=35414&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.016&_=1742157394362',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=900565&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1742157467042',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=835647&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1742157515852',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=781660&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1742157597159',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=781660&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.018&_=1742157597159',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=38800&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.017&_=1742157806551',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=762249&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1742157857000',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=36128&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&max_paintwear=0.016&_=1742157914353',
    ]

    выгода = []

    for url in urls:
        try:
            print(f"\n🔵 Отправка запроса: {url}")
            response = requests.get(url, headers=headers, timeout=10)
            print(f"🟢 Ответ сервера ({url}): {response.status_code}")

            if response.status_code != 200:
                print(f"🔴 Ошибка {response.status_code}: {response.text[:500]}")
                continue

            data = response.json()
            print(f"🗂️ Ключи JSON: {list(data.keys())}")

            items = data.get('data', {}).get('items', [])
            print(f"📦 Найдено {len(items)} предметов")

            if not items:
                print(f"⚠️ Сервер не вернул предметов для {url}")
                continue

            goods_infos = data.get("data", {}).get("goods_infos", {})
            if not goods_infos:
                print(f"⚠️ Нет данных о товарах в ответе API {url}")
                continue

            item_id = next(iter(goods_infos), None)
            if not item_id:
                print(f"⚠️ Не найден item_id в goods_infos {url}")
                continue

            item_name = goods_infos[item_id].get("market_hash_name", "Неизвестный предмет")

            # Инициализация списка parsed_skins
            parsed_skins = []

            for item in items:
                try:
                    price = item.get('price')
                    paintwear = item.get('asset_info', {}).get('paintwear')
                    if price is None or paintwear is None:
                        print(f"⚠️ Отсутствует цена или износ для предмета: {item}")
                        continue

                    skin = {
                        "Название": item_name,
                        "Цена": float(price),
                        "Износ": float(paintwear),
                    }
                    parsed_skins.append(skin)
                except (ValueError, AttributeError) as e:
                    print(f"⚠️ Ошибка при обработке предмета: {e}")
                    continue

            for skin in parsed_skins:
                print(f"Обрабатываем {skin['Название']} (Износ: {skin['Износ']}, Цена: {skin['Цена']})")

                # Проверка выгодности для Glock-18 | Water Elemental (Field-Tested)
                if skin['Название'] == "Glock-18 | Water Elemental (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.1509:
                           ratio = 44.3 / skin['Цена']
                           print(f"  Проверка условия 1: износ < 0.1509, ratio={ratio:.2f}")
                           if ratio > 1.18:
                              print(f"  Этот скин выгодный! (Износ < 0.1509, ratio = {ratio:.2f})")
                              skin["ratio"] = ratio
                              выгода.append(skin)
                    if skin['Износ'] < 0.1524:
                       ratio = 42.99 / skin['Цена']
                       print(f"  Проверка условия 2: износ < 0.1524, ratio={ratio:.2f}")
                       if ratio > 1.18:
                          print(f"  Этот скин выгодный! (Износ < 0.1524, ratio = {ratio:.2f})")
                          skin["ratio"] = ratio
                          выгода.append(skin)
                    if skin['Износ'] < 0.1544:
                        ratio = 41.4 / skin['Цена']
                        print(f"  Проверка условия 3, ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.1544, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    if skin['Износ'] < 0.1555:
                        ratio = 40.4 / skin['Цена']
                        print(f"  Проверка условия 4, ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.1555, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    if skin['Износ'] < 0.1568:
                        ratio = 39.4 / skin['Цена']
                        print(f"  Проверка условия 5, ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.1568, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    if skin['Износ'] < 0.1578:
                        ratio = 38.5 / skin['Цена']
                        print(f"  Проверка условия 6, ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.1578, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)

                # Проверка выгодности для M4A1-S | Hyper Beast (Field-Tested)
                elif skin['Название'] == "M4A1-S | Hyper Beast (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.159:
                            ratio = 234 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.159, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.159, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1649:
                            ratio = 228 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.1649, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1649, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.168:
                            ratio = 226 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.168, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.168, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.171:
                            ratio = 222 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.171, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.171, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.18:
                            ratio = 217 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.18, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.18, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1855:
                            ratio = 206 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.1855, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1855, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.192:
                            ratio = 201 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.192, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.192, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.197:
                            ratio = 194 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.197, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.197, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.200:
                            ratio = 191 / skin['Цена']
                            print(f"  Проверка условия 9: износ < 0.200, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.200, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.2088:
                            ratio = 186 / skin['Цена']
                            print(f"  Проверка условия 10: износ < 0.2088, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.2088, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для M4A4 | 龍王 (Dragon King) (Field-Tested)
                elif skin['Название'] == "M4A4 | 龍王 (Dragon King) (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.1513:
                            ratio = 92 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.1513, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1513, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1525:
                            ratio = 91 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.1525, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1525, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1538:
                            ratio = 90 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.1538, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1538, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1546:
                            ratio = 89 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.1546, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1546, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1556:
                            ratio = 88.4 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.1556, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1556, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1581:
                            ratio = 86.3 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.1581, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1581, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.16:
                            ratio = 85 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.16, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.16, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.163:
                            ratio = 83 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.163, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.163, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.167:
                            ratio = 78.6 / skin['Цена']
                            print(f"  Проверка условия 9: износ < 0.167, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.167, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для P250 | Muertos (Factory New)
                elif skin['Название'] == "P250 | Muertos (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.001:
                            ratio = 186 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.003:
                            ratio = 171 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0068:
                            ratio = 150 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)        
                        elif skin['Износ'] < 0.009:
                            ratio = 139 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0113:
                            ratio = 124.5 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)        
                        elif skin['Износ'] < 0.015:
                            ratio = 109 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.162:
                            ratio = 106 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.162, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.162, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1645:
                            ratio = 104 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.1645, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1645, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.166:
                            ratio = 102 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.166, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.166, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.1683:
                            ratio = 98 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.1683, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.1683, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для Desert Eagle | Crimson Web (Minimal Wear)
                elif skin['Название'] == "Desert Eagle | Crimson Web (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0733:
                            ratio = 500 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0733, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0733, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0777:
                            ratio = 433 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0777, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0777, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.081:
                            ratio = 399 / skin['Цена']     
                            print(f"  Проверка условия 3: износ < 0.081, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.081, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0825:
                            ratio = 381 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0825, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0825, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0866:
                            ratio = 340 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0866, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0866, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 310 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.09, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.09, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.092:
                            ratio = 290 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.092, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.092, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0933:
                            ratio = 277 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.0933, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0933, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для UMP-45 | Blaze (Factory New)
                elif skin['Название'] == "UMP-45 | Blaze (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.002:
                            ratio = 162 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0032:
                            ratio = 153 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0032, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0032, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.005:
                            ratio = 140 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.006:
                            ratio = 125 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.006, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.006, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0070:
                            ratio = 121 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0070, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0070, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)      
# Проверка выгодности для M4A1-S | Hyper Beast (Minimal Wear)
                elif skin['Название'] == "M4A1-S | Hyper Beast (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.081:
                            ratio = 425 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.081, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.081, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0823:
                            ratio = 415 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0823, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0823, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0845:
                            ratio = 400 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0845, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0845, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0855:
                            ratio = 390 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0855, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0855, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для AK-47 | Nightwish (Factory New)
                elif skin['Название'] == "AK-47 | Nightwish (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0015:
                            ratio = 485 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0027:
                            ratio = 463 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0027, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0027, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0038:
                            ratio = 452 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0038, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0038, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0046:
                            ratio = 446 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0046, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0046, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0065:
                            ratio = 437 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0065, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0065, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.008:
                            ratio = 430 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.008, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.008, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.01:
                            ratio = 430 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.01, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.01, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.012:
                            ratio = 422 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.012, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.012, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.014:
                            ratio = 415 / skin['Цена']
                            print(f"  Проверка условия 9: износ < 0.014, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.014, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.016:
                            ratio = 405 / skin['Цена']
                            print(f"  Проверка условия 10: износ < 0.016, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.016, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.018:
                            ratio = 400 / skin['Цена']
                            print(f"  Проверка условия 11: износ < 0.018, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.018, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для Desert Eagle | Conspiracy (Factory New)
                elif skin['Название'] == "Desert Eagle | Conspiracy (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0015:
                            ratio = 140 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0025:
                            ratio = 126 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0025, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0025, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0040:
                            ratio = 112 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.007:
                            ratio = 103 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.007, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.007, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0065:
                            ratio = 101 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0065, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0065, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.011:
                            ratio = 90 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.011, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.011, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.015:
                            ratio = 82 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.018:
                            ratio = 75 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.018, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.018, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для Glock-18 | Bullet Queen (Factory New)
                elif skin['Название'] == "Glock-18 | Bullet Queen (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0015:
                            ratio = 467 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0022:
                            ratio = 428 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0022, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0022, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0040:
                            ratio = 359 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.005:
                            ratio = 325 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0065:
                            ratio = 307 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0065, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0065, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для MAC-10 | Neon Rider (Factory New)
                elif skin['Название'] == "MAC-10 | Neon Rider (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0015:
                            ratio = 173 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0025:
                            ratio = 166 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0025, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0025, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0040:
                            ratio = 159 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})") 
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.005:
                            ratio = 158 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0065:
                            ratio = 152 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0065, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0065, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.011:
                            ratio = 132 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.011, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.011, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0135:
                            ratio = 123 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.0135, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0135, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0159:
                            ratio = 114 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.0159, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0159, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для USP-S | Printstream (Factory New)
                elif skin['Название'] == "USP-S | Printstream (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0015:
                            ratio = 1450 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.003:
                            ratio = 1393 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0045:
                            ratio = 1350 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0045, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0045, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.00599:
                            ratio = 1305 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.00599, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.00599, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.007:
                            ratio = 1275 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.007, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.007, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.009:
                            ratio = 1240 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для Glock-18 | Franklin (Factory New)
                elif skin['Название'] == "Glock-18 | Franklin (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.001:
                            ratio = 505 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.002:
                            ratio = 452 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.003:
                            ratio = 430 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0040:
                            ratio = 404 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.005:
                            ratio = 390 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0075:
                            ratio = 370 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.01:
                            ratio = 344 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.01, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.01, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для Desert Eagle | Printstream (Factory New)
                elif skin['Название'] == "Desert Eagle | Printstream (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0015:
                            ratio = 1116 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0025:
                            ratio = 1037 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0025, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0025, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0040:
                            ratio = 995 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.006:
                            ratio = 939 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.006, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.006, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0074:
                            ratio = 915 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0074, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0074, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.009:
                            ratio = 885 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.011:
                            ratio = 864 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.011, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.011, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0135:
                            ratio = 854 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.0135, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0135, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.016:
                            ratio = 832 / skin['Цена']
                            print(f"  Проверка условия 9: износ < 0.016, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.016, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.018:
                            ratio = 790 / skin['Цена']
                            print(f"  Проверка условия 10: износ < 0.018, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.018, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для StatTrak™ M4A1-S | Chantico's Fire (Factory New)
                elif skin['Название'] == "StatTrak™ M4A1-S | Chantico's Fire (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0033:
                            ratio = 3333 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0033, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0033, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0043:
                            ratio = 2887 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0043, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0043, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.015:
                            ratio = 2250 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.015, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.017:
                            ratio = 1180 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.017, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.017, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для M4A1-S | Control Panel (Factory New)
                elif skin['Название'] == "M4A1-S | Control Panel (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0021:
                            ratio = 367 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0021, ratio={ratio:.2f}")
                            if ratio > 1.18:
                                print(f"  Этот скин выгодный! (Износ < 0.0021, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0032:
                            ratio = 350 / skin['Цена']
                            print(f"  Проверка условия 2: ratio={ratio:.2f}")
                        if ratio > 1.15:
                            print(f"  Этот скин выгодный! (Износ < 0.168, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    elif skin['Износ'] < 0.004:
                        ratio = 328 / skin['Цена']
                        print(f"  Проверка условия 3: ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.171, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    elif skin['Износ'] < 0.006:
                        ratio = 313 / skin['Цена']
                        print(f"  Проверка условия 4: ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.175, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    elif skin['Износ'] < 0.0088:
                        ratio = 300 / skin['Цена']
                        print(f"  Проверка условия 5: ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.18, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                            # Проверка выгодности для P90 | Cold Blooded (Factory New)
                elif skin['Название'] == "P90 | Cold Blooded (Factory New)":
                 if skin['Износ'] is not None and skin['Цена'] is not None:
                    if skin['Износ'] < 0.002:
                        ratio = 562 / skin['Цена']
                        print(f"  Проверка условия 1: ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.16, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    elif skin['Износ'] < 0.0038:
                        ratio = 544 / skin['Цена']
                        print(f"  Проверка условия 2: ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.168, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    elif skin['Износ'] < 0.0053:
                        ratio = 505 / skin['Цена']
                        print(f"  Проверка условия 3: ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.171, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    elif skin['Износ'] < 0.0066:
                        print(f"  Проверка условия 4: ratio={ratio:.2f}")
                        ratio = 480 / skin['Цена']
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.175, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    elif skin['Износ'] < 0.0088:
                        ratio = 457 / skin['Цена']
                        print(f"  Проверка условия 5: ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.18, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    elif skin['Износ'] < 0.012:
                        ratio = 427 / skin['Цена']
                        print(f"  Проверка условия 6: ratio={ratio:.2f}")
                        if ratio > 1.18:
                            print(f"  Этот скин выгодный! (Износ < 0.187, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)                                                                                                              
        except json.JSONDecodeError:
            print(f"⚠️ Ошибка: сервер вернул не JSON! Текст ответа:\n{response.text[:500]}")
        except Exception as e:
            print(f"❌ Ошибка при обработке {url}: {e}")

    # Выводим список всех выгодных скинов
    print("\nСписок всех выгодных скинов:")
    for i, skin in enumerate(выгода, 1):
        print(f"Скин #{i}:")
        print(f"  Название: {skin['Название']}")
        print(f"  Износ: {skin['Износ']}")
        print(f"  Цена: {skin['Цена'] if skin['Цена'] is not None else 'Цена не найдена'}")
        if 'ratio' in skin:
            print(f"  Выгода (ratio): {skin['ratio']:.2f}")
        else:
            print("  Выгода (ratio): не рассчитана")

# Запуск функции сбора данных
collect_data()
        # Функция для запуска скрипта и получения вывода
def run_script():
    try:
        result = subprocess.run(['python3', '1variant.py'], capture_output=True, text=True, timeout=300)
        return result.stdout if result.stdout else "Скрипт завершился без вывода."
    except subprocess.TimeoutExpired:
        return "Ошибка: скрипт выполнялся слишком долго и был остановлен."
    except Exception as e:
        return f"Ошибка при запуске скрипта: {e}"