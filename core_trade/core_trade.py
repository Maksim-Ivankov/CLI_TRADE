# ядро исторической торговли на 1 сете

import os
import sys
sys.path.insert(1,os.path.join(sys.path[0],'../../'))
from imports import *
from core_trade.check_if_signal import Сheck_if_signal




class Core_trade:
    def __init__(self,settings,set_settings):

        self.settings = settings # здесь общие переменные
        self.set_settings = set_settings # здесь держим текущие настройки торговли

        self.DEPOSIT = self.settings['DEPOSIT'] # Депозит
        self.LEVERAGE = self.set_settings['LEVERAGE'] # торговое плечо
        self.COMMISSION_MAKER = self.settings['COMMISSION_MAKER'] # комиссия а вход
        self.COMMISSION_TAKER = self.settings['COMMISSION_TAKER'] # комиссия на выхд
        self.VOLUME = self.settings['VOLUME'] # сколько свечей получить при запросе к бирже
        self.VOLUME_5MIN = self.settings['VOLUME_5MIN'] # сколько свечей получить в режиме слежения за цено
        self.MYDIR_5MIN = self.settings['MYDIR_1min']
        self.MYDIR_WORKER = self.settings['MYDIR_TF']

        self.DEPOSIT_GLOBAL = self.DEPOSIT
        self.DEPOSIT_START_GLOBAAL = self.settings['DEPOSIT_START']
        self.DEPOSIT_START = self.DEPOSIT_GLOBAL

        # вспомогательные переменные
        self.trade_param = {}
        self.data_numbers = []
        self.INDEX_START = 20
        self.trade_final = {}
        self.sdelky_trade_final = {}
        self.count_trade = 0


    def start_trade(self,def_finish):
        self.trade_param['sost_trade'] = False # сейчас не стоим в сделке
        self.calculation_step_df(self.settings['coins_worker'][0])  # считаем шаг отставания фреймов
        for index in range(self.VOLUME):
            self.settings['index_trade_in_day'] = index
            self.trade_param['index_work'] = index
            self.data_numbers.append(index) # добавляем в массив номера итераций - 0,1,2,3 - имитируем реальную торговлю
            self.trade_param['data_numbers'] = self.data_numbers
            self.trade_param['index_trade'] = index
            if index>self.INDEX_START: # начинаем не с нуля, а с 20-ой свечи
                if self.trade_param['sost_trade'] == False: # если нет позиции
                    try:
                        for x,result in enumerate(self.settings['coins_worker']):
                            df = pd.read_csv(f'{self.settings['MYDIR_TF']}{self.settings['day_trade']}/{result}.csv') # получили датафрейм из файла
                            self.trade_param['coin'] = result # монета, которую сейча срассматриваем
                            self.trade_param['df_now_step'] = df.iloc[self.data_numbers] # фрейм по текущий шаг иетрации по текущей монете
                            vol_min_here = self.set_settings['VALUE_TRADE_MIN']
                            vol_max_here = self.set_settings['VALUE_TRADE_MAKS']
                            if self.settings['regime_volume'] == 0: # если режим объёмов динамический
                                vol_min_here = self.settings['VOLUME_dinamic'][self.trade_param['coin']][0]
                                vol_max_here = self.settings['VOLUME_dinamic'][self.trade_param['coin']][1]
                            if self.trade_param['df_now_step']['VOLUME'][index]*self.trade_param['df_now_step']['open'][index]>int(vol_min_here) and self.trade_param['df_now_step']['VOLUME'][index]*self.trade_param['df_now_step']['open'][index]<int(vol_max_here):
                                check_signal = Сheck_if_signal(self.trade_param['df_now_step'],self.settings) # определяем тренд - 
                                self.trade_param['trend'] = check_signal.work_strat_trade() # определяем тренд - 
                                if self.trade_param['trend'] != 'нет сигнала': # если есть сигнал
                                    self.count_trade = self.count_trade + 1 # счетчик сделок
                                    self.trade_param['index_trade_for_final'] = index
                                    break
                                else:
                                    self.trade_param['trend'] = "нет сигнала"  
                            else:
                                self.trade_param['trend'] = "нет сигнала"  
                        # если получили сигнал и объём за свечку больше минимального объема (настройка) и меншье максимального объёма (настройка)  
                        if self.trade_param['trend'] != "нет сигнала":
                            # если есть сигнал, то открываем позицию - направление, объём, цена входа, c
                            self.trade_param['price_treyd'] = self.trade_param['df_now_step']['close'][index] #цена входа в сделку
                            self.trade_param['open_time_trade'] = self.trade_param['df_now_step']['open_time'][index] # время открытия сделки
                            self.open_position() # открываем позицию 
                            continue
                    except Exception as e:
                        print(f'Ошибка ядра торговли - {e}')
                else:
                    try:
                        df_see = pd.read_csv(f'{self.settings['MYDIR_1min']}{self.settings['day_trade']}/{self.trade_param['coin']}.csv') # получаем фрейм слежения по монете в сделке
                        self.trade_param['df_see'] = df_see.iloc[int(self.search_step_see(self.trade_param['index_trade'])):int(self.search_step_see(self.trade_param['index_trade'])+self.trade_param['timeframe'])] # получили датафрейм мини из файла
                    except Exception as e:
                        print(f'Находимся в конце фрейма, не успеваем выйти из сделки - {e}')
                    for nonindex, row in self.trade_param['df_see'].iterrows():
                        TP_here = self.set_settings['TP']
                        SL_here = self.set_settings['SL']
                        if self.settings['regime_profit'] == 0:
                            TP_here = self.settings['tp_sl_dinamic'][self.trade_param['coin']][0]
                            SL_here = self.settings['tp_sl_dinamic'][self.trade_param['coin']][1]
                        if self.check_trade(row['close'],self.COMMISSION_MAKER,self.COMMISSION_TAKER,float(TP_here),float(SL_here),self.LEVERAGE,row['high'],row['low']):
                            self.one_trayde_final = { # данные по текущей сделке
                                'coin' : self.trade_param['coin'], # монета сделки
                                'index_trade' : self.trade_param['index_trade_for_final'], # индекс входа в сделку
                                'trend' : self.trade_param['trend'], # лонг или шорт
                                'profit' : round(self.profit,1), # результат за сделку
                                'comission' : round(self.comission,1), # комиссия за сделку
                                'depo' : round(self.DEPOSIT_GLOBAL,1), # депозит
                                'how_time' : int((self.trade_param['index_work']-self.trade_param['index_trade_for_final'])*(self.settings['VOLUME_5MIN']/self.settings['VOLUME'])), # сколько минут стояли в сделке
                                'take_profit_price': self.trade_param['take_profit_price'],
                                'stop_loss_price': self.trade_param['stop_loss_price']

                            }
                            self.trade_final['depo_trade_finish'] = round(self.DEPOSIT_GLOBAL,1) # депозит в конце торговли
                            self.sdelky_trade_final[self.count_trade-1] = self.one_trayde_final
                            break # чекаем монету по шагам итерации между большим и мальеньким фреймомd
            if float(self.DEPOSIT_GLOBAL)/float(self.DEPOSIT_START_GLOBAAL) < 0.4:
                print(f'{self.DEPOSIT_GLOBAL} | {self.DEPOSIT_START_GLOBAAL}')
                self.trade_final['if_depo_slif'] = 1 # слили депо, маржа
                break
            else:
                self.trade_final['if_depo_slif'] = 0 # не слили депо, отторговали весь объём
            
        # колбек в котором возвращается результат работы торговли - все данные
        self.trade_final['depo_start'] = self.DEPOSIT_START # начальный депозит в этот день = депозит конечный в прошлый день
        self.trade_final['sdelky_trade_final'] = self.sdelky_trade_final
        if len(self.trade_final['sdelky_trade_final']) == 0: self.trade_final['depo_trade_finish'] = round(self.DEPOSIT_GLOBAL,1) # ели сделок не было, то депозит остается прежним

        def_finish(self.trade_final)



    # Закрываем сделку
    def close_trade(self,status,procent,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE):
        if status == '+': # если закрыли в плюс
            self.profit = LEVERAGE*self.DEPOSIT_GLOBAL*procent - LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER)
            self.comission = LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER)
            self.DEPOSIT_GLOBAL = self.DEPOSIT_GLOBAL + LEVERAGE*self.DEPOSIT_GLOBAL*procent - LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER) # обновляем размер депо
            self.DEPOSIT_GLOBAL = round(self.DEPOSIT_GLOBAL,2)
            self.place_open_position_profit = round(LEVERAGE*self.DEPOSIT_GLOBAL*procent-LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER),2)
        if status == '-': # если закрыли в минус
            self.profit = -LEVERAGE*self.DEPOSIT_GLOBAL*procent - LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER)
            self.comission = LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER)
            self.DEPOSIT_GLOBAL = self.DEPOSIT_GLOBAL - LEVERAGE*self.DEPOSIT_GLOBAL*procent - LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER) # обновляем размер депо
            self.DEPOSIT_GLOBAL = round(self.DEPOSIT_GLOBAL,2)
            self.place_open_position_profit = round(-LEVERAGE*self.DEPOSIT_GLOBAL*procent-LEVERAGE*self.DEPOSIT_GLOBAL*(COMMISSION_MAKER+COMMISSION_TAKER),2)
        self.trade_param['sost_trade'] = False

    # когда в сделке - чекаем, словили тп или сл
    def check_trade(self,price,COMMISSION_MAKER,COMMISSION_TAKER,TP,SL,LEVERAGE,high,low):
        if self.trade_param['trend'] == 'long':
            if float(price)>float(self.trade_param['take_profit_price']):
                self.signal_for_logs_regime_0 = 'Тейк'
                self.close_trade('+',TP,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
                return 1
            if float(price)<float(self.trade_param['stop_loss_price']):
                self.signal_for_logs_regime_0 = 'Стоп'
                self.close_trade('-',SL,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
                return 1
        if self.trade_param['trend'] == 'short':
            if float(price)<float(self.trade_param['take_profit_price']):
                self.signal_for_logs_regime_0 = 'Тейк'
                self.close_trade('+',TP,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
                return 1
            if float(price)>float(self.trade_param['stop_loss_price']):
                self.signal_for_logs_regime_0 = 'Стоп'
                self.close_trade('-',SL,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
                return 1
        # if self.trade_param['trend'] == 'long':
        #     if float(price)>float(self.trade_param['take_profit_price']) or float(high)>float(self.trade_param['take_profit_price']):
        #         self.signal_for_logs_regime_0 = 'Тейк'
        #         self.close_trade('+',TP,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
        #         return 1
        #     if float(price)<float(self.trade_param['stop_loss_price']) or float(low)<float(self.trade_param['take_profit_price']):
        #         self.signal_for_logs_regime_0 = 'Стоп'
        #         self.close_trade('-',SL,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
        #         return 1
        # if self.trade_param['trend'] == 'short':
        #     if float(price)<float(self.trade_param['take_profit_price']) or float(low)<float(self.trade_param['take_profit_price']):
        #         self.signal_for_logs_regime_0 = 'Тейк'
        #         self.close_trade('+',TP,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
        #         return 1
        #     if float(price)>float(self.trade_param['stop_loss_price'])  or float(high)>float(self.trade_param['take_profit_price']):
        #         self.signal_for_logs_regime_0 = 'Стоп'
        #         self.close_trade('-',SL,COMMISSION_MAKER,COMMISSION_TAKER,LEVERAGE)
        #         return 1

    # считаем шаг остатвания фреймов
    def calculation_step_df(self,coin):
        df_work = pd.read_csv(f'{self.settings['MYDIR_TF']}{self.settings['day_trade']}/{coin}.csv') # получили датафрейм из файла
        df_see = pd.read_csv(f'{self.settings['MYDIR_1min']}{self.settings['day_trade']}/{coin}.csv') # получили датафрейм мини из файла
        for index, row in df_work.iterrows():
            self.close_time_work_now = row['close_time']
            break
        for index, row in df_see.iterrows():
            if row['close_time'] == self.close_time_work_now:
                self.trade_param['step_df'] = index
                self.trade_param['timeframe'] = self.settings['VOLUME_5MIN']/self.settings['VOLUME']
                break


    # считаем шаг совпадения времени датафрейма рабочего и слежения
    def search_step_see(self,index):
        return (self.trade_param['step_df'] + (self.settings['VOLUME_5MIN']/self.settings['VOLUME'])*index)

    # открывает лонг или шорт
    def open_position(self):
        self.trade_param['sost_trade'] = True
        TP_here = self.set_settings['TP']
        SL_here = self.set_settings['SL']
        if self.settings['regime_profit'] == 0:
            TP_here = self.settings['tp_sl_dinamic'][self.trade_param['coin']][0]
            SL_here = self.settings['tp_sl_dinamic'][self.trade_param['coin']][1]
        self.trade_param['take_profit_price'] = self.get_take_profit(self.trade_param['trend'],self.trade_param['price_treyd'],float(TP_here)) # получаем цену тэйк профита
        self.trade_param['stop_loss_price'] = self.get_stop_loss(self.trade_param['trend'],self.trade_param['price_treyd'],float(SL_here)) # получаем цену стоп лосса

    # получаем цену тейк профита в зависимости от направления
    def get_take_profit(self,trend,price_trade,TP): 
        if trend == 'long':
            return price_trade*(1+TP)
        if trend == 'short':
            return price_trade*(1-TP)

    # получаем цену стоп лосса в зависимости от направления
    def get_stop_loss(self,trend,price_trade,SL): 
        if trend == 'long':
            return price_trade*(1-SL)
        if trend == 'short':
            return price_trade*(1+SL)



































