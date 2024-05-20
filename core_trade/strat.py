
# Стратегия 2 логика, возвращает сигнал
import os
import sys
sys.path.insert(1,os.path.join(sys.path[0],'../../'))
from imports import *


class Strat:
    def __init__(self,df,settings):
        self.df = df
        self.settings = settings


    def check_signal(self):
        return self.MOM_strat(self.df)



    def DEMA_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.DEMA(df, timeperiod=timeperiod)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def EMA_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.EMA(df, timeperiod=timeperiod)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def HT_TRENDLINE_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.HT_TRENDLINE(df,timeperiod=timeperiod)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def KAMA_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.KAMA(df)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def MA_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.MA(df)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def MIDPOINT_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.MIDPOINT(df)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def MIDPRICE_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.MIDPRICE(df)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def SMA_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.SMA(df)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def TEMA_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.TEMA(df)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def TRIMA_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.TRIMA(df)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def WMA_strat(self,df_celka,timeperiod,history_count):
        mas_res_binary = []
        mas_res_signal = []
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.WMA(df)
        for i in range(len(df)):
            if df['open'][i] > a.iloc[i]:
                mas_res_binary.append(1)
                if mas_res_binary[-1] == 1 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 0:
                # if mas_res_binary[-1] == 1 and mas_res_binary[-history_count:-1].count(mas_res_binary[-history_count:-1][0]) == len(mas_res_binary[-history_count:-1]) and mas_res_binary[-2] == 0:
                    mas_res_signal.append('long')
                else: mas_res_signal.append('нет сигнала')
            else:
                mas_res_binary.append(0)
                if mas_res_binary[-1] == 0 and len(set(mas_res_binary[-history_count:-1])) == 1 and mas_res_binary[-2] == 1:
                    mas_res_signal.append('short')
                else: mas_res_signal.append('нет сигнала')
        return mas_res_signal[-1]
    
    def ADX_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.ADX(df,timeperiod)
        if a.iloc[-1] == 'nan': return 'нет сигнала'
        if a.iloc[-1]<10: return 'long'
        elif a.iloc[-1]>90: return 'short'
        else: return 'нет сигнала'
    
    def ADXR_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.ADXR(df,timeperiod)
        if a.iloc[-1] == 'nan': return 'нет сигнала'
        if a.iloc[-1]<10: return 'long'
        elif a.iloc[-1]>90: return 'short'
        else: return 'нет сигнала'
    
    def APO_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.APO(df,timeperiod)
        if a.iloc[-1] == 'nan': return 'нет сигнала'
        if a.iloc[-1]<0: return 'short'
        elif a.iloc[-1]>0: return 'long'
        else: return 'нет сигнала'
    
    def AROON_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.AROON(df,timeperiod)
        if a['aroondown'].iloc[-1]==100: return 'short'
        elif a['aroonup'].iloc[-1]==100: return 'long'
        else: return 'нет сигнала'
    
    def BOP_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.BOP(df,timeperiod)
        if a.iloc[-1]>0.8: return 'short'
        elif a.iloc[-1]<-0.8: return 'long'
        else: return 'нет сигнала'
    
    def CCI_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.CCI(df,timeperiod)
        if a.iloc[-1]>100: return 'short'
        elif a.iloc[-1]<-100: return 'long'
        else: return 'нет сигнала'

    def CMO_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.CMO(df,timeperiod)
        if a.iloc[-1]>30: return 'short'
        elif a.iloc[-1]<-30: return 'long'
        else: return 'нет сигнала'

    def DX_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.DX(df,timeperiod)
        if a.iloc[-1]>50: return 'short'
        elif a.iloc[-1]<10: return 'long'
        else: return 'нет сигнала'

    def MACD_strat(self,df_celka, fastperiod=12, slowperiod=26, signalperiod=9):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.MACD(df,fastperiod, slowperiod, signalperiod)
        if a['macdsignal'].iloc[-1]>1: return 'short'
        elif a['macdsignal'].iloc[-1]<0: return 'long'
        else: return 'нет сигнала'

    def MFI_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.MFI(df,timeperiod)
        if a.iloc[-1]>80: return 'short'
        elif a.iloc[-1]<20: return 'long'
        else: return 'нет сигнала'

    def MINUS_DI_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.MINUS_DI(df,timeperiod)
        if a.iloc[-1]<10: return 'short'
        # elif a.iloc[-1]<20: return 'long'
        else: return 'нет сигнала'

    def MINUS_DM_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.MINUS_DM(df,timeperiod)
        if a.iloc[-1]<10: return 'short'
        # elif a.iloc[-1]<20: return 'long'
        else: return 'нет сигнала'

    def MOM_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.MOM(df,timeperiod)
        print(f'{self.settings['number_set']}|{self.settings['day_trade']}|{self.settings['index_trade_in_day']}|{a.iloc[-1]}')
        if a.iloc[-1]>4: return 'long'
        elif a.iloc[-1]<-0.5: return 'short'
        else: return 'нет сигнала'

    def PLUS_DI_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.PLUS_DI(df,timeperiod)
        # print(a.iloc[-1])
        # time.sleep(0.5)
        if a.iloc[-1]>30: return 'long'
        elif a.iloc[-1]<10: return 'short'
        else: return 'нет сигнала'

    def ROC_strat(self,df_celka, timeperiod=14):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.ROC(df, timeperiod)
        # print(a.iloc[-1])
        # time.sleep(0.5)
        if a.iloc[-1]>2: return 'long'
        elif a.iloc[-1]<-2: return 'short'
        else: return 'нет сигнала'

    def CDLEVENINGSTAR_strat(self,df_celka):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.CDLEVENINGSTAR(df)
        # print(a.iloc[-1])
        # time.sleep(0.5)
        if a.iloc[-1]==-100: return 'short'
        else: return 'нет сигнала'

    def ROCR_strat(self,df_celka):
        df = df_celka.copy()
        df.rename(columns={'VOLUME':'volume'},inplace=True)
        a = abstract.ROCR(df)
        print(a.iloc[-1])
        time.sleep(0.5)
        if a.iloc[-1]==-100: return 'short'
        else: return 'нет сигнала'























