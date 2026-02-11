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



chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")


ua = UserAgent()


headers = {
    'User-Agent': ua.random,
    'Cookie':  'Device-id=rdvBY8LpiMek9eAtSTxW; Locale-Supported=ru; game=csgo; session=1-WWbewILiBp0AHK7LmTnuqW5eRqtdH5SkBuRLFbMTCSZQ2037676197; csrf_token=IjcxZGVlOWVhZGVlOWUxZjFiNjEyYjEzMDAzMDgwMDQyZjAwNGQwY2Ii.aYiJwg.KVghv2wVDmxajgGQF8aYqLwWO68',
}

def collect_data():
    urls = [
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=779243&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1770379375047',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=779243&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.033&_=1770379375047',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=34699&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1770382358600',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=34699&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.02&_=1770382358600',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=779263&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1770382732872',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=779263&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.02&_=1770382732872',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115935&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1770385663817',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115935&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.022&_=1770385663817',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115935&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.003&_=1770385663817',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=42201&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.008&_=1770402275972',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116198&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1770402919871',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116198&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.005&_=1770402919871',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=956587&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1770403011274',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=956587&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.02&_=1770403011274',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=956587&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.0051&_=1770403011274',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=956587&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.01&_=1770403011274',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=956587&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.015&_=1770403011274',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=956587&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.00&max_paintwear=0.023&_=1770403011274',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968244&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770404803702',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968244&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770404803702',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968244&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770404803702',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968244&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.099&_=1770404803702',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=921527&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770405407742',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=921527&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770405407742',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=921527&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.099&_=1770405407742',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=781643&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770448943698',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=781643&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770448943698',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968125&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770450192724',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968125&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770450192724',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968125&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.099&_=1770450192724',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968125&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.11&_=1770450192724',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115675&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770451511444',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115675&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770451511444',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115675&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770451511444',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115675&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770451511444',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115675&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.099&_=1770451511444',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115675&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.011&_=1770451511444',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115675&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.012&_=1770451511444',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116168&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770457754664',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116168&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770457754664',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116168&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770457754664',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116168&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.095&_=1770457754664',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968043&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770458044268',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968043&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770458044268',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968043&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770458044268',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968043&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770458044268',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968043&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.095&_=1770458044268',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968043&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.099&_=1770458044268',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968043&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.11&_=1770458044268',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116077&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770459220193',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116077&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770459220193',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116077&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770459220193',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116077&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.099&_=1770459220193',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1116077&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.11&_=1770459220193',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968134&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770465613535',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968134&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770465613535',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968134&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770465613535',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968134&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770465613535',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968134&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.099&_=1770465613535',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968134&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.11&_=1770465613535',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115995&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770467870706',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115995&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770467870706',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115995&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770467870706',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=1115995&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770467870706',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968278&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770468378122',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968278&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770468378122',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968278&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770468378122',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=968278&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770468378122',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=773778&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770469520048',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=773778&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770469520048',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=773778&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770469520048',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=900615&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770470100364',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=900615&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770470100364',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=900615&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770470100364',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=900615&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770470100364',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=900615&page_num=2&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.099&_=1770470100364',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=857611&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.075&_=1770470552867',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=857611&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.08&_=1770470552867',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=857611&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.085&_=1770470552867',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=857611&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.09&_=1770470552867',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=857611&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.095&_=1770470552867',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=857611&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.07&max_paintwear=0.0999&_=1770470552867',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=45412&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.18&_=1770475065756',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=45412&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.21&_=1770475065756',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=45412&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.24&_=1770475065756',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=45432&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.18&_=1770475689023',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=45432&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.21&_=1770475689023',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=45432&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.24&_=1770475689023',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=835781&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.18&_=1770476434657',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=835781&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.21&_=1770476434657',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=835781&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.24&_=1770476434657',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=836015&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.18&_=1770477026190',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=836015&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.21&_=1770477026190',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=836015&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.24&_=1770477026190',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=835874&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.18&_=1770477450620',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=835874&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.21&_=1770477450620',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=835874&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.24&_=1770477450620',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=33960&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.18&_=1770478429183',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=33960&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.21&_=1770478429183',
        'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=33960&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&min_paintwear=0.15&max_paintwear=0.24&_=1770478429183',
        # '',
        # '',
        # '',
        # '',
        # '',
        # '',
        
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

                # Проверка выгодности для MAG-7 | Justice (Factory New)
                if skin['Название'] == "MAG-7 | Justice (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0075:
                           ratio = 507 / skin['Цена']
                           print(f"  Проверка условия 1: износ < 0.1509, ratio={ratio:.2f}")
                           if ratio > 1.24:
                              print(f"  Этот скин выгодный! (Износ < 0.1509, ratio = {ratio:.2f})")
                              skin["ratio"] = ratio
                              выгода.append(skin)
                    if skin['Износ'] < 0.011:
                       ratio = 455 / skin['Цена']
                       print(f"  Проверка условия 2: износ < 0.1524, ratio={ratio:.2f}")
                       if ratio > 1.24:
                          print(f"  Этот скин выгодный! (Износ < 0.1524, ratio = {ratio:.2f})")
                          skin["ratio"] = ratio
                          выгода.append(skin)
                    if skin['Износ'] < 0.015:
                        ratio = 422 / skin['Цена']
                        print(f"  Проверка условия 3, ratio={ratio:.2f}")
                        if ratio > 1.24:
                            print(f"  Этот скин выгодный! (Износ < 0.1544, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    if skin['Износ'] < 0.018:
                        ratio = 392 / skin['Цена']
                        print(f"  Проверка условия 4, ratio={ratio:.2f}")
                        if ratio > 1.24:
                            print(f"  Этот скин выгодный! (Износ < 0.1555, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    if skin['Износ'] < 0.022:
                        ratio = 373 / skin['Цена']
                        print(f"  Проверка условия 5, ratio={ratio:.2f}")
                        if ratio > 1.24:
                            print(f"  Этот скин выгодный! (Износ < 0.1568, ratio = {ratio:.2f})")
                            skin["ratio"] = ratio
                            выгода.append(skin)
                    # if skin['Износ'] < 0.1578:
                    #     ratio = 36.9 / skin['Цена']
                    #     print(f"  Проверка условия 6, ratio={ratio:.2f}")
                    #     if ratio > 1.24:
                    #         print(f"  Этот скин выгодный! (Износ < 0.1578, ratio = {ratio:.2f})")
                    #         skin["ratio"] = ratio
                    #         выгода.append(skin)

                # Проверка выгодности для FAMAS | Valence (Factory New)
                elif skin['Название'] == "FAMAS | Valence (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.002:
                            ratio = 438 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.159, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.159, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0043:
                            ratio = 351 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.1649, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1649, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.006:
                            ratio = 338 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.168, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.168, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.011:
                            ratio = 315 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.171, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.171, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.017:
                            ratio = 300 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.17, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.17, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        
                # Проверка выгодности для MAC-10 | Disco Tech (Factory New)
                elif skin['Название'] == "MAC-10 | Disco Tech (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.001:
                            ratio = 605 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.1513, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1513, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.003:
                            ratio = 538 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.1525, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1525, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.005:
                            ratio = 508 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.1538, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1538, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.009:
                            ratio = 480 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.1546, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1546, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.011:
                            ratio = 468 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.1556, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1556, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0135:
                            ratio = 454 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.1581, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1581, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.017:
                            ratio = 450 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.16, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.16, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)


                # Проверка выгодности для Glock-18 | Shinobu (Factory New)
                elif skin['Название'] == "Glock-18 | Shinobu (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.001:
                            ratio = 600 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0024:
                            ratio = 560 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0032:
                            ratio = 533 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)        
                        elif skin['Износ'] < 0.0047:
                            ratio = 502 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0062:
                            ratio = 481 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)        
                        elif skin['Износ'] < 0.0085:
                            ratio = 451 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.015, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.01:
                            ratio = 440 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.162, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.162, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0124:
                            ratio = 418 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.1645, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1645, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0144:
                            ratio = 408 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.166, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.166, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0162:
                            ratio = 400 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.1683, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1683, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.02:
                            ratio = 380 / skin['Цена']
                            print(f"  Проверка условия 8: износ < 0.1683, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.1683, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)        

                # Проверка выгодности для USP-S | Orion (Factory New)
                elif skin['Название'] == "USP-S | Orion (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.001:
                            ratio = 3710 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0733, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0733, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0022:
                            ratio = 3200 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0777, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0777, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0042:
                            ratio = 2777 / skin['Цена']     
                            print(f"  Проверка условия 3: износ < 0.081, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.081, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.005:
                            ratio = 2700 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0825, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0825, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0066:
                            ratio = 2540 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0866, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0866, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        
                # Проверка выгодности для P2000 | Royal Baroque (Factory New)
                elif skin['Название'] == "P2000 | Royal Baroque (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.0022:
                            ratio = 35 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0032:
                            ratio = 32.55 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0032, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0032, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0044:
                            ratio = 31 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.01:
                            ratio = 28 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.006, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.006, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)  

                # Проверка выгодности для USP-S | Jawbreaker (Factory New)
                elif skin['Название'] == "USP-S | Jawbreaker (Factory New)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.01:
                            ratio = 372 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0126:
                            ratio = 340 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0027, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0027, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0141:
                            ratio = 328 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0038, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0038, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.018:
                            ratio = 303 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0046, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0046, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.023:
                            ratio = 280 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0065, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0065, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                       
                # Проверка выгодности для MP9 | Arctic Tri-Tone (Minimal Wear)
                elif skin['Название'] == "MP9 | Arctic Tri-Tone (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 75.3 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 71 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0025, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0025, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 66 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 60.5 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.007, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.007, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.095:
                            ratio = 55.4 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.0065, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0065, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для M4A4 | Temukau (Minimal Wear)
                elif skin['Название'] == "M4A4 | Temukau (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 680 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 654 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0022, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0022, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 636 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 614 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                # Проверка выгодности для XM1014 | Entombed (Minimal Wear)
                elif skin['Название'] == "XM1014 | Entombed (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 38.6 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 36.8 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.0025, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0025, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 35.5 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})") 
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 34 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                                
                # Проверка выгодности для UMP-45 | Crimson Foil (Minimal Wear)
                elif skin['Название'] == "UMP-45 | Crimson Foil (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 82.2 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.0015, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0015, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 77.6 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 74 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.0045, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0045, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 70 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.00599, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.00599, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.099:
                            ratio = 62 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.007, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.007, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.11:
                            ratio = 55 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.009, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.009, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для MAC-10 | Derailment (Minimal Wear)
                elif skin['Название'] == "MAC-10 | Derailment (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 127.2 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 122.2 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 118 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 112 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.95:
                            ratio = 107 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.099:
                            ratio = 99 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.011:
                            ratio = 93 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.01, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.01, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0199:
                            ratio = 81 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.01, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.01, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)        
                                
                # Проверка выгодности для USP-S | Bleeding Edge (Minimal Wear)
                elif skin['Название'] == "USP-S | Bleeding Edge (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 78 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 71.2 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 63 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 58.5 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                          
                # Проверка выгодности для AUG | Eye of Zapems (Minimal Wear)
                elif skin['Название'] == "AUG | Eye of Zapems (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 110 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 104 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 98 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 92 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.095:
                            ratio = 87 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.099:
                            ratio = 80 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.11:
                            ratio = 65 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.01, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.01, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                
                # Проверка выгодности для Glock-18 | Glockingbird (Minimal Wear)
                elif skin['Название'] == "Glock-18 | Glockingbird (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 67.8 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 60 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 56 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 52 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.095:
                            ratio = 49 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0999:
                            ratio = 45.4 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                                
                # Проверка выгодности для Dual Berettas | Sweet Little Angels (Minimal Wear)
                elif skin['Название'] == "Dual Berettas | Sweet Little Angels (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 102 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 95 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 91 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 85.5 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.95:
                            ratio = 81 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0999:
                            ratio = 76 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                                
                elif skin['Название'] == "MP7 | Bloodsport (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 536 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 521 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 494 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 475 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.95:
                            ratio = 447 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0999:
                            ratio = 425 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.011:
                            ratio = 395 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.01, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.01, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)        
                                    # Проверка выгодности для Dual Berettas | Sweet Little Angels (Minimal Wear)
                elif skin['Название'] == "Dual Berettas | Sweet Little Angels (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 102 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 95 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 91 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 85.5 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.95:
                            ratio = 81 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0999:
                            ratio = 76 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                     # Проверка выгодности для Dual Berettas | Sweet Little Angels (Minimal Wear)
                elif skin['Название'] == "Dual Berettas | Sweet Little Angels (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 96 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 88 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 80 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 75 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                 # Проверка выгодности для M4A1-S | Glitched Paint (Minimal Wear)
                elif skin['Название'] == "M4A1-S | Glitched Paint (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 92 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 83.7 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 77 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 69 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.95:
                            ratio = 81 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)

                # Проверка выгодности для P90 | Attack Vector (Minimal Wear)
                elif skin['Название'] == "P90 | Attack Vector (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 180 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 172 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 166 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 162 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.95:
                            ratio = 157 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0999:
                            ratio = 154 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
               
                # Проверка выгодности для StatTrak™ P90 | Nostalgia (Minimal Wear)
                elif skin['Название'] == "StatTrak™ P90 | Nostalgia (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 140 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 135/ skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 132 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        # elif skin['Износ'] < 0.09:
                        #     ratio = 136 / skin['Цена']
                        #     print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                        #     if ratio > 1.24:
                        #         print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                        #         skin["ratio"] = ratio
                        #         выгода.append(skin)
                        
                        
                        
                                    # Проверка выгодности для P250 | Epicenter (Minimal Wear)
                elif skin['Название'] == "P250 | Epicenter (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 190 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 181 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 171 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 160 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.095:
                            ratio = 150 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0999:
                            ratio = 140 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.11:
                            ratio = 121 / skin['Цена']
                            print(f"  Проверка условия 7: износ < 0.01, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.01, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin) 
                # Проверка выгодности для USP-S | Printstream (Minimal Wear)
                elif skin['Название'] == "USP-S | Printstream (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 654 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 600 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 582 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 570 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.95:
                            ratio = 557 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0999:
                            ratio = 540 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                # Проверка выгодности для M4A4 | In Living Color (Minimal Wear)
                elif skin['Название'] == "M4A4 | In Living Color (Minimal Wear)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.075:
                            ratio = 571 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.08:
                            ratio = 548 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.085:
                            ratio = 538 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.09:
                            ratio = 527 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.95:
                            ratio = 511 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.0999:
                            ratio = 496 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)         
                # ★ Specialist Gloves | Crimson Web (Field-Tested)
                elif skin['Название'] == "★ Specialist Gloves | Crimson Web (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.16:
                            ratio = 1955 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.17:
                            ratio = 1875 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.18:
                            ratio = 1785 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.19:
                            ratio = 1710 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.20:
                            ratio = 1630 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.21:
                            ratio = 1553 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)                               
                        elif skin['Износ'] < 0.22:
                            ratio = 1470 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.23:
                            ratio = 1390 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.24:
                            ratio = 1310 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)     
                                
                                # ★ ★ Moto Gloves | POW! (Field-Tested)
                elif skin['Название'] == "★ ★ Moto Gloves | POW! (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.16:
                            ratio = 1377 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.17:
                            ratio = 1307 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.18:
                            ratio = 1242 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.19:
                            ratio = 1192 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.20:
                            ratio = 1116 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.21:
                            ratio = 1064 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)                               
                        elif skin['Износ'] < 0.22:
                            ratio = 971 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                # ★ Driver Gloves | Black Tie (Field-Tested)
                elif skin['Название'] == "★ Driver Gloves | Black Tie (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.16:
                            ratio = 2045 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.17:
                            ratio = 1963 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.18:
                            ratio = 1900 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.19:
                            ratio = 1824 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.20:
                            ratio = 1740 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.21:
                            ratio = 1664 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)                               
                        elif skin['Износ'] < 0.22:
                            ratio = 1599 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.23:
                            ratio = 1526 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.24:
                            ratio = 1451 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)    
                 # ★ ★ Specialist Gloves | Field Agent (Field-Tested)
                elif skin['Название'] == "★ Specialist Gloves | Field Agent (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.16:
                            ratio = 2056 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.17:
                            ratio = 1963 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.18:
                            ratio = 1900 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.19:
                            ratio = 1824 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.20:
                            ratio = 1787 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.21:
                            ratio = 1600 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)                               
                        elif skin['Износ'] < 0.22:
                            ratio = 1500 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.23:
                            ratio = 1400 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.24:
                            ratio = 1300 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)  
                                
                # ★ Driver Gloves | Snow Leopard (Field-Tested)
                elif skin['Название'] == "★ Driver Gloves | Snow Leopard (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.16:
                            ratio = 3850 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.17:
                            ratio = 3733 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.18:
                            ratio = 3600 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.19:
                            ratio = 3500 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.20:
                            ratio = 3366 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.21:
                            ratio = 3273 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)                               
                        elif skin['Износ'] < 0.22:
                            ratio = 3161 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.23:
                            ratio = 3051 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.24:
                            ratio = 2947 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)                  
                                
                                # ★ AK-47 | Redline (Field-Tested)
                elif skin['Название'] == "AK-47 | Redline (Field-Tested)":
                    if skin['Износ'] is not None and skin['Цена'] is not None:
                        print(f"Проверка скина {skin['Название']}: износ={skin['Износ']}, цена={skin['Цена']}")
                        if skin['Износ'] < 0.16:
                            ratio = 444 / skin['Цена']
                            print(f"  Проверка условия 1: износ < 0.001, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.001, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.17:
                            ratio = 431 / skin['Цена']
                            print(f"  Проверка условия 2: износ < 0.002, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.002, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.18:
                            ratio = 410 / skin['Цена']
                            print(f"  Проверка условия 3: износ < 0.003, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.003, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.19:
                            ratio = 385 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.20:
                            ratio = 362 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.21:
                            ratio = 338 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)                               
                        elif skin['Износ'] < 0.22:
                            ratio = 318 / skin['Цена']
                            print(f"  Проверка условия 4: износ < 0.0040, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0040, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.23:
                            ratio = 296 / skin['Цена']
                            print(f"  Проверка условия 5: износ < 0.005, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.005, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)
                        elif skin['Износ'] < 0.24:
                            ratio = 280 / skin['Цена']
                            print(f"  Проверка условия 6: износ < 0.0075, ratio={ratio:.2f}")
                            if ratio > 1.24:
                                print(f"  Этот скин выгодный! (Износ < 0.0075, ratio = {ratio:.2f})")
                                skin["ratio"] = ratio
                                выгода.append(skin)                      
                                
                                
                                
                                                               
        except json.JSONDecodeError:
            print(f"⚠️ Ошибка: сервер вернул не JSON! Текст ответа:\n{response.text[:500]}")
        except Exception as e:
            print(f"❌ Ошибка при обработке {url}: {e}")

    
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


collect_data()
        
def run_script():
    try:
        result = subprocess.run(['python3', '1variant.py'], capture_output=True, text=True, timeout=300)
        return result.stdout if result.stdout else "Скрипт завершился без вывода."
    except subprocess.TimeoutExpired:
        return "Ошибка: скрипт выполнялся слишком долго и был остановлен."
    except Exception as e:
        return f"Ошибка при запуске скрипта: {e}"
