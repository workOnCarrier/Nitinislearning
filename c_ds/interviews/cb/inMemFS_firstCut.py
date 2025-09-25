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
            sub_path = path[len(self._name_) + 1:] # drop current name and the /
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
                    nested_sub_path = sub_path[sep_loc + 1:]
                    if sub_dir_obj:
                        return sub_dir_obj.ls(nested_sub_path)
        else:
            result = [s._name_ for s in self._subdirs_]
            for f in self._files_.keys():
                result.append(f)
            return result
        
    def readContentFromFile(self, path: str):
        # if the file name terminates in this dir
        sub_dir_path = path[len(self._name_) + 1:]
        if len(sub_dir_path) == 0:
            return
        sep_loc = sub_dir_path.find("/")
        if sep_loc  == -1:
            # file exists in curr dir -- return the contents of the file
            sub_file_name = sub_dir_path
            if sub_file_name not in self._files_.keys():
                raise Exception("file not found")
            file_obj = self._files_[sub_file_name]
            return file_obj.readContentFromFile()
        else:
            sub_dir_name = sub_dir_path[:sep_loc]
            nested_subdir_path = sub_dir_path[sep_loc + 1:]
            if sub_dir_name not in self._subdirs_.keys():
                raise Exception("sub dir path not found")
            subdir_obj = self._subdirs_[sub_dir_name]
            return subdir_obj.readContentFromFile(nested_subdir_path)

    def mkdir(self, path):
        sub_dir_path = path[len(self._name_) + 1:]
        if len(sub_dir_path) == 0:
            return
        sep_loc = sub_dir_path.find("/")
        if sep_loc  == -1:
            sub_dir_name = sub_dir_path
            if sub_dir_name not in self._subdirs_.keys():
                self._subdirs_[sub_dir_name] = Dir(sub_dir_name)
        else:
            sub_dir_name = sub_dir_path[:sep_loc]
            nested_subdir_path = sub_dir_path[sep_loc + 1:]
            if sub_dir_name not in self._subdirs_.keys():
                self._subdirs_[sub_dir_name] = Dir(sub_dir_name)
            subdir_obj = self._subdirs_[sub_dir_name]
            subdir_obj.mkdir(nested_subdir_path)

    def addContentToFile(self, filePath: str, content: str):
        sub_dir_path = filePath[len(self._name_) + 1:]
        if len(sub_dir_path) == 0:
            return
        sep_loc = sub_dir_path.find("/")
        if sep_loc  == -1:
            if sub_dir_path not in self._files_.keys():
                self._files_[sub_dir_path] = File(sub_dir_path)
            file_obj = self._files_[sub_dir_path]
            file_obj.addContentToFile(content)
        else:
            sub_dir_name = sub_dir_path[:sep_loc]
            nested_subdir_path = sub_dir_path[sep_loc + 1:]
            if sub_dir_name not in self._subdirs_.keys():
                self._subdirs_[sub_dir_name] = Dir(sub_dir_name)
            subdir_obj = self._subdirs_[sub_dir_name]
            subdir_obj.addContentToFile(nested_subdir_path, content)
    
class FileSystem:

    def __init__(self):
        self._root_ = Dir("/")

    def ls(self, path: str) -> List[str]:
        self._root_.ls(path)

    def mkdir(self, path: str) -> None:
        self._root_.mkdir(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self._root_.addContentToFile(filePath, content)

    def readContentFromFile(self, filePath: str) -> str:
        self._root_.readContentFromFile(filePath)


# Your FileSystem object will be instantiated and called as such:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
def test():
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

if __name__ == "__main__":
    test()