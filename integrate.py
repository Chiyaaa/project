import os
import getpass
import subprocess as sp
from lvm import VolumeGroup,LogicalVolume

while True:
    print("""
Press 1 : To manage AWS
Press 2 : To manage Docker
Press 3 : Logical Volume Management
Press 4 : Exit

""")
    choice =  int(input("Which Technology you want to manage : "))
    if choice == 1:
        print("\t\t\tWelcome to the TUI of AWS (By Simran)")
        print("\t\t\t--------------------------------------")
        print("\t\t\t\t\tMenu")
        print("\t\t\t\t\t----")
        print("""
 Press  1 : To Login into AWS CLI
 Press  2 : To Launch a instance
 Press  3 : To Start a Instance
 Press  4 : To Stop a Instance 
 Press  5 : To Describe All Instances 
 Press  6 : To Create a Volume
 Press  7 : To Attach volume with instance
 Press  8 : For Partitioning the attached volume
 Press  9 : To configure Web Server
 Press 10 : To Format Partition
 Press 11 : To Mount the Web Server to Volume
 Press 12 : Exit
		""")
        while True:
            print("AWS Management Choice: ",end="")
            ch=input()
            if int(ch) == 1:
                os.system("aws configure")
            elif int(ch) == 2:
                print("""
            		Press 1:  AWS Linux
            		Press 2:  Redhat Linux
            			""")
                print("Image Name :  ",end="")
                img=input()
                if int(img) ==1:
                    key = input("Enter Your Key Name : ")
                    os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids sg-0c111e5b44f074df9 --count 1".format(key))
                elif int(img) == 2:
                    print("Enter Your Key name: ",end ="")
                    key = input()
                    os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids sg-0c111e5b44f074df9 --count 1".format(key))
            elif int(ch)==3:
                print("Enter Instance Id : ",end = "")
                uid = input()
                os.system(" aws ec2 start-instances --instance-id {}".format(uid))
            elif int(ch) == 4:
                print("Enter Instance Id : ",end = "")
                uid = input()
                os.system(" aws ec2 stop-instances --instance-id {}".format(uid))
            elif int(ch) == 5:
                os.system("aws ec2 describe-instances")
            elif int(ch) == 6:
                print("Enter Size : ",end = "")
                size = input()
                print("Enter availability zone : ",end = "")
                zone = input()
                print("Enter volume type : ",end= "")
                vtype = input()
                os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,vtype))
            elif int(ch) == 7:
                os.system("tput setaf 3")
                print("\t\t\tVolume Zone & Instance Zone Must be same !!!")
                print("\t\t\t--------------------------------------------")
                os.system("tput setaf 7")
                print("Enter volume-id : ",end = "")
                vid = input()
                print("Enter instance-id : ",end = "")
                iid = input()
                print("Enter device : /dev/",end= "")
                device = input()
                os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(vid,iid,device))
            elif int(ch) == 8:
                print("Enter IP : ",end = "")
                ip = input()
                print("Enter key : ",end = "")
                key = input()
                print("Enter device : /dev/",end= "")
                device = input()
                os.system(" ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))
            elif int(ch) == 9:
                os.system("tput setaf 3")
                print("\t\t\tHTTPD must be installed...")
                print("\t\t\t--------------------------")
                os.system("tput setaf 7")
                print("Enter IP : ",end = "")
                ip = input()
                print("Enter key : ",end = "")
                key = input()
                os.system(" ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))
            elif int(ch) == 10:
                print("Enter IP : ",end = "")
                ip = input()
                print("Enter key : ",end = "")
                key = input()
                print("Enter Device : /dev/",end="")
                device = input()
                os.system(" ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(ip,key,device))
            elif int(ch) == 11:
                print("Enter IP : ",end = "")
                ip = input()
                print("Enter key : ",end = "")
                key = input()
                print("Enter Device : /dev/",end="")
                device = input()
                os.system(" ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(ip,key,device))
            elif int(ch) == 12:
                break
            else:
                print("You Entered Wrong Choice ...")
    elif choice == 2:
        while True:
            print("""
 Press  1 : To Start Docker(Docker must be installed)
 Press  2 : To see Docker Images
 Press  3 : To Run Docker
 Press  4 : To See All Running OS 
 Press  5 : To Pull an Image
 Press  6 : To Stop Container
 Press  7 : To Delete Container 
 Press  8 : To Stop Docker
 Press  9 : Exit
			""")
            print("Enter Your Choice : ",end="")
            ch=input()
            if int(ch) == 1:
                os.system("systemctl start docker")
            elif int(ch) == 2:
                os.system("docker images")
            elif int(ch) == 3:
                image = input("\nGive The Image Name : ")
                version = input("\nEnter Required Version : ")
                os_name = input("\nEnter The Name You Want to Give: ")
                print(" docker run -it --name {} {}:{}".format(image, version, os_name))
                os.system(" docker run -it --name {} {}:{}".format(os_name,image, version))
            elif int(ch) == 4:
                os.system("docker ps -a")
            elif int(ch) == 5:
                image = input("\nGive The Image Name : ")
                version = input("\nEnter Version : ")
                os.system("docker pull {}:{}".format(image,version))
            elif int(ch) == 6:
                os_name = input("Enter The OS Name Which You Want to Stop: ")
                os.system("docker stop {}".format(os_name))
            elif int(ch) == 7:
                os_name = input("Enter The OS Name Which You Want to Delete: ")
                os.system("docker rm {}".format(os_name))
            elif int(ch) == 8:
                os.system("systemctl stop docker")
                print("---------------Your Docker Service has Stopped --------------")
            elif int(ch) == 9:
                break
            else:
                print("You Entered Wrong Choice ...")
    elif choice == 3:
        while True:
            print("----------------------------------------------------------Welcome TO LVM (Logical Volume Management) Automation---------------------------------------------")
            print("\n")
            print("""
1).  Manage Volume Groups
2).  Manage Logical Volumes
3).  Exit 
    """)
            print("\n")
            # Take Choice of User
            ch=int(input("Enter your Choice : "))
            if ch == 1:
                # Ask to User on which Volume Group he/she want to perform tasks/operations & Create VolumeGroup Class to Manage that Volume Group
                vg_name = VolumeGroup(input("Volume Group Name :")) 
                while True:
                    print("Volume Group -------> {0}".format(vg_name.vg_info['vg_name']))
                    print("""
A). Create Volume Group
B). Display Volume Group Information
C). Extend Volume Group Size
D). Merge two Volume Groups
E). Reduce Volume Group Size
F). Rename Volume Group
G). Remove Volume Group
H). Add Volume From Another Volume Group
I). Exit
""")
                    print("\n")
                    # Take Input that what operation user would like to perform
                    ch=input("What do you want to do => ")
                    if ch == 'A':
                        print("Create")
                        # Take list of Volume
                        volumes=[volume.replace(" ","") for volume in input("Enter volumes : ").split(",")]
                        print(volumes)
                        # Create Volume Group
                        vg_name.create(volumes)
                    elif ch == 'B':
                        # Display Volume Group Information
                        vg_name.display()
                    elif ch == 'C':
                        print("Extend")
                        # Take Volumes List
                        volumes=[volume.replace(" ","") for volume in input("Enter volumes : ").split(",")]
                        # Extend Volume
                        vg_name.extend(volumes)
                    elif ch == 'D':
                        print("Merge")
                        # Take Volume Group which will be merged
                        vg = VolumeGroup(input("Merged Volume Group :"))
                        # Merge Volume Group
                        vg_name.merge(vg)
                        # Delete Reference of Merged Volume Group
                        del vg
                    elif ch == 'E':
                        print("Reduce")
                        # Reduce Volume Group . For this take input Volume
                        vg_name.reduce(input("Enter volume name (which we want to remove from Volume Group) : "))
                    elif ch == 'F':
                        print("Rename")
                        # Rename VOlume Group . Take New Volume Group Name
                        vg_name.rename(input("New Volume Group Name : "))
                    elif ch == 'G':
                        print("Remove")
                        # Remove Volume Group
                        vg_name.remove()
                    elif ch == 'H':
                        print("Add")
                        # Split Volume form Another Volume Group 
                        vg_name.add(VolumeGroup(input("Enter Volume Group : ")),input("Volume Name : "))
                    elif ch == 'I':
                        break
            elif ch == 2:
                lv_name = LogicalVolume(input("Enter Logical Volume Name : "),VolumeGroup(input("Enter Volume Group Name : ")))
                while True:
                    print("Logical Volume   ----->  {0}".format(lv_name.lv_info['lv_name']))
                    print("Volume Group     ----->  {0}".format(lv_name.vg.vg_info['vg_name']))
                    print("""
A). Create Logical Volume
B). Format Logical Volume
C). Mount Logical Volume
D). Unmount Logical Volume
E). Extend Logical Volume
F). Reduce Logical Volume
G). Remove Logical Volume
H). Display Logical Volume
I). Exit
""")
                    print("\n")
                    ch=input("What do you want to do => ")
                    if ch == 'A':
                        # Create Logical Volume
                        print("Create")
                        lv_name.create(input("Enter Logical Volume Size : "))
                    elif ch == 'B':
                        print("Format")
                        # Format Logical Volume
                        lv_name.format(input("Format Type : "))
                    elif ch == 'C':
                        print("Mount")
                        # Mount Logical Volume
                        lv_name.mount(input("Mount Point : "))
                    elif ch == 'D':
                        print("Unmount")
                        # Unmount Logical Volume
                        lv_name.unmount()
                    elif ch == 'E':
                        print("Extend")
                        # Extend Logical Volume
                        lv_name.extend(input("Extend Volume Size : "))
                    elif ch == 'F':
                        print("Reduce")
                        # Reduce Logical Volume
                        lv_name.reduce(input("Volume Size After Reducing : "))
                    elif ch == 'G':
                        print("Remove")
                        # Remove Logical Volume
                        lv_name.remove()
                    elif ch == 'H':
                        print("Display")
                        # Display Logical Volume Information
                        lv_name.display()
                    elif ch == 'I':
                        print("Exit")
                        break
            elif ch == 3:
                break
    


    elif choice == 4:
        break
