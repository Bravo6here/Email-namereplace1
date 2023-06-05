filepath_names = R"\Email-namereplace1\Input\Names.txt" # Copypaste path to names
filepath_email = R"\Email-namereplace1\Input\letter.txt"
output_path = R"\Email-namereplace1\Output"
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