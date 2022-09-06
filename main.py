import json
import creds
from app import App
import os, pathlib, time
import concurrent.futures
from datetime import datetime 
import requests
import pandas as pd
import threading
from deepdiff import DeepDiff
from smartapi import SmartConnect
import calendar
from math import sqrt
from joblib import Parallel, delayed
from csv import DictWriter

import sys
#sys.stdout = open('logfile', 'w')
class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
f = open(f"temp/{datetime.now().strftime('mylogfile_%H_%M_%d_%m_%Y.txt')}", 'w')
backup = sys.stdout
sys.stdout = Tee(sys.stdout, f)


def strategy(i):
	creds.trade_list.append([])
	df1=creds.user_data

	"""if(df1['NIFTY']['EXS CE BUY']!=df1['NIFTY']['NEW CE BUY']):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['EXS EXP BUY'],df1['NIFTY']['EXS CE BUY'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Exs Lots"][i]),int(df1["NIFTY"]["Exs Slice"][i]),sym,token,"SELL",i)
		sym,token=gettokenid("NIFTY",df1['NIFTY']['NEW EXP BUY'],df1['NIFTY']['NEW CE BUY'],"CE")
		pushorder(int(df1["NIFTY"]["Lots"][i]),int(df1["NIFTY"]["Slice"][i]),sym,token,"BUY",i)
		print("strategy planing done")
	if(df1['NIFTY']['EXS PE BUY']!=df1['NIFTY']['NEW PE BUY']):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['EXS EXP BUY'],df1['NIFTY']['EXS PE BUY'],"PE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Exs Lots"][i]),int(df1["NIFTY"]["Exs Slice"][i]),sym,token,"SELL",i)
		sym,token=gettokenid("NIFTY",df1['NIFTY']['NEW EXP BUY'],df1['NIFTY']['NEW PE BUY'],"PE")
		pushorder(int(df1["NIFTY"]["Lots"][i]),int(df1["NIFTY"]["Slice"][i]),sym,token,"BUY",i)
		print("strategy planing done")
	if(df1['NIFTY']['EXS CE SELL']!=df1['NIFTY']['NEW CE SELL']):

		sym,token=gettokenid("NIFTY",df1['NIFTY']['EXS EXP SELL'],df1['NIFTY']['EXS CE SELL'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Exs Lots"][i]),int(df1["NIFTY"]["Exs Slice"][i]),sym,token,"BUY",i)
		sym,token=gettokenid("NIFTY",df1['NIFTY']['NEW EXP SELL'],df1['NIFTY']['NEW CE SELL'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Lots"][i]),int(df1["NIFTY"]["Slice"][i]),sym,token,"SELL",i)
		print("strategy planing done")
	if(df1['NIFTY']['EXS PE SELL']!=df1['NIFTY']['NEW PE SELL']):

		sym,token=gettokenid("NIFTY",df1['NIFTY']['EXS EXP SELL'],df1['NIFTY']['EXS PE SELL'],"PE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Exs Lots"][i]),int(df1["NIFTY"]["Exs Slice"][i]),sym,token,"BUY",i)
		sym,token=gettokenid("NIFTY",df1['NIFTY']['NEW EXP SELL'],df1['NIFTY']['NEW PE SELL'],"PE")
		pushorder(int(df1["NIFTY"]["Lots"][i]),int(df1["NIFTY"]["Slice"][i]),sym,token,"SELL",i)
		print("strategy planing done")"""
	if(int(df1["NIFTY"]["Force Sell"][0])==1):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['EXS EXP SELL'],df1['NIFTY']['EXS CE SELL'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Exs Lots"][i]),int(df1["NIFTY"]["Exs Slice"][i]),sym,token,"BUY",i)
	if(int(df1["NIFTY"]["Force Sell"][1])==1):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['EXS EXP SELL'],df1['NIFTY']['EXS PE SELL'],"PE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Exs Lots"][i]),int(df1["NIFTY"]["Exs Slice"][i]),sym,token,"BUY",i)
	if(int(df1["NIFTY"]["Force Sell"][2])==1):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['NEW EXP SELL'],df1['NIFTY']['NEW CE SELL'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Lots"][i]),int(df1["NIFTY"]["Slice"][i]),sym,token,"SELL",i)
	if(int(df1["NIFTY"]["Force Sell"][3])==1):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['NEW EXP SELL'],df1['NIFTY']['NEW PE SELL'],"PE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Lots"][i]),int(df1["NIFTY"]["Slice"][i]),sym,token,"SELL",i)
	
	if(int(df1["NIFTY"]["Force Buy"][0])==1):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['EXS EXP BUY'],df1['NIFTY']['EXS CE BUY'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Exs Lots"][i]),int(df1["NIFTY"]["Exs Slice"][i]),sym,token,"SELL",i)
	if(int(df1["NIFTY"]["Force Buy"][1])==1):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['EXS EXP BUY'],df1['NIFTY']['EXS PE BUY'],"PE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Exs Lots"][i]),int(df1["NIFTY"]["Exs Slice"][i]),sym,token,"SELL",i)
	if(int(df1["NIFTY"]["Force Buy"][2])==1):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['NEW EXP BUY'],df1['NIFTY']['NEW CE BUY'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["NIFTY"]["Lots"][i]),int(df1["NIFTY"]["Slice"][i]),sym,token,"BUY",i)
	if(int(df1["NIFTY"]["Force Buy"][3])==1):
		sym,token=gettokenid("NIFTY",df1['NIFTY']['NEW EXP BUY'],df1['NIFTY']['NEW PE BUY'],"PE")
		pushorder(int(df1["NIFTY"]["Lots"][i]),int(df1["NIFTY"]["Slice"][i]),sym,token,"BUY",i)
		print("sym",sym,"token",token)


	
	if(int(df1["BNF"]["Force Sell"][0])==1):
		sym,token=gettokenid("BANKNIFTY",df1['BNF']['EXS EXP SELL'],df1['BNF']['EXS CE SELL'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["BNF"]["Exs Lots"][i]),int(df1["BNF"]["Exs Slice"][i]),sym,token,"BUY",i)
	if(int(df1["BNF"]["Force Sell"][1])==1):
		sym,token=gettokenid("BANKNIFTY",df1['BNF']['EXS EXP SELL'],df1['BNF']['EXS PE SELL'],"PE")
		print("sym",sym,"token",token)
		pushorder(int(df1["BNF"]["Exs Lots"][i]),int(df1["BNF"]["Exs Slice"][i]),sym,token,"BUY",i)
	if(int(df1["BNF"]["Force Sell"][2])==1):
		sym,token=gettokenid("BANKNIFTY",df1['BNF']['NEW EXP SELL'],df1['BNF']['NEW CE SELL'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["BNF"]["Lots"][i]),int(df1["BNF"]["Slice"][i]),sym,token,"SELL",i)
	if(int(df1["BNF"]["Force Sell"][3])==1):
		sym,token=gettokenid("BANKNIFTY",df1['BNF']['NEW EXP SELL'],df1['BNF']['NEW PE SELL'],"PE")
		print("sym",sym,"token",token)
		pushorder(int(df1["BNF"]["Lots"][i]),int(df1["BNF"]["Slice"][i]),sym,token,"SELL",i)
	
	if(int(df1["BNF"]["Force Buy"][0])==1):
		sym,token=gettokenid("BANKNIFTY",df1['BNF']['EXS EXP BUY'],df1['BNF']['EXS CE BUY'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["BNF"]["Exs Lots"][i]),int(df1["BNF"]["Exs Slice"][i]),sym,token,"SELL",i)
	if(int(df1["BNF"]["Force Buy"][1])==1):
		sym,token=gettokenid("BANKNIFTY",df1['BNF']['EXS EXP BUY'],df1['BNF']['EXS PE BUY'],"PE")
		print("sym",sym,"token",token)
		pushorder(int(df1["BNF"]["Exs Lots"][i]),int(df1["BNF"]["Exs Slice"][i]),sym,token,"SELL",i)
	if(int(df1["BNF"]["Force Buy"][2])==1):
		sym,token=gettokenid("BANKNIFTY",df1['BNF']['NEW EXP BUY'],df1['BNF']['NEW CE BUY'],"CE")
		print("sym",sym,"token",token)
		pushorder(int(df1["BNF"]["Lots"][i]),int(df1["BNF"]["Slice"][i]),sym,token,"BUY",i)
	if(int(df1["BNF"]["Force Buy"][3])==1):
		sym,token=gettokenid("BANKNIFTY",df1['BNF']['NEW EXP BUY'],df1['BNF']['NEW PE BUY'],"PE")
		pushorder(int(df1["BNF"]["Lots"][i]),int(df1["BNF"]["Slice"][i]),sym,token,"BUY",i)
		print("sym",sym,"token",token)

	



