class hit:
    def __init__(self, id_m, id_s, time_stamp):
        self.id_m = id_m
        self.id_s = id_s
        self.time_stamp = time_stamp
    def __str__(self):
        return '{:}, {:}, {:}'.format(self.id_m, self.id_s, self.time_stamp)
    def __lt__(self, other):
        return self.time_stamp <= other.time_stamp 
    def __mt__(self, other):
        return self.time_stamp >= other.time_stamp 
