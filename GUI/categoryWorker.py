
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
    def __init__(self, cmdline, test_suite, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.cmdline = cmdline
        self.test_suite = test_suite
        self.outputData = None

    def __del__(self):
    	self.wait()

    def start(self):
        QtCore.QThread.start(self)

    def run(self):
		stderr = _sudo_exec(self.cmdline, ROOT_PASSWORD)
		stderrAsList = stderr.split('\r\n')
		results = []

		for test in self.test_suite:
			if test == "spi_lock":
				# test 1
				flockdn_res = self.FLOCKDN(stderrAsList)
				results.append(flockdn_res)
			elif test == "bios_smi":
				# test 2
				smm_bwp_2_res = self.SMM_BWP_2(stderrAsList)
				tco_smi_lock_res = self.TCO_SMI_LOCK(stderrAsList)
				smi_lock_res = self.SMI_LOCK(stderrAsList)
				global_smi_en_res = self.Global_SMI_EN(stderrAsList)
				tco1_cnt_en_res = self.TCO1_CNT(stderrAsList)
				results+=[smm_bwp_2_res,tco_smi_lock_res,smi_lock_res,global_smi_en_res,tco1_cnt_en_res]
			elif test == "bios_kbrd_buffer":
				# test 3
				bios_keyboard_buff = self.BIOS_Keyboard_Buffer(stderrAsList)
				results.append(bios_keyboard_buff)
			elif test == "bios_wp":
				# test 4
				bioswe_res = self.BIOSWE(stderrAsList)
				ble_res = self.BLE(stderrAsList)
				src_res = self.SRC(stderrAsList)
				tss = self.TSS(stderrAsList)
				smm_bwp_res = self.SMM_BWP(stderrAsList)
				results += [bioswe_res,ble_res,src_res,tss,smm_bwp_res]
			elif test == "smm":	
				# test 5
				d_lck_res = self.D_LCK(stderrAsList)
				results.append(d_lck_res)
			elif test == "rtclock":
				# test 6 = 
				rtc_ue_res = self.UE(stderrAsList)
				rtc_ll_res = self.LL(stderrAsList)
				rtc_ul_res = self.UL(stderrAsList)
				results+=[rtc_ue_res,rtc_ll_res,rtc_ul_res]
			elif test == "ia32cfg":
				#test 7
				ia32_lock = self.Lock(stderrAsList)
				results.append(ia32_lock)
			elif test == "spi_desc":
				#test 8
				bbra_bbwa = self.BRRA_and_BRWA(stderrAsList)
				results.append(bbra_bbwa)
			elif test == "spi_fdopss":
				#test 9
				fdopss_res = self.FDOPSS(stderrAsList)
				results.append(fdopss_res)
			elif test == "bios_ts":
				#test 10
				bild_res = self.BILD(stderrAsList)
				tss_2_res = self.TSS_2(stderrAsList)
				results += [bild_res,tss_2_res]
			elif test == "smrr":
				#test 11
				smrr_range_base_res = self.Checking_SMRR_range_base_programming(stderrAsList)
				smrr_range_mask_res = self.Checking_SMRR_range_mask_programming(stderrAsList)
				smrr_same_on_logical_cpus = self.Verifying_SMRR_range_base_and_mask_are_same_on_all_logical_cpus(stderrAsList)
				smrr_ia32_physbase_res = self.IA32_SMRR_PHYSBASE(stderrAsList)
				smrr_protection_cache_res = self.SMRR_Protection_Cache_Attack(stderrAsList)
				results += [smrr_range_base_res,smrr_range_mask_res,
						   smrr_same_on_logical_cpus,smrr_ia32_physbase_res,
				           smrr_protection_cache_res]
			elif test == "remap":
				#test 12
				remap_win_conf_res = self.Remap_window_configuration(stderrAsList)
				touud_res = self.TOUUD(stderrAsList)
				tolud_res = self.TOLUD(stderrAsList)
				results+=[touud_res,tolud_res]
			elif test == "memconfig":
				#test 13
				bdsm_res = self.BDSM(stderrAsList)
				bgsm_res = self.BGSM(stderrAsList)
				ggc_res = self.GGC(stderrAsList)
				dpr_res = self.DPR(stderrAsList)
				mseg_mask_res = self.MESEG_MASK(stderrAsList)
				pavpc_res = self.PAVPC(stderrAsList)
				remapbase_res = self.REMAPBASE(stderrAsList)
				remaplimit_res = self.REMAPLIMIT(stderrAsList)
				tolud_2_res = self.TOLUD_2(stderrAsList)
				tom_res = self.TOM(stderrAsList)
				touud_2_res = self.TOUUD_2(stderrAsList)
				tseg_mb_res = self.TSEGMB(stderrAsList)
				results+=[bdsm_res,bgsm_res,ggc_res,dpr_res,mseg_mask_res,pavpc_res,
						  remapbase_res,remaplimit_res,tolud_2_res,tom_res,
						  touud_2_res,tseg_mb_res]
			elif test == "smm_dma":
				#test 14
				test_14_res_list = self.TSEG_1_and_SMRR_range(stderrAsList)
				tseg_1_res = test_14_res_list[0]
				smrr_range_res = test_14_res_list[1]
				results+=[tseg_1_res,smrr_range_res]
			elif test == "s3bootscript":
				#test 15
				s3bootscript_res = self.S3_Boot_Script(stderrAsList)
				dispatch_opcodes_res = self.Dispatch_Opcodes(stderrAsList)
				results+=[s3bootscript_res,dispatch_opcodes_res]

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



# ----------------------------------------------------------------------------- #
#				BIOS Interface Lock including Top Swap Mode
# ----------------------------------------------------------------------------- #

    def BILD(self, stderrList):
    	"""
			BIOS Interface Lock including Top Swap Mode
    	"""
    	item = 'UNKNOWN'
    	phrase = "BiosInterfaceLockDown (BILD) control ="
    	for line in stderrList:
    		if phrase in line:
    			try:
	    			idx = line.index('=')
	    			item = line[idx+2]
	    			break
	    		except:
	    			item = 'UNKNOWN'

    	res =   [BILD_COLOR_CODE,
    		    BILD_CRITICALITY,
    		    BILD_EXPECTED_RESULT,
    		    item,
    		    BILD_DESCRIPTION,
    		    BILD_REPR,
    		    BILD_TEST_NAME]
        return res
    def TSS_2(self, stderrList):
    	"""
			BIOS Interface Lock including Top Swap Mode
    	"""
    	item = 'UNKNOWN'
    	msg_success = "BIOS Top Swap mode is enabled (TSS = 1)"
    	msg_failure = "BIOS Top Swap mode is disabled (TSS = 0)"
    	for line in stderrList:
    		if msg_success in line:
    			item = "1"
    			break
    		elif msg_failure in line:
    			item = "0"
    			break

    	res =   [TSS_2_COLOR_CODE,
    		    TSS_2_CRITICALITY,
    		    TSS_2_EXPECTED_RESULT,
    		    item,
    		    TSS_2_DESCRIPTION,
    		    TSS_2_REPR,
    		    TSS_2_TEST_NAME]
        return res

# ----------------------------------------------------------------------------- #
#							CPU SMM Cache Poisoning
# ----------------------------------------------------------------------------- #


    def Checking_SMRR_range_base_programming(self, stderrList):
    	"""
			For CPU SMM Cache Poisoning
    	"""
    	item = 'UNKNOWN'
    	msg_success = "OK so far. SMRR range base is programmed"
    	msg_failure = "SMRR range base is not programmed"
    	for line in stderrList:
    		if msg_success in line:
    			item = "passed"
    			break
    		elif msg_failure in line:
    			item = "failed"
    			break

    	res =   [SMRR_range_base_COLOR_CODE,
    		    SMRR_range_base_CRITICALITY,
    		    SMRR_range_base_EXPECTED_RESULT,
    		    item,
    		    SMRR_range_base_DESCRIPTION,
    		    SMRR_range_base_REPR,
    		    SMRR_range_base_TEST_NAME]
        return res

    def Checking_SMRR_range_mask_programming(self, stderrList):
    	"""
			For CPU SMM Cache Poisoning
    	"""
    	item = 'UNKNOWN'
    	msg_success = "OK so far. SMRR range is enabled"
    	msg_failure = "SMRR range is not enabled"
    	for line in stderrList:
    		if msg_success in line:
    			item = "passed"
    			break
    		elif msg_failure in line:
    			item = "failed"
    			break

    	res =   [SMRR_range_mask_COLOR_CODE,
    		    SMRR_range_mask_CRITICALITY,
    		    SMRR_range_mask_EXPECTED_RESULT,
    		    item,
    		    SMRR_range_mask_DESCRIPTION,
    		    SMRR_range_mask_REPR,
    		    SMRR_range_mask_TEST_NAME]
        return res

    def Verifying_SMRR_range_base_and_mask_are_same_on_all_logical_cpus(self, stderrList):
    	"""
			For CPU SMM Cache Poisoning
    	"""
    	item = 'UNKNOWN'
    	msg_success = "OK so far. SMRR range base/mask match on all logical CPUs"
    	msg_failure = "SMRR range base/mask do not match on all logical CPUs"
    	for line in stderrList:
    		if msg_success in line:
    			item = "passed"
    			break
    		elif msg_failure in line:
    			item = "failed"
    			break

    	res =   [SMRR_range_base_and_mask_are_same_COLOR_CODE,
    		    SMRR_range_base_and_mask_are_same_CRITICALITY,
    		    SMRR_range_base_and_mask_are_same_EXPECTED_RESULT,
    		    item,
    		    SMRR_range_base_and_mask_are_same_DESCRIPTION,
    		    SMRR_range_base_and_mask_are_same_REPR,
    		    SMRR_range_base_and_mask_are_same_TEST_NAME]
        return res

    def IA32_SMRR_PHYSBASE(self, stderrList):
    	"""
			For CPU SMM Cache Poisoning
    	"""
    	item = 'UNKNOWN'
    	phrase = "IA32_SMRR_PHYSBASE = "
    	for line in stderrList:
    		if phrase in line:
    			try:
	    			idx_start = line.index(phrase) + len(phrase)
	    			idx_end = line.index('<<')-1
	    			item = line[idx_start:idx_end]
	    			break
	    		except:
	    			item = "UNKNOWN"

    	res =   [IA32_SMRR_PHYSBASE_COLOR_CODE,
    		    IA32_SMRR_PHYSBASE_CRITICALITY,
    		    IA32_SMRR_PHYSBASE_EXPECTED_RESULT,
    		    item,
    		    IA32_SMRR_PHYSBASE_DESCRIPTION,
    		    IA32_SMRR_PHYSBASE_REPR,
    		    IA32_SMRR_PHYSBASE_TEST_NAME]
        return res

    def SMRR_Protection_Cache_Attack(self, stderrList):
    	"""
			For CPU SMM Cache Poisoning
    	"""
    	item = 'UNKNOWN'
    	msg_success = "SMRR protection against cache attack is properly configured"
    	msg_failure = "SMRR protection against cache attack is not configured properly"
    	for line in stderrList:
    		if msg_success in line:
    			item = "passed"
    			break
    		elif msg_failure in line:
    			item = "failed"
    			break

    	res =   [SMMR_PROTECTION_AGAINST_CACHE_ATTACK_COLOR_CODE,
    		    SMMR_PROTECTION_AGAINST_CACHE_ATTACK_CRITICALITY,
    		    SMMR_PROTECTION_AGAINST_CACHE_ATTACK_EXPECTED_RESULT,
    		    item,
    		    SMMR_PROTECTION_AGAINST_CACHE_ATTACK_DESCRIPTION,
    		    SMMR_PROTECTION_AGAINST_CACHE_ATTACK_REPR,
    		    SMMR_PROTECTION_AGAINST_CACHE_ATTACK_TEST_NAME]
        return res


# ----------------------------------------------------------------------------- #
#					   Memory Remap Configuration
# ----------------------------------------------------------------------------- #

    def Remap_window_configuration(self, stderrList):
    	"""
			For Memory Remap Configuration -chipsec/modules/remap.py
    	"""
    	item = 'UNKNOWN'
    	msg_success = "Remap window configuration is correct: REMAPBASE <= REMAPLIMIT < TOUUD"
    	msg_failure = "Remap window configuration is not correct"
    	for line in stderrList:
    		if msg_success in line:
    			item = "passed"
    			break
    		elif msg_failure in line:
    			item = "failed"
    			break

    	res =   [RemapWindowConfig_COLOR_CODE,
    		    RemapWindowConfig_CRITICALITY,
    		    RemapWindowConfig_EXPECTED_RESULT,
    		    item,
    		    RemapWindowConfig_DESCRIPTION,
    		    RemapWindowConfig_REPR,
    		    RemapWindowConfig_TEST_NAME]
        return res

    def TOUUD(self, stderrList):
    	"""
			For Memory Remap Configuration -chipsec/modules/remap.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "TOUUD"
    	same_phrase_other_test = 'PCI'
    	for line in stderrList:
    		if phrase in line:
    		   if same_phrase_other_test not in line:
    		   		try:
	    		   		start_idx = line.index(phrase)
	    		   		item = line[start_idx:]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [TOUUD_COLOR_CODE,
    		    TOUUD_CRITICALITY,
    		    TOUUD_EXPECTED_RESULT,
    		    item,
    		    TOUUD_DESCRIPTION,
    		    TOUUD_REPR,
    		    TOUUD_TEST_NAME]
        return res


    def TOLUD(self, stderrList):
    	"""
			For Memory Remap Configuration -chipsec/modules/remap.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "TOLUD"
    	same_phrase_other_test = 'PCI'
    	for line in stderrList:
    		if phrase in line:
    		   if same_phrase_other_test not in line:
    		   		try:
	    		   		start_idx = line.index(phrase)
	    		   		item = line[start_idx:]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [TOLUD_COLOR_CODE,
    		    TOLUD_CRITICALITY,
    		    TOLUD_EXPECTED_RESULT,
    		    item,
    		    TOLUD_DESCRIPTION,
    		    TOLUD_REPR,
    		    TOLUD_TEST_NAME]
        return res

# ----------------------------------------------------------------------------- #
#				 Host Bridge Memory Map Locks
# ----------------------------------------------------------------------------- #

    def BDSM(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_BDSM"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [BDSM_COLOR_CODE,
    		    BDSM_CRITICALITY,
    		    BDSM_EXPECTED_RESULT,
    		    item,
    		    BDSM_DESCRIPTION,
    		    BDSM_REPR,
    		    BDSM_TEST_NAME]
        return res

    def BGSM(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_BGSM"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [BGSM_COLOR_CODE,
    		    BGSM_CRITICALITY,
    		    BGSM_EXPECTED_RESULT,
    		    item,
    		    BGSM_DESCRIPTION,
    		    BGSM_REPR,
    		    BGSM_TEST_NAME]
        return res

    def DPR(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_DPR"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [DPR_COLOR_CODE,
    		    DPR_CRITICALITY,
    		    DPR_EXPECTED_RESULT,
    		    item,
    		    DPR_DESCRIPTION,
    		    DPR_REPR,
    		    DPR_TEST_NAME]
        return res

    def GGC(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_GGC"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [GGC_COLOR_CODE,
    		    GGC_CRITICALITY,
    		    GGC_EXPECTED_RESULT,
    		    item,
    		    GGC_DESCRIPTION,
    		    GGC_REPR,
    		    GGC_TEST_NAME]
        return res

    def MESEG_MASK(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_MESEG_MASK"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [MESEG_MASK_COLOR_CODE,
    		    MESEG_MASK_CRITICALITY,
    		    MESEG_MASK_EXPECTED_RESULT,
    		    item,
    		    MESEG_MASK_DESCRIPTION,
    		    MESEG_MASK_REPR,
    		    MESEG_MASK_TEST_NAME]
        return res

    def PAVPC(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_PAVPC"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [PAVPC_COLOR_CODE,
    		    PAVPC_CRITICALITY,
    		    PAVPC_EXPECTED_RESULT,
    		    item,
    		    PAVPC_DESCRIPTION,
    		    PAVPC_REPR,
    		    PAVPC_TEST_NAME]
        return res

    def REMAPBASE(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_REMAPBASE"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [REMAPBASE_COLOR_CODE,
    		    REMAPBASE_CRITICALITY,
    		    REMAPBASE_EXPECTED_RESULT,
    		    item,
    		    REMAPBASE_DESCRIPTION,
    		    REMAPBASE_REPR,
    		    REMAPBASE_TEST_NAME]
        return res

    def REMAPLIMIT(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_REMAPLIMIT"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [REMAPLIMIT_COLOR_CODE,
    		    REMAPLIMIT_CRITICALITY,
    		    REMAPLIMIT_EXPECTED_RESULT,
    		    item,
    		    REMAPLIMIT_DESCRIPTION,
    		    REMAPLIMIT_REPR,
    		    REMAPLIMIT_TEST_NAME]
        return res

    def TOLUD_2(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_TOLUD"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [TOLUD_2_COLOR_CODE,
    		    TOLUD_2_CRITICALITY,
    		    TOLUD_2_EXPECTED_RESULT,
    		    item,
    		    TOLUD_2_DESCRIPTION,
    		    TOLUD_2_REPR,
    		    TOLUD_2_TEST_NAME]
        return res

    def TOM(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_TOM"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [TOM_COLOR_CODE,
    		    TOM_CRITICALITY,
    		    TOM_EXPECTED_RESULT,
    		    item,
    		    TOM_DESCRIPTION,
    		    TOM_REPR,
    		    TOM_TEST_NAME]
        return res

    def TOUUD_2(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_TOUUD"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [TOUUD_2_COLOR_CODE,
    		    TOUUD_2_CRITICALITY,
    		    TOUUD_2_EXPECTED_RESULT,
    		    item,
    		    TOUUD_2_DESCRIPTION,
    		    TOUUD_2_REPR,
    		    TOUUD_2_TEST_NAME]
        return res

    def TSEGMB(self, stderrList):
    	"""
			 Host Bridge Memory Map Locks -chipsec/modules/memconfig.py
    	"""
    	item = 'UNKNOWN'
    	phrase = "PCI0.0.0_TSEGMB"
    	for line in stderrList:
    		if phrase in line:
    		   		try:
    		   			start_idx = line.index(phrase)
	    		   		end_idx = line.index("LOCKED")+len("LOCKED")+1
	    		   		item = line[start_idx:end_idx]
	    		   		item = item.strip()
	    		   		break
	    		   	except:
	    		   		item = "UNKNOWN"

    	res =   [TSEGMB_COLOR_CODE,
    		    TSEGMB_CRITICALITY,
    		    TSEGMB_EXPECTED_RESULT,
    		    item,
    		    TSEGMB_DESCRIPTION,
    		    TSEGMB_REPR,
    		    TSEGMB_TEST_NAME]
        return res

# ----------------------------------------------------------------------------- #
#				SMM TSEG Range Configuration Check
# ----------------------------------------------------------------------------- #

    def TSEG_1_and_SMRR_range(self, stderrList):
    	"""
			 SMM TSEG Range Configuration Check -chipsec/modules/smm_dma.py
    	"""
    	item1 = 'UNKNOWN'
    	item2 = 'UNKNOWN'
    	phrase = "SMM TSEG Range Configuration Check"
    	for i in range(len(stderrList)):
    		if phrase in stderrList[i]:
    		   		try:
    		   			TSEG_line = stderrList[i+2]
    		   			tseg_start_idx = TSEG_line.index('TSEG')
    		   			tseg_end_idx = TSEG_line.index('(size')
    		   			item1 = TSEG_line[tseg_start_idx: tseg_end_idx]

    		   			SMRR_range_line = stderrList[i+3]
    		   			smrr_start_idx = SMRR_range_line.index('SMRR')
    		   			smrr_end_idx = SMRR_range_line.index('(size')
    		   			item2 = SMRR_range_line[smrr_start_idx: smrr_end_idx]
    		   			break
	    		   	except:
	    		   		item1 = "UNKNOWN"
	    		   		item2 = "UNKNOWN"

    	res1 =   [TSEG_1_COLOR_CODE,
    		    TSEG_1_CRITICALITY,
    		    TSEG_1_EXPECTED_RESULT,
    		    item1,
    		    TSEG_1_DESCRIPTION,
    		    TSEG_1_REPR,
    		    TSEG_1_TEST_NAME]

    	res2 =   [SMRR_Range_COLOR_CODE,
    		    SMRR_Range_CRITICALITY,
    		    SMRR_Range_EXPECTED_RESULT,
    		    item2,
    		    SMRR_Range_DESCRIPTION,
    		    SMRR_Range_REPR,
    		    SMRR_Range_TEST_NAME]

        return [res1, res2]
        


# ----------------------------------------------------------------------------- #
#				S3 Resume Boot-Script Protections
# ----------------------------------------------------------------------------- #
    def S3_Boot_Script(self, stderrList):
	    	"""
				 S3 Resume Boot-Script Protections -/common/uefi/s3bootscript.py
	    	"""
	    	item = 'UNKNOWN'
	    	msg_failure_1 = "S3 Boot-Script and Dispatch entry-points do not appear to be protected"
	    	msg_failure_2 = "S3 Boot-Script is not in SMRAM but Dispatch entry-points appear to be protected. Recommend further testing"
	    	msg_success = "S3 Boot-Script is inside SMRAM. The script is protected but Dispatch opcodes cannot be inspected"
	    	for line in stderrList:
	    		if (msg_failure_1 in line) or (msg_failure_2 in line):
	    				item = "Unprotected"
	    				break
	    		elif msg_success in line:
	    				item = "Protected"
	    				break

	    	res =   [S3_BootScript_COLOR_CODE,
	    		    S3_BootScript_CRITICALITY,
	    		    S3_BootScript_EXPECTED_RESULT,
	    		    item,
	    		    S3_BootScript_DESCRIPTION,
	    		    S3_BootScript_REPR,
	    		    S3_BootScript_TEST_NAME]
	        return res
    def Dispatch_Opcodes(self, stderrList):
	    	"""
				 S3 Resume Boot-Script Protections -/common/uefi/s3bootscript.py
	    	"""
	    	item = 'UNKNOWN'
	    	msg_failure = "S3 Boot-Script and Dispatch entry-points do not appear to be protected"
	    	msg_success = "S3 Boot-Script is not in SMRAM but Dispatch entry-points appear to be protected. Recommend further testing"
	    	msg_state_unknown_dispatch = "S3 Boot-Script is inside SMRAM. The script is protected but Dispatch opcodes cannot be inspected"
	    	for line in stderrList:
	    		if (msg_failure in line):
	    				item = "Unprotected"
	    				break
	    		elif msg_success in line:
	    				item = "Protected"
	    				break
	    		elif msg_state_unknown_dispatch in line:
	    				item = "UNKNOWN,\nDispatch Opcodes\nCan not be\ninspected"
	    				break

	    	res =   [Dispatch_Opcodes_COLOR_CODE,
	    		    Dispatch_Opcodes_CRITICALITY,
	    		    Dispatch_Opcodes_EXPECTED_RESULT,
	    		    item,
	    		    Dispatch_Opcodes_DESCRIPTION,
	    		    Dispatch_Opcodes_REPR,
	    		    Dispatch_Opcodes_TEST_NAME]
	        return res


# ----------------------------------------------------------------------------- #
#				SMM TSEG Range Configuration Check
# ----------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------- #
#				End Runnable QThread For Parsing Test Output
# ------------------------------------------------------------------------------------------------- #
