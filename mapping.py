# -*- mode: Python; coding: utf-8 -*-

class Mapping(object):
    def __init__(self, items):
        self.item_list = items
        self.items = dict((index, item) for index, item in enumerate(items))
        self.index = dict((item, index) for index, item in enumerate(items))
    
    def __contains__(self, item):
        return item in self.index

    def __getitem__(self, item):
        return self.index[item]

    def __iter__(self):
        return iter(self.index)

    def __len__(self):
        return len(self.index)

    def __repr__(self):
        return "<%s with %d entries>" % (self.__class__.__name__, len(self))

    def add(self, item):
        if item not in self:
            index = len(self)
            self.items[index] = item
            self.index[item] = index
        return item

    def get(self, item, default=None):
        return self.index.get(item, default)

    def item(self, index):
        return self.items[index]

    def keys(self):
        """Preserving original order"""
        return self.item_list
