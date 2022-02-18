import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(host="localhost", database="haibui", user="haibui", cursor_factory=RealDictCursor)
cursor = conn.cursor()

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="haibui", user="haibui", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("connection to database failed!")
#         print("error name is ", error)
#         time.sleep(2)