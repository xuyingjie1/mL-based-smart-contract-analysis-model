from deal_ast import getSourceUnit,getKeys
#import json_tools
import os.path
#分层
#将得到的AST树字典进行分层
def getInfo(output):
    for key in output.keys():
        if type(output[key])==list:
            for value in output[key]:
                getInfo(value)
        print(key,output[key])
#getInfo(output)

# c = (Tree().add("",output).set_global_opts(title_opts=op.TitleOpts(title="AST")).render("ast.html"))


if __name__ == '__main__':
    Path = "D:\\区块链\\smartbugs\\dataset\\arithmetic"
    files = os.listdir(Path)
    file1 = os.path.join(Path, files[1])
    output = getSourceUnit(file1)


