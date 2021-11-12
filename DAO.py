import vertica_python as connector

class DBHelper:
	def __init__(self):
		self.con= connector.connect(host='127.0.0.1',
             					port= '5433',
            					user='dbadmin',
             					password='',
             					database='docker'
            				    )
		#print(self.con)
            	
	def insert_user(self,employee):
        	try:
        		query="Insert into mydatabase.Employees Values({},'{}','{}',{})".format(int(employee.get_id()),employee.get_firstName(),employee.get_lastName(),int(employee.get_age()))
        		print(query)
        		cur=self.con.cursor()
        	
        		cur.execute(query)
        		self.con.commit()
        		print("Employee inserted successfully")
        	except Exception as e:
        		print("Oops!", e.__class__, "occurred.")
        	
	def fetch_all_records(self):
		try:
			query="Select employeeId,firstName,lastName,age from mydatabase.Employees;"
			print(query)
			cur=self.con.cursor()
			cur.execute(query)
			rows=cur.fetchall()
			for row in rows:
				print("employeeId : ",row[0])
				print("firstName : ",row[1])
				print("lastName : ",row[2])
				print("age : ",row[3])
				print("")
		except Exception as e:
			print("Oops!", e.__class__, "occurred.")
			
			
	def delete_employee_record(self,ID):
		try:
			query="Delete from mydatabase.Employees where employeeId={}".format(int(ID))
			print(query)
			cur=self.con.cursor()
			cur.execute(query)
			self.con.commit()
			print("Record deleted successfully")
		except Exception as e:
			print("Oops!", e.__class__, "occurred.")
		
	def update_employee_record(self,employee):
		try:
			query="Update mydatabase.Employees Set firstName='{}',lastName='{}',age={} where employeeId={}".format(employee.get_firstName(),employee.get_lastName(),int(employee.get_age()),int(employee.get_id()))
			print(query)
			cur=self.con.cursor()
			cur.execute(query)
			self.con.commit()
			print("Employee Record updated")
		except Exception as e:
			print("Oops!", e.__class__, "occurred.")
		
