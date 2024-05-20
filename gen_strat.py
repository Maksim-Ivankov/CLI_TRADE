

from imports import *


class Gen_strat(object):
    """docstring for ClassName."""
    def __init__(self, settings):
        super(Gen_strat, self).__init__()

        self.settings = settings

        self.HOW_MACH_SET = self.settings['HOW_MACH_SET'] # размер сета нсатроек

        if self.settings['regime_profit'] == 1: # если режим профита фиксированный
            self.TP = '0.005,0.008,0.01,0.012,0.014,0.016,0.018,0.02'
            self.SL = '0.005,0.008,0.01,0.012,0.014,0.016,0.018,0.02'
        if self.settings['regime_profit'] == 1: # если режим профита динамический
            self.TP = '2,4,6,8,10,12,14,16,18,20,25'
            self.SL = '0.005,0.008,0.01,0.012,0.014,0.016,0.018,0.02'
        if self.settings['regime_volume'] == 1: # если режим объёмов фиксированный
            self.VALUE_TRADE_MIN = '50000,100000,200000,400000' # объём торговли мин в $
            self.VALUE_TRADE_MAKS = '600000,800000,1000000,1400000,1800000,2200000,5000000' # объём торговли макс в $
        if self.settings['regime_volume'] == 0: # если режим объёмов динамический
            self.VALUE_TRADE_MIN = '0.2,0.4,0.6,0.8' # объём динамический процент
            self.VALUE_TRADE_MAKS = '1.2,1.4,1.6,1.8,2' # объём динамический процент
        self.CANAL_MAX = '0.7,0.75,0.8,0.85,0.9' # нахождение внутри канала сверху
        self.CANAL_MIN = '0.1,0.2,0.3,0.4' # нахождение внутри канала снизу
        self.LEVERAGE = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20'

        open(self.settings['set_strat'], "w").close() # очищаем файл перед новой записью
        for i in range(self.HOW_MACH_SET):
            self.generate_to_file()





    def generate_to_file(self):
        self.CANAL_MAX_gen = random.choice(self.CANAL_MAX.split(','))
        self.CANAL_MIN_gen = random.choice(self.CANAL_MIN.split(','))
        self.VALUE_TRADE_MIN_gen = random.choice(self.VALUE_TRADE_MIN.split(','))
        self.VALUE_TRADE_MAKS_gen = random.choice(self.VALUE_TRADE_MAKS.split(','))
        self.TP_gen = random.choice(self.TP.split(','))
        self.SL_gen = random.choice(self.SL.split(','))
        self.LEVERAGE_gen = random.choice(self.SL.split(','))

        str_settings=f'{self.CANAL_MAX_gen},{self.CANAL_MIN_gen},{self.VALUE_TRADE_MIN_gen},{self.VALUE_TRADE_MAKS_gen},{self.TP_gen},{self.SL_gen},{self.LEVERAGE_gen}'

        f = open(self.settings['set_strat'],'a',encoding='utf-8')
        f.write('\n'+str_settings)
        f.close()










































































