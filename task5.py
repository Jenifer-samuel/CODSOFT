def add_contacts(contacts):
    name=input("Enter Name:").upper()
    num=int(input("Enter phone number:"))
    email=input("Enter email:").lower()
    address=input("Enter address:").upper()
    print("Details of",name,"added successfully")
    return(contacts.append([name,num,email,address]))

def view_contacts(contacts):
    if(len(contacts)>0):
        print("----------------Your Contact Details----------")
        for contact in contacts:
            print("Name:",contact[0])
            print("Phone Number:",contact[1])
            print("Email",contact[2])
            print("Address:",contact[3])
            print("----------------------------------------")
    else:
        print("No Details Recorded")

def search(contacts,name):
    c=0
    for contact in contacts:
        if(name==contact[0]):
            print("Name:",contact[0])
            print("Phone Number:",contact[1])
            print("Email:",contact[2])
            print("Address:",contact[3])
            c=c+1
    if(c==0):
        print("Name Not Found")
                 
def update(contacts,name):
    c=0
    for contact in contacts:
        if(name==contact[0]):
            print("What to update?\n1.Name\n2.Phone Number\n3.Email\n4.Address\n5.All")
            choice=int(input("Enter Your Choice(1/2/3/4):"))
            if(choice==1):
                contact[0]=input("Enter Updated Name:").upper()
                print("Updated Name:",contact[0])
            elif(choice==2):
                contact[1]=int(input("Enter Updated phone number:"))
                print("Updated Phone Number:",contact[1])
            elif(choice==3):
                contact[2]=input("Enter Updated Email:").lower()
                print("Updated Email:",contact[2])
            elif(choice==4):
                contact[3]=input("Enter Updated Address:").upper()
                print("Updated Address:",contact[3])
            elif(choice==5):
                contact[0]=input("Enter Updated Name:").upper()
                contact[1]=int(input("Enter Updated phone number:"))
                contact[2]=input("Enter Updated Email:").lower()
                contact[3]=input("Enter Updated Address:").upper()
                print("Updated Details:\n1.Name:",contact[0],"\n2.Phone Number:",contact[1],"\n3.Email:",contact[2],"\n4.Address:",contact[3])
            else:
                print("Please Enter a Valid choice!!")
            c=c+1
    if(c==0):
        print("Name Not Found")
        

def delete(contacts,name):
    c=0
    for contact in contacts:
        if(name==contact[0]):
            contacts.remove(contact)
            print("Contact of",name,"is Deleted Successfully")
            c=c+1
    if(c==0):
        print("Name Not Found")
       
def main():
    contacts=[]
    print("------------Welcome to Contact Details Management------------------")
    x=1
    while(x):
        print("1.Add Contacts\n")
        print("2.View Contacts\n")
        print("3.Search Contact\n")
        print("4.Update Contact\n")
        print("5.Delete Contact\n")
        print("6.Exit\n")
        print("---------------------------------------------------------------------")
        choice=int(input("Enter Your Choice(1/2/3/4/5/6):"))
        if(choice==1):
            add_contacts(contacts)
            print("---------------------------------------------------------------------")
        elif(choice==2):
            view_contacts(contacts)
            print("---------------------------------------------------------------------")
        elif(choice==3):
            name=input("Enter Name:").upper()
            search(contacts,name)
            print("---------------------------------------------------------------------")
        elif(choice==4):
            name=input("Enter Name:").upper()
            update(contacts,name)
            print("---------------------------------------------------------------------")
        elif(choice==5):
            name=input("Enter Name:").upper()
            delete(contacts,name)
            print("---------------------------------------------------------------------")
        elif(choice==6):
            print("Exiting...")
            print("---------------------------------------------------------------------")
            x=0
            
        else:
            print("Please Enter A Valid Choice!!")

main()
        
