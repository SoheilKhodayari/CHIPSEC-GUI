
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

		self.setHorizontalHeaderLabels(['Color Code','Criticality','Expected Result','Test Result','Test Description','Option Under Test','Test Name'])



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


    	# test 1
    	flockdn_res = self.FLOCKDN(stderrAsList)

    	# test 2
    	smm_bwp_2_res = self.SMM_BWP_2(stderrAsList)
    	tco_smi_lock_res = self.TCO_SMI_LOCK(stderrAsList)
    	smi_lock_res = self.SMI_LOCK(stderrAsList)
    	global_smi_en_res = self.Global_SMI_EN(stderrAsList)
    	tco1_cnt_en_res = self.TCO1_CNT(stderrAsList)

    	# test 3
    	bios_keyboard_buff = self.BIOS_Keyboard_Buffer(stderrAsList)

    	# test 4
    	bioswe_res = self.BIOSWE(stderrAsList)
    	ble_res = self.BLE(stderrAsList)
    	src_res = self.SRC(stderrAsList)
    	tss = self.TSS(stderrAsList)
    	smm_bwp_res = self.SMM_BWP(stderrAsList)

    	# test 5
    	d_lck_res = self.D_LCK(stderrAsList)

    	# test 6 = 
    	rtc_ue_res = self.UE(stderrAsList)
    	rtc_ll_res = self.LL(stderrAsList)
    	rtc_ul_res = self.UL(stderrAsList)

    	#test 7
    	ia32_lock = self.Lock(stderrAsList)

    	#test 8
    	bbra_bbwa = self.BRRA_and_BRWA(stderrAsList)

    	#test 9
    	fdopss_res = self.FDOPSS(stderrAsList)


    	results = [flockdn_res,
    	smm_bwp_2_res, 
    	tco_smi_lock_res,
    	smi_lock_res,
    	global_smi_en_res,
    	tco1_cnt_en_res,
    	bios_keyboard_buff,
    	bioswe_res,
    	ble_res,
    	src_res,
    	tss,
	   	smm_bwp_res,
	   	d_lck_res,
	   	rtc_ue_res,
	   	rtc_ll_res,
	   	rtc_ul_res,
	   	ia32_lock,
	   	bbra_bbwa,
	   	fdopss_res
	   	]
    	self.outputData = results


# ----------------------------------------------------------------------------- #
#				 SPI Flash Controller Configuration Lock
# ----------------------------------------------------------------------------- #
    def FLOCKDN(self, stderrList):
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'FLOCKDN' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'


    	res = [FLOCKDN_COLOR_CODE,
    		    FLOCKDN_CRITICALITY,
    		    FLOCKDN_EXPECTED_RESULT,
    		    item,
    		    FLOCKDN_DESCRIPTION,
    		    FLOCKDN_REPR,
    		    FLOCKDN_TEST_NAME]
        return res