def mul_order(n,obj,trade_list):

	def place_order(orderparams):

		try:
			orderID = obj.placeOrder(orderparams)
			print("The order id is: {}".format(orderID))
		except Exception as e:  
			time.sleep(1) 
			try:
				orderID = obj.placeOrder(orderparams)
				print("The order id is: {}".format(orderID))
				creds.ORDERS.append(orderID)
			except Exception as e: 
				time.sleep(1)
				try:
					orderID = obj.placeOrder(orderparams)
					creds.ORDERS.append(orderID)
					print("The order id is: {}".format(orderID))
				except Exception as e:
					print("Order placement failed: {}".format(e))
	def place_multiple_orders(tradeList):
		df1=creds.user_data
		if(int(df1['NIFTY']['WAIT'])==0):
			with concurrent.futures.ThreadPoolExecutor() as executor:
				executor.map(place_order, tradeList)
		else:
			for i in tradeList:
				df1=creds.user_data
				time.sleep(int(df1['NIFTY']['WAIT']))
				print("Added delay of",int(df1['NIFTY']['WAIT']),"seconds")
				place_order(i)
		

	start = datetime.now()
	place_multiple_orders(trade_list)
	end = datetime.now()
	print("orders sent to exchange in",end - start)


def checkorderstatus(n,obj):
	orderbook=obj.orderBook()['data']
	#n,y,z=0;
	#print("orderbook sent")
	if(len(orderbook)!=0):

		new = pd.DataFrame(orderbook)
		first_column = new.pop('averageprice')
		new.insert(0, 'averageprice', first_column)
		first_column = new.pop('orderstatus')
		new.insert(0, 'orderstatus', first_column)
		first_column = new.pop('unfilledshares')
		new.insert(0, 'unfilledshares', first_column)
		first_column = new.pop('lotsize')
		new.insert(0, 'lotsize', first_column)
		first_column = new.pop('transactiontype')
		new.insert(0, 'transactiontype', first_column)
		first_column = new.pop('tradingsymbol')
		new.insert(0, 'tradingsymbol', first_column)

		unf=new[new['unfilledshares'] > str(0)]
		sts=new['orderstatus'].to_list()
		mylist = list(set(sts))

		#print(mylist)
		print("orderbook exporting......")
		#print(new)
		"""with open('spreadsheet.csv','w') as outfile:
			writer = DictWriter(outfile, ('symboltoken','quantity','strikeprice','optiontype','expirydate'))
			writer.writeheader()
			writer.writerows(orderbook)"""
		#new.to_excel(f"{creds.USER_NAME[n]}1.xlsx")
		with pd.ExcelWriter(f"{creds.USER_NAME[n]}.xlsx") as writer:
			unf.to_excel(writer,sheet_name='UnFilled')
			for i in mylist:
				status=new[new['orderstatus'] == str(i)]
				status.to_excel(writer,sheet_name=str(i))
			new.to_excel(writer, sheet_name='ALL')
		print(f"{n} orderbook exported successfully")
	else:
		print("Empty OrderBook")





