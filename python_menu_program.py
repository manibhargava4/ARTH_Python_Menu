import sys,time,os
import getpass
import subprocess as sub
#os.system("pip3 install pyfiglet")
from pyfiglet import Figlet


# Functions

def typewriter(words,slp):
	for char in words:
		sys.stdout.write(char)
		sys.stdout.flush()
		if char != "\n":
			time.sleep(slp)
		else:
			time.sleep(1)


def render(text,style,slp):
	f = Figlet(font=style)
	print("\n")
	typewriter(f.renderText(text),slp)


# Main Code Startes from here


# Main Heading


os.system("tput setaf 2")
typewriter("""\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n
												AUTOMATION\n
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n""",0.0001)
os.system("tput setaf 7")
render("""\t\t\tPython
		Menu
		Program""",'speed',0.000001)
os.system("tput setaf 6")
typewriter("""\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBy:
																Banka Mani Bhargava
																Amogh Hedge
																Kanav Gupta
																Veeramanodreddy
																Girish Chowdary\n""",0.01)



# Authentication for using this program


password = getpass.getpass("Enter the password to continue (Hint: Winner) = ")

if password != "1" :
	print("Try again")
	exit()


# List of Technology Available with this program
while 5 > 4:
	os.system("tput setaf 7")
	typewriter("""
										In Which Technology do you want to interact with?
	  press 1 :  DOCKER
	  press 2 :  LINUX COMMANDS AND LVM
	  press 3 :  AWS
	  press 4 :  HADOOP
	  press 5 :  EXIT
	""",0.0000001)

	os.system("tput setaf 6")
	t = input("Enter your choice = ")


	# DOCKER


	if int(t) == 1:
		print("\t \t \t Welcome, This is a Menu Program for DOCKER")
		print(" \n -------------------------------------------------------------------------------------------------------------------")
		os.system("tput setaf 7")
		while 5 > 4:
			dInput=int(input("""Choose from the below operations you want to perform in Docker ? :
	1. To install Docker.
	2. To start Docker services.
	3. To know the Status of Docker.
	4. To Download the Docker Image into your OS.
	5. To See the list of Docker Images installed.
	6. To Install Docker Image.
	7. Boot previous installed os
	8. To Terminate Docker Image.
	9. To enable Docker to run continuously
	10.To disable Docker
	11.Go back to menu.
	12.Exit 
	"""))
			if dInput == 1:
				os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")		
				os.system("dnf install docker-ce --nobest")
				input("Press Enter to Continue")
				os.system("clear")
			elif dInput == 2:
				os.system("systemctl start docker")
				input("Press Enter to Continue")
				os.system("clear")
			elif dInput == 3:
				os.system("systemctl status docker")
				input("Press Enter to Continue")
				os.system("clear")
			elif dInput == 4:
				sub.getoutput("systemctl start docker")
				imageName = input("Enter full name of image to download (Like centos:7): ")
				os.system("docker pull {}".format(imageName))
				os.system("docker images")
				input("Press Enter to Continue")
				os.system("clear")
			elif dInput == 5:
				os.system("docker images")
				input("Press Enter to Continue")
				os.system("clear")
			elif dInput == 6:
				os.system("docker image")
				imageName = input("Enter full name of Docker Image(like centos:7): ")	
				osName = input("Enter Your OS Name(eg:CentOSv7): ")
				os.system("docker run -it --name {} {}".format(osName,imageName))
				input("Press Enter to Continue")
				os.system("clear")
			elif dInput == 7:
				os.system("docker ps")
				sub.getoutput("systemctl start docker")
				docId = input("Enter OS Name or OS ID to start Docker Service: ")
				so.system("docker start {}".format(docId))
				os.system("docker attach {}".format(docId))
				input("Press Enter to Continue")
				os.system("clear")
			elif dInput == 8:
				os.system("docker ps")
				sub.getoutput("systemctl start docker")
				docId = input("Enter OS Name or OS ID to Remove Docker Image: ")
				os.system("docker rm {}".format(docId))
				input("Press Enter to Continue")
				os.system("clear")
			elif dInput == 9:
				os.system("systemctl enable docker")
			elif dInput == 10:
				os.system("systemctl disable docker")
			elif dInput == 11:
				break
			elif dInput == 12:
				exit()
			else:
				print("Enter correct input")


	# LINUX COMMANDS

		os.system("tput setaf 7")
	elif int(t) == 2:
		while 5 > 4:
			print("""\t\t\t BASIC LINUX COMMANDS
		  		\n\t\t\t ---------------------
		  press 1:  Check Date                        press 16: Copy a file
		  press 2:  View Calender                     press 17: Open Python terminal
		  press 3:  Reboot                            press 18: Show details of CPU
		  press 4:  Exit                              press 19: Check status of RAM
		  press 5:  Configure Webserver               press 20: Create a new user
		  press 6:  Check STATUS of Webserver         press 21: Check IP of the system
		  press 7:  Deactivate webserver              press 22: Show task manager
		  press 8:  Check details of your HARD_DISK   press 23: Clear cache
		  press 9:  Show all ports in use             press 24: create partition
		  press 10: Create a file                     press 25: LVM
		  press 11: Create a directory                press 26: Go back to main menu
		  press 12: List all files and folder         press 27: Exit
		  press 13: View the contents of the file
		  press 14: Remove a file
		  press 15: Remove a folder
		  
		  """)
			
			ch = input("Enter your input = ")
			
			if int(ch)== 1:
				os.system("date")
			elif int(ch)== 2:
				os.system("cal")
			elif int(ch)== 3:
				os.system("reboot")
			elif int(ch)== 4:
				exit()
			elif int(ch)== 5:
				os.system("systemctl start httpd")
			elif int(ch)== 6:
				os.system("systemctl status httpd")
			elif int(ch)== 7:
				os.system("systemctl stop httpd")
			elif int(ch)== 8:
				os.system("fdisk -l")
			elif int(ch)== 9:
				os.system("netstat -tnlp")
			elif int(ch)== 10:
				name=input("Enter file name with extension: ")
				os.system("gedit {}". format(name))
			elif int(ch)== 11:
				name=input("Enter name of the directory: ")
				os.system("mkdir {}". format(name))
			elif int(ch)== 12:
				os.system("ls")
			elif int(ch)== 13:
				name=input("Enter name of the file: ")
				os.system("cat {}". format(name))
			elif int(ch)== 14:
				name=input("Enter name of the file you want to remove: ")
				os.system("rm {}". format(name))
			elif int(ch)== 15:
				name=input("Enter name of the directory: ")
				os.system("rm -rf {}". format(name))
			elif int(ch)== 16:
				n=input("Enter name of the file you want to copy: ")
				m=input("Enter new name: ")
				os.system("cp {} {}". format(n,m))
			elif int(ch)== 17:
				os.system("python3")
			elif int(ch)== 18:
				os.system("ls cpu")
			elif int(ch)== 19:
				os.system("free -m")
			elif int(ch)== 20:
				n=input("User Name: ")
				os.system("add user {}". format(n))
			elif int(ch)== 21:
				os.system("ifconfig enp0s3")
			elif int(ch)== 22:
				os.system("top")
			elif int(ch)== 23:
				os.system("echo 3> /proc/sys/vm/drop-caches")
			elif int(ch)== 24:
				os.system("fdisk -l")
				disk=input("Enter the disk name : ")
				size= input("Enter the size of the partion (+size(M,G,T..)/size(in sectors): ")
				os.system("echo -e \"n\np\n\n\n{}\nw\n\" | fdisk {} ". format(size,disk)) 
			elif int(ch)==25 :
				while 5 > 4:
					os.system("clear")
					os.system("tput setaf 3")
					x=input("""1. Do u want to add any disk to vg 
	2. create logical volume
	3. create new vg
	4. extend the partition
	5. Go back to main menu
	6. Exit \n""")
					 
					if int(x)==1:
						name=input("Enter the disk name u want to add to vg: ")
						vggroup=input("Enter the vg name : ")
						os.system("pvcreate {} ". format(name))
						os.system("vgextend  {} {} ". format(vggroup,name))
					elif int(x)==2:
						pvname=input("Enter the partition name : ")
						vggroup=input("Enter the vg name : ")
						sizee=input("Enter the size of the partition : ")
						os.system("lvcreate --size {} --name {} {} ". format(sizee,pvname,vggroup))
						os.system("mkfs.ext4 /dev/{}/{} ". format(vggroup,pvname))
						dire=input("name of the folder u want to mount ")
						os.system("mkdir {} ". format(dire))
						os.system("mount /dev/{}/{} {} ". format(vggroup,pvname,dire))
					elif int(x)==3:
						name=input("Enter the disk name u want to add to vg: ")
						vggroup=input("Enter the vg name : ")
						os.system("pvcreate {} ". format(name))
						os.system("vgcreate  {} {} ". format(vggroup,name))
					elif int(x)==4:
						sizee=input("Enter the size u wanna extend ")
						pvname=input("Name of the volume ")
						os.system("pvextend --size {} {}  ". format(sizee,pvname))
						os.system("resize2fs /dev/python/{} ". format(pvname))
					elif int(x)==5:
						break
					elif int(x)==6:
						exit()
					else:
						print("Enter correct input")
			elif int(ch) == 26:
				break
			elif int(ch) == 27:
				exit()  
			else:
			 	print("Invalid Choice")
		
	elif int(t) == 3:
		print("welcome to menu")
		print("""
\n
1. display all instances and their details
2. start an instance
3. stop an instance
4. terminate an instance
5. display all security groups
6. display all images
7. display all s3 buckets
8. remove a bucket
9. create a bucket
10.view billing
11.create a EBS volume
12.Go back to menu
13.Exit
""")
		while True:
			print("please write the option number you want to choose:", end=' ')
			y=input()
			x=int(y)
			if (x==1):
				cmd="aws ec2 describe-instances" 
				"""\
				--filters Name=tag-key,Values=Name \
				--query Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value} --output table"""
				os.system(cmd)
			elif(x==2):
				print("type the instance id which you want to start")
				id=input()
				cmd="aws ec2 start-instances --instance-ids {}".format(id)
				os.system(cmd) 
			elif (x==3):
				print("enter the id of the instance that you want to stop")
				id=input()
				cmd="aws ec2 stop-instances --instance-ids {}".format(id)
				os.system(cmd)
			elif (x==4):
				print("enter the id of the instance that you want to terminate")
				id=input()
				cmd="aws ec2 terminate-instances --instance-ids {}".format(id)
				os.system(cmd)
			elif (x==5):
				cmd="aws ec2 describe-security-groups"
				os.system(cmd)
			elif (x==6):
				cmd="aws ec2 describe-images \
	--filters Name=tag:Type,Values=Custom \
	--query 'Images[*].[ImageId]' \
	--output text"
				os.system(cmd)
			elif (x==7):
				cmd="aws s3api list-buckets --query Buckets[].Name"
				os.system(cmd)
			elif (x==8):
				print("enter the name of the bucket")
				b=input()
				print("enter the name of the file with extension")
				f=input()
				cmd="aws s3 rm s3://{}/{}".format(b,f)
				os.system(cmd)
			elif (x==9):
				print("enter a unique name of the bucket")
				b=input()
				cmd="aws s3api create-bucket --bucket b --region ap-south-1".format(b)
				os.system(cmd)
			elif (x==10):
				cmd="aws route53domains view-billing \
	--region ap-south-1 \
	--start-time 1514764800 \
	--end-time 1577836800"
				os.system(cmd)
			elif (x==11):
				print("enter the size of the EBS volume")
				s=input()
				cmd="aws ec2 create-volume \
	--volume-type gp2 \
	--size s \
	--availability-zone ap-south-1a".format(b)
				os.system(cmd)
			elif (x==12):
				break
			elif (x==13):
				exit()
		else:
			print("Enter correct input")

	elif int(t) == 4 :
		print("\t \t \t Welcome, This is a Menu Program for HADOOP")
		print(" \n ----------------------------------------------------------------------------")
		os.system("tput setaf 7")
		print (" \n Did you installed Hadoop?")
		c = input(" (yes/no) ")
		if  c == "no":
			master_ip = input("Enter ip address for Master node: ")
			os.system("scp  hadoop-1.2.1-1.x86_64.rpm {}:/root".format(master_ip))
			os.system("scp jdk-8u171-linux-x64.rpm  {}:/root".format(master_ip))
			os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm; rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(master_ip))
			#slave_ip = input("Enter ip address for slave node: ")
			#client_ip = input("Enter ip address for client node: ")
		elif c == "yes":
			while 5 > 4:
				hInput=int(input("""Choose from the below operations you want to perform in Hadoop ? :
		1. To create Hadoop Master node
		2. To create Hadoop Slave node
		3. To create Hadoop Client node
		4. To upload file to the Cluster
		5. To Check all files in the Cluster
		6. Exit. 
		"""))
				if int(hInput) == 1:
					while 5 > 4:
						ip = (input("Enter IP address of PC that you want to make it as master (eg: 192.168.32.45): "))
						chk = sub.getstatusoutput("ping {} -c 1".format(ip))
						if int(chk[0]) == 0:
							os.system("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:9001</value> \n</property> \n</configuration>' > core-site.xml | mv core-site.xml /etc/hadoop/".format(ip))
							os.system("scp /etc/hadoop/core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
							while 5 > 4:
								dirname = input("Enter Directory Name for nanenode (eg: name): ")
								check = sub.getstatusoutput("mkdir /{}".format(dirname))
								if int(check[0]) == 0:
									sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.name.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site.xml | mv hdfs-site.xml /etc/hadoop/".format(dirname))
									os.system("hadoop namenode -format")
									sub.getoutput("hadoop-daemon.sh start namenode")
									os.system("systemctl stop firewalld")
									print("Your Name node (Master) is created successfully.")
									input("Press Enter to Continue")
									break
							break
				elif int(hInput) == 2:
					while 5 > 4:
						ip = (input("Enter IP address of master node (eg: 192.168.32.45): "))
						chk = sub.getstatusoutput("ping {} -c 1".format(ip))
						ip1 = (input("Enter IP address of data node (eg: 192.168.32.45): "))
						chk1 = sub.getstatusoutput("ping {} -c 1".format(ip1))
						if (int(chk1[0])) == 0:
							sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:9001</value> \n</property> \n</configuration>' > core-site1.xml | mv core-site1.xml /etc/hadoop/".format(ip))
							os.system("scp /etc/hadoop/core-site1.xml {}:/etc/hadoop/core-site.xml".format(ip1))
							while 5 > 4:
								dirname = input("Enter Directory Name for nanenode (eg: name): ")
								check = sub.getstatusoutput("mkdir /{}".format(dirname))
								os.system("scp -r /{} {}:/".format(dirname,ip1))
								if int(check[0]) == 0:
									sub.getstatusoutput("echo '<configuration> \n<property> \n<name>dfs.data.dir</name> \n<value>/{}</value> \n</property> \n</configuration>' > hdfs-site1.xml | mv hdfs-site1.xml /etc/hadoop/".format(dirname))
									os.system("scp /etc/hadoop/hdfs-site1.xml {}:/etc/hadoop/hdfs-site.xml".format(ip1))
									sub.getoutput("ssh {} hadoop-daemon.sh start datanode".format(ip1))
									os.system("systemctl stop firewalld")
									print("Your Data node (Slave) is created successfully.")
									typewriter("Hadoop Cluster Details: ",0.001)
									os.system("hadoop dfsadmin -report")
									input("Press Enter to Continue")
									os.system("clear")
									break
						break
				elif int(hInput) == 3:
					while 5 > 4:
						ip = (input("Enter IP address of Master node (eg: 192.168.32.45): "))
						chk = sub.getstatusoutput("ping {} -c 1".format(ip))
						ip2 = (input("Enter IP address of client node (eg: 192.168.32.45): "))
						chk2 = sub.getstatusoutput("ping {} -c 1".format(ip2))
						if (int(chk[0])) and (int(chk[0])) == 0:
							if ip2 != ip:
								sub.getstatusoutput("echo '<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{}:9001</value> \n</property> \n</configuration>' > core-site3.xml | mv core-site3.xml /etc/hadoop/".format(ip))
								os.system("scp /etc/hadoop/core-site3.xml {}:/etc/hadoop/core-site.xml".format(ip2))
								print("Your Client is created successfully")
								input("Press enter to continu")
								break					
				elif int(hInput) == 4:
					i = input("Do you want to upload empty file ? (yes/no): ")
					if i == "yes":
						file = input("Enter name of the file: ")
						os.system("hadoop fs -touchz {} /".format(file))
						print("Check your filename in the below file list")
						os.system("hadoop fs -ls /")
					elif i == "no":
						name = input("Give your file a name: ")
						text = input("Enter your desired text in the file: ")
						sub.getstatusoutput("echo '{}' > {}".format(text,name))
						os.system("hadoop fs -put {} /".format(name))
						print("Check yout filename in the below file list")
						os.system("hadoop fs -ls /")
				elif int(hInput) == 5:
					os.system("hadoop fs -ls /")
				elif int(hInput) == 6:
					break
				else:
					print("Invalid input, please try again.")
		else:
			print("Invalid input. please try again.")
	elif int(t) == 5:
		exit()
	else:
		print("Enter correct input")


	
   

  

 
 
   
