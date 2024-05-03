from venv import logger 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
from get_24 import get_company_name_24, get_title_24, get_headquater_24, get_Description_24, get_Requirement_24, get_Right_24, get_Deadline_24, get_Salary_24, get_Place_24, get_Level_24, get_Way_24, get_SrcPic_24, get_DateSubmit_24, get_CompanyPlace_24, get_CompanyScale_24

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
    
def get_profile_info_24(driver, url):
    try:
        driver.get(url)
        sleep(2)
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        company_name = get_company_name_24(page_source)
        title = get_title_24(page_source)
        headquater = get_headquater_24(page_source)
        description = get_Description_24(page_source)
        requirement = get_Requirement_24(page_source)
        right = get_Right_24(page_source)
        deadline = get_Deadline_24(page_source)
        salary = get_Salary_24(page_source)
        place = get_Place_24(page_source)
        level = get_Level_24(page_source)
        way = get_Way_24(page_source)
        srcpic = get_SrcPic_24(page_source)
        datesub = get_DateSubmit_24(page_source) 
        company_place = get_CompanyPlace_24(page_source) 
        company_scale = get_CompanyScale_24(page_source) 
        # company_review = get_CompanyReview_24(page_source)
        return [title, company_name, salary, datesub, deadline, place, way, level, description, requirement, right, headquater, srcpic, company_place, company_scale]
    except Exception as e:
        logger.error(f"Error occurred while scraping data from {url}: {e}")
        return []
    
def is_duplicated(info, data):
    for i in data:
        if all(info[j] == i[j] for j in range(len(info))):
            return True
    return False


def get_vieclam24(driver):
    try:
        url = 'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?page=1&sort_q='
        driver.get(url)
        sleep(2)
        profile_urls = get_profile_urls_24(driver, url)
        data = []
        for i in profile_urls:
            info = get_profile_info_24(driver, i)
            print('>> Vieclam24:', info)
            if info:
                data.append(info)
        return data
    except Exception as e:
        print(f"Error occurred while get data 24h: {e}")
        return []