def pushorder(lots,slicing,sym,token,type,z):
	qt=0
	while(qt<lots):
		qt+=slicing
		orderbook(sym,token,type,slicing,z)
	print("slicing done")
	



def orderbook(sym,token,type,qty,z):
	new_dict = {"variety": str("NORMAL"), 
				"tradingsymbol" : str(sym),
				"symboltoken" : str(token),
				"transactiontype": str(type), 
				"exchange": str("NFO"),
				"ordertype": str("MARKET"), 
				"producttype": str("CARRYFORWARD"),
				"duration": str("DAY"), 
				"price": str("0"),
				"quantity": str(qty),
				"triggerprice": str("0")}
	#print(z)
	creds.trade_list[z].append(new_dict)
	#creds.orderbook = pd.concat([creds.orderbook,new_row])

def gettokenid(name,date,strike,ce_pe):
	import datetime
	datem = datetime.datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
	month=str(calendar.month_abbr[int(datem.month)]).upper()
	year=str(int(datem.year%2000))
	day=str(('{:02d}'.format(datem.day)))
	sym=str(name)+day+month+year+str(strike)+str(ce_pe).upper()
	df=creds.token_info
	token=df[(df['symbol']==sym)]
	print("sym=",sym,"token",token["token"].iloc[0]	)
	return sym,token["token"].iloc[0]

