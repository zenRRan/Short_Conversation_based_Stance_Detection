
#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@author: 'zenRRan'
@license: Apache Licence 
@contact: zenrran@qq.com
@software: PyCharm
@file: test.py
@time: 2018/4/30 14:34
"""

import HyperParams
from HyperParams import Alphabet
from torch.autograd import Variable
from Common import *
import torch
import jieba
import tkinter as tk



def seq2id(seq, word_alpha):
    id = []
    for word in seq:
        degit = word_alpha.from_string(word)
        if degit >= 0:
            id.append(degit)
        else:
            id.append(word_alpha.from_string(unk_key))
    return id




if __name__ == '__main__':
    window = tk.Tk()
    # window.size()
    window.geometry('400x300')
    word_dic_path = './word_dic.txt'
    label_dic_path = './label_dic.txt'
    word_alpha = Alphabet()
    label_alpha = Alphabet()
    word_alpha.read(word_dic_path)
    label_alpha.read(label_dic_path)
    fmodel = './Module/0.params'
    model = torch.load(fmodel)


    def prediction():
        show_label.config(text='')
        post = post_entry.get()
        response = response_entry.get()
        if post == '' and response == '':
            show_label.config(text=pr_wrong)
            return
        if post == '':
            show_label.config(text=post_wrong)
            return
        if response == '':
            show_label.config(text=response_wrong)
            return
        # post = input('post:')
        # response = input('response:')
        post = jieba.cut(post)
        response = jieba.cut(response)
        post = ' '.join(post)
        # print(post)
        response = ' '.join(response)
        post = seq2id(post, word_alpha)
        response = seq2id(response, word_alpha)
        post = Variable(torch.LongTensor([post]))
        response = Variable(torch.LongTensor([response]))
        pred = model(post, response)
        label_idx = (torch.max(pred, 1)[1]).data.sum()
        # print((torch.max(pred, 1)))
        stance = label_alpha.id2string[label_idx]
        if stance == 'n':
            show_label.config(text='反对博主立场！')
            # print('反对博主立场！')
        elif stance == 'm':
            show_label.config(text='既不支持也不反对！')
            # print('既不支持也不反对！')
        else:
            # print('支持博主立场！')
            show_label.config(text='支持博主立场！')
        # print('---------------------------------------------')


    post_label = tk.Label(window, text='post:')
    response_label = tk.Label(window, text='response:')
    post_entry = tk.Entry(window)
    response_entry = tk.Entry(window)
    btn = tk.Button(window, text='predict', command=prediction)
    show_label = tk.Label(window)
    post_wrong = 'please input post!'
    response_wrong = 'please input response!'
    pr_wrong = 'please input post and response first!'

    post_label.pack()
    post_entry.pack()
    response_label.pack()
    response_entry.pack()
    show_label.pack()
    btn.pack()
    window.mainloop()

# while(True):


'''
蔬菜晚礼服，好漂亮，太有创意了！
太有创意受不了。

这配乐！这表演都太精彩了简直是神人组合！
合成之美，节奏之美。

今天天气真的很不错啊  祝大家旅愉快途
谢谢你  我们玩的很开心的呢

今天天气真好
嗯呐 我也这么觉得
'''

