import os
import getpass
import aws
import basic
import docker
import lvm

while True:
    print("""
Press 1 : To manage AWS
Press 2 : To manage Docker
Press 3 : Logical Volume Management
Press 4 : Basic Linux Commands
Press 5 : Exit

""")
    choice =  int(input("Which Technology you want to manage : "))

    if choice == 1:
        aws.main()

    elif choice == 2:
        docker.main()

    elif choice == 3:
        lvm.main()

    elif choice == 4:
        basic.main()

    elif choice == 5:
        break
