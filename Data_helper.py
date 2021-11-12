import DAO
import Employee

class data_helper:

	def __init__(self):
		self.__myObject= DAO.DBHelper()
	
	
	def insert_data(self):
		
		
		ID=input("Enter EmployeeID ->")
		firstName=input("Enter new firstName ->")
		lastName=input("Enter new lastName ->")
		age=input("Enter new age ->")
		
		employee = Employee.Employee(ID,firstName,lastName,age)
		self.__myObject.insert_user(employee)
		
	def update_data(self):
		ID=input("Enter EmployeeID ->")
		firstName=input("Enter firstName ->")
		lastName=input("Enter lastName ->")
		age=input("Enter age ->")
		
		employee = Employee.Employee(ID,firstName,lastName,age)
		self.__myObject.update_employee_record(employee)
		
	def get_all_data(self):
		self.__myObject.fetch_all_records()
		
	def delete_data(self):
		ID= input("Enter EmployeeId -> ")
		self.__myObject.delete_employee_record(ID)
		
