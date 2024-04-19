import logging
import random as rd

from deropy.dvm.functions.Function import Function


class Dero(Function):
    def __init__(self):
        func_parameters = {
            'value': {"type": "int", "value": None},
        }
        super().__init__("dero", 10000, 0, func_parameters)

    def _exec(self, *args, **kwargs):
        value = "0000000000000000000000000000000000000000000000000000000000000000"
        self.parameters['value']['value'] = value
        return value
    
    def _computeGasStorageCost(self):
        return 0
            
        
def dero():
    return Dero()()
