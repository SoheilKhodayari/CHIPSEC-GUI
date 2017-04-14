
import os 


BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# -- ROOT_PASSWORD
ROOT_PASSWORD = "9759865"

# -- RELATIVE_REPORT_PATH
RELATIVE_REPORTS_FOLDER = "/reports"
REPORT_PATH = BASE_PATH + RELATIVE_REPORTS_FOLDER



# ----------------------------------------------------------------------------- #
#						APP MSG, ERRORS, ETC
# ----------------------------------------------------------------------------- #

# When user requests the test summary window from the top bar and the window
# is not yet available (no test has runned)
SHOW_TEST_SUMMARY_REQUEST_ERROR_TITLE = "Unauthorized Action"
SHOW_TEST_SUMMARY_REQUEST_ERROR_LMSG = "No Test Summary Exists Yet!"
# ----------------------------------------------------------------------------- #
#						Test Names And Explanations
# ----------------------------------------------------------------------------- #


# @Note: tests are fetched automatically from the modules/common directory.
# to use below dictionary instead, pass true to _fetch_test_suite_list() function.
# below dictionary is not used by default
AVAILABLE_TESTS = ['bios_kbrd_buffer','bios_smi','bios_ts',
'bios_wp','ia32cfg','rtclock','smm','smrr','spi_desc','spi_fdopss','spi_lock']

TEST_TOOL_TIPS = {'bios_kbrd_buffer': 'msg1',
				'bios_smi': 'msg2',
				'bios_ts': 'msg3',
				'bios_wp': 'msg4',
				'ia32cfg': 'msg5',
				'rtclock': 'msg6',
				'smm': 'msg7',
				'smrr': 'msg8',
				'spi_desc': 'msg9',
				'spi_fdopss': 'msg10',
				'spi_lock':'msg11'}


DETAILED_TEST_TOOL_TIPS = {'bios_kbrd_buffer': 'msg1',
				'bios_smi': 'msg2',
				'bios_ts': 'msg3',
				'bios_wp': 'msg4',
				'ia32cfg': 'msg5',
				'rtclock': 'msg6',
				'smm': 'msg7',
				'smrr': 'msg8',
				'spi_desc': 'msg9',
				'spi_fdopss': 'msg10',
				'spi_lock':'msg11'}


ADDITIONAL_TEST_USAGE_MESSAGE = "You can select and run your own tests."
ADDITIONAL_TEST_I_SHORT_MSG = "This test will NOT be executed when selecting ALL other pre-defined tests."
ADDITIONAL_TEST_I_LONG_MSG = "Test Format is Intel's Chipsec Format, see github.com/chipsec/chipsec for more!"



# ----------------------------------------------------------------------------- #
#						Test RUN Mode Messages
# ----------------------------------------------------------------------------- #


VERBOSE_MODE_SHORT_MSG = "This will activate verbose mode."
VERBOSE_MODE_LONG_MSG = "Equivalant to -v --verbose commandline!"

DEBUG_MODE_SHORT_MSG = "show debug output"
DEBUG_MODE_LONG_MSG = "Equivalant to -d --debug commandline!"

FAILFAST_MODE_SHORT_MSG = "fail on any exception and exit (don't mask exceptions)"
FAILFAST_MODE_LONG_MSG = "Equivalant to -d --debug commandline!"

NOTIME_MODE_SHORT_MSG = "don't log timestamps"
NOTIME_MODE_LONG_MSG = "Equivalant to --no_time commandline!"

IGNORE_PLATFORM_MODE_SHORT_MSG = "run chipsec even if the platform is not recognized"
IGNORE_PLATFORM_MODE_LONG_MSG = "Equivalant to -i --ignore_platform commandline!"

NODRIVER_MODE_SHORT_MSG = "chipsec won't need kernel mode functions so don't load chipsec driver"
NODRIVER_MODE_LONG_MSG = "Equivalant to -n --no_driver commandline!"


# ----------------------------------------------------------------------------- #
#						END Test RUN Mode Messages
# ----------------------------------------------------------------------------- #



# ------------------------------------------------------------------------------------------------- #
#						Test Category Messages
# ------------------------------------------------------------------------------------------------- #


# @Warning:  Test Color Labels are pre-defined and their absolute text MUST NOT 
#            be changed because the appropriate color is determined from the text.
#            one can only use the following values:
#			 1- RED          => Criticality HIGH 
#			 2- ORANGE       => Criticality NORMAL 
#			 3- ORANGE_LIGHT => Criticality LOW
#			 4- YELLOW       => Criticality LOW
#			 5- GREEN        => Not Critical

# ----------------------------------------------------------------------------- #
#						SPI Flash Controller Configuration Lock
# ----------------------------------------------------------------------------- #

FLOCKDN_COLOR_CODE = "RED"
FLOCKDN_CRITICALITY = "HIGH"
FLOCKDN_EXPECTED_RESULT = "1"
FLOCKDN_DESCRIPTION = "FLOCKDN description goes here\ndescription goes here" # use \n for newlines!
FLOCKDN_REPR = "FLOCKDN"
FLOCKDN_TEST_NAME = "SPI Flash Controller\nConfiguration Lock"

