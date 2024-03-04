import re
from random import choice
import pymorphy2
from pytrovich.enums import NamePart, Gender, Case
from pytrovich.maker import PetrovichDeclinationMaker
from pytrovich.detector import PetrovichGenderDetector

global morph
global maker
global detector
global job_pattern
global name_pattern

morph = pymorphy2.MorphAnalyzer()
maker = PetrovichDeclinationMaker()
detector = PetrovichGenderDetector()
job_pattern = re.compile(r"{\w*}")
name_pattern = re.compile(r"{{\w*}}")

def get_case(execution_control):

	try:
		case = re.search(job_pattern, execution_control).group(0)[1:-1]
	except AttributeError:
		return "no responsible"

	if case == "accs":
		return ("accs", Case.ACCUSATIVE)
	elif case == "ablt":
		return ("ablt", Case.INSTRUMENTAL)

def change_name_case(responsible, case):

	if case == "no responsible":
		return responsible

	while True:
		try:
			name = re.search(name_pattern, responsible).group()[2:-2]
		except AttributeError:
			break

		gender = detector.detect( middlename="Семёнович")

		if name.isupper():
			case_name = maker.make(NamePart.LASTNAME, gender, case[1],  name.lower())
			case_name = case_name.upper()
		else:
			case_name = maker.make(NamePart.LASTNAME, gender, case[1],  name)

		responsible = responsible.replace('{{'+name+'}}', case_name)

	return responsible

def change_job_case(responsible, execution_control, case):
	if case == "no responsible":
		return execution_control

	while True:
		try:
			word = re.search(job_pattern, responsible).group()[1:-1]
		except AttributeError:
			break

		case_word = morph.parse(word)[0].inflect({case[0]})[0]

		responsible = responsible.replace('{'+word+'}', case_word)

	return execution_control.replace('{'+case[0]+'}', responsible)

def create_responsible(execution_control, responsible):
	case = get_case(execution_control)
	responsible = change_name_case(responsible, case)
	return (change_job_case(responsible, execution_control, case))
