class command(object):
	
	def __parse__(self):

		cmd = [x.strip() for x in self.cmd.strip().split()]

		if cmd[0] not in self.__cmdAttr__:
			try:
				self.__masterCmdFunc__[cmd[0]]()
				return
			except Exception:
				print("Couldn't identify command "+cmd[0])
				return None

		self.cmd = cmd[0]

		for key,value in self.__cmdAttr__[cmd[0]].items():
			value.clear()

		lastVisitedAttr = None
		cmdAttr = self.__cmdAttr__[cmd[0]]
		for x in cmd[1:]:
			if x in cmdAttr:
				lastVisitedAttr = x
			else:
				if lastVisitedAttr is None:
					print("Couldn't identify "+x+' command')
					return None
				else:
					cmdAttr[lastVisitedAttr].append(x)
		return 1
	

	def __exit__(self):
		print("Good Bye")
		import sys
		sys.exit(0)


	def __clear__(self):
		import os
		try:
		 	k = os.system('clear')
		except Exception :
			pass

	def __executePlist__(self):
		import problemFun
		problems_ = problemFun.getProblems(self.__cmdAttr__[self.cmd])
		if problems_ is None:
			print("Couldn't find any problem")
			return
		print("Total number of result found :	"+str(len(problems_)))
		problemFun.print_(problems_,True)
	
	def __executePstmt__(self):
		import problemFun
		pstmts_,error = problemFun.getProblemStatement(self.__cmdAttr__[self.cmd])
		for pstmt in pstmts_:
			try:
				pstmt.print_()
			except Exception:
				pass
		if len(error)>0:
			print("Error:-")
			for er in error:
				print('*     '+er)
	
	def execute(self,cmd):
		self.cmd = cmd
		status = self.__parse__()
		if status is not None:
			self.__masterCmdFunc__[self.cmd]()


	def __init__(self):
		self.__cmdAttr__ = {}

		self.__masterCmdFunc__ = {'plist':self.__executePlist__,'pstmt':self.__executePstmt__,'exit':self.__exit__,'quit':self.__exit__,'close':self.__exit__,'clear':self.__clear__}

		self.__cmdAttr__['plist'] = {'-u':[],'-h':[],'-tags':[],'-type':[],'-print':[],'-pname':[]}
		self.__cmdAttr__['pstmt'] = {'-pid':[],'-pname':[]} 
	
