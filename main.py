# данная cli будет использоваться только под торговлю сетом на биг дате. Максимально коннкретизируем задачу. Здесь не будет выбора режима торговли, построения гуи или еще чего.
# Просто торговля биг датой на сете настроек и сохранение в логи информации по торговли и в exel таблицу. Всё.
# Цель этой проги - получить оптимальные параметры для торговли в долгую. Вырабатать стратегию торговли для торговли в реале. 
# Сет формируется здесь же через режим - использовать готовый сет из файла, либо сформировать новый.

from imports import *
from gen_strat import Gen_strat

class Main:
    # Срабатывает при создании объекта
    def __init__(self):
        super().__init__()
        
        self.settings = {}

        # Первичные данные, настройки системы
        self.settings['MYDIR_TF'] = 'big_data/'
        self.settings['MYDIR_1min'] = 'big_data/1min/'
        self.settings['MYDIR_5min'] = 'big_data/5min/'
        self.settings['MYDIR_15min'] = 'big_data/15min/'
        self.settings['set_strat'] = 'big_data/set_strat.txt'
        self.settings['how_mach_coin_trade'] = 20 # сколько монет торговать
        self.settings['HOW_MACH_SET'] = 20 # сколько настроек сгенерировать
        self.settings['how_mach_coin_trade_start'] = 5 # c какой по счету монеты торговать из отсортированного списка
        self.settings['DEPOSIT'] = 100 # начальный депозит
        self.settings['COMMISSION_MAKER'] = 0.002 # комиссия мейкер
        self.settings['COMMISSION_TAKER'] = 0.001 # комиссия тейкер

        self.settings['strategy_coin'] = 1 # стратения выбора монет
        self.settings['regime_set'] = 1 # 1 - использовать сет настреок из файла, 0 - сформировать сет настроек
        self.settings['regime_profit'] = 1 # Режим ТП и СЛ, 1 - фиксированный, 0 - Динамический
        self.settings['regime_volume'] = 1 # Режим объёмов, 1 - фиксированный, 0 - Динамический

        # вспомогательные переменные
        self.set_settings_once = []
        self.count_settings = 0
        self.set_settings = {} # здесь хранится сет настроек в виде словаря

        self.get_set_settings() # получаем сет настроек в словарь 




    # генерирует сет настроек в файл, если режим 0 или берет сет из файла при режиме 1, сохраняет данные в словарь set_settings 
    def get_set_settings(self):
        if self.settings['regime_set'] == 0: # если режим = 0 (сормировать сет натсроек)
            Gen_strat(self.settings) # то формируем настройки в файл
        with open(self.settings['set_strat'],encoding='utf-8') as file: # получаем данные из файла сета настроек
            for line in file:
               if line.rstrip()!='': # если строка не пустая
                    self.set_settings_once = line.rstrip().split(',') # то добавляем настройки в массив
                    self.set_settings[self.count_settings] = {}
                    self.set_settings[self.count_settings]['CANAL_MAX'] = self.set_settings_once[0]
                    self.set_settings[self.count_settings]['CANAL_MIN'] = self.set_settings_once[1]
                    self.set_settings[self.count_settings]['VALUE_TRADE_MIN'] = self.set_settings_once[2]
                    self.set_settings[self.count_settings]['VALUE_TRADE_MAKS'] = self.set_settings_once[3]
                    self.set_settings[self.count_settings]['TP'] = self.set_settings_once[4]
                    self.set_settings[self.count_settings]['SL'] = self.set_settings_once[5]
                    self.set_settings[self.count_settings]['LEVERAGE'] = self.set_settings_once[6]

                    self.count_settings+=1
                   

















































if __name__ == "__main__":
    app = Main()