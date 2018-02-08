class header(object):
	def __init__(self,header=None):
		if header is not None:
			self.__setAttr__(header)

	def __setAttr__(self,header):
		header = list(header.children)
		try:
			self.title = header[0].get_text()
		except Exception :
			pass
		try:
			self.timeLimitPerTest =str (list(header[1].children)[1])
		except Exception :
			pass
		try:
			self.memoryLimitPerTest = str(list(header[2].children)[1])
		except Exception :
			pass
		try:
			self.input = str(list(header[3].children)[1])
		except Exception :
			pass
		try:
			self.output = str(list(header[4].children)[1])
		except Exception :
			pass

	def print_(self):
		print('')
		try:
			print('          '+self.title+'\n')
		except Exception :
			pass
		try:
			print("Time limit per Test :-  "+self.timeLimitPerTest)
		except Exception :
			pass
		try:
			print("Memory limit per Test :-  "+self.memoryLimitPerTest)
		except Exception :
			pass
		try:
			print("Input :-  "+self.input)
		except Exception :
			pass
		try:
			print("Output :-  "+self.output)
		except Exception :
			pass	
		print("\n**********				*********\n")
		 

class sampleTest(object):
	def __init__(self,input_,ouput_):
		self.input = input_
		self.output = ouput_

	def print_(self):
		try:
			print("Input:-")
			print(self.input)
		except Exception :
			pass
		try:
			print("Output:-")
			print(self.output)
		except Exception :
			pass


class problemStatement(object):
	def __init__(self,pstmt):
		self.__setAttr__(pstmt)
	
	def __setAttr__(self,pstmt):
		try:
			from bs4 import BeautifulSoup as bsoup
		except ImportError:
			print("Please install BeautifulSoup (bs4).")
			return
		pstmt = list(pstmt.children)
		length = len(pstmt)
		self.header = header(pstmt[0])
		self.__setStatement__(pstmt[1]) 
		if length>2:
			self.__setInputSpecification__(pstmt[2])
		if length>3:
			self.__setOuputSpecification__(pstmt[3])
		if length>4:
			self.__setSampleTest__(pstmt[4])
		if length>5:
			self.__setNotes__(pstmt[5])

	def __setStatement__(self,stmt):
		try:
			self.statement = stmt.get_text()
		except Exception :
			pass

	def __setInputSpecification__(self,input_):
		try:
			self.input = list(input_.children)[1].get_text()
		except Exception :
			pass

	def __setOuputSpecification__(self,output_):
		try:
			self.output = list(output_.children)[1].get_text()
		except Exception :
			pass

	def __setSampleTest__(self,sample):
		self.sample = []
		input_ = sample.find_all(class_='input')
		output_ = sample.find_all(class_='output')
		if type(input_) == type(None) or type(output_) == type(None):
			return
		for i in range(len(input_)):
			line = list(input_[i].find('pre').children)
			inp = ''
			for j in range(0,len(line),2):
				inp += line[j]+'\n'
			line = list(output_[i].find('pre').children)
			out = ''
			for j in range(0,len(line),2):
				out += line[j]+'\n'
			self.sample.append(sampleTest(inp,out))
	

	def __setNotes__(self,notes):
		notes_ = list(notes.children)
		notes = ''
		for note in notes_[1:]:
			try:
				notes += (note.get_text())+'\n'
			except Exception:
				try:
					notes += str(note)
				except Exception:
					pass
		if notes != '':
			self.notes = notes

	def print_(self):
		try:
			self.header.print_()	
		except Exception :
			pass
		try:
			print("STATEMENT :-\n")
			print(self.statement+'\n')
		except Exception:
			pass
		try:
			print("Input:-\n"+self.input)
			print()
		except Exception :
			pass
		try:
			print("Ouput:-\n"+self.output)
			print()
		except Exception:
			pass
		try:
			print("Sample Tests:-\n")
			for sample in self.sample:
				sample.print_()
				print('')
		except Exception :
			pass
		try:
			print('Notes:-\n'+self.notes)
		except Exception :
			pass


class problem(object):
	__status__ = 0
	__problems__ ={}

	def __init__(self,prblm):
		self.update(prblm)
		
	def setSolvedByAttr(self,cnt):
		self.solvedBy = cnt

	def setProblemStatement(self,pstmt):
		self.pstmt = problemStatement(pstmt)

	def update(self,prblm):
		try:
			self.id = prblm['contestId']
		except Exception:
			pass
		try:
			self.index = prblm['index']
		except Exception:
			pass
		try:
			self.type = prblm['type']
		except Exception:
			pass
		try:
			self.title = prblm['name']
		except Exception:
			pass
		try:
			self.points = prblm['points']
		except Exception:
			pass
		try:
			self.tags = prblm['tags']
		except Exception:
			pass
	
	def print_(self,pflag_=False):
		print('')
		try:
			print('*	'+str(self.id)+self.index+' : '+self.title)
		except Exception :
			pass
		if pflag_ == False:
			return
		try:
			print("Tags :-",end='  ')
			for tag in self.tags:
				print(tag,end=', ')
			print('')
		except Exception :
			pass
		
		try:
			print("Points :- "+str(self.points))
		except Exception :
			pass
		try:
			print("Solved By :- "+str(self.solvedBy))
		except Exception :
			pass			
