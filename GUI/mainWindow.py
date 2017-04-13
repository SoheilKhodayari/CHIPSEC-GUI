# ----------------------------------------------------------------------------- #
#						     Import Libraries
# ----------------------------------------------------------------------------- #

import sys
import os
import csv
import uuid, time
import xlwt  # sudo pip install xlwt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import Qt
from utils import _sudo_exec 
from local_settings import AVAILABLE_TESTS, TEST_TOOL_TIPS,DETAILED_TEST_TOOL_TIPS
from local_settings import VERBOSE_MODE_SHORT_MSG, VERBOSE_MODE_LONG_MSG, \
						   DEBUG_MODE_SHORT_MSG, DEBUG_MODE_LONG_MSG, \
						   FAILFAST_MODE_SHORT_MSG, FAILFAST_MODE_LONG_MSG, \
						   NOTIME_MODE_SHORT_MSG, NOTIME_MODE_LONG_MSG, \
						   IGNORE_PLATFORM_MODE_SHORT_MSG, IGNORE_PLATFORM_MODE_LONG_MSG, \
						   NODRIVER_MODE_SHORT_MSG, NODRIVER_MODE_LONG_MSG, \
						   ADDITIONAL_TEST_I_SHORT_MSG, ADDITIONAL_TEST_I_LONG_MSG, \
						   ADDITIONAL_TEST_USAGE_MESSAGE, REPORT_PATH, ROOT_PASSWORD, \
						   BASE_PATH

from categoryWorker import *


lib_path = os.path.abspath(os.path.join('../chipsec'))
sys.path.insert(0, lib_path)
from chipsec.chipset import Chipset_Code


# ----------------------------------------------------------------------------- #
#						  END Import Libraries
# ----------------------------------------------------------------------------- #

class TestCaseRow(QtGui.QWidget):
	def __init__(self, labelText, testName, testShortDesc, testLongDesc):
		super(TestCaseRow, self).__init__()

		self.labelText = labelText
		self.testName = testName
		self.descShort = testShortDesc
		self.descDetailed = testLongDesc

		self.layout = QHBoxLayout(self)
		self.checkBox = QtGui.QCheckBox(self)
		self.label = QtGui.QLabel(self)
		self.label.setText(self.labelText)
		self.checkBox.setFixedWidth(20)
		self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

		self.layout.addWidget(self.checkBox)
		self.layout.addWidget(self.label)
		if testName != "--ALL--":
			self.iBtn = QtGui.QPushButton('i',self)
			self.iBtn.setFixedSize(15,18)
			self.iBtn.clicked.connect(lambda: self._show_desc_dialog(self.testName, self.descShort, self.descDetailed))
			self.layout.addWidget(self.iBtn)
		self.setLayout(self.layout)


	def _show_desc_dialog(self, testName, descShort, descDetailed):

		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)

		if testName == "--Other--":
			msg.setText("check this box to run another test of your own.") 
		else:
			msg.setText("This is {0} tool tip message box.".format(testName))
		msg.setInformativeText(descShort)
		msg.setWindowTitle("Help")
		msg.setDetailedText(descDetailed)

		msg.setStandardButtons(QMessageBox.Ok) # | QMessageBox.Cancel
		msg.buttonClicked.connect(msg.close)
		retval = msg.exec_()




