import pandas as pd
import matplotlib.pyplot as plt 
import datetime

class TempInfo():
	def __init__(self, datafile='namakanui_temp.log'):
		'''
    	Read Namakanui Temperature data
    	
    	Input:
    	datafile = log data file name, default: 'namakanui_temp.log'
    	
        Use:

        data = data.TempInfo(datafile)
       '''
		self._datafile = datafile
		
		#read and organize data
		data=pd.read_table(datafile,delimiter=r"\s+", comment='#', header=None)
		data.columns=['hst', 'b3_pll', 'b3_110k', 'b3_p01', 'b3_15k', 'b3_wca', 'b6_pll', 'b6_4k', 'b6_110k', 'b6_p0', 'b6_15k', 'b6_p1', 'b7_pll', 'b7_4k', 'b7_110k', 'b7_p0', 'b7_15k', 'b7_p1']
		data.drop(data.tail(1).index, inplace=True)  # delete the time data at the last line
		data['hst']=pd.to_datetime(data['hst'], format='%Y-%m-%dT%H:%M:%S')
		self.data=data

	def PllTmp(self, sensor='b6_pll', time_start='2019-10-11T06:10:00', time_end='2019-10-11T20:20:00', display=True):
		'''
    	Pll temperature information for specified day
        
        Input:

        sensor = 'b3_pll' or 'b6_pll' or 'b7_pll' (default is b6_pll)
		time_start = 'yyyy-mm-ddTHH:MM:SS'
		time_end = 'yyyy-mm-ddTHH:MM:SS'
		display = True or False
		
        Use:

        hist = data.Hist(sensor, time_start, time_end, display)
        
        (time description example : 2019-10-11T20:20:00)      
        '''		
		#variable
		time_start = pd.to_datetime(time_start, format='%Y-%m-%dT%H:%M:%S')
		time_end = pd.to_datetime(time_end, format='%Y-%m-%dT%H:%M:%S')
		data_select=self.data[(self.data['hst'] > time_start) & (self.data['hst'] < time_end)].loc[:,['hst',sensor]]

		if (sensor == 'b3_pll') | (sensor == 'b6_pll') | (sensor == 'b7_pll'):
			if display == True:
				plt.scatter(data_select['hst'], data_select[sensor], s=0.5, label=sensor)
				plt.xlim(time_start, time_end)
				plt.axhline(y=318.15, color='r', linestyle='-')
				plt.xlabel('HST')
				plt.ylabel('(K)')
				plt.legend()
				plt.gcf().autofmt_xdate()
				plt.grid() 
		else:
			raise Exception('Wrong indication of sensor name. Type in \'b3_pll\' or \'b6_pll\' or \'b7_pll\'')
		
		return(min(data_select[sensor])-273.15, max(data_select[sensor])-273.15)

	def PllTmp_1day(self, sensor='b6_pll', display=True):
		'''
    	Pll temperature information for 1 day
        
        Input:

        sensor = 'b3_pll' or 'b6_pll' or 'b7_pll' (default is b6_pll)
		display = True or False
		
        Use:

        hist = data.Hist(sensor, time_start, time_end, display)
        
        (time description example : 2019-10-11T20:20:00)      
        '''			
		#variable
		time_start = datetime.datetime.now() - datetime.timedelta(1)
		time_end = datetime.datetime.now()
		data_select=self.data[(self.data['hst'] > time_start) & (self.data['hst'] < time_end)].loc[:,['hst',sensor]]

		if (sensor == 'b3_pll') | (sensor == 'b6_pll') | (sensor == 'b7_pll'):
			if display == True:
				plt.scatter(data_select['hst'], data_select[sensor], s=0.5, label=sensor)
				plt.xlim(time_start, time_end)
				plt.axhline(y=318.15, color='r', linestyle='-')
				plt.xlabel('HST')
				plt.ylabel('(K)')
				plt.legend()
				plt.gcf().autofmt_xdate()
				plt.grid() 
		else:
			raise Exception('Wrong indication of sensor name. Type in \'b3_pll\' or \'b6_pll\' or \'b7_pll\'')
					
		return(min(data_select[sensor])-273.15, max(data_select[sensor])-273.15)
	
	def Hist(self, time_start='2019-10-11T06:10:00', time_end='2019-10-11T20:20:00', bins=12):
		'''
    	Display and return histogram of operation time for specified day
        
        Input:

        bins  =  bin number of histgraham
        time_start = 'yyyy-mm-ddTHH:MM:SS'
		time_end = 'yyyy-mm-ddTHH:MM:SS'


        Use:

        hist = data.Hist(time_start, time_end, bins)
        
        (time description example : 2019-10-11T20:20:00)
        
        '''	
        
		#variable
		data_select=self.data[(self.data['hst'] > time_start) & (self.data['hst'] < time_end)]['hst']

		hist=plt.hist(data_select, bins=bins)
		plt.grid() 
		plt.gcf().autofmt_xdate()
			
		return(hist)

	def Hist_1day(self, bins=12):
		'''
    	Display and return histogram of operation time for 1day
        
    	Input:

        bins  =  bin number of histgraham

        Use:

        hist = data.Hist_1day(bins)
        '''
	
		#variable
		time_start = datetime.datetime.now() - datetime.timedelta(1)
		time_end = datetime.datetime.now()
		data_select=self.data[(self.data['hst'] > time_start) & (self.data['hst'] < time_end)]['hst']

		hist=plt.hist(data_select,bins=bins)
		plt.gcf().autofmt_xdate()
		plt.grid() 
			
		return(hist)