def saveTokeninfo():
	try:
		path = pathlib.Path(__file__).parent.resolve()
		dff=pd.read_excel(os.path.join(path,"tokens.xlsx"))
		creds.token_info=dff
		print("existing token info imported")
	except:
		url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
		d = requests.get(url).json()
		token_df = pd.DataFrame.from_dict(d)
		token_df["expiry"] = pd.to_datetime(token_df["expiry"])
		token_df = token_df.astype({"strike":float})
		token_df.to_excel("alltokens.xlsx")
		df=token_df
		creds.token_info= df[(df['exch_seg']=="NFO") & (df["instrumenttype"]==("OPTIDX" or "OPTSTK")) & ((df["name"]==("BANKNIFTY")) | (df["name"]==("NIFTY")))]
		print("token_info saved")
		print(creds.token_info)
		creds.token_info.to_excel("tokens.xlsx")





def instances(n,i,j,k):
	#for n,(i,j,k) in enumerate(zip(creds.user_data["NIFTY"]["ACC"],creds.user_data["NIFTY"]["Lots"],creds.user_data["NIFTY"]["Slice"])):
		obj = SmartConnect(api_key = creds.API_KEY[n])
		data = obj.generateSession(creds.USER_NAME[n],creds.PWD[n])
		strategy(n)
		#print(creds.trade_list[n])
		tl=pd.DataFrame(creds.trade_list[n])
		tl['rank'] = tl.groupby(['tradingsymbol','quantity', 'transactiontype']).cumcount()
		tl=tl.sort_values(['tradingsymbol', 'rank'])
		#tl.to_csv(f"{n}t.csv")
		tl.drop("rank", axis=1, inplace=True)
		creds.trade_list[n]= tl.to_dict('records')
		zz=pd.DataFrame(creds.trade_list[n])
		zz.to_csv(f't{n}.csv')


		print("sending orderbook")
		print(zz)
		mul_order(n,obj,creds.trade_list[n])
		checkorderstatus(n,obj)


def main():
	def take_response():
		a1=creds.user_data
		app.update_parameters()
		b1=creds.user_data
		a=DeepDiff(a1,b1)
		if a=={} :
			print("\n\nPress enter after making changes on excel sheet to run the bot")
			print("Or press 's' to stop the bot")
			cm=input("")
			if(cm=='s'):
				#print("stop bot command issued")
				stop_check()
			time.sleep(1)
		else:
			print("changes found.placing orders")
			st = datetime.now()
			creds.orderbook=creds.trade_list
			creds.trade_list.clear()
			creds.trade_list = [[],[]]
			creds.ORDERS.clear()
			#try:
			Parallel(n_jobs=len(creds.USER_NAME), prefer="threads")(delayed(instances)(n,i,j,k) for n,(i,j,k) in enumerate(zip(creds.user_data["NIFTY"]["ACC"],creds.user_data["NIFTY"]["Lots"],creds.user_data["NIFTY"]["Slice"])))
			#except Exception as e:
			#	print(e)
			#	print("Error occured. Unable to execute module")
			ed=datetime.now()
			print("module ran in",ed-st)
			print("\n\n***Restarting Bot***\n\n")
			print("Looking for changes..........")
		take_response()

	def stop_check():
		#th1.join()
		print("BOT STOPPED.SHUTING DOWN")
		app.shutdown()
		exit()
	print("\n\n***Running Version code",creds.version_code,"***\n\n")
	print("Setting up Bot...Please Wait.....")
	saveTokeninfo()
	#print("Please make some Changes on Excel Sheet...............")
	

	with open('config.json') as f:
		config = json.load(f)
		f.close()

	app = App(config)
	app.start()

	take_response()

if __name__ == '__main__':
	#print("main")
	th1 = threading.Thread(target=main())

	th1.start()

