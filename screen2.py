# -*- coding: utf-8 -*-
class Screen(object):
    
    @property
    def width(self):
    	return self._width

    @withd.setter
    def width(self,width):
    	if not isinstance(width,int):
    		raise ValueError('score must be an integer')
    	if width < 0:
    		raise ValueError('score must over zero')
        self._width = width

        
    @property
    def height(self):
    	return self._height

    @height.setter
    def height(self,height):
    	if not isinstance(height,int):
            raise ValueError('score must be an integer')
        if height < 0:
            raise ValueError('score must over zero')
        else:
            self._height = height

    @property 
    def resolution(self):
        return self._width*self._height