# try:
#     filobject=open("mycv.txt", 'w')
# except Exception as e:
#     print(e)
#     exit()
# else:
#     print(filobject)
#     filobject.seek(100)
#     filobject.write("My name is Ahmed\n")
#     filobject.write("Shell Script is Easy]\n")
#     filobject.write("------------------------------------\n")
#     filobject.close()



try:
    filobject=open("mycv.txt", 'w')
except Exception as e:
    print(e)
    exit()
else:
    print(filobject)
    filobject.write("My name is Ahmed\n")
    # filobject.seek(10)
    filobject.writelines(["Carol\n","Ahmed\n","Aya\n","test\n"])
    # for l in ["Carol\n","Ahmed\n","Aya\n","test\n"]:
    #     filobject.write(l)

    filobject.close()