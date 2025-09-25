class File:
    def __init__(self, filename: str):
        self._name_ = filename
        self._contents_ = ""
    def addContentToFile (self, data: str):
        self._contents_ += data
    def readContentFromFile(self):
        return self._contents_
    def ls(self):
        return self._name_

class Dir:
    def __init__(self, dirname: str):
        self._name_ = dirname
        self._subdirs_ = {}
        self._files_ = {}
#    def add_dir(self, name: str, dir_obj: Dir):
#        self._subdirs_[name] = dir_obj
#    def add_file(self, name: str, file_obj: File):
#        self._files_[name] = file_obj
    def ls(self, path = None):
        if path:
            sub_path = path[len(self._name_):] # drop current name and the /
            print(f"\t\t in ls({path}) sub_path({len(sub_path)}):{sub_path}")
            if len(sub_path) > 0:
                sep_loc = sub_path.find("/")
                if sep_loc == -1:
                    sub_dir = sub_path
                    if sub_dir in self._subdirs_.keys():
                        return self._subdirs_[sub_dir].ls()
                    elif sub_dir in self._files_.keys():
                        return self._files_[sub_dir].ls()
                    else:
                        raise "file path not found"
                    pass
                else:
                    sub_dir = sub_path[:sep_loc]
                    sub_dir_obj = self._subdirs_[sub_dir]
                    nested_sub_path = sub_path[sep_loc:]
                    if sub_dir_obj:
                        return sub_dir_obj.ls(nested_sub_path)
            else:
                return self.ls()
        else:
            result = [s for s in self._subdirs_.keys()]
            for f in self._files_.keys():
                result.append(f)
            return result
        
    def readContentFromFile(self, path: str):
        # if the file name terminates in this dir
        sub_dir_path = path[len(self._name_):]
        sep_loc = sub_dir_path.find("/")
        print(f"\t\t readContentFromFile -- sub_dir_path:{sub_dir_path} \t path:{path} \tcurrent dir:{self._name_}")
        if sep_loc  == -1:
            # file exists in curr dir -- return the contents of the file
            sub_file_name = path
            print(f"\t\t readContentFromFile file:{sub_file_name} \tfor path:{path} \t current_dir:{self._name_}")
            if sub_file_name not in self._files_.keys():
                raise Exception("file not found")
            file_obj = self._files_[sub_file_name]
            return file_obj.readContentFromFile()
        else:
            sub_dir_name = sub_dir_path[:sep_loc]
            nested_subdir_path = sub_dir_path[sep_loc + 1:]
            print(f"\t\t readContentFromFile subdir:{sub_dir_name} \tfor path:{path} \t current_dir:{self._name_}")
            if sub_dir_name not in self._subdirs_.keys():
                raise Exception(f"sub dir path:{path} not found")
            subdir_obj = self._subdirs_[sub_dir_name]
            return subdir_obj.readContentFromFile(nested_subdir_path)

    def mkdir(self, path):
        sub_dir_path = path[len(self._name_):]
        if len(sub_dir_path) == 0:
            print(f"\t\t mkdir found sub_dir_path of len 0 \t for path:{path}")
            return
        sep_loc = sub_dir_path.find("/")
        if sep_loc  == -1:
            sub_dir_name = sub_dir_path
            if sub_dir_name not in self._subdirs_.keys():
                print(f"\t\t making subdir:{sub_dir_name} \tfor path:{path}")
                self._subdirs_[sub_dir_name] = Dir(sub_dir_name)
        else:
            sub_dir_name = sub_dir_path[:sep_loc]
            nested_subdir_path = sub_dir_path[sep_loc:]
            print(f"\t\t making subdir:{sub_dir_name} \t with nested subdir:{nested_subdir_path} \t for path:{path}")
            if sub_dir_name not in self._subdirs_.keys():
                self._subdirs_[sub_dir_name] = Dir(sub_dir_name)
            subdir_obj = self._subdirs_[sub_dir_name]
            subdir_obj.mkdir(nested_subdir_path)

    def addContentToFile(self, filePath: str, content: str):
        sub_dir_path = filePath[len(self._name_):]
        sep_loc = sub_dir_path.find("/")
        print(f"\t\t addContentToFile -- sub_dir_path:{sub_dir_path} \t current dir:{self._name_}")
        if sep_loc  == -1:
            print(f"\t\t addContentToFile file:{filePath} \t for path:{filePath}")
            if sub_dir_path not in self._files_.keys():
                self._files_[filePath] = File(filePath)
            file_obj = self._files_[filePath]
            file_obj.addContentToFile(content)
        else:
            sub_dir_name = sub_dir_path[:sep_loc]
            nested_subdir_path = sub_dir_path[sep_loc + 1:]
            print(f"\t\t addContentToFile subdir:{sub_dir_name} \t with nesstd subdir:{nested_subdir_path} \t for path:{filePath}")
            if sub_dir_name not in self._subdirs_.keys():
                self._subdirs_[sub_dir_name] = Dir(sub_dir_name)
            subdir_obj = self._subdirs_[sub_dir_name]
            subdir_obj.addContentToFile(nested_subdir_path, content)
    
class FileSystem:

    def __init__(self):
        self._root_ = Dir("/")

    def ls(self, path: str) -> list:
        return self._root_.ls(path)

    def mkdir(self, path: str) -> None:
        self._root_.mkdir(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self._root_.addContentToFile(filePath, content)

    def readContentFromFile(self, filePath: str) -> str:
        return self._root_.readContentFromFile(filePath)



# Your FileSystem object will be instantiated and called as such:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
def test_1():
    obj = FileSystem()
    path = "/"
    ls_output = obj.ls(path)
    print(f"\t ls_output({path}):{ls_output}")

    path = "/a/b/c"
    obj.mkdir(path)
    print(f"\t mkdir({path})")

    filepath = "/a/b/c/d"
    content = "hello"
    obj.addContentToFile(filepath, content)
    print(f"\t addContentToFile({filepath}):{content}")

    path = "/a/b"
    ls_output = obj.ls(path)
    print(f"\t ls_output({path}):{ls_output}")

    read_contents = obj.readContentFromFile(filepath)
    print(f"\t read_contents({filepath}):{read_contents}")

def test_2():
    # ["FileSystem",    "mkdir",    "ls",   "ls",           "mkdir",    "ls",   "ls",   "addContentToFile", "readContentFromFile",  "ls",   "readContentFromFile"]
    # [ [],         ["/zijzllb"],   ["/"],  ["/zijzllb"],   ["/r"],     ["/"],  ["/r"],["/zijzllb/hfktg","d"],["/zijzllb/hfktg"],["/"],["/zijzllb/hfktg"]]
    obj = FileSystem()
    obj.mkdir("/zijzllb")
    print(obj.ls("/"))
    print(obj.ls("/zijzllb"))
    obj.mkdir("/r")
    print(obj.ls("/r"))
    obj.addContentToFile("/zijzllb/hfktg","d")
    print("")
    print(obj.readContentFromFile("/zijzllb/hfktg"))
    print(obj.ls("/"))
    print(obj.readContentFromFile("/zijzllb/hfktg"))

if __name__ == "__main__":
    test_1()