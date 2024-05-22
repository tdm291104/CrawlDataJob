import csv
import mysql.connector

def csv_mysql():
    # Kết nối tới cơ sở dữ liệu MySQL
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="job"
    )
    cursor = db_connection.cursor()

    # Đường dẫn tới file CSV
    csv_file_path = "job_listings.csv"

    # Mở file CSV và đọc dữ liệu
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Bỏ qua dòng tiêu đề nếu có
        # Chèn dữ liệu vào cơ sở dữ liệu MySQL
        for row in csvreader:
            sql = "INSERT INTO job_listings (Title, Company_Name, Salary, DateSub, Deadline, Place, Way, Level, Description, Requirement, Rights, Headquater, Srcpic, Company_Place, Company_Scale) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = tuple(row)
            cursor.execute(sql, values)

    # Lưu các thay đổi và đóng kết nối
    db_connection.commit()
    cursor.close()
    db_connection.close()