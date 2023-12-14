class Filehandler:
    def write_file(self,text):
        fp = open("data.py", "a", encoding="utf-8")
        fp.write(text)
        fp.write("\n")
        fp.close()