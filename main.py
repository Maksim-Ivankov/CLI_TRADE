# данная cli будет использоваться только под торговлю сетом на биг дате. Максимально коннкретизируем задачу. Здесь не будет выбора режима торговли, построения гуи или еще чего.
# Просто торговля биг датой на сете настроек и сохранение в логи информации по торговли и в exel таблицу. Всё.
# Цель этой проги - получить оптимальные параметры для торговли в долгую. Вырабатать стратегию торговли для торговли в реале. 
# Сет формируется здесь же через режим - использовать готовый сет из файла, либо сформировать новый.

from imports import *
from gen_strat import Gen_strat
from core_trade.core_trade import Core_trade

class Main:
    # Срабатывает при создании объекта
    def __init__(self):
        super().__init__()
        
        self.settings = {}

        # Первичные данные, настройки системы
        self.settings['MYDIR_1min'] = 'big_data/1min/'
        self.settings['MYDIR_5min'] = 'big_data/5min/'
        self.settings['MYDIR_TF'] = self.settings['MYDIR_5min'] # рабочий таймфрейм
        self.settings['MYDIR_15min'] = 'big_data/15min/'
        self.settings['set_strat'] = 'big_data/set_strat.txt'
        self.settings['how_mach_coin_trade'] = 20 # сколько монет торговать
        self.settings['HOW_MACH_SET'] = 20 # сколько настроек сгенерировать
        self.settings['how_mach_coin_trade_start'] = 20 # c какой по счету монеты торговать из отсортированного списка
        self.settings['DEPOSIT'] = 100 # начальный депозит
        self.settings['COMMISSION_MAKER'] = 0.002 # комиссия мейкер
        self.settings['COMMISSION_TAKER'] = 0.001 # комиссия тейкер


        self.settings['strategy_coin'] = 1 # стратения выбора монет 1- по объёму, 2 - по проценту движения
        self.settings['regime_set'] = 1 # 1 - использовать сет настреок из файла, 0 - сформировать сет настроек
        self.settings['regime_profit'] = 1 # Режим ТП и СЛ, 1 - фиксированный, 0 - Динамический
        self.settings['regime_volume'] = 1 # Режим объёмов, 1 - фиксированный, 0 - Динамический

        # вспомогательные переменные
        self.set_settings_once = []
        self.count_settings = 0
        self.set_settings = {} # здесь хранится сет настроек в виде словаря
        tp_sl_dinamic = {} # динамические тейк профит и стоп лосс
        VOLUME_dinamic = {} # динамические объёмы

        self.get_set_settings() # получаем сет настроек в словарь set_settings

        for i in range(len(self.set_settings)): # итерируемся по кол-ву настроек в сете настроек
            # self.set_settings[i] - натсройки текущего шага итерации
            if i>0: # начинаем торговать со второго дня в сете, за первый день собираем монеты для торговли
                self.settings['coins_worker'] = self.get_mass_coin_for_strategy(i) # получаем список монет, с которыми будем работать сегодня

                for coin in self.settings['coins_worker']:
                    if self.settings['regime_set_trade_profit'] == "Динамический":
                        tp_sl_dinamic[coin] = self.cslculat_dinamic_TP_SL(pd.read_csv(f'{self.settings['MYDIR_15min']}{i-1}/{coin}.csv')) # вычисляем динамические TP и SL для одной монеты 'BTCUSDT': [0.05,0.02] и так по каждой монете
                    if self.settings['regime_set_trade_volume'] == "Динамический":
                        VOLUME_dinamic[coin] = self.cslculat_dinamic_VALUE(pd.read_csv(f'{self.settings['MYDIR_15min']}{i-1}/{coin}.csv')) # вычисляем динамические объёмы для одной монеты 'BTCUSDT': [6500512,415515125] и так по каждой монете


                self.finish_trade = self.colbeak_etap # функция, которая срабатывает при выполнении одного этапа торговли - по одной натсройке
                self.trade_start = Core_trade(self.master,self.settings) # создаем экземпляр класса ядра торговли
                self.trade_start.start_trade(self.finish_trade) # стартуем ядро  торговли





    # колбэк из ядра торговли
    def colbeak_etap(self,data_final):
        print('Закончили этап торговли')
        self.data_final = data_final

    # считаем динамические объёмы для одной омнеты по датафрейму
    def cslculat_dinamic_VALUE(self,df):
        VOLUME_coin = 0
        for nonindex, row in df.iterrows():
            VOLUME_coin=VOLUME_coin+row['VOLUME']*row['open']
        return [VOLUME_coin*self.settings['VALUE_TRADE_MIN']/100,VOLUME_coin*self.settings['VALUE_TRADE_MAKS']/100]

    # счтаем динамический тейк и стоп для одной омнеты по датафрейму
    def cslculat_dinamic_TP_SL(self,df):
        my_max = df['open'].loc[df['open'].idxmax()]
        my_min = df['close'].loc[df['close'].idxmin()]
        moving = 1-(my_min/my_max)
        return [moving*self.settings['TP']/100,self.settings['SL']]

    # получаем массив монет, которые будем торговать сегодня
    def get_mass_coin_for_strategy(self,day):
        arr = next(os.walk(f'{self.settings['MYDIR_15min']}{day-1}/'))[2]
        result_coin_spisok = []
        result = []
        for i in range(len(arr)):
            arr[i] = arr[i][:-4]
        if self.settings['strategy_coin'] == 1: # выбор монет по объёму за прошлый день
            for coin in arr:
                df = pd.read_csv(f'{self.settings['MYDIR_15min']}{day-1}/{coin}.csv')
                VOLUME_coin = 0
                for nonindex, row in df.iterrows():
                    VOLUME_coin=VOLUME_coin+row['VOLUME']*row['open']
                result_coin_spisok.append([coin,VOLUME_coin])
            result_coin_spisok.sort(key = lambda x: x[1], reverse=True)
            for i in range(self.settings['how_mach_coin_trade_start'],self.settings['how_mach_coin_trade_start']+int(self.settings['how_mach_coin_trade'])):   
                result.append(result_coin_spisok[i][0])
        if self.settings['strategy_coin'] == 2:  # выбор монет по проценту движения за день
            for coin in arr:
                df = pd.read_csv(f'{self.settings['MYDIR_15min']}{day-1}/{coin}.csv')
                my_max = df['open'].loc[df['open'].idxmax()]
                my_min = df['open'].loc[df['open'].idxmin()]
                moving = 1-(my_min/my_max)
                result_coin_spisok.append([coin,moving])
            result_coin_spisok.sort(key = lambda x: x[1], reverse=True)
            for i in range(self.settings['how_mach_coin_trade_start'],self.settings['how_mach_coin_trade_start']+int(self.settings['how_mach_coin_trade'])):
                result.append(result_coin_spisok[i][0])
        
        df_work = pd.read_csv(f'{self.settings['MYDIR_TF']}0/{result[0]}.csv') # получили датафрейм из файла
        df_see = pd.read_csv(f'{self.settings['MYDIR_1min']}0/{result[0]}.csv') # получили датафрейм из файла
        self.settings['VOLUME'] = len(df_work) # сохраняем объёмы фреймов раочего
        self.settings['VOLUME_5MIN'] = len(df_see) # сохраняем объёмы фреймов слежения
        return(result)
        
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