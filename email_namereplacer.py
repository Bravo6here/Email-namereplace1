filepath_names = R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Python web scrapping\Email-namereplace1\Input\Names.txt"
filepath_email = R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Python web scrapping\Email-namereplace1\Input\letter.txt"
output_path = R"C:\Users\Jan - Hall 3000\Desktop\Pythonus\Python web scrapping\Email-namereplace1\Output"
output_path += R"\ "
sender_name = "Bravo"

with open(f"{filepath_names}", "r") as namefile:
    names = namefile.readlines()
with open(f"{filepath_email}", "r") as namefile:
    email_content = namefile.read()

for name in names:
    name = name.strip()
    email = email_content
    email = email.replace("[name]", name)
    email = email.replace("[sendersname]", sender_name)
    with open(f"{output_path}{name}_email.txt", "w") as a:
        a.write(f"{email}")