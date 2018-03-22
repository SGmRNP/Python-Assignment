# to run this code , one library needs to be installed
# mysql.connector
# In order to connect to the database
# username, databasename, password and hostname
# needs to be provided

# importing library
import mysql.connector
# establishing connection to database
cnnx = mysql.connector.connect(
                            user='user_name',
                            database='database_name',
                            password='password',
                            hostname='hostname')

cursor = cnnx.cursor()

query1a = ("SELECT city_id, count(city_id) FROM Hotels"
           "ORDER BY count(city_id) DESC LIMIT 10")

query1b = ("SELECT city_id, SUM(rooms) FROM Hotels"
           "GROUP BY city_id"
           "ORDER BY SUM(rooms) DESC LIMIT 10")

query2 = ("SELECT user_id,SUM(rooms) FROM Hotels"
          "GROUP BY user_id"
          "ORDER BY SUM(rooms) DESC LIMIT 1")

query3 = ("SELECT user_id, COUNT(user_id) FROM Hotels"
          "WHERE booking_date BETWEEN CURDATE() -INTERVAL 30 DAY AND CURDATE()"
          "ORDER BY COUNT(user_id) DESC LIMIT 10")

cursor.execute(query1a)
print("Top 10 cities with the highest number of bookings\n")

for (city_id, count(city_id)) in cursor:
    print("City: {}, number of bookings: {}".format(city_id, count(city_id)))

cursor.execute(query1b)
print("\nTop 10 cities with the highest number of rooms booked\n")

for (city_id, SUM(rooms)) in cursor:
    print("City: {}, number of rooms booked: {}".format(city_id, SUM(rooms)))

cursor.execute(query2)
print("\nUser who has booked the maximum number of rooms till date\n")

for (user_id, SUM(rooms)) in cursor:
    print("Userid: {}, number of rooms booked: {}".format(user_id, SUM(rooms)))

cursor.execute(query3)
print("\nTop 10 users having maximum number of bookings in last 30 days\n")

for (user_id, COUNT(user_id)) in cursor:
    print("User id: {},number of bookings: {}".format(user_id, COUNT(user_id)))


cursor.close()
cnnx.close()

