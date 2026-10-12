#contact book using dictionary
contacts ={}
while True:
    print("menu")
    print("\n1.add contact","\n2.search contact","\n3.update contact","\n4.delete contact","\n5.display contacts","\n6.exit")
    choice = int(input("enter choice"))
    if choice==1:
        name=input("enter name:")
        phone = input("enter phone No:")
        contacts[name]=phone
        print("contact added successfully")
    elif choice==2:
        name=input("enter name:")
        if name in contacts:
            print("phone:",contacts[name])
        else:
            print("contact not found")
    elif  choice==3:
         name=input("Enter Name : ")
         if name in contacts:
             phone=input("Enter New Phone : ")
             contacts[name]=phone
             print("Updated Successfully")
         else:
             print("Contact Not Found")
    
    elif choice == 4: 
        name = input("Enter Name: ") 
        if name in contacts: 
            del contacts[name] 
            print("Deleted Successfully") 
        else: 
            print("Contact Not Found") 
 
    elif choice == 5: 
        print("\nCONTACT LIST")
        if not contacts:
            print("No contacts available.")
        else:
            for name, phone in contacts.items(): 
                print(f"{name}\t{phone}") 
 
    elif choice == 6: 
        print("Thank You") 
        break 
 
    else: 
        print("Invalid Choice. Please try again.")
        
