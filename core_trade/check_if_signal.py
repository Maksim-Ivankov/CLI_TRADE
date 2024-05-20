# проверяем, есть ли сигнал
import os
import sys
sys.path.insert(1,os.path.join(sys.path[0],'../../'))
from imports import *
from core_trade.strat import Strat


class Сheck_if_signal:
    def __init__(self,df,settings):
        self.df = df
        self.settings = settings

    def work_strat_trade(self):
        result_strat = Strat(self.df,self.settings)
        print(result_strat)
        return result_strat.check_signal()
        




























