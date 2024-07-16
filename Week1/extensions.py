s = input("File name: ")
if '.' in s:
    s_list = s.strip().lower().split('.')
    if s_list[-1] in ["gif", "png"]:
        print("image/" + s_list[-1])
    elif s_list[-1] in ["jpg", "jpeg"]:
        print("image/jpeg")
    elif s_list[-1] in ["pdf", "zip"]:
        print("application/" + s_list[-1])
    elif s_list[-1] == "txt":
        print("text/plain")
    elif s_list[-1] == "bin":
        print("application/octet-stream")
else:
    print("application/octet-stream")


"""

types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

s = input("File name: ").strip().lower().split(".")[-1]
print(types.get(s, "application/octet-stream"))

"""