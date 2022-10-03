"""
    deal with files

    steps
        1- open the file
                ---> you must specify the filepath , operation you want to do
                open('filepath' , openning_mode)
                1-read ---> r
                2- write ---> w
                3- append ---> a

            fileobject ----> IOTextWrapper
        2- do -operation -
            read
                IOTextWrapper.read()
            write , append
                IOTextWrapper.write(content)

        3- close the file
            IOTextWrapper.close()

"""
####################################################################################3

# try:
#     filobject=open("students.txt", 'r')
# except Exception as e:
#     print(e)
#     exit()
# else:
#     print(filobject)
#     filedata= filobject.read()  # read all file content into a string
#     print(filedata)
#
#     filobject.close()



###################################

# try:
#     filobject=open("students.txt", 'r')
# except Exception as e:
#     print(e)
#     exit()
# else:
#     print(filobject)
#     filedata= filobject.read(10)  # read all file content into a string ---
#     print(filedata)
#
#     filobject.close()


#####################################
# try:
#     filobject=open("students.txt", 'r')
# except Exception as e:
#     print(e)
#     exit()
# else:
#     print(filobject)
#     filedata= filobject.readlines()  # read all file content into a string ---
#     print(filedata)
#
#     filobject.close()
#############################################

# try:
#     filobject=open("students.txt", 'r')
# except Exception as e:
#     print(e)
#     exit()
# else:
#     print(filobject)
#     filobject.seek(10)
#     filedata= filobject.read()  # read all file content into a string ---
#     print(filedata)
#
#     filobject.close()




try:
    filobject=open("students.txt", 'r')
except Exception as e:
    print(e)
    exit()
else:
    print(filobject)
    filedata= filobject.readline()
    print(filedata)
    filedata = filobject.readline()
    print(filedata)
    filedata = filobject.readline()
    print(filedata)

    filobject.close()






















