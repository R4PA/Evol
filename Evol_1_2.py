from tkinter import *
import pdb
import numpy as np
import random
import time
import sys,tty,termios
import os

animals=[]

WIDTH=500
HEIGHT=500
RESO=20
RAW=WIDTH/RESO
ANIMALCOUNT=30
animalid=0
LABELSIZE=8
colors=["red","blue","green","orange"]

MUTATION=float(10)


feed=[] #2 viimeisinta syntyma ja kuolemaviestia
feedSwitch=float(0)
minHealth=float(50)
maxHealth=float(50)
minMaxspeed=float(RESO/10)
maxMaxspeed=float(RESO/10)
minEating=float(3)
maxEating=float(3)
minMutator=float(MUTATION)
maxMutator=float(MUTATION)
minBabyCount=float(1)
maxBabyCount=float(1)
minMatingtime=float(1)
maxMatingtime=float(1)

NminHealth=float(50)
NmaxHealth=float(50)
NminMaxspeed=float(RESO/10)
NmaxMaxspeed=float(RESO/10)
NminEating=float(3)
NmaxEating=float(3)
NminMutator=float(MUTATION)
NmaxMutator=float(MUTATION)
NminBabyCount=float(1)
NmaxBabyCount=float(1)
NminMatingtime=float(1)
NmaxMatingtime=float(1)

dieded=0

records=[]



def feeder(newFeed):
	global feed
	global feedSwitch
	feed[feedSwitch]=newFeed
	if(feedSwitch==0):
		feedSwitch=1
	else:
		feed=0
	return 0


