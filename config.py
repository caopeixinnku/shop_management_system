# -*- coding=utf-8 -*-
import os
class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass

# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://TestUser:caopeixin628@127.0.0.1:3306/dbsclab2020?charset=utf8'
    DEBUG = True

# define the config
config = {
    'default': DevelopmentConfig
}
