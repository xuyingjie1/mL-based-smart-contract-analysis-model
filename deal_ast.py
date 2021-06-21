import os
import solcx
#import solcast
from solidity_parser import parser
import json
# 获取智能合约的ast树结构,返回字典数据类型,使用pysolc获取ast树结构
def getAst(Path):
    source = solcx.compile_files([Path],
                             output_values=["ast"],
                             solc_version="0.4.25")
    key = list(source.keys())[0]
    ast = source[key]["ast"]
    return dict(ast)
#获取该ast树的所有结点
node = []
def getKeys(ast,node):
    if type(ast) == dict:
        for key in ast.keys():
            node.append(key)
            getKeys(ast[key],node)
    elif type(ast) == list:
        for key in ast:
            getKeys(key,node)
# 获取智能合约的
def getSourceUnit(Path):
    sourceUnit = parser.parse_file(Path)
    return dict(sourceUnit)
if __name__ == '__main__':

    #output1 = getAst(file2)

    Path = "D:\\区块链\\smartbugs\\dataset\\arithmetic"
    Path1 = "D:\\区块链\\SolidiFI-benchmark\\buggy_contracts\\Overflow-Underflow"
    files = os.listdir(Path)
    files_2 = os.listdir(Path1)
    file1 = os.path.join(Path, files[4])
    file2 = os.path.join(Path1, files_2[3])
    output = getSourceUnit(file1)
    print(json.dumps(output,ensure_ascii=False,indent=4))
    #print(output1)
#sourceUnitObject = parser.objectify(output)
#获取pragmas参数指令
#print(sourceUnitObject.pragmas)
#获取一个sol文件中所有合同名称
#print(sourceUnitObject.contracts.keys())
#print(sourceUnitObject.contracts.values())
#获取一个合同中的所有函数名称
#contract = list(sourceUnitObject.contracts.keys())[0]
#获取一个合同中对应函数的权限
#functions = list(sourceUnitObject.contracts[contract].functions.keys())[0]
#print(sourceUnitObject.contracts[contract].functions[functions].visibility)
#print(sourceUnitObject.contracts[contract].functions[functions].stateMutability)
#获取一个合同中的状态变量
#print(sourceUnitObject.contracts[contract].stateVars)
#node1 = getKeys(output,node)
#print(node)
#print(ast)