# ----------------------------------------------------------------------------- #
#					End SPI Flash Controller Configuration Lock
# ----------------------------------------------------------------------------- #



# ----------------------------------------------------------------------------- #
#						SMI Events Configuration Options
# ----------------------------------------------------------------------------- #


SMM_BWP_2_COLOR_CODE = "ORANGE"
SMM_BWP_2_CRITICALITY = "NORMAL"
SMM_BWP_2_EXPECTED_RESULT = "1"
SMM_BWP_2_DESCRIPTION = "SMM_BWP description goes here\ndescription goes here" # use \n for newlines!
SMM_BWP_2_REPR = "SMM_BWP"
SMM_BWP_2_TEST_NAME = "SMI Events Configuration"


SMM_BWP_2_COLOR_CODE = "ORANGE"
SMM_BWP_2_CRITICALITY = "NORMAL"
SMM_BWP_2_EXPECTED_RESULT = "1"
SMM_BWP_2_DESCRIPTION = "SMM_BWP description goes here\ndescription goes here" # use \n for newlines!
SMM_BWP_2_REPR = "SMM_BWP"
SMM_BWP_2_TEST_NAME = "SMI Events Configuration"


TCO_SMI_LOCK_COLOR_CODE = "RED"
TCO_SMI_LOCK_CRITICALITY = "HIGH"
TCO_SMI_LOCK_EXPECTED_RESULT = "1"
TCO_SMI_LOCK_DESCRIPTION = "TCO SMI configuration must\nbe locked (TCO SMI Lock)\ndescription goes here\ndescription goes here" # use \n for newlines!
TCO_SMI_LOCK_REPR = "TCO SMI configuration (TCO SMI Lock)"
TCO_SMI_LOCK_TEST_NAME = "SMI Events Configuration"

SMI_LOCK_COLOR_CODE = "RED"
SMI_LOCK_CRITICALITY = "HIGH"
SMI_LOCK_EXPECTED_RESULT = "1"
SMI_LOCK_DESCRIPTION = "SMI events global configuration\nmust be locked (SMI Lock)\ndescription goes here\ndescription goes here" # use \n for newlines!
SMI_LOCK_REPR = "SMI events global configuration (SMI Lock)"
SMI_LOCK_TEST_NAME = "SMI Events Configuration"


Global_SMI_EN_COLOR_CODE = "GREEN"
Global_SMI_EN_CRITICALITY = "Not Critical"
Global_SMI_EN_EXPECTED_RESULT = "1"
Global_SMI_EN_DESCRIPTION = "Global SMI Enable description goes here\ndescription goes here" # use \n for newlines!
Global_SMI_EN_REPR = "Global SMI Enable"
Global_SMI_EN_TEST_NAME = "SMI Events Configuration"


TCO_SMI_EN_COLOR_CODE = "GREEN"
TCO_SMI_EN_CRITICALITY = "Not Critical"
TCO_SMI_EN_EXPECTED_RESULT = "1"
TCO_SMI_EN_DESCRIPTION = "TCO SMI Enable (TCO1_CNT) description goes here\ndescription goes here" # use \n for newlines!
TCO_SMI_EN_REPR = "TCO SMI Enable (TCO1_CNT)"
TCO_SMI_EN_TEST_NAME = "SMI Events Configuration"



# ----------------------------------------------------------------------------- #
#					End	SMI Events Configuration Options
# ----------------------------------------------------------------------------- #



# ----------------------------------------------------------------------------- #
#						BIOS Keyboard Buffer
# ----------------------------------------------------------------------------- #


BIOS_KEYBOARD_BUFF_COLOR_CODE = "ORANGE_LIGHT"
BIOS_KEYBOARD_BUFF_CRITICALITY = "LOW"
BIOS_KEYBOARD_BUFF_EXPECTED_RESULT = "Empty/Zero"
BIOS_KEYBOARD_BUFF_DESCRIPTION = "BIOS Keyboard Buffer\ndescription goes here\ndescription goes here" # use \n for newlines!
BIOS_KEYBOARD_BUFF_REPR = "BIOS Keyboard Buffer"
BIOS_KEYBOARD_BUFF_TEST_NAME = "Pre-boot Passwords in\nthe BIOS Keyboard Buffer"



# ----------------------------------------------------------------------------- #
#						End BIOS Keyboard Buffer
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#					   BIOS Region Write Protection
# ----------------------------------------------------------------------------- #


BIOSWE_COLOR_CODE = "ORANGE_LIGHT"
BIOSWE_CRITICALITY = "LOW"
BIOSWE_EXPECTED_RESULT = "0"
BIOSWE_DESCRIPTION = "BIOSWE description goes here\ndescription goes here" # use \n for newlines!
BIOSWE_REPR = "BIOSWE"
BIOSWE_TEST_NAME = "BIOS Region Write Protection"

BLE_COLOR_CODE = "RED"
BLE_CRITICALITY = "HIGH"
BLE_EXPECTED_RESULT = "1"
BLE_DESCRIPTION = "BLE description goes here\ndescription goes here" # use \n for newlines!
BLE_REPR = "BLE"
BLE_TEST_NAME = "BIOS Region Write Protection"

