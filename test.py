import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="job"
    )
    if connection.is_connected():
        print("Kết nối thành công đến cơ sở dữ liệu MySQL trên XAMPP.")

        # Tạo một con trỏ để thực hiện các truy vấn SQL
        cursor = connection.cursor()

        # Lệnh tạo bảng job
        job_table_sql = """
        CREATE TABLE IF NOT EXISTS jobtable (
            JobID INT AUTO_INCREMENT PRIMARY KEY,
            Title VARCHAR(255),
            CompanyID INT,
            Salary VARCHAR(255),
            DateSub DATE,
            Deadline DATE,
            Place VARCHAR(255),
            Way VARCHAR(255),
            Level VARCHAR(255),
            Description TEXT,
            Requirement TEXT,
            Rights TEXT,
            Headquater VARCHAR(255),
            Srcpic VARCHAR(255)
        )
        """
        # Lệnh tạo bảng company
        company_table_sql = """
        CREATE TABLE IF NOT EXISTS companytable (
            CompanyID INT AUTO_INCREMENT PRIMARY KEY,
            CompanyName VARCHAR(255),
            CompanyPlace VARCHAR(255),
            CompanyScale VARCHAR(255),
            CompanyReview VARCHAR(255)
        )
        """
        cursor.execute(job_table_sql)
        cursor.execute(company_table_sql)
        print("Bảng đã được tạo thành công.")

except mysql.connector.Error as error:
    print("Lỗi khi kết nối đến cơ sở dữ liệu:", error)

finally:
    # Đóng kết nối sau khi sử dụng
    if 'connection' in locals():
        connection.close()
        print("Kết nối đã được đóng.")