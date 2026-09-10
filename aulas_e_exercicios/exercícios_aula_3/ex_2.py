class viagi:
    def __init__(self, km, hr, mn):
        self.dist = km
        self.hrs = hr
        self.min = mn

    def velo_media(self):
        tempo = self.hrs + (self.min / 60)
        if tempo == 0: return 0
        return self.dist / tempo

v = viagi(400, 5, 25)
print(v.velo_media())
