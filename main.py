import csv
from venv import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from Get_jobinfo import get_vieclam24
from Get_companyinfo import get_congty24
import mysql.connector
import datetime
from csv_mysql import csv_mysql

def save_crawl_time(crawl_time):
    with open('crawl_times.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['CrawlTime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({'CrawlTime': crawl_time})

def save_data_toJob_csv(data):
    existing_data = read_existingJob_data()  # Read existing data from CSV
    new_data, duplicates  = filter_new_data(data, existing_data)

    if new_data:
        with open('job_listings.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title', 'Company_Name', 'Salary', 'DateSub', 'Deadline', 'Place', 'Way', 'Level', 'Description', 'Requirement', 'Rights', 'Headquater', 'Srcpic', 'Company_Place', 'Company_Scale']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            for item in new_data:
                writer.writerow({field: item[i] for i, field in enumerate(fieldnames)})
    if duplicates:
        print("Warning: Duplicate data encountered. The following entries were not saved:")
        for duplicate in duplicates:
            print(duplicate['Title'])

def save_dataCompany_to_csv(data):
    existing_data = read_existingCompany_data()  # Read existing data from CSV
    new_data, duplicates  = filter_new_data(data, existing_data)

    if new_data:
        with open('company_listings.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'GT', 'DC', 'QM']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()    
            for item in new_data:
                writer.writerow({field: item[i] for i, field in enumerate(fieldnames)})
    if duplicates:
        print("Warning: Duplicate data encountered. The following entries were not saved:")
        for duplicate in duplicates:
            print(duplicate['Name'])  # Print the names of duplicate entries    

def read_existingJob_data():
    try:
        with open('job_listings.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_data = [row for row in reader]
        return existing_data
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist

def read_existingCompany_data():
    try:
        with open('company_listings.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_data = [row for row in reader]
        return existing_data
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist

def filter_new_data(new_data, existing_data):
    new_entries = []
    duplicates = []
    for new_item in new_data:
        is_duplicate = False
        for existing_item in existing_data:
            if new_item == existing_item:  # Check if the new item matches any existing item
                duplicates.append(new_item)
                is_duplicate = True
                break
        if not is_duplicate:
            new_entries.append(new_item)
    return new_entries, duplicates


def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    try:
        with webdriver.Chrome(options=chrome_options) as driver:
            start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = get_vieclam24(driver)  # Chỉ truyền driver vào hàm
            data1 = get_congty24(driver)
            end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data_toJob_csv(data)
            save_dataCompany_to_csv(data1)
            save_crawl_time(start_time + " - " + end_time)
            csv_mysql()

    except Exception as e:
        logger.error(f"Error occurred while scraping data: {e}")
    print('>> Done')

if __name__ == '__main__':
    main()







# def save_data_to_mysql(data):
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="123456",
#             database="job"
#         )

#         cursor = connection.cursor()

#         sql = "INSERT INTO job_listings (Title, Company_Name, Salary, DateSub, Deadline, Place, Way, Level, Description, Requirement, Rights, Headquater, Srcpic, Company_Place, Company_Scale) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
#         for item in data:
#             cursor.execute(sql, item)

#         connection.commit()
#         print("Data inserted successfully into MySQL database")
#     except mysql.connector.Error as error:
#         print(f"Error occurred while inserting data into MySQL database: {error}")
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")