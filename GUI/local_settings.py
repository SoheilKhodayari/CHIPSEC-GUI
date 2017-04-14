
import os 



# ----------------------------------------------------------------------------- #
#						OS ROOT PASSWORD
# ----------------------------------------------------------------------------- #

# -- ROOT_PASSWORD
ROOT_PASSWORD = "9759865"


# ----------------------------------------------------------------------------- #
#						APP SETTING
# ----------------------------------------------------------------------------- #

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# -- RELATIVE_REPORT_PATH
RELATIVE_REPORTS_FOLDER = "/reports"
REPORT_PATH = BASE_PATH + RELATIVE_REPORTS_FOLDER

# -- MODULES PATH HELPER
CHIPSEC_PATH = BASE_PATH[:BASE_PATH.rindex('/GUI')]
OTHER_MODULES_DIR = CHIPSEC_PATH + "/chipsec/modules"
COMMON_DIR = CHIPSEC_PATH + "/chipsec/modules/common"
SECURE_BOOT_DIR = COMMON_DIR + "/secureboot"
UEFI_DIR = COMMON_DIR + "/uefi"

QRY_MODULE_PATH = {
	"memconfig":OTHER_MODULES_DIR,
	"remap": OTHER_MODULES_DIR,
	"smm_dma": OTHER_MODULES_DIR,
	"variables": SECURE_BOOT_DIR,
	"access_uefispec":UEFI_DIR,
	"s3bootscript": UEFI_DIR,
	"bios_kbrd_buffer":COMMON_DIR,
	"bios_smi":COMMON_DIR,
	"bios_ts":COMMON_DIR,
	"bios_wp":COMMON_DIR,
	"ia32cfg":COMMON_DIR,
	"rtclock":COMMON_DIR,
	"smm":COMMON_DIR,
	"smrr":COMMON_DIR,
	"spi_desc":COMMON_DIR,
	"spi_fdopss":COMMON_DIR,
	"spi_lock":COMMON_DIR
}

TEST_DIRECTIORY_LIST = [COMMON_DIR,SECURE_BOOT_DIR,UEFI_DIR,OTHER_MODULES_DIR]
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


# @Note: tests are fetched automatically from the dirs in TEST_DIRECTIORY_LIST
# to use below lisr instead, pass true to _fetch_test_suite_list() function.
# below list is not used by default
AVAILABLE_TESTS = QRY_MODULE_PATH.keys()

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
D_LCK_REPR = "D_LCK"
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

IA32_Lock_COLOR_CODE = "ORANGE"
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


BBRA_BBWA_COLOR_CODE = "ORANGE"
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

# ----------------------------------------------------------------------------- #
#				BIOS Interface Lock including Top Swap Mode
# ----------------------------------------------------------------------------- #


BILD_COLOR_CODE = "RED"
BILD_CRITICALITY = "HIGH"
BILD_EXPECTED_RESULT = "1"
BILD_DESCRIPTION = "BILD \ndescription goes here\ndescription goes here" # use \n for newlines!
BILD_REPR = "BILD"
BILD_TEST_NAME = "BIOS Interface Lock \nincluding Top Swap Mode"

TSS_2_COLOR_CODE = "YELLOW"
TSS_2_CRITICALITY = "LOW"
TSS_2_EXPECTED_RESULT = "0"
TSS_2_DESCRIPTION = "TSS \ndescription goes here\ndescription goes here" # use \n for newlines!
TSS_2_REPR = "TSS"
TSS_2_TEST_NAME = "BIOS Interface Lock \nincluding Top Swap Mode"



# ----------------------------------------------------------------------------- #
#				End BIOS Interface Lock including Top Swap Mode
# ----------------------------------------------------------------------------- #



# ----------------------------------------------------------------------------- #
#							CPU SMM Cache Poisoning
# ----------------------------------------------------------------------------- #


SMRR_range_base_COLOR_CODE = "ORANGE"
SMRR_range_base_CRITICALITY = "NORMAL"
SMRR_range_base_EXPECTED_RESULT = "Passed"
SMRR_range_base_DESCRIPTION = "SMRR_range_base_programming\ndescription goes here\ndescription goes here" # use \n for newlines!
SMRR_range_base_REPR = "SMRR_range_base_programming"
SMRR_range_base_TEST_NAME = "CPU SMM Cache Poisoning"


SMRR_range_mask_COLOR_CODE = "ORANGE"
SMRR_range_mask_CRITICALITY = "NORMAL"
SMRR_range_mask_EXPECTED_RESULT = "Passed"
SMRR_range_mask_DESCRIPTION = "SMRR_range_mask_programming\ndescription goes here\ndescription goes here" # use \n for newlines!
SMRR_range_mask_REPR = "SMRR_range_mask_programming"
SMRR_range_mask_TEST_NAME = "CPU SMM Cache Poisoning"


