class FileReader:
    def __init__(self,filename,mode):
        try:
            self.file=open(filename,mode)
        except IOError:
            print("FILE NOT FOUND")
        else:
            print("FILE OPENED")
    def read(self):
        data=self.file.read()
        print(data)
        print("FILE READ SUCCESSFULLY")
        self.file.close()
        print("FILE CLOSED")
class FileWriter:
    def __init__(self,filename,mode):
        self.file=open(filename,mode)
    def write(self,data):
        self.file.write(data)
        print("Written in file")
        self.file.close()
        print("FILE CLOSED")
while True:
    print("PLEASE SELECT AN OPTION OR ENTER -1 to EXIT")
    print("1. READ DATA FROM EXISTING FILE")
    print("2. WRITE DATA TO EXISTING OR NEW FILE")
    print("3. APPEND DATA TO EXISTING OR NEW FILE")
    try:
        choice=int(input("SELECT YOUR CHOICE :"))
        if choice==-1:
            print("THANK YOU ")
            break
        if choice not in [1,2,3]:
            print("INVALID CHOICE. TRY AGAIN")
            continue
    except ValueError:
        print("PLEASE SELECT FROM THE GIVEN OPTIONS")
    else:
        filename = input("PLEASE ENTER COMPLETE PATH OF THE FILE :")
        if choice==1:
            file=FileReader(filename,'r')
            file.read()
        elif choice==2:
           file=FileWriter(filename,'w')
           data=input("ENTER THE DATA :")
           file.write(data)
        else:
            file=FileWriter(filename,'a')
            data = input("ENTER THE DATA TO APPEND:")
            file.write(data)



