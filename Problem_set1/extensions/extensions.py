# get input from a user 
# compare extension and input 
# print type of extension

def main():
    extension = input("File name: ").strip().lower()
    if extension.startswith("."):
        return
    match extension:
        case extension if extension.endswith(".gif"):
            print("image/gif")
        case extension if  extension.endswith(".jpg") or extension.endswith(".jpeg"):
            print("image/jpeg")
        case extension if  extension.endswith(".png"):
            print("image/png")
        case extension if  extension.endswith(".pdf"):
            print("application/pdf")
        case extension if  extension.endswith(".txt"):
            print("text/plain")
        case extension if  extension.endswith(".zip"):
            print("application/zip")
        case _:
            print("application/octet-stream")

main()