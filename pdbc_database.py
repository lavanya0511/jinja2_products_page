import mysql.connector as connector
connection = connector.connect(
    host = "localhost",
    user = "pdbc_project",
    password = "Lavanya@0511",
    database = "fast_api"
)
cursor = connection.cursor()
def get_products():
    cursor.execute("select * from products")
    products = cursor.fetchall()
    return products