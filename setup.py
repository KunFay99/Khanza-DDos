import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pkg install python")
    os.system("pkg install python3")
    os.system("python3 -m pip install --upgrade-pip")
    os.system("pip install colorama")
    os.system("pip install tqdm")
   

elif c == "1":
    os.system("pkg install python")
    os.system("pkg install python3")
    os.system("python3 -m pip install --upgrade-pip")
    os.system("pip install colorama")
    os.system("pip install tqdm")
   
print("Done.")
