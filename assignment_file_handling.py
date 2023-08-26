# create a text file and add the below content without quotation marsk
"""
Hi *user*!

We've found the best article for you based on your interest: *title*
Please click *here* to open the article
"""

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# after running the program three times
# the file user_email.txt must have all three users content


def update_email_template(user, title, link):
    f = open("email_template.txt", "r")
    content = f.read()
    # print(content)

    content = content.replace("*user*", user)
    content = content.replace("*title*", title)
    content = content.replace("*here*", link)
    f.close()
    # print(content)

    f1 = open("user_email.txt", "a")
    f1.write(content)
    f1.close()


update_email_template(
    "Awais", "I wish I knew when I was 20", "https://cheeltech.com")
update_email_template("Siraj", "Its not over Until I win",
                      "https://cheeltech.com")
update_email_template(
    "Faraz", "Python for Website Development", "https://cheeltech.com")
