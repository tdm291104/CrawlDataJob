from venv import logger
def get_company_name_24(source):
    return source.find('h2', class_='font-normal text-16 text-se-neutral-64 mb-4').get_text(' ', strip=True)

def get_title_24(source):
    return source.find('h1', class_='font-semibold text-18 md:text-24 leading-snug').get_text(' ', strip=True)

def get_Salary_24(source):
    return source.find('p', class_='font-semibold text-14 text-[#8B5CF6]').get_text(' ', strip=True)

def get_DateSubmit_24(source):
    div = source.find_all('div', class_ = 'jsx-d84db6a84feb175e md:flex md:border-b border-[#DDD6FE] mb-4')
    datesub = div[0].find('div',class_ = 'flex items-center mb-4 md:w-[33%]').find('p', class_ = 'text-14').get_text(' ',strip = True)
    return datesub  

def get_Deadline_24(source):
    h2 = source.find_all('h2', class_ ='ml-3 text-14 md:flex pt-0 md:pt-[5px] my-0')
    dl = h2[1].find_all('p')
    return dl[1].get_text(' ',strip=True)

def get_Place_24(source):
    h2 = source.find_all('h2', class_ ='ml-3 text-14 md:flex pt-0 md:pt-[5px] my-0')
    place = h2[2].find_all('p')
    return place[1].get_text(' ',strip=True)

def get_Way_24(source):
    div = source.find_all('div', class_ = 'jsx-d84db6a84feb175e md:flex md:border-b border-[#DDD6FE] mb-4')
    way = div[1].find('div',class_ = 'flex items-center mb-4 md:w-[33%]').find('p', class_ = 'text-14').get_text(' ',strip = True)
    return way  

def get_Level_24(source):
    div = source.find_all('div', class_ = 'jsx-d84db6a84feb175e md:flex md:border-b border-[#DDD6FE] mb-4')
    divv = div[2].find_all('div', class_ = 'flex items-center mb-4 w-full md:w-[33%]')
    if len(div[2].find_all('div', class_ = 'flex items-center mb-4 w-full md:w-[33%]')) == 2:
        level = divv[1].find_all('p', class_ = 'text-14')
        return level[0].get_text(' ',strip=True)
    elif len(div[2].find_all('div', class_ = 'flex items-center mb-4 w-full md:w-[33%]')) == 3:
        level = divv[2].find_all('p', class_ = 'text-14')
        return level[0].get_text(' ',strip=True)

def get_Description_24(source):
    div = source.find_all('div', class_ = 'jsx-d84db6a84feb175e mb-2 text-14 break-words text-se-neutral-80 text-description')
    return div[0].get_text(' ', strip=True)

def get_Requirement_24(source):
    div = source.find_all('div', class_ = 'jsx-d84db6a84feb175e mb-2 text-14 break-words text-se-neutral-80 text-description')
    return div[1].get_text(' ', strip=True)

def get_Right_24(source):
    div = source.find_all('div', class_ = 'jsx-d84db6a84feb175e mb-2 text-14 break-words text-se-neutral-80 text-description')
    return div[2].get_text(' ', strip=True)

def get_headquater_24(source):
    div = source.find_all('div', class_ ='text-14 text-se-grey-48 font-semibold')
    return div[0].get_text(' ',strip=True)

def get_SrcPic_24(source):
    div = source.find('div', class_ ='md:flex w-full items-start')
    return div.find('img').get('src')

def get_CompanyPlace_24(source):
    div = source.find_all('div', class_ = 'text-14 text-se-grey-48 font-semibold')
    return div[0].get_text(' ', strip=True)

def get_CompanyScale_24(source):
    div = source.find_all('div', class_ = 'text-14 text-se-grey-48 font-semibold')
    return div[1].get_text(' ', strip=True)

def get_CompanyReview_24(source):
    div = source.find('div', class_ = 'max-h-[84px] overflow-hidden mt-4 text-14 text-se-neutral-84 mb-2')
    return div.get_text(' ', strip=True)

def get_CompanyinfoPalce_24(soure):
    div = soure.find_all('div', class_ = 'max-w-[68%] text-se-neutral-100-n font-light sm:max-w-[68%] md:max-w-[70%] lg:max-w-[76%]')
    return div[0].get_text(' ', strip=True)

def get_CompanyinfoQuyMO_24(soure):
    div = soure.find_all('div', class_ = 'max-w-[68%] text-se-neutral-100-n font-light sm:max-w-[68%] md:max-w-[70%] lg:max-w-[76%]')
    return div[1].get_text(' ', strip=True)

def get_CompanyindoGT_24(soure):
    div =  soure.find('div', class_ = 'mb-12 px-4 sm:px-0')
    divs = div.find_all('div', class_ = 'text-base break-words text-se-neutral-80 font-light BoxIntroduction_contentIntroductionShow__c7ck2')
    return divs[0].get_text(' ', strip = True)

def get_CompanyinfoName_24(soure):
    div = soure.find('div', class_ = 'text-center mb-2 max-w-[99%] xs:max-w-full sm:text-left sm:max-w-[85%]')
    return div.get_text(' ', strip=True)



    
    
    





    