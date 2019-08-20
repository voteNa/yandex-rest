class BirthdayStat:
    data = {}

    def setMonth(self, month: int, value: list):
        self.data[month] = value

    def toJSON(self):
        result = {}
        for i in range(1, 13):
            item = []
            if self.data.get(i):
                item = self.data.get(i)
            result[i] = item
        return result
