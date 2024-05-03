import csv
from venv import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from Get_jobinfo import get_vieclam24
import mysql.connector

# def save_data_to_csv(data):
#     with open('job_listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['Title', 'Company_Name', 'Salary', 'DateSub', 'Deadline', 'Place', 'Way', 'Level', 'Description', 'Requirement', 'Right', 'Headquater', 'Srcpic', 'Company_Place', 'Company_Scale', 'Company_Review']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for item in data:
#             writer.writerow({field: item[i] for i, field in enumerate(fieldnames)})

def save_data_to_mysql(data):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="job"
        )

        cursor = connection.cursor()

        sql = "INSERT INTO job_listings (Title, Company_Name, Salary, DateSub, Deadline, Place, Way, Level, Description, Requirement, Rights, Headquater, Srcpic, Company_Place, Company_Scale) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        for item in data:
            cursor.execute(sql, item)

        connection.commit()
        print("Data inserted successfully into MySQL database")
    except mysql.connector.Error as error:
        print(f"Error occurred while inserting data into MySQL database: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    try:
        with webdriver.Chrome(options=chrome_options) as driver:
            data = get_vieclam24(driver)  # Chỉ truyền driver vào hàm
            save_data_to_mysql(data)
    except Exception as e:
        logger.error(f"Error occurred while scraping data: {e}")
    print('>> Done')

if __name__ == '__main__':
    main()
