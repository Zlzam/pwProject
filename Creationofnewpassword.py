#User account
userName = "bSmith"
accountName = "Bob.smith"
defaultPassword = "f7*Q09/G" #testing password, intentionally failing 15 check

hashedNewPassword = '50' #Temp Hash
oldPwordHashes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '19', '20', '24'] #Temp hashes

#rules


#code
def password_check(password):
    #dictionary
    password_rules = {
    "Passwords cannot contain a user’s account name": accountName not in password,
    "Passwords cannot contain a user’s username": userName not in password,
    "Passwords cannot be one of the most recent 24 passwords": hashedNewPassword not in oldPwordHashes[-24:] ,
    "Passwords must be at least 15 characters in length.": len(password) >= 15,
    #"Passwords must contain at least two uppercase letters" : 

    # "Passwords must contain at least two lowercase letters" :

    # "Passwords must contain at least two numbers" :

    # "Passwords must contain at least two special chars “!@#$&*.”" :

    #    # #New passwords should differ from the user's previous password by at least 4 characters." :
    }
    
    for count, (rule, passed) in enumerate(password_rules.items(), start=1):
        if passed:
            print(f"Test {count} passed")
        else:
            print(f"Test {count} failed: {rule}")


def main_menu():
    while True:
        print("\n--- Main Menu (Tests implemented: 4/9) ---")
        print("1. Use hardcoded test password")
        print("2. Custom password")
        print("3. Hash function test (Not implemented)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        match choice:
            case "1":
                print("Test password check")
                password_check(defaultPassword)
            case "2":
                password = input("Enter your custom password: ")
                password_check(password)
            case "3":
                print("Hash function test not implemented")
            case "4":
                print("Exiting...")
                break  
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main_menu()

# #Accept
# ELSE
# ACCEPT password
# END IF

# #Maintenance of passwords
# #Passwords must be changed at least every 60 days
# IF passwordAge >= 60 days
# REQUIRE password change
# END IF

# #Passwords cannot be changed more than once per day
# IF timeSinceLastChange < 1 day
# REJECT password change
# END IF

# #A network account will be locked for 60 minutes after three incorrect passwords are attempted in 60 minutes.
# WHILE account is not locked

# INPUT passwordEntered

# IF passwordEntered == Password
# RETURN true
# ELSE
# RECORD failedAttempt with currentTime
# END IF

# failedAttempts = countFailuresWithinLast60Minutes()

# IF failedAttempts >= 3
# lockAccountFor(60 minutes)
# RETURN false
# END IF

# END WHILE