SRC_COLOR_CODE = "GREEN"
SRC_CRITICALITY = "Not Critical"
SRC_EXPECTED_RESULT = "-"
SRC_DESCRIPTION = "SRC description goes here\ndescription goes here" # use \n for newlines!
SRC_REPR = "SRC"
SRC_TEST_NAME = "BIOS Region Write Protection"

TSS_COLOR_CODE = "ORANGE_LIGHT"
TSS_CRITICALITY = "LOW"
TSS_EXPECTED_RESULT = "0"
TSS_DESCRIPTION = "TSS description goes here\ndescription goes here" # use \n for newlines!
TSS_REPR = "TSS"
TSS_TEST_NAME = "BIOS Region Write Protection"


SMM_BWP_COLOR_CODE = "ORANGE"
SMM_BWP_CRITICALITY = "NORMAL"
SMM_BWP_EXPECTED_RESULT = "1"
SMM_BWP_DESCRIPTION = "SMM_BWP description goes here\ndescription goes here" # use \n for newlines!
SMM_BWP_REPR = "SMM_BWP"
SMM_BWP_TEST_NAME = "BIOS Region Write Protection"



# ----------------------------------------------------------------------------- #
#						End BIOS Region Write Protection
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#				 Compatible SMM memory (SMRAM) Protection
# ----------------------------------------------------------------------------- #

D_LCK_COLOR_CODE = "ORANGE"
D_LCK_CRITICALITY = "NORMAL"
D_LCK_EXPECTED_RESULT = "1"
D_LCK_DESCRIPTION = "D_LCK_ description goes here\ndescription goes here" # use \n for newlines!
D_LCK_REPR = "D_LCK_"
D_LCK_TEST_NAME = "Compatible SMM memory\n(SMRAM) Protection"


# ----------------------------------------------------------------------------- #
#				End Compatible SMM memory (SMRAM) Protection
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#				 Protected RTC Memory Locations
# ----------------------------------------------------------------------------- #

UE_COLOR_CODE = "YELLOW"
UE_CRITICALITY = "LOW"
UE_EXPECTED_RESULT = "1"
UE_DESCRIPTION = "UE description goes here\ndescription goes here" # use \n for newlines!
UE_REPR = "UE"
UE_TEST_NAME = "Protected RTC\nMemory Locations"

LL_COLOR_CODE = "YELLOW"
LL_CRITICALITY = "LOW"
LL_EXPECTED_RESULT = "1"
LL_DESCRIPTION = "LL description goes here\ndescription goes here" # use \n for newlines!
LL_REPR = "LL"
LL_TEST_NAME = "Protected RTC\nMemory Locations"

UL_COLOR_CODE = "YELLOW"
UL_CRITICALITY = "LOW"
UL_EXPECTED_RESULT = "1"
UL_DESCRIPTION = "UL description goes here\ndescription goes here" # use \n for newlines!
UL_REPR = "UL"
UL_TEST_NAME = "Protected RTC\nMemory Locations"


# ----------------------------------------------------------------------------- #
#				 End Protected RTC Memory Locations
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- #
#				IA32 Feature Control Lock
# ----------------------------------------------------------------------------- #

IA32_Lock_COLOR_CODE = "ORANGE_LIGHT"
IA32_Lock_CRITICALITY = "NORMAL"
IA32_Lock_EXPECTED_RESULT = "1"
IA32_Lock_DESCRIPTION = "Lock description goes here\ndescription goes here" # use \n for newlines!
IA32_Lock_REPR = "Lock"
IA32_Lock_TEST_NAME = "IA32 Feature\nControl Lock"



# ----------------------------------------------------------------------------- #
#				End IA32 Feature Control Lock
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#				SPI Flash Region Access Control
# ----------------------------------------------------------------------------- #


BBRA_BBWA_COLOR_CODE = "ORANGE_LIGHT"
BBRA_BBWA_CRITICALITY = "NORMAL"
BBRA_BBWA_EXPECTED_RESULT = "Passed"
BBRA_BBWA_DESCRIPTION = "BBRA and BBWA \ndescription goes here\ndescription goes here" # use \n for newlines!
BBRA_BBWA_REPR = "BBRA and BBWA"
BBRA_BBWA_TEST_NAME = "SPI Flash Region\nAccess Control"



# ----------------------------------------------------------------------------- #
#				End SPI Flash Region Access Control
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#				SPI Flash Descriptor Security Override Pin-Strap
# ----------------------------------------------------------------------------- #

FDOPSS_COLOR_CODE = "RED"
FDOPSS_CRITICALITY = "HIGH"
FDOPSS_EXPECTED_RESULT = "1"
FDOPSS_DESCRIPTION = "FDOPSS \ndescription goes here\ndescription goes here" # use \n for newlines!
FDOPSS_REPR = "FDOPSS"
FDOPSS_TEST_NAME = "SPI Flash Descriptor \nSecurity Override Pin-Strap"


# ----------------------------------------------------------------------------- #
#				End SPI Flash Descriptor Security Override Pin-Strap
# ----------------------------------------------------------------------------- #
