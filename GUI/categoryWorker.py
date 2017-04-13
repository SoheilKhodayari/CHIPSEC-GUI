
# ----------------------------------------------------------------------------- #
#						     Import Libaries
# ----------------------------------------------------------------------------- #

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from utils import _sudo_exec
from local_settings import *
from local_settings import ROOT_PASSWORD

# ----------------------------------------------------------------------------- #
#						   Category Table Class
# ----------------------------------------------------------------------------- #


class categoryTable(QtGui.QTableWidget):
    def __init__(self, data, *args):
        QtGui.QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setmydata(self):

        for i in range(self.rows):
            for j in range(self.cols):
            	cell_data = str(self.data[i][j])
                newitem = QtGui.QTableWidgetItem(cell_data)	
                self.setItem(i,j,newitem)

                # color i, j=0 based on data
                if j == 0:
                	if cell_data == "RED":
                		self.item(i,j).setBackground(QtGui.QColor(220,20,60))
                	elif cell_data == "YELLOW":
                		self.item(i,j).setBackground(QtGui.QColor(255,255,102))
                	elif cell_data == "ORANGE":
                		self.item(i,j).setBackground(QtGui.QColor(204,102,0))
                	elif cell_data == "ORANGE_LIGHT":
                		self.item(i,j).setBackground(QtGui.QColor(255,153,51))
                	elif cell_data == "GREEN":
                		self.item(i,j).setBackground(QtGui.QColor(0,204,0))

		self.setHorizontalHeaderLabels(['Color Code','Criticality', 'Test Result','Expected Result','Test Description','Option Under Test','Test Name'])



# ----------------------------------------------------------------------------- #
#				Runnable QThread For Parsing Test Output
# ----------------------------------------------------------------------------- #


class PythonThread (QtCore.QThread):
    def __init__(self, cmdline, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.cmdline = cmdline
        self.outputData = None

    def __del__(self):
    	self.wait()

    def start(self):
        QtCore.QThread.start(self)

    def run(self):
    	stderr = _sudo_exec(self.cmdline, ROOT_PASSWORD)
    	stderrAsList = stderr.split('\r\n')
    	results = []

  #   	self.outputData = [['RED','HIGH','1','1','this is description\n description\ndescription','FLOCKDB','smm'],
  #   	['ORANGE','HIGH','1','1','this is description\n description\ndescription','FLOCKDB','smm'],
		# ['ORANGE_LIGHT','HIGH','1','1','this is description\n description\ndescription','FLOCKDB','smm'],
		# ['YELLOW','HIGH','1','1','this is description\n description\ndescription','FLOCKDB','smm'],
		# ['GREEN','HIGH','1','1','this is description\n description\ndescription','FLOCKDB','smm']
  #   	]


    	flockdn_res = self.FLOCKDN(stderrAsList)
    	results.append(flockdn_res)


    	self.outputData = results

    def FLOCKDN(self, stderrList):
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'FLOCKDN' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    		except:
	    			item = 'UNKNOWN'

    	return [FLOCKDN_COLOR_CODE,
    		    FLOCKDN_CRITICALITY,
    		    FLOCKDN_EXPECTED_RESULT,
    		    item,
    		    FLOCKDN_DESCRIPTION,
    		    FLOCKDN_REPR,
    		    FLOCKDN_TEST_NAME]

    def SMM_BWP(self, stderr):
    	pass

    def SMI_LOCK(self, stderr):
    	pass

    def Global_SMI_EN(self, stderr):
    	pass

    def TCO1_CNT(self, stderr):
    	pass

    def BIOS_Keyboard_Buffer(self, stderr):
    	pass

    def BIOSWE(self, stderr):
    	pass

    def BLE(self, stderr):
    	pass

    def SRC(self, stderr):
    	pass

    def TSS(self, stderr):
    	pass

    def SMM_BWP(self, stderr):
    	pass

    def D_LCK(self, stderr):
    	pass

    def UE(self, stderr):
    	pass

    def LL(self, stderr):
    	pass

    def UL(self, stderr):
    	pass

    def Lock(self, stderr):
    	pass

    def BRRA_and_BRWA(self, stderr):
    	pass

    def FDOPSS(self, stderr):
    	pass

    def BILD(self, stderr):
    	pass

    def TSS(self, stderr):
    	pass

    def Checking_SMRR_range_base_programming(self, stderr):
    	pass

    def Checking_SMRR_range_mask_programming(self, stderr):
    	pass

    def Verifying_SMRR_range_base_and_mask_are_same_on_all_logical_cpus(self, stderr):
    	pass

    def IA32_SMRR_PHYSBASE(self, stderr):
    	pass

    def Remap_window_configuration(self, stderr):
    	pass

    def TOUUD(self, stderr):
    	pass

    def TOLUD(self, stderr):
    	pass

    def BDSM(self, stderr):
    	pass

    def BGSM(self, stderr):
    	pass

    def DPR(self, stderr):
    	pass

    def GGC(self, stderr):
    	pass

    def MESEG_MASK(self, stderr):
    	pass

    def PAVPC(self, stderr):
    	pass

    def REMAPBASE(self, stderr):
    	pass

    def REMAPLIMIT(self, stderr):
    	pass

    def TOLUD(self, stderr):
    	pass

    def TOM(self, stderr):
    	pass

    def TOUUD(self, stderr):
    	pass

    def TSEGMB(self, stderr):
    	pass

    def TSEG_1(self, stderr):
    	pass

    def SMRR_range(self, stderr):
    	pass

    def BLE_1(self, stderr):
    	pass

    def BLE_2(self, stderr):
    	pass

    def TSEG_2(self, stderr):
    	pass

