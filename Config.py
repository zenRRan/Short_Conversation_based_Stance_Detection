#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@author: 'zenRRan'
@license: Apache Licence 
@contact: zenrran@qq.com
@software: PyCharm
@file: Config.py
@time: 2018/3/5 14:08
"""

from configparser import ConfigParser
from HyperParams import HyperParams

class Config2HyperParams(object):
    def __init__(self, config_file):
        self.config = ConfigParser()
        self.HyperParams = HyperParams()
        self.config.read(config_file)

        '''
        Parameters load
        '''
        self.HyperParams.embed_size = self.config.getint('Parameters', 'embed_size')
        self.HyperParams.Steps = self.config.getint('Parameters', 'Steps')
        self.HyperParams.lr = self.config.getfloat('Parameters', 'lr')
        self.HyperParams.dropout = self.config.getfloat('Parameters', 'dropout')
        self.HyperParams.batch_size = self.config.getint('Parameters', 'batch_size')
        self.HyperParams.word_cut_off = self.config.getint('Parameters', 'word_cut_off')
        self.HyperParams.decay = self.config.getfloat('Parameters', 'decay')
        self.HyperParams.lr_decay = self.config.getfloat('Parameters', 'lr_decay')
        self.HyperParams.clip_grad = self.config.getfloat('Parameters', 'clip_grad')

        '''
        pre_train load
        '''
        self.HyperParams.pred_emd_dim = self.config.getint('pre_train_load', 'pred_emd_dim')
        self.HyperParams.using_English_data = self.config.getboolean('pre_train_load', 'using_English_data')
        self.HyperParams.using_Chinese_data = self.config.getboolean('pre_train_load', 'using_Chinese_data')
        self.HyperParams.pred_emd_dim = self.config.getint('pre_train_load', 'pred_emd_dim')

        '''
        Network load
        '''
        self.HyperParams.biLSTM = self.config.getboolean('Network', 'biLSTM')
        self.HyperParams.biLSTM_hidden_num = self.config.getint('Network', 'biLSTM_hidden_num')
        self.HyperParams.biLSTM_hidden_size = self.config.getint('Network', 'biLSTM_hidden_size')

        self.HyperParams.biGRU = self.config.getboolean('Network', 'biGRU')
        self.HyperParams.biGRU_hidden_num = self.config.getint('Network', 'biGRU_hidden_num')
        self.HyperParams.biGRU_hidden_size = self.config.getint('Network', 'biGRU_hidden_size')

        self.HyperParams.CNN = self.config.getboolean('Network', 'CNN')
        self.HyperParams.kernel_sizes = self.config.getint('Network', 'kernel_sizes')
        self.HyperParams.kernel_num = self.config.getint('Network', 'kernel_num')

        '''
        Optimizer
        '''
        self.HyperParams.Adam = self.config.getboolean('Optimizer', 'Adam')
        self.HyperParams.SGD = self.config.getboolean('Optimizer', 'SGD')

        '''
        Path
        '''
        self.HyperParams.main_address = self.config.get('Path', 'main_address')
        self.HyperParams.chn_pred_embedding_path = self.config.get('Path', 'chn_pred_embedding_path')
        self.HyperParams.eng_pred_embedding_path = self.config.get('Path', 'eng_pred_embedding_path')
        self.HyperParams.dev_file = self.config.get('Path', 'dev_file')
        self.HyperParams.write_file_name = self.config.get('Path', 'write_file_name')
        self.HyperParams.train_file = self.config.get('Path', 'train_file')
        self.HyperParams.test_file = self.config.get('Path', 'test_file')
        self.HyperParams.save_pred_emd_path = self.config.get('Path', 'save_pred_emd_path')


        print('loaded config file!')


