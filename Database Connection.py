import mysql.connector
connection = mysql.connector.connect(host='localhost',
                             user='root',
                             password='NGERNNGa_382563!@',
                            database = 'project_demo'
                           )
cursor = connection.cursor()
query = ('SELECT email FROM customer')
cursor.execute(query)
lst = []
lst = [ i[0] for i in cursor]
# print(lst)
cursor.execute(query)
new_list = []
for all in cursor:
    new_list.append(all[0])
# print(new_list)

query = f"SELECT email from customer WHERE email = 'one@nyu.edu'"
cursor.execute(query)
user = [ i[0] for i in cursor if i[0] == 'one@nyu.edu' ]
print(user)
