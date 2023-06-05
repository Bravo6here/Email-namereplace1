filepath_names = R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Python web scrapping\Email-namereplace1\Input\Names.txt"
filepath_email = R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Python web scrapping\Email-namereplace1\Input\letter.txt"
with open(f"{filepath_names}", "r") as namefile:
    names = namefile.readlines()
with open(f"{filepath_email}", "r") as namefile:
    email = namefile.read()
    print(email)