
import os 


BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# -- ROOT_PASSWORD
ROOT_PASSWORD = "9759865"

# -- RELATIVE_REPORT_PATH
RELATIVE_REPORTS_FOLDER = "/reports"
REPORT_PATH = BASE_PATH + RELATIVE_REPORTS_FOLDER


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








