# returns file type based on file ending

phototype = input("File name:").strip().lower()

if ".jpeg" in phototype:
    print("image/jpeg")
elif ".gif" in phototype:
    print("image/gif")
elif ".jpg" in phototype:
    print("image/jpeg")
elif ".png" in phototype:
    print("image/png")
elif ".pdf" in phototype:
    print("application/pdf")
elif ".txt" in phototype:
    print("text/plain")
elif ".zip" in phototype:
    print("application/zip")
else:
    print("application/octet-stream")