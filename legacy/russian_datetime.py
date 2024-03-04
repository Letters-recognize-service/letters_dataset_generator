from datetime import date as dt
from time import mktime

Bs = ["января", "февраля", "марта", "апреля", "мая", "июня",
	"июля", "августа", "сентября", "октября", "ноября", "декабря"]
bs = ["янв", "фев", "мар", "апр", "мая", "июня",
	"июля", "авг", "сен", "окт", "ноя", "дек"]

class date(dt):
	def __init__(self, year, month, day):
		dt(year, month, day)
		
	def strftime(self, format):
		if ("%b" in format):
			format = format.replace("%b", bs[self.month-1])
			date = dt(self.year, self.month, self.day)
			return (date.strftime(format), mktime(date.timetuple()))
		elif ("%B" in format):
			format = format.replace("%B", Bs[self.month-1])
			date = dt(self.year, self.month, self.day)
			return (date.strftime(format), mktime(date.timetuple()))
		else:
			date = dt(self.year, self.month, self.day)
			return (date.strftime(format), mktime(date.timetuple()))