SMRR_range_base_and_mask_are_same_COLOR_CODE = "ORANGE"
SMRR_range_base_and_mask_are_same_CRITICALITY = "NORMAL"
SMRR_range_base_and_mask_are_same_EXPECTED_RESULT = "Passed"
SMRR_range_base_and_mask_are_same_DESCRIPTION = "Verifying SMRR\nrange base\nand mask are\nsame on all\nlogical_cpus description" # use \n for newlines!
SMRR_range_base_and_mask_are_same_REPR = "Same SMRR range\nBase and Mask\non all logical cpus"
SMRR_range_base_and_mask_are_same_TEST_NAME = "CPU SMM Cache Poisoning"


IA32_SMRR_PHYSBASE_COLOR_CODE = "RED"
IA32_SMRR_PHYSBASE_CRITICALITY = "HIGH"
IA32_SMRR_PHYSBASE_EXPECTED_RESULT = "Permissible Values"
IA32_SMRR_PHYSBASE_DESCRIPTION = "IA32_SMRR_PHYSBASE \ndescription goes here\ndescription goes here" # use \n for newlines!
IA32_SMRR_PHYSBASE_REPR = "IA32_SMRR_PHYSBASE"
IA32_SMRR_PHYSBASE_TEST_NAME = "CPU SMM Cache Poisoning"

SMMR_PROTECTION_AGAINST_CACHE_ATTACK_COLOR_CODE = "ORANGE"
SMMR_PROTECTION_AGAINST_CACHE_ATTACK_CRITICALITY = "NORMAL"
SMMR_PROTECTION_AGAINST_CACHE_ATTACK_EXPECTED_RESULT = "Passed"
SMMR_PROTECTION_AGAINST_CACHE_ATTACK_DESCRIPTION = "SMRR Protection Against\nCache Attack\ndescription goes here" # use \n for newlines!
SMMR_PROTECTION_AGAINST_CACHE_ATTACK_REPR = "SMRR Protection Against\nCache Attack"
SMMR_PROTECTION_AGAINST_CACHE_ATTACK_TEST_NAME = "CPU SMM Cache Poisoning"

# ----------------------------------------------------------------------------- #
#						  End CPU SMM Cache Poisoning
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#					   Memory Remap Configuration
# ----------------------------------------------------------------------------- #


RemapWindowConfig_COLOR_CODE = "GREEN"
RemapWindowConfig_CRITICALITY = "Not Critical"
RemapWindowConfig_EXPECTED_RESULT = "Passed"
RemapWindowConfig_DESCRIPTION = "Remap Window Configuration\ndescription goes here\ndescription goes here" # use \n for newlines!
RemapWindowConfig_REPR = "Remap Window Configuration"
RemapWindowConfig_TEST_NAME = "Memory Remap Configuration"

TOUUD_COLOR_CODE = "ORANGE"
TOUUD_CRITICALITY = "NORMAL"
TOUUD_EXPECTED_RESULT = "Permissible Values"
TOUUD_DESCRIPTION = "TOUUD \ndescription goes here\ndescription goes here" # use \n for newlines!
TOUUD_REPR = "TOUUD"
TOUUD_TEST_NAME = "Memory Remap Configuration"

TOLUD_COLOR_CODE = "ORANGE"
TOLUD_CRITICALITY = "NORMAL"
TOLUD_EXPECTED_RESULT = "Permissible Values"
TOLUD_DESCRIPTION = "TOLUD \ndescription goes here\ndescription goes here" # use \n for newlines!
TOLUD_REPR = "TOLUD"
TOLUD_TEST_NAME = "Memory Remap Configuration"



# ----------------------------------------------------------------------------- #
#					  End Memory Remap Configuration
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#				 Host Bridge Memory Map Locks
# ----------------------------------------------------------------------------- #


BDSM_COLOR_CODE = "YELLOW"
BDSM_CRITICALITY = "LOW"
BDSM_EXPECTED_RESULT = "LOCKED"
BDSM_DESCRIPTION = "BDSM \ndescription goes here\ndescription goes here" # use \n for newlines!
BDSM_REPR = "BDSM"
BDSM_TEST_NAME = "Host Bridge Memory\nMap Locks"


BGSM_COLOR_CODE = "YELLOW"
BGSM_CRITICALITY = "LOW"
BGSM_EXPECTED_RESULT = "LOCKED"
BGSM_DESCRIPTION = "BGSM \ndescription goes here\ndescription goes here" # use \n for newlines!
BGSM_REPR = "BGSM"
BGSM_TEST_NAME = "Host Bridge Memory\nMap Locks"


DPR_COLOR_CODE = "ORANGE"
DPR_CRITICALITY = "NORMAL"
DPR_EXPECTED_RESULT = "LOCKED"
DPR_DESCRIPTION = "DPR \ndescription goes here\ndescription goes here" # use \n for newlines!
DPR_REPR = "DPR"
DPR_TEST_NAME = "Host Bridge Memory\nMap Locks"

GGC_COLOR_CODE = "GREEN"
GGC_CRITICALITY = "Not Critical"
GGC_EXPECTED_RESULT = "LOCKED"
GGC_DESCRIPTION = "GGC \ndescription goes here\ndescription goes here" # use \n for newlines!
GGC_REPR = "GGC"
GGC_TEST_NAME = "Host Bridge Memory\nMap Locks"

