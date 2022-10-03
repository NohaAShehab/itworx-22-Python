try:
    filobject=open("demo.txt", 'a')
except Exception as e:
    print(e)
    exit()
else:
    print(filobject)
    filobject.write("My name is Shehab\n")
    filobject.seek(10)
    filobject.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


    filobject.close()