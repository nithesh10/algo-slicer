import os, pathlib, time
from threading import Thread
import creds

import pandas as pd


class App(Thread):

	_can_shutdown = False
	_database = {}
	def __init__(self, config:dict):
		Thread.__init__(self, daemon=False)
		self.CONFIG = config
		self.key = creds.API_KEY
		path = pathlib.Path(__file__).parent.resolve()
		self.filepath = os.path.join(path, config['filename'])

		self.update_parameters()

	def update_parameters(self):

		df1 = pd.read_excel(self.filepath,'Nifty',usecols="C,D,F,G")
		df2 = pd.read_excel(self.filepath,'BNF',usecols="C,D,F,G")
		df3 = pd.read_excel(self.filepath,'Nifty Customer Code')
		df4 = pd.read_excel(self.filepath,'BNF Customer Code')
		data={
			"NIFTY":
			{
				"EXS CE SELL":df1.iloc[0][0],
				"EXS PE SELL":df1.iloc[1][0],
				"EXS EXP SELL":df1.iloc[2][0],
				"NEW CE SELL":df1.iloc[4][0],
				"NEW PE SELL":df1.iloc[5][0],
				"NEW EXP SELL":df1.iloc[7][0],

				"EXS CE BUY":df1.iloc[0][2],
				"EXS PE BUY":df1.iloc[1][2],
				"EXS EXP BUY":df1.iloc[2][2],
				"NEW CE BUY":df1.iloc[4][2],
				"NEW PE BUY":df1.iloc[5][2],
				"NEW EXP BUY":df1.iloc[7][2],

				"ACC":df3['Client Code'].dropna().to_numpy(),
				"Lots":df3['New Total Lots'].dropna().to_numpy(),
				"Slice":df3['New Slicing'].dropna().to_numpy(),
				"Exs Lots":df3['Exs Total Lots'].dropna().to_numpy(),
				"Exs Slice":df3['Exs Slicing'].dropna().to_numpy(),
				"Force Sell":df1['FORCE S'].dropna().to_numpy(),
				"Force Buy":df1['FORCE B'].dropna().to_numpy(),


				"NIFTY QTY FRZ":df3['Qty Freeze'].dropna().to_numpy(),
				"WAIT":df3['Wait Time'].dropna().to_numpy(),

			},
			"BNF":
			{
				"EXS CE SELL":df2.iloc[0][0],
				"EXS PE SELL":df2.iloc[1][0],
				"EXS EXP SELL":df2.iloc[2][0],
				"NEW CE SELL":df2.iloc[4][0],
				"NEW PE SELL":df2.iloc[5][0],
				"NEW EXP SELL":df2.iloc[7][0],

				"EXS CE BUY":df2.iloc[0][2],
				"EXS PE BUY":df2.iloc[1][2],
				"EXS EXP BUY":df2.iloc[2][2],
				"NEW CE BUY":df2.iloc[4][2],
				"NEW PE BUY":df2.iloc[5][2],
				"NEW EXP BUY":df2.iloc[7][2],

				"ACC":df4['Client Code'].dropna().to_numpy(),
				"Lots":df4['New Total Lots'].dropna().to_numpy(),
				"Slice":df4['New Slicing'].dropna().to_numpy(),
				"Exs Lots":df4['Exs Total Lots'].dropna().to_numpy(),
				"Exs Slice":df4['Exs Slicing'].dropna().to_numpy(),
				"Force Sell":df2['FORCE S'].dropna().to_numpy(),
				"Force Buy":df2['FORCE B'].dropna().to_numpy(),

				"NIFTY QTY FRZ":df4['Qty Freeze'].dropna().to_numpy(),
				"WAIT":df4['Wait Time'].dropna().to_numpy(),
			}

		}
		creds.user_data=data;

		#return data
	def shutdown(self):
		self._can_shutdown = True

	def run(self):
		while True:
			try:
				if self._can_shutdown: break

			except Exception as e:
				_ = f"outer loop, {e}"
				print(_)
				continue