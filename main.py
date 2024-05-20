# данная cli будет использоваться только под торговлю сетом на биг дате. Максимально коннкретизируем задачу. Здесь не будет выбора режима торговли, построения гуи или еще чего.
# Просто торговля биг датой на сете настроек и сохранение в логи информации по торговли и в exel таблицу. Всё.
# Цель этой проги - получить оптимальные параметры для торговли в долгую. Вырабатать стратегию торговли для торговли в реале. 
# Сет формируется здесь же через режим - использовать готовый сет из файла, либо сформировать новый.

from imports import *

class Main:
    # Срабатывает при создании объекта
    def __init__(self):
        super().__init__()
        
        self.settings = {}


        # Первичные данные, настройки системы
        self.settings['MYDIR_TF'] = 'DF/big_data/'
        self.settings['MYDIR_1min'] = 'DF/big_data/1min/'
        self.settings['MYDIR_5min'] = 'DF/big_data/5min/'
        self.settings['MYDIR_15min'] = 'DF/big_data/15min/'
        self.settings['set_strat'] = 'set_settings/big_data/set_strat.txt'
        self.settings['how_mach_coin_trade'] = 20 # сколько монет торговать
        self.settings['work_tf'] = '5min' # рабочий таймфрейм
        self.settings['see_tf'] = '1min' # таймфрейм слежения
        self.settings['DEPOSIT'] = 100 # начальный депозит
        self.settings['LEVERAGE'] = 1 # плечо
        self.settings['COMMISSION_MAKER'] = 0.002 # комиссия мейкер
        self.settings['COMMISSION_TAKER'] = 0.001 # комиссия тейкер
        self.settings['VALUE_TRADE_MIN'] = 100000  # Объём минимальный в долларах
        self.settings['VALUE_TRADE_MAKS'] = 1000000 # Объём максимальный в долларах - диапазон
        self.settings['VALUE_TRADE_MIN_procent'] = 0.2 # процент объёма от дневного движения цены минимальный
        self.settings['VALUE_TRADE_MAKS_procent'] = 1 # процент объёма от дневного движения цены максимальный
        self.settings['TP'] = 0.012 # Тейк
        self.settings['SL'] = 0.02 # Стоп
        self.settings['TP_procent'] = 20 # Тейк в процентах
        self.settings['strategy_coin'] = 1 # стратения выбора монет

        self.settings['regime_set'] = 1 # 1 - использовать сет настреок из файла, 0 - сформировать сет настроек
        self.settings['regime_profit'] = 1 # Режим ТП и СЛ, 1 - фиксированный, 0 - Динамический
        self.settings['regime_volume'] = 1 # Режим объёмов, 1 - фиксированный, 0 - Динамический



        if self.settings['regime_set'] == 0:

        
















































if __name__ == "__main__":
    app = Main()