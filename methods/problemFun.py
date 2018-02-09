from problem import *
from bs4 import BeautifulSoup as bsoup
from get import *


def createProblems(prblms):
	for prblm in prblms:
		createProblem(prblm)


def createProblem(prblm):
	id_ = str(prblm['contestId'])+prblm['index']
	if id_ in problem. __problems__:
		problem.__problems__[id_].update(prblm)
		return problem.__problems__[id_]
	p = problem(prblm)
	problem.__problems__[id_] = p
	return p


def createProblem_(stmt,id_):
	try:
		name = stmt.find(class_='title').get_text().strip()
	except Exception :
		return None
	index = name[0]
	try:
		name = name[2:].strip()
	except Exception:
		return None
	prblm = {'contestId':id_,'index':index,'name':name}
	prblm = createProblem(prblm)
	prblm.setProblemStatement(stmt)
	return prblm


def setProblemStatistics(prblmStats):
	for p in prblmStats:
		id_ = str(p['contestId'])+p['index']
		if id_ in problem.__problems__:
			problem.__problems__[id_].setSolvedByAttr(p['solvedCount'])


def print_(problems_,pflag_=False):
	length = len(problems_)
	problems_ = [key for key in problems_]
	for i in range(0,length,10):
		k = min(length,i+10)
		for j in range(i,k,1):
			problems_[j].print_(pflag_)
		if k == length:
			return 
		n = min(10,length-k)
		k = input("Type Y/y to get next "+str(n)+" questions :- ")
		if k =='y' or k == 'Y':
			continue
		else:
			break


def filterByType(type_,problems=None):
	problems_ = {}
	if problems is not None:
		if len(type_) == 0:
			return problems
		type_ = [x.upper() for x in type_]
		for prblm in problems:
			if prblm.index in  type_:
				problems_[prblm] = ''
		return problems_

	for key,prblm in problem.__problems__.items():
		if len(type_)>0:
			if prblm.index in type_:
				problems_[prblm]=''	
		else:
			problems_[prblm] = ''
	return problems_


def filterByTags(tags,problems):
	if len(tags) == 0:
		return problems
	tags = [tag.lower() for tag in tags]
	problems_ = {}
	for p in problems:
		for tag in tags:
			try:
				for tag1 in p.tags:
					if tag in tag1:
						problems_[p]=''
						break
			except Exception:
				pass
	return problems_
		

def filterProblems(attrs,problems_=None):
	problems_ = filterByType(attrs['-type'],problems_)
	problems_ = filterByTags(attrs['-tags'],problems_)	
	return problems_


def getProblems(attrs):
	if len(attrs['-u']) + len(attrs['-h']) == 0:
		problems_ = []
		if problem.__status__ == 1:
			problems_ = filterProblems(attrs)
		else:
			url = "http://codeforces.com/api/problemset.problems"

			response = getData(url)
			if response is None:
				print("Please Check your net Connection.")
				return None

			response = getDic(response)
			if response is None:
				print("Please check your net connection.")
				return None

			if response['status'] == 'OK':
				result = response['result']
				createProblems(result['problems'])
				setProblemStatistics(result['problemStatistics'])	
				problem.__status__ = 1
				problems_ = filterProblems(attrs)
			else:
				print(response['comment']) 
				return None
		if len(attrs['-pname'])>0:
			problems_ = filterProblemsByName(attrs['-pname'],problems_)
		return problems_

	else:
		problems_ = {}
		
		length = len(attrs['-u']) + len(attrs['-h'])

		if length>1:
			print("Please try for only one user at a time")
			return None
		handle = ''

		try:
			handle = attrs['-u'][0]	
		except Exception:
			handle = attrs['-h'][0]
		url = "http://codeforces.com/api/user.status"
		params = {'handle':handle}
	
		response = getData(url,params)

		if response is None:
			print("Please check your net connection")
			return None
	
		response = getDic(response)
		if response is None:
			print("Please check your net connection")
			return None

		if response['status'] == 'OK':
			result = response['result']
			for p in result:
				prblm = None
				if(len(attrs['-verdict']))>0 and 'verdict' in p:
					for v in attrs['-verdict']:
						V = v.upper()
						if V in p['verdict']:
							prblm = createProblem(p['problem'])
							break
						else:
							continue
				else:
					prblm = createProblem(p['problem'])
				if prblm is not None:
					problems_[prblm] = ''
			problems_ = filterProblems(attrs,problems_)
		else:
			print(response['comment'])
			return None
	
		if len(attrs['-pname'])>0:
			problems_ = filterProblemsByName(attrs['-pname'],problems_)
		return problems_	
		
def filterProblemsByName(pname,problems):
	problems_ = []
	for prblm in problems:
		name = ''
		try:
			name = (str(prblm.id) + prblm.index + prblm.title).lower()
		except Exception:
			continue
		for name_ in pname:
			status = 1
			name1_ = [x.lower() for x in name_.split('&')]
			for n in name1_:
				if n not in name:
					status = 0
					break
			if status == 1:
				problems_.append(prblm)
				break
	return problems_

def getStatement(url):
	response = getData(url)
	if response is None:
		return 1
	try:
		soup = bsoup(response.content,'html.parser')
		return soup.find(class_='problem-statement')
	except Exception :
		return None
		
def getProblemStatement(attrs):
	error = []
	pstmts_ = []
	for prblm in attrs['-pid']:
		if prblm in problem.__problems__:
			try:
				p = problem.__problems__[prblm]
				pstmts_.append(p.pstmt)
				continue
			except Exception:
				pass

		url ="http://codeforces.com/contest/"
		id_ =''
		index = ''
		try:
			id_ = prblm[0:-1]
			index = prblm[-1]
			url += id_+'/problem/'+index
		except Exception:
			error.append(prblm + ' is not a valid problem id') 
			continue
		pstmt =getStatement(url)
		if type(pstmt) == type(1):
			error.append("Please check your net connection")
			return pstmts_,error

		if type(pstmt) == type(None):	
			error.append("Perhapes problems with id "+prblm+" does not exist")
			continue	
		
		if prblm not in problem.__problems__:
			prblm = createProblem_(pstmt,id_)
			try:
				pstmts_.append(prblm.pstmt)
				continue
			except Exception:
				continue

		prblm = problem.__problems__[prblm]
		prblm.setProblemStatement(pstmt)
		try:
			pstmts_.append(prblm.pstmt)
		except Exception:
			error.append("No problem statement found for id "+prblm)

	return pstmts_,error