# ----------------------------------------------------------------------------- #
#				 SMI Events Configuration Functions
# ----------------------------------------------------------------------------- #

    def SMM_BWP_2(self, stderrList):
    	"""
			For SMI Events Configuration
    	"""
    	item = 'UNKNOWN'
    	msg_fail = "SMM BIOS region write protection has not been enabled (SMM_BWP is not used)"
    	msg_success = "SMM BIOS region write protection is enabled (SMM_BWP is used)"
    	for line in stderrList:
    		if msg_success in line:
    			item = "1"
    			break
    		elif msg_fail in line:
    			item = "0"
    			break

    	res =   [SMM_BWP_2_COLOR_CODE,
    		    SMM_BWP_2_CRITICALITY,
    		    SMM_BWP_2_EXPECTED_RESULT,
    		    item,
    		    SMM_BWP_2_DESCRIPTION,
    		    SMM_BWP_2_REPR,
    		    SMM_BWP_2_TEST_NAME]
        return res 


    def TCO_SMI_LOCK(self, stderrList):
    	item = 'UNKNOW'
    	msg_fail = "TCO SMI event configuration is not locked. TCO SMI events can be disabled"
    	msg_success = "TCO SMI configuration is locked (TCO SMI Lock)"
    	for line in stderrList:
    		if msg_success in line:
    			item = "1"
    			break
    		elif msg_fail in line:
    			item = "0"
    			break

    	res =   [TCO_SMI_LOCK_COLOR_CODE,
    		    TCO_SMI_LOCK_CRITICALITY,
    		    TCO_SMI_LOCK_EXPECTED_RESULT,
    		    item,
    		    TCO_SMI_LOCK_DESCRIPTION,
    		    TCO_SMI_LOCK_REPR,
    		    TCO_SMI_LOCK_TEST_NAME]
        return res 

    def SMI_LOCK(self, stderrList):
    	item = 'UNKNOWN'
    	msg_fail = "SMI events global configuration is not locked. SMI events can be disabled"
    	msg_success = "SMI events global configuration is locked (SMI Lock)"
    	for line in stderrList:
    		if msg_success in line:
    			item = "1"
    			break
    		elif msg_fail in line:
    			item = "0"
    			break
    			
    	res =   [SMI_LOCK_COLOR_CODE,
    		    SMI_LOCK_CRITICALITY,
    		    SMI_LOCK_EXPECTED_RESULT,
    		    item,
    		    SMI_LOCK_DESCRIPTION,
    		    SMI_LOCK_REPR,
    		    SMI_LOCK_TEST_NAME]
        return res 

    def Global_SMI_EN(self, stderrList):
    	item = 'UNKNOWN'
    	phrase = 'Global SMI enable'
    	for line in stderrList:
    		if phrase in line:
    			try:
    				q = line.split(':')
    				item = q[1].strip()
    				break
    			except:
    				item = 'UNKNOWN'
    	res =   [Global_SMI_EN_COLOR_CODE,
    		    Global_SMI_EN_CRITICALITY,
    		    Global_SMI_EN_EXPECTED_RESULT,
    		    item,
    		    Global_SMI_EN_DESCRIPTION,
    		    Global_SMI_EN_REPR,
    		    Global_SMI_EN_TEST_NAME]
        return res 


    def TCO1_CNT(self, stderrList):
    	item = 'UNKNOWN'
    	phrase = 'TCO SMI enable'
    	for line in stderrList:
    		if phrase in line:
    			try:
    				q = line.split(':')
    				item = q[1].strip()
    				break
    			except:
    				item = 'UNKNOWN'
    	res =   [TCO_SMI_EN_COLOR_CODE,
    		    TCO_SMI_EN_CRITICALITY,
    		    TCO_SMI_EN_EXPECTED_RESULT,
    		    item,
    		    TCO_SMI_EN_DESCRIPTION,
    		    TCO_SMI_EN_REPR,
    		    TCO_SMI_EN_TEST_NAME]
        return res 

# ----------------------------------------------------------------------------- #
#				 BIOS Keyboard Buffer
# ----------------------------------------------------------------------------- #

    def BIOS_Keyboard_Buffer(self, stderrList):
    	item = 'UNKOWN'
    	phrase_success = "Keyboard buffer looks empty"
    	phrase_failure = "Keyboard buffer is not empty"
    	for line in stderrList:
    		if phrase_success in line:
    			item = "Looks Empty/Zero"
    			break
    		elif phrase_failure in line:
    			item = "Not Empty/Zero"
    			break
    	res =   [BIOS_KEYBOARD_BUFF_COLOR_CODE,
    		    BIOS_KEYBOARD_BUFF_CRITICALITY,
    		    BIOS_KEYBOARD_BUFF_EXPECTED_RESULT,
    		    item,
    		    BIOS_KEYBOARD_BUFF_DESCRIPTION,
    		    BIOS_KEYBOARD_BUFF_REPR,
    		    BIOS_KEYBOARD_BUFF_TEST_NAME]
        return res 

