#!/usr/bin/python3
import os,sys



def run():
	
	if "update" == sys.argv[1]:
		try:
			Port = str(sys.argv[2])
			times = str(sys.argv[3])
			
			os.system("pkill -f ipgeo.py")
			
			print ("[x] Killed ")
			
			os.system("nohup python3 /nemo/ipgeo.py " + Port + " " + times + " & exit")
			
			print("[x] Updated Port ", Port , "| Many's ",times)
						
		except:
			
			print(main())
	elif "run" == sys.argv[1]:
		try:
			
			Port = str(sys.argv[2])
			times = str(sys.argv[3])

			os.system("nohup python3 /nemo/ipgeo.py " + Port + " " + times + " & exit")
			
			print("[x] Running Port :", Port , "| Many's :",times)
						
		except:
			# ~ print("1")
			print(main())

	elif "kill" == sys.argv[1]:
		
		try:
			
			os.system("pkill -f ipgeo.py")
			print("[x] KILLED")

		except:
			
			print(main())

	else:
		pass



def main():
	
	return (""" 
	

███╗░░░███╗███████╗██████╗░░██████╗░█████╗░██╗░░░██╗░█████╗░██╗██████╗░██╗
████╗░████║██╔════╝██╔══██╗██╔════╝██╔══██╗██║░░░██║██╔══██╗██║██╔══██╗██║
██╔████╔██║█████╗░░██║░░██║╚█████╗░██║░░██║██║░░░██║███████║██║██║░░██║██║
██║╚██╔╝██║██╔══╝░░██║░░██║░╚═══██╗██║░░██║██║░░░██║██╔══██║██║██║░░██║██║
██║░╚═╝░██║███████╗██████╔╝██████╔╝╚█████╔╝╚██████╔╝██║░░██║██║██████╔╝██║
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝

    HOW TO USE :

[i] To update:
	
	sudo med.py update  port manys
	  
[i] To run:
	
	sudo med.py run port manys
	  
[i] To kill:
	
    sudo med.py kill

	""")
	

if __name__ == "__main__":
	
	try:
	
		run()
	
	except:
		
		print(main())
		
		
