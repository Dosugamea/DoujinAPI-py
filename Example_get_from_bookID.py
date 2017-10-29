import DoujinAPI

dj = DoujinAPI.DoujinDB(key="INPUT_YOUR_API_KEY")
id= "B967803"
print(dj.get_info(id))

if dj.get_info(id) == True:
    print(dj.create_txt())
else:
    print("Get Failed")