class mainWindow(QtGui.QWidget):

	def __init__(self, parent):

		super(mainWindow, self).__init__()
		self.parent = parent
		self.test_summary_widget = None

		# -- specify test options for the chipsec
		self._test_options_dict = {}
		self._test_suite = None    # list of all available test names

		self._desired_test_list = [] # list of selected tests to run

		self._test_case_row_widgets = [] # list of row widgets

		self._first_run_done = False


		self._fetch_test_suite_list(False) # pass True to read from Settings
		self._initUI()


	# ---------------------------------------------------------------------------------#
	#							CHIOSEC TEST API
	# ---------------------------------------------------------------------------------#

	def add_chipsec_option(self, key, value):
		"""
			key is a linux switch (i.e  -m specifies module)
			value is the switch value (i.e common.bios_wp for -m switch)
		"""
		self._test_options_dict[key] = value

	def remove_chipsec_option(self,key):

		del self._test_options_dict[key]

	def set_chipsec_option_dict(self,dictionary):

		self._test_options_dict = dictionary

	def _fetch_test_suite_list(self, read_from_settings = False):
		"""
			Fetch available module names
			ATTENTION: File names are treated as module names in case of True 
					   being passed for read_from_settings

		"""
		if read_from_settings:
			global AVAILABLE_TESTS
			self._test_suite = AVAILABLE_TESTS
			return AVAILABLE_TESTS
		modules_dir = "../chipsec/modules/common"
		results = []
		for file in os.listdir(modules_dir):
			if self.parent.get_app_model() == "pyc":
				if (file.endswith(".pyc")) and (file != "__init__.pyc"):
					results.append(file[:-4])
			else:
				if (file.endswith(".py")) and (file != "__init__.py"):
					results.append(file[:-3])		
		self._test_suite = results
		return results




	# ---------------------------------------------------------------------------------#
	#						    END CHIOSEC TEST API
	# ---------------------------------------------------------------------------------#


	# ---------------------------------------------------------------------------------#
	#						    SETUP MAIN GRAPHIC
	# ---------------------------------------------------------------------------------#

	def _initUI(self):

		self.hSpaceing=QtGui.QHBoxLayout()
		self.lbl1=QtGui.QLabel()
		self.lbl1.setFixedHeight(20)
		self.hSpaceing.addWidget(self.lbl1)


		# ------------------ TestSuite Checkbox Area -------------------------------------------------#
		vlay = QVBoxLayout()
		global TEST_TOOL_TIPS
		global DETAILED_TEST_TOOL_TIPS

		selectAllRowWidget = TestCaseRow("<< SELECT ALL >>","--ALL--","","")
		self._test_case_row_widgets.append(selectAllRowWidget)
		vlay.addWidget(selectAllRowWidget)
		selectAllRowWidget.checkBox.stateChanged.connect(lambda checked: self._on_test_suite_item_state_changed(checked, selectAllRowWidget))

		for test in self._test_suite:
			shortDesc = ""
			longDesc = ""
			if test in TEST_TOOL_TIPS:
				shortDesc = TEST_TOOL_TIPS[test]
			if test in DETAILED_TEST_TOOL_TIPS:
				longDesc = DETAILED_TEST_TOOL_TIPS[test]

			rowWidget = TestCaseRow(test,test,shortDesc,longDesc)
			self._test_case_row_widgets.append(rowWidget)
			vlay.addWidget(rowWidget)

			# connect to event handler
			rowWidget.checkBox.stateChanged.connect(lambda checked, r=rowWidget: self._on_test_suite_item_state_changed(checked, r))


		self.OtherTestRowWidget = TestCaseRow("<< OTHER TEST >>","--Other--","test file must be set on the right-hand side window",ADDITIONAL_TEST_I_LONG_MSG)
		self._test_case_row_widgets.append(self.OtherTestRowWidget)
		vlay.addWidget(self.OtherTestRowWidget)
		self.OtherTestRowWidget.checkBox.stateChanged.connect(lambda checked: self._on_test_suite_item_state_changed(checked, self.OtherTestRowWidget))

		scroll = QtGui.QScrollArea()
		scroll.setWidgetResizable(True)
		scroll.setFixedHeight(300)
		scroll.setFixedWidth(400)

		self.scrollWidget = QWidget()
		self.scrollWidget.setLayout(vlay)
		scroll.setWidget(self.scrollWidget)


		self.TestSuiteOverallLayout = QtGui.QVBoxLayout()
		self.TestSuiteOverallLayout.addWidget(scroll)

		# ------------------ END TestSuite Checkbox Area ---------------------------------------------#



		scroll2 = QtGui.QScrollArea()
		scroll2.setWidgetResizable(True)
		scroll2.setFixedHeight(300)
		scroll2.setFixedWidth(400)
		OverallQVLayoutNearTestSuite = QtGui.QVBoxLayout()

		# -- create Hboxes and add to OverallQVLayoutNearTestSuite as a row
		self._enable_output_save_lbl = QtGui.QLabel()
		self._enable_output_save_lbl.setText("Save Test Output:")
		self._enable_output_save_lbl.setFixedWidth(110)
		self._enable_output_save_chkbox = QtGui.QCheckBox()
		QHRow1 = QtGui.QHBoxLayout()
		QHRow1.addWidget(self._enable_output_save_lbl)
		QHRow1.addWidget(self._enable_output_save_chkbox)


		self._test_save_output_type_lbl = QtGui.QLabel()
		self._test_save_output_type_lbl.setText("Output Type:")
		self._test_save_output_type_lbl.setFixedWidth(80)
		self._test_save_output_type_combo = QtGui.QComboBox()
		self._test_save_output_type_combo.addItems([".xml",".txt"])
		self._test_save_output_type_combo.setFixedWidth(80)
		QHRow2 = QtGui.QHBoxLayout()
		QHRow2.setAlignment(QtCore.Qt.AlignLeft)
		QHRow2.addWidget(self._test_save_output_type_lbl)
		QHRow2.addWidget(self._test_save_output_type_combo)

		self._save_output_dir_lbl = QtGui.QLabel()
		self._save_output_dir_lbl.setText("Saving Directory:")
		self._save_output_dir_lbl.setFixedWidth(110)
		self._save_output_dir_btn = QtGui.QPushButton("Browse",self)
		self._save_output_dir_btn.clicked.connect(self._open_browse_save_output_dir)
		self._save_output_dir_le = QtGui.QLineEdit()
		self._save_output_dir_le.setReadOnly(True)
		self._save_output_dir_le.setText("<< no directory selected >>")
		self._save_output_dir_lbl.setFixedHeight(13)
		QHRow3 = QHBoxLayout()
		QHRow3.setAlignment(QtCore.Qt.AlignLeft)
		QHRow4 = QHBoxLayout()
		QHRow3.addWidget(self._save_output_dir_lbl)
		QHRow4.addWidget(self._save_output_dir_btn)
		QHRow4.addWidget(self._save_output_dir_le)


		# draw a horizonal line
		hrr = QtGui.QFrame()
		hrr.setObjectName(QString.fromUtf8("line"))
		hrr.setGeometry(QRect(320,150,118,3))
		hrr.setFrameShape(QFrame.HLine)
		hrr.setFrameShadow(QFrame.Sunken)
		QHRow5 = QHBoxLayout()
		QHRow5.addWidget(hrr)

		# -- select OTHER test files (browse test files)
		self._other_test_lbl = QtGui.QLabel()
		self._other_test_lbl.setText("Additional Tests:")
		self._other_test_i_btn = QtGui.QPushButton("i", self)
		self._other_test_i_btn.setFixedSize(15,18)
		self._other_test_i_btn.clicked.connect(lambda c,m=ADDITIONAL_TEST_USAGE_MESSAGE, s=ADDITIONAL_TEST_I_SHORT_MSG, l=ADDITIONAL_TEST_I_LONG_MSG : self._show_msg_dialog(m,s,l))
		QHRow6 = QHBoxLayout()
		QHRow6.setAlignment(QtCore.Qt.AlignLeft)
		QHRow6.addWidget(self._other_test_lbl)
		QHRow6.addWidget(self._other_test_i_btn)


		self._other_test_browse_btn = QtGui.QPushButton("Browse",self)
		self._other_test_browse_btn.clicked.connect(self._open_browse_select_other_test)
		self._other_test_browse_le = QtGui.QLineEdit()
		self._other_test_browse_le.setReadOnly(True)
		self._other_test_browse_le.setText("<< no file selected >>")

		QHRow7 = QHBoxLayout()
		QHRow7.addWidget(self._other_test_browse_btn)
		QHRow7.addWidget(self._other_test_browse_le)



		self._execute_test_lbl = QtGui.QLabel()
		self._execute_test_lbl.setText("Run Test(s):")
		self._execute_test_lbl.setFixedWidth(80)
		self._execute_test_btn = QtGui.QPushButton("Run Now")
		self._execute_test_btn.clicked.connect(self._on_execute_test_btn_clicked)

		QHRow9 = QtGui.QHBoxLayout()
		QHRow9.addWidget(self._execute_test_lbl)
		QHRow9.addWidget(self._execute_test_btn)

		# draw a horizonal line
		hrrow = QtGui.QFrame()
		hrrow.setObjectName(QString.fromUtf8("line"))
		hrrow.setGeometry(QRect(320,150,118,3))
		hrrow.setFrameShape(QFrame.HLine)
		hrrow.setFrameShadow(QFrame.Sunken)
		QHRow8 = QHBoxLayout()
		QHRow8.addWidget(hrrow)


		OverallQVLayoutNearTestSuite.addLayout(QHRow1)
		OverallQVLayoutNearTestSuite.addLayout(QHRow3)
		OverallQVLayoutNearTestSuite.addLayout(QHRow4)
		OverallQVLayoutNearTestSuite.addLayout(QHRow2)
		OverallQVLayoutNearTestSuite.addLayout(QHRow5)
		OverallQVLayoutNearTestSuite.addLayout(QHRow6)
		OverallQVLayoutNearTestSuite.addLayout(QHRow7)
		OverallQVLayoutNearTestSuite.addLayout(QHRow8)
		OverallQVLayoutNearTestSuite.addLayout(QHRow9)

		# -- end create Hboxes to add to OverallQVLayoutNearTestSuite as a row

		scrollWidget2 = QWidget()
		scrollWidget2.setLayout(OverallQVLayoutNearTestSuite)
		scroll2.setWidget(scrollWidget2)
		self.TestSuiteOverallLayout2 = QtGui.QVBoxLayout()
		self.TestSuiteOverallLayout2.addWidget(scroll2)



		# -- Test Option/Setting ------------------------------------#

		settingVLayout = QVBoxLayout()

		self._module_lbl = QtGui.QLabel()
		self._module_lbl.setText("module:")
		self._module_lbl.setFixedWidth(80)
		self._module_le = QtGui.QLineEdit()
		self._module_le.setReadOnly(True)
		settingHLayout1 = QHBoxLayout()
		settingHLayout1.addWidget(self._module_lbl)
		settingHLayout1.addWidget(self._module_le)


		self._module_args_lbl = QtGui.QLabel()
		self._module_args_lbl.setText("module args:")
		self._module_args_lbl.setFixedWidth(80)
		self._module_args_le = QtGui.QLineEdit()
		self._module_args_le.setPlaceholderText("format: arg0,arg1")
		settingHLayout2 = QHBoxLayout()
		settingHLayout2.addWidget(self._module_args_lbl)
		settingHLayout2.addWidget(self._module_args_le)


		global Chipset_Code
		self._platform_lbl = QtGui.QLabel()
		self._platform_lbl.setText("platform:")
		self._platform_lbl.setFixedWidth(80)
		self._cb_platform = QComboBox()
		self._cb_platform.addItems([""] + Chipset_Code.keys())
		self._platform_le = QLineEdit()
		self._platform_le.setReadOnly(True)
		self._cb_platform.currentIndexChanged.connect(self.selectionchange)
		settingHLayout5 = QHBoxLayout()
		settingHLayout5.addWidget(self._platform_lbl)
		settingHLayout5.addWidget(self._cb_platform)
		settingHLayout5.addWidget(self._platform_le)


		self._verbose_mode_lbl = QtGui.QLabel()
		self._verbose_mode_lbl.setText("verbose mode:")
		self._verbose_mode_lbl.setFixedWidth(150)
		self._verbose_mode_chk = QtGui.QCheckBox()
		self._verbose_mode_info_lbl = QtGui.QLabel()
		self._verbose_mode_info_lbl.setText("(info)")
		self._verbose_mode_i = QtGui.QPushButton('i',self)
		self._verbose_mode_i.setFixedSize(15,18)
		self._verbose_mode_i.clicked.connect(lambda c,m="vebose mode",s=VERBOSE_MODE_SHORT_MSG,l=VERBOSE_MODE_LONG_MSG: self._show_msg_dialog(m,s,l))
		settingHLayout3 = QHBoxLayout()
		settingHLayout3.addWidget(self._verbose_mode_lbl)
		settingHLayout3.addWidget(self._verbose_mode_chk)
		settingHLayout3.addWidget(self._verbose_mode_info_lbl)
		settingHLayout3.addWidget(self._verbose_mode_i)


		self._debug_mode_lbl = QtGui.QLabel()
		self._debug_mode_lbl.setText("debug mode:")
		self._debug_mode_lbl.setFixedWidth(150)
		self._debug_mode_chk = QtGui.QCheckBox()
		self._debug_mode_info_lbl = QtGui.QLabel()
		self._debug_mode_info_lbl.setText("(info)")
		self._debug_mode_i = QtGui.QPushButton('i',self)
		self._debug_mode_i.setFixedSize(15,18)
		self._debug_mode_i.clicked.connect(lambda c,m="debug mode",s=DEBUG_MODE_SHORT_MSG,l=DEBUG_MODE_LONG_MSG: self._show_msg_dialog(m,s,l))
		settingHLayout4 = QHBoxLayout()
		settingHLayout4.addWidget(self._debug_mode_lbl)
		settingHLayout4.addWidget(self._debug_mode_chk)
		settingHLayout4.addWidget(self._debug_mode_info_lbl)
		settingHLayout4.addWidget(self._debug_mode_i)


		self._failfast_mode_lbl = QtGui.QLabel()
		self._failfast_mode_lbl.setText("failfast mode:")
		self._failfast_mode_lbl.setFixedWidth(150)
		self._failfast_mode_chk = QtGui.QCheckBox()
		self._failfast_mode_info_lbl = QtGui.QLabel()
		self._failfast_mode_info_lbl.setText("(info)")
		self._failfast_mode_i = QtGui.QPushButton('i',self)
		self._failfast_mode_i.setFixedSize(15,18)
		self._failfast_mode_i.clicked.connect(lambda c,m="failfast mode",s=FAILFAST_MODE_SHORT_MSG,l=FAILFAST_MODE_LONG_MSG: self._show_msg_dialog(m,s,l))
		settingHLayout6 = QHBoxLayout()
		settingHLayout6.addWidget(self._failfast_mode_lbl)
		settingHLayout6.addWidget(self._failfast_mode_chk)
		settingHLayout6.addWidget(self._failfast_mode_info_lbl)
		settingHLayout6.addWidget(self._failfast_mode_i)


		self._notime_mode_lbl = QtGui.QLabel()
		self._notime_mode_lbl.setText("no-time mode:")
		self._notime_mode_lbl.setFixedWidth(150)
		self._notime_mode_chk = QtGui.QCheckBox()
		self._notime_mode_info_lbl = QtGui.QLabel()
		self._notime_mode_info_lbl.setText("(info)")
		self._notime_mode_i = QtGui.QPushButton('i',self)
		self._notime_mode_i.setFixedSize(15,18)
		self._notime_mode_i.clicked.connect(lambda c,m="no-time mode",s=NOTIME_MODE_SHORT_MSG,l=NOTIME_MODE_LONG_MSG: self._show_msg_dialog(m,s,l))
		settingHLayout7 = QHBoxLayout()
		settingHLayout7.addWidget(self._notime_mode_lbl)
		settingHLayout7.addWidget(self._notime_mode_chk)
		settingHLayout7.addWidget(self._notime_mode_info_lbl)
		settingHLayout7.addWidget(self._notime_mode_i)


		self._ignore_platform_mode_lbl = QtGui.QLabel()
		self._ignore_platform_mode_lbl.setText("ignore-platform mode:")
		self._ignore_platform_mode_lbl.setFixedWidth(150)
		self._ignore_platform_mode_chk = QtGui.QCheckBox()
		self._ignore_platform_mode_info_lbl = QtGui.QLabel()
		self._ignore_platform_mode_info_lbl.setText("(info)")
		self._ignore_platform_mode_i = QtGui.QPushButton('i',self)
		self._ignore_platform_mode_i.setFixedSize(15,18)
		self._ignore_platform_mode_i.clicked.connect(lambda c,m="ignore-platform mode",s=IGNORE_PLATFORM_MODE_SHORT_MSG,l=IGNORE_PLATFORM_MODE_LONG_MSG: self._show_msg_dialog(m,s,l))
		settingHLayout8 = QHBoxLayout()
		settingHLayout8.addWidget(self._ignore_platform_mode_lbl)
		settingHLayout8.addWidget(self._ignore_platform_mode_chk)
		settingHLayout8.addWidget(self._ignore_platform_mode_info_lbl)
		settingHLayout8.addWidget(self._ignore_platform_mode_i)



		self._nodriver_mode_lbl = QtGui.QLabel()
		self._nodriver_mode_lbl.setText("no-driver mode:")
		self._nodriver_mode_lbl.setFixedWidth(150)
		self._nodriver_mode_chk = QtGui.QCheckBox()
		self._nodriver_mode_info_lbl = QtGui.QLabel()
		self._nodriver_mode_info_lbl.setText("(info)")
		self._nodriver_mode_i = QtGui.QPushButton('i',self)
		self._nodriver_mode_i.setFixedSize(15,18)
		self._nodriver_mode_i.clicked.connect(lambda c,m="no-driver mode",s=NODRIVER_MODE_SHORT_MSG,l=NODRIVER_MODE_LONG_MSG: self._show_msg_dialog(m,s,l))
		settingHLayout9 = QHBoxLayout()
		settingHLayout9.addWidget(self._nodriver_mode_lbl)
		settingHLayout9.addWidget(self._nodriver_mode_chk)
		settingHLayout9.addWidget(self._nodriver_mode_info_lbl)
		settingHLayout9.addWidget(self._nodriver_mode_i)



		settingVLayout.addLayout(settingHLayout1)
		settingVLayout.addLayout(settingHLayout2)
		settingVLayout.addLayout(settingHLayout5)
		settingVLayout.addLayout(settingHLayout3)
		settingVLayout.addLayout(settingHLayout4)
		settingVLayout.addLayout(settingHLayout6)
		settingVLayout.addLayout(settingHLayout7)
		settingVLayout.addLayout(settingHLayout8)
		settingVLayout.addLayout(settingHLayout9)
		# -- End Test Option/Setting --------------------------------#





		# -- setup main content -------------------------------------#
		self.v=QtGui.QHBoxLayout()
		self.v.addLayout(self.TestSuiteOverallLayout)
		self.v.addLayout(self.TestSuiteOverallLayout2)

		# -- setup group --------------------------------------------#
		self.group=QtGui.QGroupBox('Test Selection')
		self.groupOptions=QtGui.QGroupBox('Test Settings')
		self.groupOptions.setLayout(settingVLayout)
		self.group.setLayout(self.v)
		self.Vbox=QtGui.QVBoxLayout()
		HLayoutBelowSpacing = QHBoxLayout()
		HLayoutBelowSpacing.addWidget(self.group)
		HLayoutBelowSpacing.addWidget(self.groupOptions)
		self.Vbox.addLayout(self.hSpaceing)
		self.Vbox.addLayout(HLayoutBelowSpacing)
		self.setLayout(self.Vbox)


	# ---------------------------------------------------------------------------------#
	#							Uitls
	# ---------------------------------------------------------------------------------#


	def _show_error_dialog(self, message, descShort, descDetailed):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText(message)
		msg.setInformativeText(descShort)
		msg.setWindowTitle("Error")
		msg.setDetailedText(descDetailed)

		msg.setStandardButtons(QMessageBox.Ok)
		msg.buttonClicked.connect(msg.close)
		retval = msg.exec_()		

	def _show_msg_dialog(self, message, descShort, descDetailed):

		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)

		if descShort == ADDITIONAL_TEST_I_SHORT_MSG:
			msg.setText(message)
		else:
			msg.setText("This is {0} tool tip info box.".format(message))
		msg.setInformativeText(descShort)
		msg.setWindowTitle("Info")
		msg.setDetailedText(descDetailed)

		msg.setStandardButtons(QMessageBox.Ok) # | QMessageBox.Cancel
		msg.buttonClicked.connect(msg.close)
		retval = msg.exec_()

	def generate_chipsec_run_command(self):
		switch_dict = {}

		module_args_txt = self._module_args_le.text()
		module_args = ""
		if module_args_txt != "":
			module_args = module_args_txt
			switch_dict['-a'] = module_args

		platform_code = self._platform_le.text()
		if platform_code!="":
			switch_dict['-p'] = platform_code.split(":")[1]

		if self._verbose_mode_chk.isChecked():
			switch_dict['-v']=""

		if self._debug_mode_chk.isChecked():
			switch_dict['-d']=""

		if self._failfast_mode_chk.isChecked():
			switch_dict['--failfast'] = ""

		if self._notime_mode_chk.isChecked():
			switch_dict['--no_time'] = ""

		if self._ignore_platform_mode_chk.isChecked():
			switch_dict['-i']=""

		if self._nodriver_mode_chk.isChecked():
			switch_dict['-n']=""

		module_name = self._module_le.text()
		if module_name == "":
			self._show_error_dialog("Test(s) not Specified                   ","It is required to choose your desired test(s) first!","")
			return None
		elif module_name == "<< OTHER TEST >>":
			abspath = str(self._other_test_browse_le.text())
			slash_index = abspath.rindex('/')
			path = abspath[:slash_index]
			filename = abspath[slash_index+1:]
			switch_dict['-I'] = path
			switch_dict['-m']=filename
		elif module_name == "All Tests":
			# MUST DIS-ALLOW THIS CASE
			# if self._other_test_browse_le != "<< no file selected >>:"
			# 	# there are some additional tests to run
			# 	# just inculde the directory
			# 	# ATTENTION: all tests in the directory will be executed
			# 	abspath = self._other_test_browse_le.text()
			# 	slash_index = abspath.rindex('/')
			# 	path = abspath[:slash_index]
			# 	switch_dict['-I'] = path
			# no need to add -m switch in case of all tests
			module_name = "All Tests" # JUST TO PASS THE CASE WHICH IS DISALLOWED
		else:
			switch_dict['-m'] = module_name

		# -- handle save output---------------------------------------------------
		if self._enable_output_save_chkbox.isChecked():
			save_dir = self._save_output_dir_le.text()
			if save_dir == "<< no directory selected >>":
				console_message = "[Warning] No selected directory to save test summary.\n Using Default Directory {0} Instead.".format(REPORT_PATH)
				self.parent._writeOutputInSecondTerminal(console_message)
				save_dir = REPORT_PATH

			report_extention = str(self._test_save_output_type_combo.currentText())
			output_save_path = save_dir + "/" + str(uuid.uuid4()) + report_extention
			switch_dict['-x'] = output_save_path

		# --- create absoulute path for category table output
		abs_base_dir = BASE_PATH
		index = abs_base_dir.rindex('/')
		abs_path_chipsec = abs_base_dir[:index]


		# --- build the cmd from switch_dict---------------------------------------
		if self.parent.get_app_model() == "pyc":
			sudo_cmd_base = "sudo python ../gui_api.pyc"
			sudo_cmd_category = "sudo python {0}/gui_api.pyc".format(abs_path_chipsec)
		else:
			sudo_cmd_base = "sudo python ../gui_api.py"
			sudo_cmd_category = "sudo python {0}/gui_api.py".format(abs_path_chipsec)
		for key in switch_dict:
			if switch_dict[key]!="":
				tmp = " {0} {1}".format(key,switch_dict[key])
				sudo_cmd_base += tmp
				sudo_cmd_category += tmp
			else:
				temp = " {0}".format(key)
				sudo_cmd_base += temp
				sudo_cmd_category += temp


		return [sudo_cmd_base,sudo_cmd_category]


	# ---------------------------------------------------------------------------------#
	#							CAPTURE EVENTS
	# ---------------------------------------------------------------------------------#

	def _on_execute_test_btn_clicked(self):
		cmd = self.generate_chipsec_run_command()
		if cmd == None:
			return None

		cmd_tmux = cmd[0]
		cmd_cat = cmd[1]
		self._generate_categorize_output_main(cmd_cat)

		if self._first_run_done == False:
			self._first_run_done = True
			self.parent.console.runCommand(cmd_tmux, True)
		else:
			self.parent.console.runCommand(cmd_tmux, False)

		self.parent._writeOutputInSecondTerminal("\n++[Summary Generation In Progress] Please wait ...\n\n")
		

	def _open_browse_select_other_test(self):
		diag = QFileDialog()
		diag.setFileMode(QFileDialog.ExistingFile)
		diag.setFilter("Python files (*.py)")
		filenames = QStringList()
		if diag.exec_():
			filenames = diag.selectedFiles()
			file = filenames[0]
			self._other_test_browse_le.setText("{0}".format(file))
		else:
			self._other_test_browse_le.setText("<< no file selected >>")

	def _open_browse_save_output_dir(self):
		directory = QtGui.QFileDialog.getExistingDirectory(self, 'Select Save Location')
		if directory and directory != "":
			self._save_output_dir_le.setText(directory)
		else:
			self._save_output_dir_le.setText("<< no directory selected >>")

	def selectionchange(self, index):
		if index == 0:
			self._platform_le.setText("")
		else:		
			key = self._cb_platform.currentText() #Alternative: self._cb_platform.itemText(index)
			key = str(key)
			global Chipset_Code
			code_platform = Chipset_Code[key]
			text = "code: %s"%code_platform
			self._platform_le.setText(text)

	def _on_test_suite_item_state_changed(self, checked, rowWidget):
		itemName = rowWidget.labelText

		if itemName == "<< SELECT ALL >>":
			self._module_le.setText("All Tests")
		else:
			self._module_le.setText(itemName)


		for row in self._test_case_row_widgets:
			row.checkBox.blockSignals(True)

		if rowWidget.testName == "--ALL--":
			if checked > 0:
				self._desired_test_list = self._test_suite
				# check all others too

				self.OtherTestRowWidget.hide()
				for row in self._test_case_row_widgets:
					row.checkBox.setCheckState(Qt.Checked)

			else:
				# uncheck all others too
				self._desired_test_list = []
				self.OtherTestRowWidget.show()
				self._module_le.setText("")
				for row in self._test_case_row_widgets:
					row.checkBox.setCheckState(Qt.Unchecked)
		else:
			# new list with only one test, because chipsec api disallow multiple modules
			self._desired_test_list = [rowWidget.testName]
			if checked > 0:
				# if a new check box select, deselect others
				for row in self._test_case_row_widgets:
					if row != rowWidget and row.checkBox.isChecked():

						row.checkBox.setCheckState(Qt.Unchecked)
			else:
				# if this was only unchecked when all checked, deselect others 
				# and select just this element
				rowWidget.checkBox.setCheckState(Qt.Checked)
				for row in self._test_case_row_widgets:
					if row != rowWidget and row.checkBox.isChecked():
						row.checkBox.setCheckState(Qt.Unchecked)

		for row in self._test_case_row_widgets:
			row.checkBox.blockSignals(False)


	# ---------------------------------------------------------------------------------#
	#							CATEGORY OUTPUT
	# ---------------------------------------------------------------------------------#
	
	def _generate_categorize_output_main(self, command):
  		thread = PythonThread(command)
  		self.connect(thread, SIGNAL("finished()"), lambda th=thread : self._on_thread_task_finished(th))
  		thread.start()

  	def _on_thread_task_finished(self, thread):
  		self.test_summary_widget =  QtGui.QDialog(self)
  		self.test_summary_widget.setMinimumWidth(1000)
  		self.test_summary_widget.setMinimumHeight(600)


		table = categoryTable(thread.outputData)

  		QH = QHBoxLayout()
  		QH.addWidget(table)
  		self.test_summary_widget.setLayout(QH)


  		# -- top bar panel
		iconExit = QtGui.QIcon('icons/exit.png')
		exitAction = QtGui.QAction(iconExit, '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.test_summary_widget.close)

		iconSave = QtGui.QIcon('icons/borrow.jpg')
		saveAction = QtGui.QAction(iconSave, '&Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save Output')
		saveAction.triggered.connect(lambda celf, tb=table, wi=self.test_summary_widget: self._on_save_test_category_output(tb,wi))

		iconScreen = QtGui.QIcon('icons/borrow.jpg')
		shotAction = QtGui.QAction(iconScreen, '&ScreenShot', self)
		shotAction.setShortcut('Ctrl+P')
		shotAction.setStatusTip('Take ScreenShot')
		shotAction.triggered.connect(lambda celf, tb=table, wi=self.test_summary_widget: self._on_capture_screenshot(tb,wi))

		menubar = QtGui.QMenuBar(self)
		menubar.setGeometry(QtCore.QRect(0, 0, 2000, 23))
		menufile = menubar.addMenu('File')

		menufile.addAction(saveAction)
		menufile.addAction(shotAction)
		menufile.addAction(exitAction)
		self.test_summary_widget.layout().setMenuBar(menubar)
  		# -- end top bar panel

  		self.test_summary_widget.exec_() #or self.test_summary_widget.show()
  		

	def _on_save_test_category_output(self, categoryTable, mainWidget):
		filename = unicode(QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)"))    
		wbk = xlwt.Workbook()
		sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)

		for currentColumn in range(categoryTable.cols):
		    for currentRow in range(categoryTable.rows):
		        try:
					teext = str(categoryTable.item(currentRow, currentColumn).text())
					teext.strip()
					if teext == "YELLOW":
						style = xlwt.XFStyle()
						pattern = xlwt.Pattern()
						pattern.pattern = xlwt.Pattern.SOLID_PATTERN
						pattern.pattern_fore_colour = xlwt.Style.colour_map['light_yellow']
						style.pattern = pattern
						sheet.write(currentRow, currentColumn, teext, style)
					elif teext == "RED":
						style = xlwt.XFStyle()
						pattern = xlwt.Pattern()
						pattern.pattern = xlwt.Pattern.SOLID_PATTERN
						pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
						style.pattern = pattern
						sheet.write(currentRow, currentColumn, teext, style)
					elif teext == "GREEN":
						style = xlwt.XFStyle()
						pattern = xlwt.Pattern()
						pattern.pattern = xlwt.Pattern.SOLID_PATTERN
						pattern.pattern_fore_colour = xlwt.Style.colour_map['green']
						style.pattern = pattern
						sheet.write(currentRow, currentColumn, teext, style)
					elif teext == "ORANGE":
						style = xlwt.XFStyle()
						pattern = xlwt.Pattern()
						pattern.pattern = xlwt.Pattern.SOLID_PATTERN
						pattern.pattern_fore_colour = xlwt.Style.colour_map['orange']
						style.pattern = pattern
						sheet.write(currentRow, currentColumn, teext, style)
					elif teext == "ORANGE_LIGHT":
						style = xlwt.XFStyle()
						pattern = xlwt.Pattern()
						pattern.pattern = xlwt.Pattern.SOLID_PATTERN
						pattern.pattern_fore_colour = xlwt.Style.colour_map['gold']
						style.pattern = pattern
						sheet.write(currentRow, currentColumn, teext, style)
					else:
						sheet.write(currentRow, currentColumn, teext)			        	
		        except AttributeError:
		            pass
		wbk.save(filename+".xls")

	def _on_capture_screenshot(self, table, pWdidget):
	    path = QtGui.QFileDialog.getSaveFileName(
	            self, 'Save File', '', 'JPG(*.jpg)')
	    if not path.isEmpty():
	    	width = pWdidget.width()
	    	height = pWdidget.height()
	    	pWdidget.showMaximized()
	    	time.sleep(1)
	    	p = QtGui.QPixmap.grabWindow(table.winId())
	    	p.save(path, 'jpg')
	    	pWdidget.resize(width, height)


		


    
