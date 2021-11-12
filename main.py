import Data_helper
		
def control_actions(choice):
	
	if(choice=="1"):
		data= Data_helper.data_helper()
		data.insert_data()
		
	
	elif(choice=="2"):
		data= Data_helper.data_helper()
		data.update_data()
		
	elif(choice=="3"):
		data= Data_helper.data_helper()
		data.get_all_data()
		
	elif(choice=="4"):
		data= Data_helper.data_helper()
		data.delete_data()
		
	else:
		print("Invalid Request")
		
	
			

def main():
	
	while True:
		print("Enter choice of operation")
		print("1. Insert Record")
		print("2. Update Record")
		print("3. Get Records")
		print("4. Delete Record")
		print()
		choice= input()
		control_actions(choice)
		print("Do you want to continue?(Y/n)")
		confirm= input()
		if(confirm != "Y"):
			break
		

#myObject.insert_user(6,'Nikhil','Ishi',100)
#myObject.fetch_all_records();
#myObject.delete_employee_record(6)
#myObject.update_employee_record(6,"Minato","Namikaze",40)

if __name__ == "__main__":
	main()





