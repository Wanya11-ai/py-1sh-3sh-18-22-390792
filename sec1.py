

#1.sabtenam     2. vorood     3.khoroj



text = "MENU"

print(text.center(20, "="))

menu = input("lotfan yeki az gozin haye zir ra entekhab konid\n 1. sabtenam   2. voorood   3. khorog: ")

lolo=[]

match menu:

    case "1":
        print("khosh omadid! \U0001f600")
        print("lotfan farayand sabtnam ro takmil konid:")

        while True:
          name = input("lotfan name khod ra vared konid: ").strip()
          if len(name)<=1:
            print("lotfan az esm vaghei khodetoon estefade konid!")
          else:
            print("esm shoma sabt shod")
            name2= name.capitalize()
            lolo.append(name2)
            break
     

        while True:
           famili = input("lotfan famili khod ra vared konid: ").strip()
           if len(name)<=1:
                print("lotfan az famili vaghei khodetoon estefade konid!")
           else:
            print("famili shoma sabt shod")
            famili2= famili.capitalize()
            lolo.append(famili2)

            break
           
        


        address = input("address dahid: ").strip()
        while True:
          if address.isalnum()==True:
              print("address shoma sabt shod")
              lolo.append(address)
              break
          else:
                print("lotfan yek address motabar vared konid.")


        while True:
            phone = input("yek shomare tamas vared konid: ")

            if phone.isdigit() and len(phone) == 11:
                print("shomare tamas motabar ast ")
                lolo.append(phone)
                break
            else:
                print("shomare tamas namotabar ast ")
                print("doubare talash konid:")

        print(lolo)
        print("shoma sabtnam shodid.")
        


    case "2":
      print("\n--- VOOROOD ---") 
      
      if len(lolo) == 0:
             print("hich hesab sabt nashode ast!")

      else:
         while True: 
            phone_login = input("shomare tamas khod ra vared konid: ")
            password_login = input("ramz oboor khod ra vared konid: ")
            if phone_login == lolo[3] and password_login == lolo[4]: 
                print(f"\tkhosh amadid {lolo[0]} {lolo[1]}! \U0001f600 ") 
                break
            else: print("\nshomare ya ramz oboor eshtebah ast ")
            print("doubare talash konid.")

    case "3":
      print(" khodafezy")
        