# ----------------------------------------------------------------------------- #
#				 BIOS Region Write Protection
# ----------------------------------------------------------------------------- #

    def BIOSWE(self, stderrList):
    	"""
			For BIOS Region Write Protection
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'BIOSWE' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [BIOSWE_COLOR_CODE,
    		    BIOSWE_CRITICALITY,
    		    BIOSWE_EXPECTED_RESULT,
    		    item,
    		    BIOSWE_DESCRIPTION,
    		    BIOSWE_REPR,
    		    BIOSWE_TEST_NAME]
        return res

    def BLE(self, stderrList):
    	"""
			For BIOS Region Write Protection
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'BLE' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [BLE_COLOR_CODE,
    		    BLE_CRITICALITY,
    		    BLE_EXPECTED_RESULT,
    		    item,
    		    BLE_DESCRIPTION,
    		    BLE_REPR,
    		    BLE_TEST_NAME]
        return res

    def SRC(self, stderrList):
    	"""
			For BIOS Region Write Protection
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'SRC' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [SRC_COLOR_CODE,
    		    SRC_CRITICALITY,
    		    SRC_EXPECTED_RESULT,
    		    item,
    		    SRC_DESCRIPTION,
    		    SRC_REPR,
    		    SRC_TEST_NAME]
        return res

    def TSS(self, stderrList):
    	"""
			For BIOS Region Write Protection
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'TSS' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [TSS_COLOR_CODE,
    		    TSS_CRITICALITY,
    		    TSS_EXPECTED_RESULT,
    		    item,
    		    TSS_DESCRIPTION,
    		    TSS_REPR,
    		    TSS_TEST_NAME]
        return res

    def SMM_BWP(self, stderrList):
    	"""
			For BIOS Region Write Protection
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'SMM_BWP' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [SMM_BWP_COLOR_CODE,
    		    SMM_BWP_CRITICALITY,
    		    SMM_BWP_EXPECTED_RESULT,
    		    item,
    		    SMM_BWP_DESCRIPTION,
    		    SMM_BWP_REPR,
    		    SMM_BWP_TEST_NAME]
        return res

# ----------------------------------------------------------------------------- #
#				 Compatible SMM memory (SMRAM) Protection
# ----------------------------------------------------------------------------- #

    def D_LCK(self, stderrList):
    	"""
			For SMRAM Protection
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'D_LCK' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [D_LCK_COLOR_CODE,
    		    D_LCK_CRITICALITY,
    		    D_LCK_EXPECTED_RESULT,
    		    item,
    		    D_LCK_DESCRIPTION,
    		    D_LCK_REPR,
    		    D_LCK_TEST_NAME]
        return res

