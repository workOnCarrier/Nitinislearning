class File:
    def __init__(self, name):
        self._name_ = name
        self._content_ = ""

    def ls(self):
        return self._name_
    def addContentToFile(self, content: str) -> None:
        self._content_ += content
    def readContentFromFile(self) -> str:
        return self._content_

class Dir:
    def __init__(self, name):
        self._name_ = name
        self._dirs_ = {}
        self._files_ = {}
    def ls(self, path:str = None):
        if path:
            sub_path = path[len(self._name_):]
            sep_loc = sub_path.find("/")
            if sep_loc != -1:
                nested_sub_path = sub_path[sep_loc + 1:]
                next_dir = sub_path[:sep_loc] 
                if next_dir not in self._dirs_.keys():
                    raise Exception(f" expected path is not correct")
                next_dir_obj = self._dirs_[next_dir]
                next_dir_obj.ls(nested_sub_path)
            else:
                sub_file_dir = sub_path[1:]
                if sub_file_dir in self._dirs_.keys():
                    sub_dir_obj = self._dirs_[sub_file_dir]
                    return sub_dir_obj.ls()
                else:
                    return sub_file_dir
        else:
            result = [d for d in self._dirs_.keys()]
            for f in self._files_.keys():
                result.append(f)
            return sorted[result]

    def addContentToFile(self, filePath: str, content: str) -> None:
        
    def readContentFromFile(self, filePath: str) -> str:
        return 
    def mkdir(self, path: str ) -> None:
        sub_path = path[len(self._name_):]
        sep_loc = sub_path.find("/")
        if sep_loc != -1:
            nested_sub_path = sub_path[sep_loc + 1:]
            next_dir = sub_path[:sep_loc] 
            if len(nested_sub_path) == 0:
                self._dirs_[next_dir] = Dir(next_dir)
            else:
                if next_dir not in self._dirs_.keys():
                    self._dirs_[next_dir] = Dir(next_dir)
                self._dirs_[next_dir].mkdir(nested_sub_path)
        else:
            # this should not happen
            pass 

class FileSystem:

    def __init__(self):
        self.root = Dir("/")
        

    def ls(self, path: str) -> List[str]:
        return self.root.ls(path)
        

    def mkdir(self, path: str) -> None:
        self.root.mkdir(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.root.addContentToFile(filePath, content)
        

    def readContentFromFile(self, filePath: str) -> str:
        return self.root.readContentFromFile(filePath)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
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