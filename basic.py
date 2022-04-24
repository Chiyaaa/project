import os
import time

def main():
    f=1

    while(f==1):
        os.system("clear")
        print("  \n  ==============================================================================================")
        print("\t\tBasic Linux Commands Automation")
        print("\n  ==============================================================================================\n")
        print("\n\t\tSelect Any Linux Command --> \n")
        print("\t\t1: Run DATE command")
        print("\t\t2: Run CAL command")
        print("\t\t3: Run LS command")
        print("\t\t4: Show IP Address of system")
        print("\t\t5: Show Running Processes")
        print("\t\t6: Show present working Directory")
        print("\t\t7: Create Folder in Current Directory")
        print("\t\t8: Read File from Current Directory")
        print("\t\t9: Exit")
        print("\n  ==============================================================================================\n")
        op =int(input("\tEnter Your Choice:: "))
        print("\n")

        if op==1:
	    #For DATE command
            print("\n\t<<< Running DATE Command >>>\n")
            os.system("date")
	
        elif op==2:
	    #For CAL command
            print("\n\t<<< Running CAL Command >>>\n")
            os.system("cal")

        elif op==3:
	    #For LS command
            print("\n\t<<< Running LS Command >>>\n")
            os.system("ls")
	    
        elif op==4:
	    #For ifconfig command
            print("\n\t<<< Running ifconfig Command >>>\n")
            os.system("ifconfig enp0s3")
	
        elif op==5:
	    #For PS command
            print("\n\t<<< Running PS Command >>>\n")
            os.system("ps")

        elif op==6:
            #For PWD command
            print("\n\t<<< Running PWD Command >>>\n")
            os.system("pwd")
	
        elif op==7:
	    #For mkdir command
            d=input("Enter Name Of Folder You Want to Create: ")
            print("\n\tCreating Folder...\n")
            os.system("mkdir {}".format(d))
            time.sleep(1)
            print("\n\t<<< Folder Created >>>\n")

        elif op==8:
	    #For cat command
            print("\n\t<<< List of Files >>>\n")
            os.system("ls")
            print("\n")
            d=input("Enter Name Of File You Want to Read: ")
            print("\n\t Readiing File...\n")
            os.system("cat {}".format(d))

        elif op==9:
	    #Back to main menu
            print("\n\t Directing Back To Main Menu...\n")
            time.sleep(1)
            f=0
			
        else:
            print("Not an option!!!")
            f=0


if __name__=='__main__':
	main()    
