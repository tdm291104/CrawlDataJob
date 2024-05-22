from venv import logger 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
from get_24 import get_CompanyinfoPalce_24, get_CompanyinfoName_24, get_CompanyindoGT_24, get_CompanyinfoQuyMO_24

def get_profile_urls_24(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        class_name = 'relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white !bg-[#FFF5E7] border-se-blue-10'
        a = page_source.find_all('a', class_=class_name)
        all_profile_urls = []
        for profile in a:
            profile_url = 'https://vieclam24h.vn' + profile.get('href')
            if profile_url not in all_profile_urls:
                all_profile_urls.append(profile_url)
        return all_profile_urls
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from {url}: {e}")
        return []
    

def get_profilecompany_urls_24(driver, url):
    try:
        driver.get(url)
        sleep(2)
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        class_name = 'md:ml-7 w-full'
        div = page_source.find_all('div', class_=class_name)
        a = div[0].find('a')
        profile_url = 'https://vieclam24h.vn' + a.get('href')
        return profile_url
    except Exception as e:
        logger.error(f"Error occurred while extracting profile company URLs from {url}: {e}")
        return []    
    
def get_profilecompany_info_24(driver, url):
    try:
        driver.get(url)
        sleep(2)
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        namecompany = get_CompanyinfoName_24(page_source)
        gt = get_CompanyindoGT_24(page_source)
        dc = get_CompanyinfoPalce_24(page_source)
        qm = get_CompanyinfoQuyMO_24(page_source)

        return [namecompany, gt, dc, qm]
    except Exception as e:
        logger.error(f"Error occurred while scraping data from {url}: {e}")
        return []

def remove_duplicate_data(new_data, all_old_data):
    unique_data = []
    for new_item in new_data:
        duplicate = False
        for old_data in all_old_data:
            if new_item in old_data:
                duplicate = True
                break
        if not duplicate:
            unique_data.append(new_item)
    return unique_data

def get_congty24(driver):
    try:
        url = 'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?page=1&sort_q='
        driver.get(url)
        sleep(2)
        profile_urls = get_profile_urls_24(driver, url)
        data = []
        for i in profile_urls:
            profilecompany_urls = get_profilecompany_urls_24(driver, i)
            info = get_profilecompany_info_24(driver, profilecompany_urls)
            print('>> Vieclam24_Congty:', info)
            if info:
                data.append(info)
        return data
    except Exception as e:
        print(f"Error occurred while get data 24h: {e}")
        return []
