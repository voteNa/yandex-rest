class PercentileStat:
    data = []

    def setPercentile(self, percentile: dict):
        self.data.append(percentile)

    def toJSON(self):
        return self.data
