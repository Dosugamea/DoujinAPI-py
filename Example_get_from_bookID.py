import DoujinAPI

dj = DoujinAPI.DoujinDB(key="350edd0054ea6f863126")
id= "B967803"
print(dj.get_info(id))

if dj.get_info(id) == True:
    print(dj.create_txt())
else:
    print("Get Failed")