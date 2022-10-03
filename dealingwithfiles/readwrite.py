try:
    filobject=open("mycv.txt", 'r+')
except Exception as e:
    print(e)
    exit()
else:
    # data = filobject.read()
    # print(data)
    filobject.seek(10)
    filobject.write("########################33")
    filobject.close()