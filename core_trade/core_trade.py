# ядро исторической торговли на 1 сете

import os
import sys
sys.path.insert(1,os.path.join(sys.path[0],'../../../'))
from imports import *




class Core_trade:
    def __init__(self,master,settings):

        self.settings = settings
        self.master = master