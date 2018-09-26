#!/usr/bin/env python3
user_input = False
while not user_input:
    leases_directory = input("Type in the exact path in which your leases-file is located:")
    leases_file = input("Thanks, now please give me the exact name of the file:")

    LEASES_DIRECTORY = leases_directory
    LEASES_FILE = leases_file

    try:
        user_input = True
        with open("{}{}".format(LEASES_DIRECTORY, LEASES_FILE)) as scania_list:

            def start():
                x = False
                print("""
                Hi, this is Sirhc. I am your personal leases-file assistant.
                What can I help you with?
                     """)
                while not x:
                    choice = input("""
            
            
                You have three options: 
            
                [l]  -> list all active leases
                [i]  -> search for a specific IP adress
                [h]  -> search for a specific Hostname 
                """)


                    if choice == "l":
                        x = True
                        print_all_leaes()

                    elif choice == "i":
                        x = True
                        print_ip()

                    elif choice == "h":
                        x = True
                        print_hostname()

                    else:
                        print("Invalid input. Try again.\n")




            def print_all_leaes():
                print("Alright, one moment please.\n")
                text = (scania_list.read())
                all_leases = text.split("}")

                active_leases = []

                for i in all_leases:
                    if "active" in i:
                        active_leases.append(i)


                active_leases_text = "".join(active_leases)

                text_splitted = active_leases_text.splitlines()

                leases_info = []

                for i in text_splitted:
                    if "ddns-fwd-name" in i:
                        leases_info.append(i)
                    elif "hardware ethernet" in i:
                        leases_info.append(i)
                    elif "lease" in i:
                        leases_info.append(i)
                    elif "starts" in i:
                        leases_info.append(i)
                    elif "ends" in i:
                        leases_info.append(i)

                    leases_info = [i.replace("lease", "IP adress: ") for i in leases_info]
                    leases_info = [i.replace("{","") for  i in leases_info]
                    leases_info = [i.replace("set ddns-fwd-name =", "Hostname: ") for  i in leases_info]
                    leases_info = [i.replace("hardware ethernet", "Mac adress: ") for  i in leases_info]
                    leases_info = [i.replace("starts", "Start: ")  for  i in leases_info]
                    leases_info = [i.replace("ends", "Ends: ") for  i in leases_info]


                for i in leases_info:
                    print(i,"\n")

            def print_ip():
                ip = input("Please type in the IP Adress:")
                print("Alright, one moment please.\n")
                text = (scania_list.read())
                all_leases = text.split("}")

                active_leases = []

                for i in all_leases:
                    if "active" in i:
                        active_leases.append(i)

                active_leases_text = "".join(active_leases)

                text_splitted = active_leases_text.splitlines()

                leases_info = []

                for i in text_splitted:
                    if "ddns-fwd-name" in i:
                        leases_info.append(i)
                    elif "hardware ethernet" in i:
                        leases_info.append(i)
                    elif "lease" in i:
                        leases_info.append(i)
                    elif "starts" in i:
                        leases_info.append(i)
                    elif "ends" in i:
                        leases_info.append(i)

                    leases_info = [i.replace("lease", "$€IP adress: ") for i in leases_info]
                    leases_info = [i.replace("{", "") for i in leases_info]
                    leases_info = [i.replace("set ddns-fwd-name =", "$Hostname: ") for i in leases_info]
                    leases_info = [i.replace("hardware ethernet", "$Mac adress: ") for i in leases_info]
                    leases_info = [i.replace("starts", "$Start: ") for i in leases_info]
                    leases_info = [i.replace("ends", "$Ends: ") for i in leases_info]

                leases_info_text = "".join(leases_info)
                leases_splitted = leases_info_text.split("€")

                list_ip = []

                for i in leases_splitted:
                    if " " + ip + " " in i:
                        list_ip.append(i)
                        list_ip.append("\n")

                list_ip_text = "".join(list_ip)
                list_ip_splitted = list_ip_text.split("$")

                for i in list_ip_splitted:
                    print(i)




            def print_hostname():
                hostname = input("Please type in the Hostname:")
                print("Alright, one moment please. \n")
                text = (scania_list.read())
                all_leases = text.split("}")

                active_leases = []

                for i in all_leases:
                    if "active" in i:
                        active_leases.append(i)

                active_leases_text = "".join(active_leases)

                text_splitted = active_leases_text.splitlines()

                leases_info = []

                for i in text_splitted:
                    if "ddns-fwd-name" in i:
                        leases_info.append(i)
                    elif "hardware ethernet" in i:
                        leases_info.append(i)
                    elif "lease" in i:
                        leases_info.append(i)
                    elif "starts" in i:
                        leases_info.append(i)
                    elif "ends" in i:
                        leases_info.append(i)

                    leases_info = [i.replace("lease", "$€IP adress: ") for i in leases_info]
                    leases_info = [i.replace("{", "") for i in leases_info]
                    leases_info = [i.replace("set ddns-fwd-name =", "$Hostname: ") for i in leases_info]
                    leases_info = [i.replace("hardware ethernet", "$Mac adress: ") for i in leases_info]
                    leases_info = [i.replace("starts", "$Start: ") for i in leases_info]
                    leases_info = [i.replace("ends", "$Ends: ") for i in leases_info]

                leases_info_text = "".join(leases_info)
                leases_splitted = leases_info_text.split("€")

                list_hostname = []

                for i in leases_splitted:
                    if hostname in i:
                        list_hostname.append(i)
                        list_hostname.append("\n")

                list_hostname_text = "".join(list_hostname)
                list_hostname_splitted = list_hostname_text.split("$")

                for i in list_hostname_splitted:
                    print(i)





            start()



    except FileNotFoundError:
        print("""
         Sorry, I can not find that file. 
         
         Make sure the path and name of the file is correct.
         """)
        user_input = False










    
    