MESEG_MASK_COLOR_CODE = "RED"
MESEG_MASK_CRITICALITY = "HIGH"
MESEG_MASK_EXPECTED_RESULT = "LOCKED"
MESEG_MASK_DESCRIPTION = "MESEG_MASK \ndescription goes here\ndescription goes here" # use \n for newlines!
MESEG_MASK_REPR = "MESEG_MASK"
MESEG_MASK_TEST_NAME = "Host Bridge Memory\nMap Locks"

PAVPC_COLOR_CODE = "YELLOW"
PAVPC_CRITICALITY = "LOW"
PAVPC_EXPECTED_RESULT = "LOCKED"
PAVPC_DESCRIPTION = "PAVPC \ndescription goes here\ndescription goes here" # use \n for newlines!
PAVPC_REPR = "PAVPC"
PAVPC_TEST_NAME = "Host Bridge Memory\nMap Locks"

REMAPBASE_COLOR_CODE = "ORANGE"
REMAPBASE_CRITICALITY = "NORMAL"
REMAPBASE_EXPECTED_RESULT = "LOCKED"
REMAPBASE_DESCRIPTION = "REMAPBASE \ndescription goes here\ndescription goes here" # use \n for newlines!
REMAPBASE_REPR = "REMAPBASE"
REMAPBASE_TEST_NAME = "Host Bridge Memory\nMap Locks"

REMAPLIMIT_COLOR_CODE = "ORANGE"
REMAPLIMIT_CRITICALITY = "NORMAL"
REMAPLIMIT_EXPECTED_RESULT = "LOCKED"
REMAPLIMIT_DESCRIPTION = "REMAPLIMIT \ndescription goes here\ndescription goes here" # use \n for newlines!
REMAPLIMIT_REPR = "REMAPLIMIT"
REMAPLIMIT_TEST_NAME = "Host Bridge Memory\nMap Locks"

TOLUD_2_COLOR_CODE = "ORANGE"
TOLUD_2_CRITICALITY = "NORMAL"
TOLUD_2_EXPECTED_RESULT = "LOCKED"
TOLUD_2_DESCRIPTION = "TOLUD \ndescription goes here\ndescription goes here" # use \n for newlines!
TOLUD_2_REPR = "TOLUD"
TOLUD_2_TEST_NAME = "Host Bridge Memory\nMap Locks"


TOM_COLOR_CODE = "ORANGE"
TOM_CRITICALITY = "NORMAL"
TOM_EXPECTED_RESULT = "LOCKED"
TOM_DESCRIPTION = "TOM \ndescription goes here\ndescription goes here" # use \n for newlines!
TOM_REPR = "TOM"
TOM_TEST_NAME = "Host Bridge Memory\nMap Locks"


TOUUD_2_COLOR_CODE = "ORANGE"
TOUUD_2_CRITICALITY = "NORMAL"
TOUUD_2_EXPECTED_RESULT = "LOCKED"
TOUUD_2_DESCRIPTION = "TOUUD \ndescription goes here\ndescription goes here" # use \n for newlines!
TOUUD_2_REPR = "TOUUD"
TOUUD_2_TEST_NAME = "Host Bridge Memory\nMap Locks"

TSEGMB_COLOR_CODE = "ORANGE"
TSEGMB_CRITICALITY = "NORMAL"
TSEGMB_EXPECTED_RESULT = "LOCKED"
TSEGMB_DESCRIPTION = "TSEGMB \ndescription goes here\ndescription goes here" # use \n for newlines!
TSEGMB_REPR = "TSEGMB"
TSEGMB_TEST_NAME = "Host Bridge Memory\nMap Locks"


# ----------------------------------------------------------------------------- #
#				 End Host Bridge Memory Map Locks
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#				 SMM TSEG Range Configuration Check
# ----------------------------------------------------------------------------- #

TSEG_1_COLOR_CODE = "ORANGE"
TSEG_1_CRITICALITY = "NORMAL"
TSEG_1_EXPECTED_RESULT = "-"
TSEG_1_DESCRIPTION = "TSEG \ndescription goes here\ndescription goes here" # use \n for newlines!
TSEG_1_REPR = "TSEG"
TSEG_1_TEST_NAME = "SMM TSEG Range\nConfiguration Check"


SMRR_Range_COLOR_CODE = "ORANGE"
SMRR_Range_CRITICALITY = "NORMAL"
SMRR_Range_EXPECTED_RESULT = "-"
SMRR_Range_DESCRIPTION = "SMRR_Range \ndescription goes here\ndescription goes here" # use \n for newlines!
SMRR_Range_REPR = "SMRR_Range"
SMRR_Range_TEST_NAME = "SMM TSEG Range\nConfiguration Check"



# ----------------------------------------------------------------------------- #
#				 End SMM TSEG Range Configuration Check
# ----------------------------------------------------------------------------- #