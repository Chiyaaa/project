import os
import getpass

def main():
    print("\t\t\tWelcome to the TUI to make Life Easier")

    print("\t\t\t--------------------------------------")


    print("\t\t\t\t\tMenu")
    print("\t\t\t\t\t----")
    print("""
     Press  1 : To Login into AWS CLI
     Press  2 : To Launch a instance
     Press  3 : To Start a Instance
     Press  4 : To Stop a Instance 
     Press  5 : To Describe All Instances 
     Press  6 : Exit
    """)

    print("Enter Your Choice : ",end="")

    ch=input()

    if int(ch) == 1:

        os.system("aws configure")

    elif int(ch) == 2:
        print("""
            Press 1:AWS Linux
            Press 2:Redhat Linux
            """)
        print("Enter your Choice :  ",end="")
        img=input()
        if int(img) ==1:
            print("Enter Your Key name: ",end ="")
            key = input()
            os.system("aws ec2 run-instances --image-id ami-0f9fc25dd2506cf6d --subnet-id subnet-02c8d39202cd28ae7 --instance-type t2.micro --key-name {} --security-group-ids sg-0cfb581ea9318d7f3 --count 1".format(key))
        elif int(img) == 2:
            print("Enter Your Key name: ",end ="")
            key = input()
            os.system("aws ec2 run-instances --image-id ami-0b0af3577fe5e3532 --subnet-id subnet-02c8d39202cd28ae7 --instance-type t2.micro --key-name {} --security-group-ids sg-0cfb581ea9318d7f3 --count 1".format(key))


    elif int(ch) == 3:

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
        exit()
    
    else:
        print("You Entered Wrong Choice ...")

if __name__=='__main__':
        main()    
