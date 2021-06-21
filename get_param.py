import os
import json_tools
from solidity_parser import parser
Path2 = "/home/itko/桌面/论文项目/experimental data set/TOD"
Path1 = "/home/itko/桌面/论文项目/experimental data set/TOD"
Path3 = "/home/itko/桌面/论文项目/experimental data set/TOD"
Path4 = "/home/itko/桌面/论文项目/experimental data set/TOD"
file1  =  os.path.join(Path2,os.listdir(Path2)[2])
file2  =  os.path.join(Path1,os.listdir(Path1)[15])
ast_1 = dict(parser.parse_file(file1))
ast_2 = dict(parser.parse_file(file2))
def traverse(ast,values,currentKey=None):
    if isinstance(ast,list):
        for i in ast:
            traverse(i,values,currentKey)
    elif isinstance(ast,dict):
        for key,value in ast.items():
            traverse(value,values,key)
    else:
        values.append([currentKey,ast])
#print(vaules_2)
def get_somorphism(ast_value,ast_value1):
    count = 0
    vaule = []
    for node in ast_value1:
        if node in ast_value:
            if node[0] == "operator" :
                count+=1
                vaule.append(node)
            if node[0] == "type" and node[1] == "BinaryOperation":
                count+=1
                vaule.append(node)
    return count/len(ast_value1),vaule
if __name__ == "__main__":
    vaule1 = []
    traverse(ast_1,vaule1)
    vaule2 = []
    traverse(ast_2,vaule2)
    print(get_somorphism(vaule1,vaule2)[1])
