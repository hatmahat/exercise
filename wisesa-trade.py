wisesa = [
    "WWW  WWW  WWW    WWW       WWWWWWWWWWW     WWWWWWWWWW       WWWWWWWWWWW         WWWWWWWW",
    "WWW  WWW  WWW    WWW     WWW               WWWWWWWWWW     WWW                 WWWW     WWW",
    "WWW  WWW  WWW           WWW                WWWW          WWW                 WWW         WWW",
    "WWW  WWW  WWW    WWW     WWW               WWWW           WWW                WWW         WWW",
    "WWW  WWW  WWW    WWW      WWWWWWWWWWW      WWWWWWWWWW      WWWWWWWWWWW       WWWWWWWWWWWWWWW",
    "WWW  WWW  WWW    WWW               WWWW    WWWWWWWWWW               WWWW     WWWW       WWWW",
    "WWW  WWW  WWW    WWW                 WWW   WWWW                       WWW    WWW         WWW",
    " WWWWWWWWWWW     WWW                WWW    WWWW                      WWW     WWW         WWW",
    "  WWWWWWWWW      WWW      WWWWWWWWWWWW     WWWWWWWWWW      WWWWWWWWWWWW      WWW         WWW",
    "    WWWWW        WWW    WWW                WWWWWWWWWW    WWWW                WWW         WWW"
]

for i in wisesa:
    print(i)

def password(pass_int):
    pass_input = int(input("Enter pass: ").strip())
    tries = 0
    while pass_input != pass_int:
        print("Password incorrect, try again!")
        pass_input = int(input("Enter pass: ").strip())
        tries += 1
        if tries == 3:
            break
    #print("access granted!")
    print("too many tries!, system out..")

password(1234)