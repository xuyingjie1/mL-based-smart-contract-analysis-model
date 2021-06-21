from deal_ast import getAst,getKeys,getSourceUnit
from get_param import get_somorphism,traverse
import pandas as pd
import os
#选择相应的漏洞的实验数据集
Path1 = "/home/itko/桌面/论文项目/experimental data set/Unchecked-Send"
#对应基本漏洞的基本漏洞数据集
Path2 = "/home/itko/桌面/论文项目/malicious smart contract data set/unchecked_low_level_calls"
#随机选择一些无关的智能合约作为负样本
Path3 = "/home/itko/桌面/论文项目/experimental data set/Re-entrancy"
files = os.listdir(Path1)
files_1 = os.listdir(Path3)
test_files = list(filter(lambda x: ".sol" in x, files))
test_files_1 = list(filter(lambda x: ".sol" in x, files_1))
train_files = os.listdir(Path2)

#第一类处理:
number2 = []


def get_data(test_files, train_files):
    for file1 in test_files:
        try:
            ast_test = getSourceUnit(os.path.join(Path1,file1))
            number = []
            ast_list_1 = []
            traverse(ast_test,ast_list_1)
            for file2 in train_files:
                ast_train = getSourceUnit(os.path.join(Path2,file2))
                ast_list_2 = []
                traverse(ast_train,ast_list_2)
                num = get_somorphism(ast_list_2,ast_list_1)
                number.append(num[0])
            number2.append(number)
        except UnicodeDecodeError:
            pass
    return len(number2)


if __name__ == '__main__':
    get_data(test_files,train_files)
    get_data(test_files,train_files)
    data = pd.DataFrame(number2)
    data.to_csv("solidity7.csv")

