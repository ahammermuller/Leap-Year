import login


def main():
    user_first_name = input("Enter your first name: ")
    user_last_name = input("Enter your last name: ")
    user_bcit_id = input("Enter your BCIT ID: ")
    user_password = login.generate_login(user_first_name, user_last_name, user_bcit_id)
    print(f'Your login is {user_password}')
    changed_password = login.change_password()
    print(f'valid password\n{changed_password}')


if __name__ == "__main__":
    main()
