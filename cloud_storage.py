import dropbox
class TranferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(filefrom,"rb")
        dbx.files_upload(f.read(),fileto)

def main():
    access_token="17ykwnOEEJEAAAAAAAAAAb2_0jjt3VAF8bhtXAcsUzszg5uajMKE5cLHytFlhJwD"
    tranferData=TranferData(access_token)
    filefrom=input("enter file path to upload")
    fileto=input("enter full path to upload to dropbox")
    tranferData.upload_file(filefrom,fileto)
    print("file uploaded")
main()