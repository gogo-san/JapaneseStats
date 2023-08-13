import os
import pickle
import json

from .lib.ahocorapy.keywordtree import KeywordTree

'''
生成pickle序列化文件
''' 
addon_directory = os.path.dirname(__file__)

jlpt_file_path = os.path.join(addon_directory, 'jlpt.json')
jlpt_file = open(jlpt_file_path, encoding='utf_8_sig')
jlpt_data = json.load(jlpt_file)

kwtree = KeywordTree(case_insensitive=True)
#_表示临时变量，这里应该是只读走了word，没管key,因为tree只是用来看word存不存在的
for word, _ in jlpt_data.items(): 
    kwtree.add(word)
kwtree.finalize()  

kwtree_file = open("jlpt_tree.pickle", "wb")
pickle.dump(kwtree, kwtree_file)
kwtree_file.close()
