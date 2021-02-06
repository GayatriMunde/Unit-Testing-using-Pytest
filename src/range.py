class Range:
    def __init__(self, *args):
        if len(args) == 1:
            if args[0] < 0:
                self.low = args[0]
                self.high = 0 
            else:
                self.low = 0
                self.high = args[0]
        
        elif len(args) == 2:
            self.low = min(args)
            self.high = max(args)
        return

    def contains(self, value):
        return(self.low <= value <= self.high)
    
    def left_overlap(self, obj):
        return(obj.high > self.low and self.low > obj.low)  
         
    def right_overlap(self, obj):
        return(obj.low < self.high and obj.high > self.high)    
    
    def is_same(self, obj):
        return(obj.low == self.low and obj.high == self.high)
    
    def merge(self, obj):
        merge_range = Range(min(self.low, obj.low), max(self.high, obj.high))
        return(merge_range)

    def is_touching(self, obj):
        return(obj.high == self.low or obj.low == self.high)

    def is_disjoint(self, obj):
        return((self.low > obj.low and self.low > obj.high) or (self.high < obj.low and self.high < obj.high))    

    def l_stretch(self, extend_by = 1):
        if extend_by < 0:
            raise ValueError("Can extend by a positive number")
        else:
            self.low -= extend_by 

    def r_stretch(self, extend_by = 1):
        if extend_by < 0:
            raise ValueError("Can extend by a positive number")
        self.high += extend_by        

    def shift(self, shift_by = 1):
        self.low += shift_by
        self.high += shift_by      