def consoleInfoAllt():
	global feed
	global minHealth
	global maxHealth
	global minMaxspeed
	global maxMaxspeed
	global minEating
	global maxEating
	global minMutator
	global maxMutator
	global minBabyCount
	global maxBabyCount
	global minMatingtime
	global maxMatingtime

	os.system('clear')

	print("#########################ANIMALS ALIVE###############################")
	he=69-len("# Animals alive:"+str(len(animals))+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Animals alive:"+str(len(animals))+str(he_)+" #")

	print("#####################################################################")	

	print("#########################ALL TIME####################################")
	#he=69-len("# Max Health:"+str(maxHealth)+"Min Health:"+str(minHealth)+" #")
	#he_=""
	#for i in range(he):
	#	he_+=" "
	#print("# Max Health:"+str(maxHealth)+str(he_)+"Min Health:"+str(minHealth)+" #")

	he=69-len("# Max Speed:"+str(maxMaxspeed)+"Min Speed:"+str(minMaxspeed)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max Speed:"+str(maxMaxspeed)+str(he_)+"Min Speed:"+str(minMaxspeed)+" #")

	he=69-len("# Max Eating:"+str(maxEating)+"Min Eating:"+str(minEating)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max Eating:"+str(maxEating)+str(he_)+"Min Eating:"+str(minEating)+" #")


	he=69-len("# Max Mutator:"+str(maxMutator)+"Min Mutator:"+str(minMutator)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max Mutator:"+str(maxMutator)+str(he_)+"Min Mutator:"+str(minMutator)+" #")	

	he=69-len("# Max BabyCount:"+str(maxBabyCount)+"Min BabyCount:"+str(minBabyCount)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max BabyCount:"+str(maxBabyCount)+str(he_)+"Min BabyCount:"+str(minBabyCount)+" #")	

	he=69-len("# Max Matingtime:"+str(maxMatingtime)+"Min Matingtime:"+str(minMatingtime)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max Matingtime:"+str(maxMatingtime)+str(he_)+"Min Matingtime:"+str(minMatingtime)+" #")	

	print("#####################################################################")

	consoleInfoNow()

def consoleInfoNow():
	global feed
	global NminHealth
	global NmaxHealth
	global NminMaxspeed
	global NmaxMaxspeed
	global NminEating
	global NmaxEating
	global NminMutator
	global NmaxMutator
	global NminBabyCount
	global NmaxBabyCount
	global NminMatingtime
	global NmaxMatingtime


	print("#########################NOW ACTIVE##################################")
	#he=69-len("# Max Health:"+str(NmaxHealth)+"Min Health:"+str(NminHealth)+" #")
	#he_=""
	#for i in range(he):
		#he_+=" "
	#print("# Max Health:"+str(NmaxHealth)+str(he_)+"Min Health:"+str(NminHealth)+" #")

	he=69-len("# Max Speed:"+str(NmaxMaxspeed)+"Min Speed:"+str(NminMaxspeed)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max Speed:"+str(NmaxMaxspeed)+str(he_)+"Min Speed:"+str(NminMaxspeed)+" #")

	he=69-len("# Max Eating:"+str(NmaxEating)+"Min Eating:"+str(NminEating)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max Eating:"+str(NmaxEating)+str(he_)+"Min Eating:"+str(NminEating)+" #")


	he=69-len("# Max Mutator:"+str(NmaxMutator)+"Min Mutator:"+str(NminMutator)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max Mutator:"+str(NmaxMutator)+str(he_)+"Min Mutator:"+str(NminMutator)+" #")	

	he=69-len("# Max BabyCount:"+str(NmaxBabyCount)+"Min BabyCount:"+str(NminBabyCount)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max BabyCount:"+str(NmaxBabyCount)+str(he_)+"Min BabyCount:"+str(NminBabyCount)+" #")	

	he=69-len("# Max Matingtime:"+str(NmaxMatingtime)+"Min Matingtime:"+str(NminMatingtime)+" #")
	he_=""
	for i in range(he):
		he_+=" "
	print("# Max Matingtime:"+str(NmaxMatingtime)+str(he_)+"Min Matingtime:"+str(NminMatingtime)+" #")	

	print("#####################################################################")


def consoleInfoNow0():
	global feed
	global NminHealth
	global NmaxHealth
	global NminMaxspeed
	global NmaxMaxspeed
	global NminEating
	global NmaxEating
	global NminMutator
	global NmaxMutator
	global NminBabyCount
	global NmaxBabyCount
	global NminMatingtime
	global NmaxMatingtime

	global dieded

	NminHealth=float(50)
	NmaxHealth=float(50)
	NminMaxspeed=float(RESO/10)
	NmaxMaxspeed=float(RESO/10)
	NminEating=float(3)
	NmaxEating=float(3)
	NminMutator=float(MUTATION)
	NmaxMutator=float(MUTATION)
	NminBabyCount=float(1)
	NmaxBabyCount=float(1)
	NminMatingtime=float(1)
	NmaxMatingtime=float(1)

	dieded=0


def eraseRecord(a,b):
	global NminHealth
	global NmaxHealth
	global NminMaxspeed
	global NmaxMaxspeed
	global NminEating
	global NmaxEating
	global NminMutator
	global NmaxMutator
	global NminBabyCount
	global NmaxBabyCount
	global NminMatingtime
	global NmaxMatingtime
	
	if(a==0):
		if(b==0):
			NminHealth=float(50)
		else:
			NmaxHealth=float(50)
	if(a==1):
		if(b==0):
			NminMaxspeed=float(RESO/10)
		else:
			NmaxMaxspeed=float(RESO/10)
	if(a==2):
		if(b==0):
			NminEating=float(3)
		else:
			NmaxEating=float(3)
	if(a==3):
		if(b==0):
			NminMutator=float(MUTATION)
		else:
			NmaxMutator=float(MUTATION)
	if(a==4):
		if(b==0):
			NminBabyCount=float(1)
		else:
			NmaxBabyCount=float(1)
	if(a==5):
		if(b==0):
			NminMatingtime=float(1)
		else:
			NmaxMatingtime=float(1)
	return 0

def getAnimalID():
	global animalid
	return animalid

def animalID(ID):
	global animalid
	animalid=ID

def addAnimalID():
	global animalid
	animalid+=1

def nonlin(x):
	return 1/(1+np.exp(-x))

def identifyNdraw(event):
	animal=canvas.find_closest(event.x,event.y)[0]
	animal.drawInfo

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing")
canvas.pack()

tiles=[]

class Tile:
	def __init__(self,x,y,health,ID):
		self.animal=None
		self.ID=ID
		self.x=x
		self.y=y
		self.health=hex(health)
		self.HP=health
		#print self.health
		self.health=self.health.lstrip('x0')
		if(len(self.health)==0):
			self.health='00'
		if(len(self.health)==1):
			self.health='0'+str(self.health)
		#print self.health
		self.health=str('#'+str(self.health)+str(self.health)+str(self.health))
		#print self.health	
		self.shape=canvas.create_rectangle(x,y,x+RESO,y+RESO,fill=str(self.health))
		return None
#
		
	def getY(self,desc=None):
		#if(desc!=None):
				#print desc+": "+str(self.y)
		return self.y

	def getID(self):
		return self.ID

	def grow(self):
		self.HP+=random.randrange(0,2)
		if(self.HP<=255):
			self.health=hex(self.HP)
		else:
			self.health=hex(255)
			self.HP=255
		self.health=self.health.lstrip('x0')
		if(len(self.health)==0):
			self.health='00'
		if(len(self.health)==1):
			self.health='0'+str(self.health)
		#print self.health
		self.health=str('#'+str(self.health)+str(self.health)+str(self.health))
		#print self.health
		canvas.delete(self.shape)
		self.shape=canvas.create_rectangle(self.x,self.y,self.x+RESO,self.y+RESO,fill=str(self.health))		
		return 0
#
		

	def getCoord(self):
		pos=canvas.coords(self.shape)
		return pos

	def getPosCent(self):
		pos=canvas.coords(self.shape)
		poscenter=[]
		for coord in range(2):
			poscenter.append(pos[coord+2]-(RESO/2))
			
		#print "POSITIOKESKUS "+str(poscenter)
		#print "line 90 "+str(len(poscenter))
		return poscenter

	def getHP(self):
		return self.HP

	def drainHP(self,animal):
		self.HP-=int(10*animal.getEating())
		if(self.HP>=0):
			self.health=hex(self.HP)
		else:
			self.health=hex(0)
			self.HP=0
		self.health=self.health.lstrip('x0')
		if(len(self.health)==0):
			self.health='00'
		if(len(self.health)==1):
			self.health='0'+str(self.health)
		#print self.health
		self.health=str('#'+str(self.health)+str(self.health)+str(self.health))
		#print self.health
		canvas.delete(self.shape)	
		self.shape=canvas.create_rectangle(self.x,self.y,self.x+RESO,self.y+RESO,fill=str(self.health))		
		animal.draw()
		return 0

	def isEmpty(self):
		if(self.animal==None):
			return True
		else:
			return False
		
	def setAnimal(self,animal):
		self.animal=animal
		return 0
#

'''
class Animal:
	def __init__(self,x,y,ID,color,partco=None,PK=False,health=50,maxspeed=RESO/10):
		global colors
		self.ID=ID
		self.x=x
		self.y=y
		self.health=health
		self.standingID=None
		self.refreshStand()
		self.tilesAr=[]
		self.refreshTilesAr()
		self.takePartnerColor=PK
		self.partco=color
		self.color=color
		self.mating=0
		self.matingcount=0
		self.matingtime=1
		#print "Color index: "+str(self.color)
		#print "Creating: "+str(colors[self.color])
		self.shape=canvas.create_oval(x,y,x+RESO,y+RESO,fill=str(colors[self.color]))
		#self.lbl=str(self.ID)
		self.lbl=canvas.create_text(x+(RESO/2),y+(RESO/2),text="#"+str(self.ID),tags="text")
		self.draw()
		self.xspeed=0
		self.yspeed=0
		self.maxspeed=maxspeed
		self.soul=True
		self.babyCount=1
		if(color==0 or partco==0):
			self.babyCount=2
		if(color==1 or partco==1):
			self.maxspeed*=1.2
		if(color==2 or partco==2):
			self.matingtime*=0.8
		if(color==3 or partco==3):
			self.takePartnerColor=True
		return None
'''
class Infobox:
	def __init__(self, animal):
		self.animal=animal
		self.shape=canvas.create_rectangle(WIDTH-100,0,WIDTH,HEIGHT,stipple="gray50",fill="gray",tag="info")

	def clearInfo(self):
		canvas.delete("info")

class Animal:
	def __init__(self,x,y,ID,color,partco=None,PK=False,health=50,maxspeed=RESO/10,eating=3,mutator=MUTATION,babyCount=1,matingtime=1):
		global colors
		self.ID=ID
		self.x=x
		self.y=y
		self.partner=None
		self.health=float(health)
		self.eating=float(eating)
		self.mutator=float(mutator)
		self.standingID=None
		self.refreshStand()
		self.tilesAr=[]
		self.refreshTilesAr()
		self.takePartnerColor=PK
		self.partco=color
		self.color=color
		self.mating=0
		self.matingcount=0
		self.matingtime=float(matingtime)
		#print "Color index: "+str(self.color)
		#print "Creating: "+str(colors[self.color])
		self.shape=canvas.create_oval(x,y,x+RESO,y+RESO,fill=str(colors[self.color]))
		#self.lbl=str(self.ID)
		self.lbl=canvas.create_text(x+(RESO/2),y+(RESO/2),text="#"+str(self.ID),tags="text")
		self.draw()
		self.xspeed=0
		self.yspeed=0
		self.maxspeed=float(maxspeed)
		self.soul=True
		self.babyCount=babyCount
		self.info=None
		return None

#
	def drawInfo(self):
		self.info=Infobox(self)

	def wipeInfo(self):
		self.info.clearInfo()
		self.info=None

	def getHealth(self):
		return self.health
		
	def getMatingT(self):
		return self.matingtime
		
	def getMaxSpeed(self):
		return self.maxspeed
		
	def getBabyCount(self):
		return self.babyCount
		
	def getEating(self):
		return self.eating
		
	def getMutator(self):
		return self.mutator

	def refreshTilesAr(self):
		#print "oma ID: "+str(self.ID)
		self.refreshStand()
		ID=self.standingID
		#print "standing ID: "+str(ID)
		ad=[]
		v=False
		o=False
		#print str(self.x/RESO)+" pitais olla isompi kun 1 ja pitais olla pienempi kun "+str((RAW)-1)
		if(self.x/RESO>1):
			ad.append(tiles[ID-1])
			v=True
		if(self.x/RESO<(RAW)-1):
			ad.append(tiles[ID+1])
			o=True
		if(self.y/RESO>1):
			ad.append(tiles[ID-(RAW)])
			if(v):
				ad.append(tiles[ID-(RAW)-1])
			if(o):
				ad.append(tiles[ID-(RAW)+1])
		if(self.y/RESO<(HEIGHT/RESO)-1):
			ad.append(tiles[ID+(RAW)])
			if(v):
				ad.append(tiles[ID+(RAW)-1])
			if(o):
				ad.append(tiles[ID+(RAW)+1])
		self.tilesAr=ad
		return 0
		

	def refreshStand(self):
		rec=False
		#print("standing before: "+str(self.standingID))	
		#print("x: "+str(self.x))
		#print("y: "+str(self.y))
		if(self.standingID!=None):
			tiles[self.standingID].setAnimal(None)
		if(self.y<HEIGHT and self.x<WIDTH):
			self.standingID=int(RAW)*int(self.y/RESO)+int(self.x/RESO)
		else:
			self.move(self.x-1, self.y-1,rec)
		#print("standing after setting: "+str(self.standingID))
		#print "tiles lenght: "+str(len(tiles))
		if(self.standingID<=len(tiles)):
			tiles[self.standingID].setAnimal(self)
		return 0

	def draw(self):
		pos=canvas.coords(self.shape)
		canvas.delete(self.shape)
		self.shape=canvas.create_oval(pos[0],pos[1],pos[2],pos[3],fill=str(colors[self.color]))
		self.drawLabel()
		return 0
#

	def drawLabel(self):
		pos=canvas.coords(self.shape)
		leib=self.lbl
		#if(self.partner!=None):
			#self.lbl=canvas.create_text(pos[0]+(RESO/2),pos[1]+(RESO/2),font=("helvetica",LABELSIZE),fill="black",text=str(self.ID)+" matingcount:"+str(self.matingcount)+" Partner:"+str(self.partner.getID()),width=RESO*2,tags="text")
		#else:
			#self.lbl=canvas.create_text(pos[0]+(RESO/2),pos[1]+(RESO/2),font=("helvetica",LABELSIZE),fill="black",text=str(self.ID)+" matingcount:"+str(self.matingcount)+" Partner:None",width=RESO*2,tags="text")
		self.lbl=canvas.create_text(pos[0]+(RESO/2),pos[1]+(RESO/2),font=("helvetica",LABELSIZE),fill="black",text=str(self.ID),width=RESO*2,tags="text")
		canvas.delete(leib)	
		return 0
#

	def getSoul(self):
		return self.soul

	def eraseSoul(self):
		self.soul=False
		return 0
#

	def setShape(self,shape):
		self.shape=shape
		return 0
#

	def getShape(self):
		return self.shape

	def getID(self):
		return self.ID

	def refreshPosCent(self,rec=True):
		pos=canvas.coords(self.shape)
		poscent=[]
		for coord in range(2):
			poscent.append(pos[coord+2]-(RESO/2))
		if(poscent[0]>=0 and poscent[0]<=WIDTH and poscent[1]>=0 and poscent[1]<=HEIGHT):
			self.x=poscent[0]
			self.y=poscent[1]
			if(rec):
				self.refreshStand()
		else:
			print"******Virheellista koordinaattidataa*******"
			print"tried input: "+("x:"+str(poscent[0])+" y:"+str(poscent[1]))
			print ("x:"+str(self.x)+" y:"+str(self.y))
			print"self.ID: "+str(self.ID)
			print"self.standingID: "+str(self.standingID)
			print"self.tilesAr: "+str(self.tilesAr)
			print"self.takePartnerColor: "+str(self.takePartnerColor)
			print"self.partco: "+str(self.partco)
			print"self.color: "+str(self.color)
			print"self.mating: "+str(self.mating)
			print"self.matingcount: "+str(self.matingcount)
			print"self.matingtime: "+str(self.matingtime)
			print"self.health: "+str(self.health)
			print"self.xspeed: "+str(self.xspeed)
			print"self.yspeed: "+str(self.yspeed)
			print"self.maxspeed: "+str(self.maxspeed)
			print"self.soul: "+str(self.soul)
			print"self.babyCount: "+str(self.babyCount)
		return 0

	def move(self,vx,vy,rec=True):
	
		#print "LETS MOVE ####"
		#print "Kohteena: "+str(vx)+" "+str(vy)
		self.refreshPosCent(rec)
		#print "line 176 "+str(len(poscent))
		#print "Olemme kohdassa: "+str(poscent[0])+" "+str(poscent[1])
		#print "Vaadittava matka:"
		vx=vx-self.x
		#print "	X:ien erotus: "+str(vx)
		vy=vy-self.y
		#print "	Y:ien erotus: "+str(vy)
		if(vx+vy==0):
			vx+=0.00001
		potx=abs(vx)/(abs(vx)+abs(vy))
		poty=abs(vy)/(abs(vx)+abs(vy))
		if(abs(potx)+abs(poty)<=1):
			self.xspeed=abs(vx)/(abs(vx)+abs(vy))*self.maxspeed
			self.yspeed=abs(vy)/(abs(vx)+abs(vy))*self.maxspeed
			if(vx<0 and self.xspeed>0):
				self.xspeed*=-1
			if(vx>0 and self.xspeed<0):
				self.xspeed*=-1
			if(vy<0 and self.yspeed>0):
				self.yspeed*=-1
			if(vy>0 and self.yspeed<0):
				self.yspeed*=-1
		else:
			self.xspeed=0
			self.yspeed=0
		#print "Moving! "+str(self.xspeed)+" "+str(self.yspeed)
		canvas.move(self.shape,self.xspeed,self.yspeed)
		canvas.move(self.lbl,self.xspeed,self.yspeed)
		self.refreshPosCent(rec)
		return 0
#

	def getPosCent(self):
		self.refreshPosCent()
		poscenter=[self.x,self.y]
		return poscenter

	def findfood(self):
		#print("#######################")
		#print("ELAIMEN ID: #"+str(self.ID))
		#print("x ja y ennen uudelleenpaikannusta:")
		#print("x: "+str(self.x))
		#print("y: "+str(self.y))
		self.refreshPosCent()
		#print("x ja y uudelleenpaikannuksen jalkeen:")
		#print("x: "+str(self.x))
		#print("y: "+str(self.y))
		#print str(self.standingID)+"<="+str(len(tiles))
		standing=tiles[self.standingID]
		#print "Coordinaatit:"
		#print "%%%%"
		
		#print "line 216 "+str(len(poscenter))
			#print str(pos[coord+2])
		#print "%%%%"
		
		#for tile in tiles:
			#tilepos=tile.getCoord()
			#if(self.x>=tilepos[0] and self.x<tilepos[2] and self.y>=tilepos[1] and self.y<tilepos[3]):
				#standing=tile
				#print "standing: "+str(standing.getID())
				#self.refreshStand()
				#print "uusi standing: "+str(self.standingID)
				#print "TILE FOUND!"
		if(standing!=None):
			if(standing.getHP()>self.eating and self.health<100):
				standing.drainHP(self)
				self.health+=self.eating
				#print "Eating! "+str(self.health)
			if(standing.getHP()<self.eating):
				self.refreshTilesAr()
				adjacent=self.tilesAr
				#for tile in tiles:
					#if((tile.getID()==standing.getID()-1 and tile.getY("tile")==standing.getY("standing")) or (tile.getID()==standing.getID()+1 and tile.getY("tile")==standing.getY("standing")) or (tile.getID()==standing.getID()-(RAW) and tile.getY("tile")==standing.getY("standing")-RESO) or (tile.getID()==standing.getID()+(RAW) and tile.getY("tile")==standing.getY("standing")+RESO) or (tile.getID()==standing.getID()-(RAW)+1 and tile.getY("tile")==standing.getY("standing")-RESO) or (tile.getID()==standing.getID()-(RAW)-1 and tile.getY("tile")==standing.getY("standing")-RESO) or (tile.getID()==standing.getID()+(RAW)-1 and tile.getY("tile")==standing.getY("standing")+RESO) or (tile.getID()==standing.getID()+(RAW)+1) and tile.getY("tile")==standing.getY("standing")+RESO):
						#adjacent.append(tile)
				#print "line 235 "+str(len(adjacent))
				#print "adjatile "+str(tile.getID())+" "+str(tile.getHP())
				target=adjacent[0]
				for tile in adjacent:
					if(tile.getHP()>target.getHP()):
						target=tile
						#print "target "+str(target.getID())+" "+str(target.getHP())
				targetposcent=target.getPosCent()
				#print "moves towards food"
				self.move(targetposcent[0],targetposcent[1])
		return 0
#

	def mate(self,target):
		#print "juuri haettu partnerivari: "+str(self.partco)
		self.partner=target
		self.mating=1
		self.matingcount=random.randrange(5,25)*self.matingtime
		return 0
#

	def getColor(self):
		return self.color

	def findpartner(self):
		targets=[]
		for animal in animals:
			#print "get:"+str(anima.getID())+" self:"+str(self.ID)
			if(animal.getID()!=self.ID):
				targets.append(animal)
			#print "line 260 "+str(len(targets))
		#pos=canvas.coords(self.shape)
		poscenter=self.getPosCent()
		#for coord in range(2):
			#poscenter.append(pos[coord+2]-(RESO/2))
		#print "line 265 "+str(len(poscenter))
		target=targets[0]
		for kandi in targets:
			kandiposcent=kandi.getPosCent()
			targetposcent=target.getPosCent()
			if((abs(poscenter[0]-kandiposcent[0])+abs(poscenter[1]-kandiposcent[1]))<(abs(poscenter[0]-targetposcent[0])+abs(poscenter[1]-targetposcent[1]))):
				target=kandi
				targetposcent=target.getPosCent()
		if((abs(poscenter[0]-targetposcent[0])+abs(poscenter[1]-targetposcent[1]))<(RESO*0.5)):
			#print "Found partner!"	
			self.mate(target)
		else:
			#print "Move towards possible partner"
			self.move(targetposcent[0],targetposcent[1])
		return 0
#
					
	def drainHP(self):
		self.health-=1
		return 0

	def countHeritage(self,partner):
		oH=[self.health,self.maxspeed,self.eating,self.mutator,self.babyCount,self.matingtime]
		pH=[partner.getHealth(),partner.getMaxSpeed(),partner.getEating(),partner.getMutator(),partner.getBabyCount(),partner.getMatingT()]
		fh=[]
		for i in range(len(oH)):
			r=random.randrange(0,3)
			if(r==1):
				oH[i]=pH[i]
			if(r>1):
				oH[i]=(pH[i]+oH[i])/2
		
		m=random.randrange(0,2)
		hi=random.randrange(0,6)
		print("hi:"+str(hi))

		bC=oH[hi]
		#print len(oH)
		#print hi
		if(hi<=len(oH)):
			if(random.randrange(0,int(self.mutator))==1):
				if(m<1):
					if(hi!=4):
						oH[hi]*=0.9
					else:
						oH[hi]-=1
				else:
					if(hi!=4):
						oH[hi]*=1.1
					else:
						oH[hi]+=1
				#print("indeksi:"+str(hi)+"       oli:"+str(bC)+"    muutettu:"+str(oH[hi]))

		global feed
		global minHealth
		global maxHealth
		global minMaxspeed
		global maxMaxspeed
		global minEating
		global maxEating
		global minMutator
		global maxMutator
		global minBabyCount
		global maxBabyCount
		global minMatingtime
		global maxMatingtime

		global NminHealth
		global NmaxHealth
		global NminMaxspeed
		global NmaxMaxspeed
		global NminEating
		global NmaxEating
		global NminMutator
		global NmaxMutator
		global NminBabyCount
		global NmaxBabyCount
		global NminMatingtime
		global NmaxMatingtime


		if (oH[0]<minHealth):
			minHealth=oH[0]
		if (oH[0]>maxHealth):
			maxHealth=oH[0]
		if(oH[1]<minMaxspeed):
			minMaxspeed=oH[1]
		if(oH[1]>maxMaxspeed):
			maxMaxspeed=oH[1]
		if(oH[2]<minEating):
			minEating=oH[2]
		if(oH[2]>maxEating):
			maxEating=oH[2]
		if(oH[3]<minMutator):
			minMutator=oH[3]
		if(oH[3]>maxMutator):
			maxMutator=oH[3]
		if(oH[4]<minBabyCount):
			minBabyCount=oH[4]
		if(oH[4]>maxBabyCount):
			maxBabyCount=oH[4]
		if(oH[5]<minMatingtime):
			minMatingtime=oH[5]
		if(oH[5]>maxMatingtime):
			maxMatingtime=oH[5]

		if (oH[0]<NminHealth):
			NminHealth=oH[0]
			records.append([getAnimalID(),0,0])
		if (oH[0]>NmaxHealth):
			NmaxHealth=oH[0]
			records.append([getAnimalID(),0,1])
		if(oH[1]<NminMaxspeed):
			NminMaxspeed=oH[1]
			records.append([getAnimalID(),1,0])
		if(oH[1]>NmaxMaxspeed):
			NmaxMaxspeed=oH[1]
			records.append([getAnimalID(),1,1])
		if(oH[2]<NminEating):
			NminEating=oH[2]
			records.append([getAnimalID(),2,0])
		if(oH[2]>NmaxEating):
			NmaxEating=oH[2]
			records.append([getAnimalID(),2,1])
		if(oH[3]<NminMutator):
			NminMutator=oH[3]
			records.append([getAnimalID(),3,0])
		if(oH[3]>NmaxMutator):
			NmaxMutator=oH[3]
			records.append([getAnimalID(),3,1])
		if(oH[4]<NminBabyCount):
			NminBabyCount=oH[4]
			records.append([getAnimalID(),4,0])
		if(oH[4]>NmaxBabyCount):
			NmaxBabyCount=oH[4]
			records.append([getAnimalID(),4,1])
		if(oH[5]<NminMatingtime):
			NminMatingtime=oH[5]
			records.append([getAnimalID(),5,0])
		if(oH[5]>NmaxMatingtime):
			NmaxMatingtime=oH[5]
			records.append([getAnimalID(),5,1])

		consoleInfoAllt()
		

		return oH
		
	#self.health,self.maxspeed,self.eating,self.mutator,self.babyCount,self.matingtime	
#

	def multiply(self):
		self.refreshTilesAr()
		adjacent=self.tilesAr
		for baby in range(self.babyCount):
			stillPregnant=True
			if(self.takePartnerColor==True):
				for tile in adjacent:
					if(tile.isEmpty() and stillPregnant):
						animals.append(Animal(tile.getPosCent()[0],tile.getPosCent()[1],getAnimalID(),self.color,self.partco,PK=True))
						stillPregnant=False	
			else:
				for tile in adjacent:
					if(tile.isEmpty() and stillPregnant):
						H=self.countHeritage(self.partner)
						animals.append(Animal(tile.getPosCent()[0],tile.getPosCent()[1],getAnimalID(),self.color,None,False,H[0],H[1],H[2],H[3],H[4],H[5]))
						stillPregnant=False
			print "#:"+str(getAnimalID())+" "+str(colors[self.color])+" was born for #:"+str(self.ID)+" and #:"+str(self.partner.getID())+"!"
			addAnimalID()
		return 0

	'''
	def multiply(self):
		self.refreshTilesAr()
		adjacent=self.tilesAr
		for baby in range(self.babyCount):
			stillPregnant=True
			if(self.takePartnerColor==True):
				for tile in adjacent:
					if(tile.isEmpty() and stillPregnant):
						animals.append(Animal(tile.getPosCent()[0],tile.getPosCent()[1],getAnimalID(),self.color,self.partco,PK=True))
						stillPregnant=False	
			else:
				for tile in adjacent:
					if(tile.isEmpty() and stillPregnant):
						animals.append(Animal(tile.getPosCent()[0],tile.getPosCent()[1],getAnimalID(),self.color))
						stillPregnant=False
			print "#: "+str(getAnimalID())+" "+str(colors[self.color])+" was born for #:"+str(self.ID)+"!"
			addAnimalID()
		return0
	
	'''

	def live(self):
		#print "Burning calories"
		self.health-=1
		if(self.health>0):
			#print "Is alive"
			if(self.health<75 and self.mating==0):
				#print "Searches food"
				self.findfood()
			if(self.health>75 and self.mating==0):
				#print "Searches partner"
				self.findpartner()
			if(self.mating==1):
				#print "Is still mating"
				if(self.matingcount>0):
					self.matingcount-=1
				else:
					#print "Stopped maiting"
					self.multiply()
					#print "line 307 "+str(len(animals))
					self.mating=0
		else:
			#global dieded
			#dieded+=1
			#print(dieded)
			#if(dieded==30):
				#consoleInfoNow0()
			global records
			for record in records:
				if (record[0]==self.ID):
					eraseRecord(record[1],record[2])
					records.remove([record[0],record[1],record[2]])

			canvas.delete(self.shape)
			canvas.delete(self.lbl)
			return 0

#canvas.create_line(0,0,500,400)
#canvas.create_rectangle(100,100,200,250,fill='#737373')
#canvas.create_oval(100,100,200,250,fill="blue")
#canvas.create_polygon(400,10,300,300,500,300,fill="yellow")


tileID=0
print "Creating earth"
for x in range(HEIGHT*RAW):
	if(x%RESO==0):
		cx=x-(int(x/WIDTH)*WIDTH)
		cy=int(x/WIDTH)*RESO
		tiles.append(Tile(cx,cy,random.randrange(0,255),tileID))
		#print "line 324 "+str(len(tiles))
		tileID+=1


	




print "Creating life"
for animal in range(ANIMALCOUNT):
	color=random.randrange(0,4)
	animals.append(Animal(random.randrange(0,WIDTH-RESO),random.randrange(0,HEIGHT-RESO),getAnimalID(),color))
	#print "line 333 "+str(len(animals))
	#print "#: "+str(getAnimalID())+" "+str(colors[color])+" was born!"
	addAnimalID()
print "Life creation DONE"
flash=canvas.create_rectangle(0,0,WIDTH,HEIGHT,stipple="gray50",fill="red")
canvas.update()

'''
def keypress(event):
	global key
	kp=repr(event.char)
	print repr(event.char)

canvas.bind_all("<Key-x>",keypress)
print "waiting key"

'''
print "Starting everyday life"
#pdb.set_trace()
while True:
	#canvas.bind("<Enter>",identifyNdraw)
	#canvas.bind("<Leave>",canvas.delete("info"))
	#pdb.set_trace()
	#print "Growing grass"
	for tile in tiles:
		tile.grow()
	for animal in animals:
		if (animal.getSoul()==True):
			#print "Day of animal #:"+str(animal.getID())
			#animal.setShape(canvas.create_oval(canvas.coords(animal.getShape())[0],canvas.coords(animal.getShape())[1],canvas.coords(animal.getShape())[2],canvas.coords(animal.getShape())[3],fill=colors[animal.getColor()]))
			animal.draw()
			if(animal.live()==0):
				print "#: "+str(animal.getID())+" dies!"
				animal.eraseSoul()
				animals.remove(animal)
	#print "Animals: "+str(len(animals))
	#print "Tiles: "+str(len(tiles))

	tk.update()
	#time.sleep(0.5)
	#canvas.delete("all")
	
		



canvas.mainloop()

