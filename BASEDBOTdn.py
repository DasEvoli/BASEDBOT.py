import random
import json
import discord
import io
import asyncio

with open("MainResponses.json") as j:
	MainResponses = json.load(j)


class dragonnest:

	def __init__(self, bot, message):
		self.bot = bot
		self.message = message

	def savednbuild(self):
		if self.message.content == ('!savednbuild') or self.message.content == ('!savednbuild '):
			return 'Your build must contain the format !savednbuild $(name of command) (tree build url)'
		elif (self.message.content.split()[-1].startswith('https://dnss.herokuapp.com') or self.message.content.split()[-1].startswith('https://dnss-kr.herokuapp.com') or self.message.content.split()[-1].startswith('https://dnmaze.com') or self.message.content.split()[-1].startswith('http://dnskillsim.herokuapp.com/') or self.message.content.split()[-1].startswith('https://dnskillsim.herokuapp.com/')) == False:
			return 'Your URL must be from dnskillsim.herokuapp.com,dnss.herokuapp.com, dnss-kr.herokuapp.com or https://dnmaze.com or is missing the https:// prefix'
		elif self.message.content.split()[1].startswith('$') == False:
			return 'Your command created command must have $ infront'
		elif len(str(self.message.content).split()) !=3:
			return 'Can only create a link with exactly 3 arguments'
		elif len(self.message.content.split()) == 3 and '$' in self.message.content.split()[1]: 
			with open('DNbuilds.txt','r+') as dnBuilds:
				for line in dnBuilds:
					if self.message.content.lower().split()[1] == line.lower().split()[1]:
						return 'A build with this name already exists!'
		dnBuildsSave = self.message.content.replace('!savednbuild ', '')
		with open('DNbuilds.txt','a') as bnsBuilds2:
			bnsBuilds2.write(str(self.message.author.id) + ' ' + dnBuildsSave + '\n')
			return 'build "'+self.message.content.split()[2]+'" saved! Use your command "'+self.message.content.split()[1]+'" to use it!'


	def editdnbuild(self):
		if self.message.content == ('!editdnbuild') or self.message.content == ('!editdnbuild '):
			return 'Your build must contain the format !editdnbuild $(name of command) (tree build url)'
		elif (self.message.content.split()[-1].startswith('https://dnss.herokuapp.com') or self.message.content.split()[-1].startswith('https://dnss-kr.herokuapp.com') or self.message.content.split()[-1].startswith('https://dnmaze.com') or self.message.content.split()[-1].startswith('http://dnskillsim.herokuapp.com/') or self.message.content.split()[-1].startswith('https://dnskillsim.herokuapp.com/')) == False:
			return 'Your URL must be from dnskillsim.herokuapp.com,dnss.herokuapp.com, dnss-kr.herokuapp.com or https://dnmaze.com or is missing the https:// prefix'
		elif len(self.message.content.split()) == 2 and self.message.content.split()[1].startswith('$'):
			return 'Your edited command must have $ infront'
		elif len(str(self.message.content).split()) !=3:
			return 'Can only edit a link with exactly 3 arguments'
		saveL = ''
		dnBuildsSave = self.message.content.replace('!editdnbuild ', '')
		with open('DNbuilds.txt','r') as bnsBuilds2:
			for line in bnsBuilds2:
				if self.message.content.split()[1] in line:
					if str(self.message.author.id) not in line:
						return 'This is not your build so you cannot edit it.'
					elif str(self.message.author.id) in line:
						saveL = line.rsplit(' ', 1)[0] + ' ' + self.message.content.split()[-1]
		saveL += '\n'
		newLines = []
		with open('DNbuilds.txt','r') as bnsBuilds2:
			for line in bnsBuilds2:
				if self.message.content.split()[1] not in line:
					newLines.append(line)
				else:
					newLines.append(saveL)
		with open('DNbuilds.txt','w') as bnsBuilds2:
			for line in newLines:
				bnsBuilds2.write(line)
		return 'build "'+self.message.content.split()[2]+'" has been edited! Use your command "'+self.message.content.split()[1]+'" to use it!'

	def deletednbuild(self):
		if self.message.content == ('!deletednbuild') or self.message.content == ('!deletednbuild '):
			return 'Your build must contain the format !deletednbuild $(name of command)'
		if len(self.message.content.split()) == 2 and self.message.content.split()[1].startswith('$') == False:
			return 'Your command created command must have $ infront'
		if len(str(self.message.content).split()) !=2:
			return 'Can only delete a link with exactly 2 arguments'
		with open('DNbuilds.txt','r') as bnsBuilds2:
			for line in bnsBuilds2:
				if self.message.content.split()[1] in line:
					if str(self.message.author.id) not in line:
						return 'This is not your build so you cannot delete it.'
		newLines = []
		with open('DNbuilds.txt','r') as bnsBuilds2:
			for line in bnsBuilds2:
				if self.message.content.split()[1] not in line:
					newLines.append(line)
		with open('DNbuilds.txt','w') as bnsBuilds2:
			for line in newLines:
				bnsBuilds2.write(line)
		return 'Your build ' + self.message.content.split()[-1] + ' has been deleted.'

	def prefixdncommands(self): #this is for the $ prefix
		with open('DNbuilds.txt') as readBuilds:
			for line in readBuilds:
				if self.message.content.split()[0] == line.split()[-2]:
					return line.split()[-1]
	async def customdncommands(self):
		if self.prefixdncommands() == None:
			return
		else:
			await self.bot.send_message(self.message.channel, self.prefixdncommands())


	def mdb(self):
		numbercount = 1
		returnbox = []
		with open('DNbuilds.txt') as readBuilds:
			for line in readBuilds:
				if str(self.message.author.id) in line or str(self.message.author) in line:
					returnbox.append(str(numbercount)+': '+line.replace(str(self.message.author.id)+ ' ', ''))
					numbercount += 1
		if len(returnbox) == 0:
			return ['You have no saved builds!']
		else:
			return returnbox
	async def mydnbuilds(self):
		for line in self.mdb():
			await self.bot.send_message(self.message.channel, line)

	def skillbuilds(self):
		if self.message.content.lower().startswith('!skillbuilds'):
			dnClass = self.message.content.lower().replace('!skillbuilds ', '')
		elif self.message.content.lower().startswith('!krskillbuilds'):
			dnClass = self.message.content.lower().replace('!krskillbuilds ', '')
		if '!skillbuilds' == self.message.content.lower().split()[0] and len(self.message.content.split()) == 1:
			return 'https://dnskillsim.herokuapp.com/na'
		elif '!krskillbuilds' == self.message.content.lower().split()[0] and len(self.message.content.split()) == 1:
			return 'https://dnskillsim.herokuapp.com/kdn'
		else:
			try:
				if self.message.content.lower().startswith('!skillbuilds'):
					return 'http://dnskillsim.herokuapp.com/na/{}'.format(MainResponses["dnskillbuilds"][dnClass])
				elif self.message.content.lower().startswith('!krskillbuilds'):
					return 'http://dnskillsim.herokuapp.com/kdn/{}'.format(MainResponses["t5dnskillbuilds"][dnClass])
			except:	
				return '2nd argument not recognised'

	async def autobuilds(self):
		requestedBuild = []
		requestedBuilds = []
		m = self.message.content.lower()
		if 'build' in m and '?' in m and len(m.split()) > 1:
			m = m.replace('build', ' ')
			for i in MainResponses["t5dnskillbuilds"].values():
				if i in m:
					requestedBuild.append(i)
					m = m.replace(i, '')
			for i in MainResponses["t5dnskillbuilds"]:
				if i in m:
					requestedBuild.append(MainResponses["t5dnskillbuilds"][i])
					m = m.replace(MainResponses["t5dnskillbuilds"][i], '')
		if len(requestedBuild) == 0:
			return
		else:
			for i in requestedBuild:
				if i not in requestedBuilds:
					requestedBuilds.append(i)
			await self.bot.send_message(self.message.channel, 'Would you like me to PM you a list of community saved builds for {}?'.format(requestedBuilds))
			resp = await self.bot.wait_for_message(author=self.message.author)
			if 'y' not in resp.content.lower():
				await self.bot.send_message(self.message.channel, 'ok')
				return
			else:
				pmlist = []
				noB = False
				with open('DNbuilds.txt','r') as b:
					readB = b.readlines()
					for i in requestedBuilds:
						checksB = 0
						for line in readB:
							if i in line.split()[-1]:
								try:
									pmlist.append(line.replace(line.split()[0], discord.utils.get(self.message.server.members, id = line.split()[0]).name))
									checksB += 1
								except:
									pmlist.append(line.replace(line.split()[0], 'Unknown User'))
									checksB += 1
						if checksB == 0:
							noB = True
						checksB = 0
				if len(pmlist) == 0:
					await self.bot.send_message(self.message.channel, 'I\'m sorry, there appears to be no build for the class(es) requested :(')
				else:
					if noB == True:
						await self.bot.send_message(self.message.channel, 'I\'m sorry, there appears to be no build(s) made for one or more of the classes you requested :(')
					await self.bot.send_message(self.message.channel, 'I will send you the PM now!')
					for i in pmlist:
						await self.bot.send_message(self.message.author, i)


	async def pug(self):
		mrole = discord.utils.get(self.message.server.roles, name = 'pug')
		rlist = []
		for i in self.message.author.roles:
			rlist.append(i.name)
		if 'pug' not in rlist:
			await self.bot.add_roles(self.message.author, mrole)
			await self.bot.send_message(self.message.channel, 'You have signed up for <#106300530548039680> mentions!')
		elif 'pug' in rlist:
			await self.bot.remove_roles(self.message.author, mrole)
			await self.bot.send_message(self.message.channel, 'You have removed yourself from <#106300530548039680> mentions!')
	async def trade(self):
		mrole = discord.utils.get(self.message.server.roles, name = 'trade')
		rlist = []
		for i in self.message.author.roles:
			rlist.append(i.name)
		if 'trade' not in rlist:
			await self.bot.add_roles(self.message.author, mrole)
			await self.bot.send_message(self.message.channel, 'You have signed up for <#106301265817931776> mentions!')
		elif 'trade' in rlist:
			await self.bot.remove_roles(self.message.author, mrole)
			await self.bot.send_message(self.message.channel, 'You have removed yourself from <#106301265817931776> mentions!')
	async def pvp(self):
		mrole = discord.utils.get(self.message.server.roles, name = 'pvp')
		rlist = []
		for i in self.message.author.roles:
			rlist.append(i.name)
		if 'pvp' not in rlist:
			await self.bot.add_roles(self.message.author, mrole)
			await self.bot.send_message(self.message.channel, 'You have signed up for <#106300621459628032> mentions!')
		elif 'pvp' in rlist:
			await self.bot.remove_roles(self.message.author, mrole)
			await self.bot.send_message(self.message.channel, 'You have removed yourself from <#106300621459628032> mentions!')
	
	async def pugmention(self):
		m = await self.bot.send_message(self.message.channel, "{} You can only mention the trade role in the <#106300530548039680> channel. This message will be deleted in 15 seconds".format(self.message.author.mention))
		with io.open('attempts.txt','a',encoding='utf-8') as attempts:
			attempts.write('{}({}) attempted to mention @pug on {}UTC outside of the pug channel. They said: {}\n'.format(self.message.author.id, self.message.author.name, str(self.message.timestamp), self.message.content))
		await self.bot.delete_message(self.message)
		await asyncio.sleep(15)
		await self.bot.delete_message(m)
	async def trademention(self):
		m = await self.bot.send_message(self.message.channel, "{} You can only mention the trade role in the <#106301265817931776> channel. This message will be deleted in 15 seconds".format(self.message.author.mention))
		with io.open('attempts.txt','a',encoding='utf-8') as attempts:
			attempts.write('{}({}) attempted to mention @trade on {}UTC outside of the trade channel. They said: {}\n'.format(self.message.author.id, self.message.author.name, str(self.message.timestamp), self.message.content))
		await self.bot.delete_message(self.message)
		await asyncio.sleep(15)
		await self.bot.delete_message(m)
	async def pvpmention(self):
		m = await self.bot.send_message(self.message.channel, "{} You can only mention the pvp role in the <#106300621459628032> channel. This message will be deleted in 15 seconds".format(self.message.author.mention))
		with io.open('attempts.txt','a',encoding='utf-8') as attempts:
			attempts.write('{}({}) attempted to mention @pvp on {}UTC outside of the pvp channel. They said: {}\n'.format(self.message.author.id, self.message.author.name, str(self.message.timestamp), self.message.content))
		await self.bot.delete_message(self.message)
		await asyncio.sleep(15)
		await self.bot.delete_message(m)
