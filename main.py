from dbhelper import DBHelper


def main():

    db=DBHelper()

    while True:
        print("***************WELCOME***************")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                # insert user
                uid=int(input("Enter user ID :"))
                username=input("Enter user Name :")
                userphone=input("Enter user Phone :")
                db.insert_user(uid,username,userphone)
                
            elif choice==2:
                # display user
                db.fetch_all()
                pass
            elif choice==3:
                # delete user
                userid=int(input("Enter user id to which you want to delete :"))
                db.delete_user(userid)
            elif choice==4:
                # update user
                uid=int(input("Enter Id of user :"))
                username=input("Enter user New Name :")
                userphone=input("Enter user New Phone :")
                db.update_user(uid,username,userphone)
                
            elif choice==5:
                # exit user
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")


if __name__== "__main__":
    main()
            
            

