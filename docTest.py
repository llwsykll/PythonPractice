# -*- coding: utf-8 -*-

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1,b=2,c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent all last):
        ...
    KeyError:'empty'
    >>> d2.empty
    Traceback (most recent all last):
        ...
    AttributeError: 'Dict' object has no attribute 'emptu'
    '''

    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        