# ----------------------------------------------------------------------------- #
#				Protected RTC Memory Locations
# ----------------------------------------------------------------------------- #

    def UE(self, stderrList):
    	"""
			Protected RTC Memory Locations
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'UE' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [UE_COLOR_CODE,
    		    UE_CRITICALITY,
    		    UE_EXPECTED_RESULT,
    		    item,
    		    UE_DESCRIPTION,
    		    UE_REPR,
    		    UE_TEST_NAME]
        return res

    def LL(self, stderrList):
    	"""
			Protected RTC Memory Locations
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'LL' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [LL_COLOR_CODE,
    		    LL_CRITICALITY,
    		    LL_EXPECTED_RESULT,
    		    item,
    		    LL_DESCRIPTION,
    		    LL_REPR,
    		    LL_TEST_NAME]
        return res

    def UL(self, stderrList):
    	"""
			Protected RTC Memory Locations
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'UL' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [UL_COLOR_CODE,
    		    UL_CRITICALITY,
    		    UL_EXPECTED_RESULT,
    		    item,
    		    UL_DESCRIPTION,
    		    UL_REPR,
    		    UL_TEST_NAME]
        return res

# ----------------------------------------------------------------------------- #
#				IA32 Feature Control Lock
# ----------------------------------------------------------------------------- #
    def Lock(self, stderrList):

    	"""
			For IA32 Feature Control Lock
    	"""

    	phrase1='cpu'
    	phrase2='IA32_Feature_Control Lock ='
    	item = 'UNKNOWN'

    	test_success_msg = "Protected locations in RTC memory are locked"
    	test_failure_msg = "Protected locations in RTC memory are accessible (BIOS may not be using them)"

    	cpus_message_passed = False 

    	for line in stderrList:
    		if (phrase1 in line) and (phrase2 in line):
    			try:
	    			idx_cpu_num = line.index('cpu') +len('cpu')
	    			cpu_num = line[idx_cpu_num]
	    			

	    			idx_lock = line.index(phrase2) + len(phrase2) +1
	    			lock_value = line[idx_lock]

	    			if item=='UNKNOWN':
	    				item=''
	    			item += 'cpu{0}: {1},\n'.format(cpu_num,lock_value)
	    			cpus_message_passed = True # look for a possible termination from now on
	    		except:
	    			continue
	    	elif cpus_message_passed:
	    		if (test_success_msg in line) or (test_failure_msg in line):
	    			break

    	res =   [IA32_Lock_COLOR_CODE,
    		    IA32_Lock_CRITICALITY,
    		    IA32_Lock_EXPECTED_RESULT,
    		    item,
    		    IA32_Lock_DESCRIPTION,
    		    IA32_Lock_REPR,
    		    IA32_Lock_TEST_NAME]
        return res

# ----------------------------------------------------------------------------- #
#				SPI Flash Region Access Control
# ----------------------------------------------------------------------------- #

    def BRRA_and_BRWA(self, stderrList):
		#stderrList = stderr.split('\r\n')
		test_success_msg = "SPI flash permissions prevent SW from writing to flash descriptor"
		test_failure_msg = "SPI flash permissions allow SW to write flash descriptor"
		BRRA = ""
		BRWA = ""
		result = "UNKNOWN"
		flag1 = False
		flag2 = False
		for line in stderrList:
			if "BRRA" in line:
				try:
					idx = line.index('<<')
					BRRA = line[idx-3:idx-1]
					flag1 = True
					continue
				except:
					BRRA = 'UNKOWN' 
					continue 
			elif "BRWA" in line:
				try:
					idx = line.index('<<')
					BRWA = line[idx-3:idx-1]
					flag2 = True
					continue
				except:
					BRWA = 'UNKOWN' 
					continue 	 
			elif flag1 and flag2:
				if test_success_msg in line:
					result = "Passed"
					break
				elif test_failure_msg in line:
					result = "Failed"
					break
		result = "BRRA: {0},\nBRWA: {1},\n{2}".format(BRRA,BRWA,result)
		res =   [BBRA_BBWA_COLOR_CODE,
		BBRA_BBWA_CRITICALITY,
		BBRA_BBWA_EXPECTED_RESULT,
		result,
		BBRA_BBWA_DESCRIPTION,
		BBRA_BBWA_REPR,
		BBRA_BBWA_TEST_NAME]
		return res


# ----------------------------------------------------------------------------- #
#				SPI Flash Descriptor Security Override Pin-Strap
# ----------------------------------------------------------------------------- #

    def FDOPSS(self, stderrList):
    	"""
			For SPI Flash Descriptor Security Override Pin-Strap
    	"""
    	item = 'UNKNOWN'
    	for line in stderrList:
    		if 'FDOPSS' in line:
    			try:
	    			idx = line.index('<<')
	    			item = line[idx-2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [FDOPSS_COLOR_CODE,
    		    FDOPSS_CRITICALITY,
    		    FDOPSS_EXPECTED_RESULT,
    		    item,
    		    FDOPSS_DESCRIPTION,
    		    FDOPSS_REPR,
    		    FDOPSS_TEST_NAME]
        return res


    def BILD(self, stderr):
    	pass

    def TSS_2(self, stderr):
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





# ----------------------------------------------------------------------------- #
#				End Runnable QThread For Parsing Test Output
# ----------------------------------------------------------------------------- #
