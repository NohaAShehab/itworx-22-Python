try:
    filobject=open("abc.txt", 'a')
except Exception as e:
    print(e)
    exit()
else:
    print(filobject)
    filobject.write("My name is Ahmed\n")
    # filobject.seek(10)
    filobject.writelines(["Carol\n","Ahmed\n","Aya\n","test"])
    # for l in ["Carol\n","Ahmed\n","Aya\n","test\n"]:
    #     filobject.write(l)

    filobject.close()