# -*- coding: utf-8 -*-

import os 


MAIN_WINDOW_APP_TITLE = u'Platform Security Assessment Framework'

# ----------------------------------------------------------------------------- #
#						OS ROOT PASSWORD
# ----------------------------------------------------------------------------- #

# -- ROOT_PASSWORD
ROOT_PASSWORD = "9759865"



#@Note
# There is no root password in live mode
# But root password is required in a non-live mode
# use LIVE  or NON-LIVE  as the value for ENV variable
ENV = "LIVE"  #ENV = "NON-LIVE"



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

# @Note: tests are fetched automatically from the dirs in TEST_DIRECTIORY_LIST
# to use below lisr instead, pass true to _fetch_test_suite_list() function.
# below list is not used by default
AVAILABLE_TESTS = QRY_MODULE_PATH.keys()




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
				'spi_lock':'msg11',
				'memconfig':'msg11',
				'remap':'msg11',
				'smm_dma':'msg11',
				'variables':'msg11',
				'access_uefispec':'msg11',
				's3bootscript':'msg11'
				}


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
				'spi_lock':'msg11',
				'memconfig':'msg11',
				'remap':'msg11',
				'smm_dma':'msg11',
				'variables':'msg11',
				'access_uefispec':'msg11',
				's3bootscript':'msg11'
				}


ADDITIONAL_TEST_USAGE_MESSAGE = u"شما میتوانید فایلهای تست خود را نیز اجرا کنید!"
ADDITIONAL_TEST_I_SHORT_MSG = u"توجه نمایید که این تست فقط هنگامی اجرا میگردد که از پنجره کناری فعال شده باشد."
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


# Test Result Table Headers
TEST_RESULT_TABLE_HEADERS = ['Color Code','Criticality','Expected Result','Test Result','Test Description','Option Under Test','Test Name']



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
FLOCKDN_DESCRIPTION = u"بیت FLOCKDN سطح دسترسی(خواندن/نوشتن) در ثبات HSFS و برخی دیگر از ثبات های کنترلی را مشخص می¬کند.\n صفر بودن آن به معنی عدم برقراری سطوح امنیتی است. (مهم¬ترین بیتی که در این آزمون کنترل می¬شود)" # use \n for newlines!
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
SMM_BWP_2_DESCRIPTION = u"بیت SMM_BWP طریقه دسترسی به حافظه فلش دربردارنده بایوس را مشخص می کند.\n در صورتی که این بیت برابر یک باشد دسترسی به کدهای بایوس تنها از طریق حالت SMM امکان پذیر خواهد بود.\n در صورت عدم فعال بودن سطوح امنیتی PR می توانند جایگزین آن شوند و دسترسی ها را محدود کنند." # use \n for newlines!
SMM_BWP_2_REPR = "SMM_BWP"
SMM_BWP_2_TEST_NAME = "SMI Events Configuration"


TCO_SMI_LOCK_COLOR_CODE = "RED"
TCO_SMI_LOCK_CRITICALITY = "HIGH"
TCO_SMI_LOCK_EXPECTED_RESULT = "1"
TCO_SMI_LOCK_DESCRIPTION = u"اگر این بیت برابر یک باشد TCO در برابر نوشتن محافظت می شود و امنیت آن حفظ خواهد شد." # use \n for newlines!
TCO_SMI_LOCK_REPR = "TCO SMI configuration (TCO SMI Lock)"
TCO_SMI_LOCK_TEST_NAME = "SMI Events Configuration"

SMI_LOCK_COLOR_CODE = "RED"
SMI_LOCK_CRITICALITY = "HIGH"
SMI_LOCK_EXPECTED_RESULT = "1"
SMI_LOCK_DESCRIPTION = u"اگر این بیت برابر یک باشد SMI در برابر نوشتن محافظت می شود و امنیت آن حفظ خواهد شد." # use \n for newlines!
SMI_LOCK_REPR = "SMI events global configuration (SMI Lock)"
SMI_LOCK_TEST_NAME = "SMI Events Configuration"


Global_SMI_EN_COLOR_CODE = "GREEN"
Global_SMI_EN_CRITICALITY = "Not Critical"
Global_SMI_EN_EXPECTED_RESULT = "1"
Global_SMI_EN_DESCRIPTION = u"در صورت صفر بودن این بیت وقفه های سیستمی غیرفعال خواهند شد.\n سیستم در مقابل حملات بسیار حساس می شود." # use \n for newlines!
Global_SMI_EN_REPR = "Global SMI Enable"
Global_SMI_EN_TEST_NAME = "SMI Events Configuration"


TCO_SMI_EN_COLOR_CODE = "GREEN"
TCO_SMI_EN_CRITICALITY = "Not Critical"
TCO_SMI_EN_EXPECTED_RESULT = "1"
TCO_SMI_EN_DESCRIPTION = u"در صورتی که مقدار این بیت یک باشد مدار TCO امکان استفاده از وقفه های سیستمی را خواهد داشت." # use \n for newlines!
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
BIOS_KEYBOARD_BUFF_DESCRIPTION = u"این بافر به منظور ذخیره اولیه گذرواژه برای مقایسه حروف گذرواژه می باشد.\n پس از بوت شدن سیستم باید این بافر ریست شود و گذرواژه درون خود را پاک کند." # use \n for newlines!
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
BIOSWE_DESCRIPTION = u"این بیت وضعیت امکان نوشتن بر روی حافظه بایوس را مشخص می کند.\n در صورتی که نیاز به تغییراتی در کدهای بایوس باشد این بیت می تواند به صورت موقت یک شود." # use \n for newlines!
BIOSWE_REPR = "BIOSWE"
BIOSWE_TEST_NAME = "BIOS Region Write Protection"

BLE_COLOR_CODE = "RED"
BLE_CRITICALITY = "HIGH"
BLE_EXPECTED_RESULT = "1"
BLE_DESCRIPTION = u"بیت BIOSWE توسط این بیت محافظت می شود. \nدرخواست ها برای نوشتن بر روی حافظه بایوس تنها زمانی مجاز هستند که این بیت برابر صفر شده و بیت BIOSWE به صورت موقت به مقدار یک تغییر کند. " # use \n for newlines!
BLE_REPR = "BLE"
BLE_TEST_NAME = "BIOS Region Write Protection"

SRC_COLOR_CODE = "GREEN"
SRC_CRITICALITY = "Not Critical"
SRC_EXPECTED_RESULT = "-"
SRC_DESCRIPTION = u"امکان خواندن تنظیمات وقفه های سیستمی را فراهم می کند. در اکثر پلتفرم ها این مقدار برابر یک است." # use \n for newlines!
SRC_REPR = "SRC"
SRC_TEST_NAME = "BIOS Region Write Protection"

TSS_COLOR_CODE = "ORANGE_LIGHT"
TSS_CRITICALITY = "LOW"
TSS_EXPECTED_RESULT = "0"
TSS_DESCRIPTION = u"این بیت در هنگام بروزرسانی بایوس می تواند مقدار یک در خود داشته باشد." # use \n for newlines!
TSS_REPR = "TSS"
TSS_TEST_NAME = "BIOS Region Write Protection"


SMM_BWP_COLOR_CODE = "ORANGE"
SMM_BWP_CRITICALITY = "NORMAL"
SMM_BWP_EXPECTED_RESULT = "1"
SMM_BWP_DESCRIPTION = u"ثباتی امنیتی برای کنترل نوشتن بر روی کدهای حالت SMM است.\n در صورت فعال نبودن امنیت سیستم مورد تهدید قرار می گیرد ولی روش های جایگزینی برای آن وجود دارند." # use \n for newlines!
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
D_LCK_DESCRIPTION = u"در صورت فعال بودن SMRAM که کدهای بایوس را درون خود نگه داری می کند، این بیت کاربرد خواهد داشت.\n در صورت فعال بودن این بیت، مقادیر آدرس های اولیه و فعال شدن حافظه SMRAM و ... قفل خواهند شد." # use \n for newlines!
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
UE_DESCRIPTION = u" زمان واقعی سیستم باید در برابر نرمافزار ها محافظت شود. این بیت 128 بایت بالایی حافظه زمان واقعی سیستم را فعال می کند." # use \n for newlines!
UE_REPR = "UE"
UE_TEST_NAME = "Protected RTC\nMemory Locations"

LL_COLOR_CODE = "YELLOW"
LL_CRITICALITY = "LOW"
LL_EXPECTED_RESULT = "1"
LL_DESCRIPTION = u" زمان واقعی سیستم باید در برابر نرمافزار ها محافظت شود. این بیت قفل 128 بایت بالایی حافظه زمان واقعی سیستم را فعال می کند." # use \n for newlines!
LL_REPR = "LL"
LL_TEST_NAME = "Protected RTC\nMemory Locations"

UL_COLOR_CODE = "YELLOW"
UL_CRITICALITY = "LOW"
UL_EXPECTED_RESULT = "1"
UL_DESCRIPTION = u" زمان واقعی سیستم باید در برابر نرمافزار ها محافظت شود. این بیت قفل 128 بایت پایینی حافظه زمان واقعی سیستم را فعال می کند." # use \n for newlines!
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
IA32_Lock_DESCRIPTION = u"این بیت نقش قفل کننده نوشتن بر روی برخی ثبات های MSR را بر عهده دارد.\n این بیت باید همواره برابر یک باشد." # use \n for newlines!
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
BBRA_BBWA_DESCRIPTION = u"دسترسی به هر ناحیه امنیتی در حافظه های فلش باید به گونه ای باشد که کدهای مربوط به بایوس، امضای دیجیتال سیستم و ... برای همه نرم افزار ها قابل دسترس نباشند و محدودیت صحیح اعمال شود. \nدر این آزمون در صورتی که مقادیر مجاز ناحیه ها بر قرار نباشند، این مسئله را هشدار خواهد داد." # use \n for newlines!
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
FDOPSS_DESCRIPTION = u"این بیت از توصیف گر حافظه فلش در برابر باز پیکربندی محافظت می کند." # use \n for newlines!
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
BILD_DESCRIPTION = u"در صورتی که مقدار این بیت برابر یک نباشد، Bios Interface قفل نبوده و امکان دسترسی به آن وجود دارد." # use \n for newlines!
BILD_REPR = "BILD"
BILD_TEST_NAME = "BIOS Interface Lock \nincluding Top Swap Mode"

TSS_2_COLOR_CODE = "YELLOW"
TSS_2_CRITICALITY = "LOW"
TSS_2_EXPECTED_RESULT = "0"
TSS_2_DESCRIPTION = u"این بیت نباید به مدت زیادی برابر یک باشد و تنها در زمان به روزرسانی باید مقدار یک به خود بگیرد." # use \n for newlines!
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
SMRR_range_base_DESCRIPTION = u"حد پایین آدرس های محافظت شده توسط SMRR را مشخص می کند.\n باید مقدار صحیحی داشته باشد." # use \n for newlines!
SMRR_range_base_REPR = "SMRR_range_base_programming"
SMRR_range_base_TEST_NAME = "CPU SMM Cache Poisoning"


SMRR_range_mask_COLOR_CODE = "ORANGE"
SMRR_range_mask_CRITICALITY = "NORMAL"
SMRR_range_mask_EXPECTED_RESULT = "Passed"
SMRR_range_mask_DESCRIPTION = u"حد بالای آدرس های محافظت شده توسط SMRR را مشخص می¬کند.\n باید مقدار صحیحی داشته باشد." # use \n for newlines!
SMRR_range_mask_REPR = "SMRR_range_mask_programming"
SMRR_range_mask_TEST_NAME = "CPU SMM Cache Poisoning"


SMRR_range_base_and_mask_are_same_COLOR_CODE = "ORANGE"
SMRR_range_base_and_mask_are_same_CRITICALITY = "NORMAL"
SMRR_range_base_and_mask_are_same_EXPECTED_RESULT = "Passed"
SMRR_range_base_and_mask_are_same_DESCRIPTION = u"به ازای تمامی core ها مقادیر SMRR باید در حدود مجاز باشند." # use \n for newlines!
SMRR_range_base_and_mask_are_same_REPR = "Same SMRR range\nBase and Mask\non all logical cpus"
SMRR_range_base_and_mask_are_same_TEST_NAME = "CPU SMM Cache Poisoning"


IA32_SMRR_PHYSBASE_COLOR_CODE = "RED"
IA32_SMRR_PHYSBASE_CRITICALITY = "HIGH"
IA32_SMRR_PHYSBASE_EXPECTED_RESULT = "Permissible Values"
IA32_SMRR_PHYSBASE_DESCRIPTION = u"در صورتی که این ثبات در محدوده مجاز نباشد حمله کننده می تواند برای دسترسی به بخشی از فضای SMRAM مقادیر TSEG را تغییر دهد." # use \n for newlines!
IA32_SMRR_PHYSBASE_REPR = "IA32_SMRR_PHYSBASE"
IA32_SMRR_PHYSBASE_TEST_NAME = "CPU SMM Cache Poisoning"

SMMR_PROTECTION_AGAINST_CACHE_ATTACK_COLOR_CODE = "ORANGE"
SMMR_PROTECTION_AGAINST_CACHE_ATTACK_CRITICALITY = "NORMAL"
SMMR_PROTECTION_AGAINST_CACHE_ATTACK_EXPECTED_RESULT = "Passed"
SMMR_PROTECTION_AGAINST_CACHE_ATTACK_DESCRIPTION = u"محافظت از حافظه SMMR در برابر حملات حافظه کش.\n در صورت فعال نبودن حمله کننده با استفاده از حافظه کش می تواند فابل های آلوده را برای بوت سیستم بارگزاری کند." # use \n for newlines!
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
RemapWindowConfig_DESCRIPTION = u"مقادیر Limit و Base و TOUUD را چک می کند.\n در صورتی که مقدار Correct بازگردانده شود به معنای آن است که بدافزاری مقادیر را غیر مجاز نکرده است." # use \n for newlines!
RemapWindowConfig_REPR = "Remap Window Configuration"
RemapWindowConfig_TEST_NAME = "Memory Remap Configuration"

TOUUD_COLOR_CODE = "ORANGE"
TOUUD_CRITICALITY = "NORMAL"
TOUUD_EXPECTED_RESULT = "Permissible Values"
TOUUD_DESCRIPTION = u"باید مقدار مجاز داشته باشد و حد بالایی دسترسی ها در Memory Remapping را مشخص کند." # use \n for newlines!
TOUUD_REPR = "TOUUD"
TOUUD_TEST_NAME = "Memory Remap Configuration"

TOLUD_COLOR_CODE = "ORANGE"
TOLUD_CRITICALITY = "NORMAL"
TOLUD_EXPECTED_RESULT = "Permissible Values"
TOLUD_DESCRIPTION = u"باید مقدار مجاز داشته باشد و حد پایینی دسترسی ها در Memory Remapping را مشخص کند." # use \n for newlines!
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
BDSM_DESCRIPTION = " " # use \n for newlines!
BDSM_REPR = "BDSM"
BDSM_TEST_NAME = "Host Bridge Memory\nMap Locks"


BGSM_COLOR_CODE = "YELLOW"
BGSM_CRITICALITY = "LOW"
BGSM_EXPECTED_RESULT = "LOCKED"
BGSM_DESCRIPTION = " " # use \n for newlines!
BGSM_REPR = "BGSM"
BGSM_TEST_NAME = "Host Bridge Memory\nMap Locks"


DPR_COLOR_CODE = "ORANGE"
DPR_CRITICALITY = "NORMAL"
DPR_EXPECTED_RESULT = "LOCKED"
DPR_DESCRIPTION = u"در صورت فعال نبودن حمله کننده می تواند به آدرس های  جازی غیر مجاز دسترسی داشته باشد." # use \n for newlines!
DPR_REPR = "DPR"
DPR_TEST_NAME = "Host Bridge Memory\nMap Locks"

GGC_COLOR_CODE = "GREEN"
GGC_CRITICALITY = "Not Critical"
GGC_EXPECTED_RESULT = "LOCKED"
GGC_DESCRIPTION = " " # use \n for newlines!
GGC_REPR = "GGC"
GGC_TEST_NAME = "Host Bridge Memory\nMap Locks"

MESEG_MASK_COLOR_CODE = "RED"
MESEG_MASK_CRITICALITY = "HIGH"
MESEG_MASK_EXPECTED_RESULT = "LOCKED"
MESEG_MASK_DESCRIPTION = u"به علت آن که ME در حلقه -2 قرار دارد بسیار حیاتی است محدوده های تعیین شده توسط آن مقدار صحیح داشته باشند.\n همچنین برنامه های کاربر نباید در محدوده های غیرمجاز قرار گیرند." # use \n for newlines!
MESEG_MASK_REPR = "MESEG_MASK"
MESEG_MASK_TEST_NAME = "Host Bridge Memory\nMap Locks"

PAVPC_COLOR_CODE = "YELLOW"
PAVPC_CRITICALITY = "LOW"
PAVPC_EXPECTED_RESULT = "LOCKED"
PAVPC_DESCRIPTION = " " # use \n for newlines!
PAVPC_REPR = "PAVPC"
PAVPC_TEST_NAME = "Host Bridge Memory\nMap Locks"

REMAPBASE_COLOR_CODE = "ORANGE"
REMAPBASE_CRITICALITY = "NORMAL"
REMAPBASE_EXPECTED_RESULT = "LOCKED"
REMAPBASE_DESCRIPTION = u"درصورتی که Base مقدار صحیحی نداشته باشد حمله کننده به اطلاعات حساسی نظیر SMRAM دسترسی پیدا می کند." # use \n for newlines!
REMAPBASE_REPR = "REMAPBASE"
REMAPBASE_TEST_NAME = "Host Bridge Memory\nMap Locks"

REMAPLIMIT_COLOR_CODE = "ORANGE"
REMAPLIMIT_CRITICALITY = "NORMAL"
REMAPLIMIT_EXPECTED_RESULT = "LOCKED"
REMAPLIMIT_DESCRIPTION = u"درصورتی که Limit مقدار صحیحی نداشته باشد حمله کننده به اطلاعات حساسی نظیر SMRAM دسترسی پیدا می کند." # use \n for newlines!
REMAPLIMIT_REPR = "REMAPLIMIT"
REMAPLIMIT_TEST_NAME = "Host Bridge Memory\nMap Locks"

TOLUD_2_COLOR_CODE = "ORANGE"
TOLUD_2_CRITICALITY = "NORMAL"
TOLUD_2_EXPECTED_RESULT = "LOCKED"
TOLUD_2_DESCRIPTION = u"باید مقدار مجاز داشته باشد و حد پایینی دسترسی ها در Memory Remapping را مشخص کند." # use \n for newlines!
TOLUD_2_REPR = "TOLUD"
TOLUD_2_TEST_NAME = "Host Bridge Memory\nMap Locks"


TOM_COLOR_CODE = "ORANGE"
TOM_CRITICALITY = "NORMAL"
TOM_EXPECTED_RESULT = "LOCKED"
TOM_DESCRIPTION = u"اگر این آدرس تغییر کند ME به اطلاعات مورد نیازش دسترسی نخواهد داشت." # use \n for newlines!
TOM_REPR = "TOM"
TOM_TEST_NAME = "Host Bridge Memory\nMap Locks"


TOUUD_2_COLOR_CODE = "ORANGE"
TOUUD_2_CRITICALITY = "NORMAL"
TOUUD_2_EXPECTED_RESULT = "LOCKED"
TOUUD_2_DESCRIPTION = u"باید مقدار مجاز داشته باشد و حد بالایی دسترسی ها در Memory Remapping را مشخص کند." # use \n for newlines!
TOUUD_2_REPR = "TOUUD"
TOUUD_2_TEST_NAME = "Host Bridge Memory\nMap Locks"

TSEGMB_COLOR_CODE = "ORANGE"
TSEGMB_CRITICALITY = "NORMAL"
TSEGMB_EXPECTED_RESULT = "LOCKED"
TSEGMB_DESCRIPTION = u"آدرس شروع ناحیه TSEG نباید تغییر کند." # use \n for newlines!
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
TSEG_1_DESCRIPTION = u"مقدار شروع تا پایان این ثبات باید با مقدار شروع و پایان SMRR برابر باشد.\n در صورتی که مقادیر متفاوت باشند احتمال بروز حملات DMA وجود دارد و حمله کننده می تواند به کل یا بخشی از اطلاعات SMRAM دسترسی پیدا کند." # use \n for newlines!
TSEG_1_REPR = "TSEG"
TSEG_1_TEST_NAME = "SMM TSEG Range\nConfiguration Check"


SMRR_Range_COLOR_CODE = "ORANGE"
SMRR_Range_CRITICALITY = "NORMAL"
SMRR_Range_EXPECTED_RESULT = "-"
SMRR_Range_DESCRIPTION = u"مقدار شروع و پایان این ثبات باید با مقدار شروع و پایان TSEG برابر باشد.\n در صورتی که مقادیر متفاوت باشند احتمال بروز حملات DMA وجود دارد و حمله کننده می تواند به کل یا بخشی از اطلاعات SMRAM دسترسی پیدا کند." # use \n for newlines!
SMRR_Range_REPR = "SMRR_Range"
SMRR_Range_TEST_NAME = "SMM TSEG Range\nConfiguration Check"



# ----------------------------------------------------------------------------- #
#				 End SMM TSEG Range Configuration Check
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#				S3 Resume Boot-Script Protections
# ----------------------------------------------------------------------------- #


S3_BootScript_COLOR_CODE = "RED"
S3_BootScript_CRITICALITY = "HIGH"
S3_BootScript_EXPECTED_RESULT = "Protected"
S3_BootScript_DESCRIPTION = u"آدرس اسکریپت بوت پس از خروج از حالت خواب سیستم، باید محافظت شده باشد." # use \n for newlines!
S3_BootScript_REPR = "S3 Boot-Script"
S3_BootScript_TEST_NAME = "S3 Resume Boot-Script\nProtections"


Dispatch_Opcodes_COLOR_CODE = "ORANGE"
Dispatch_Opcodes_CRITICALITY = "NORMAL"
Dispatch_Opcodes_EXPECTED_RESULT = "Protected"
Dispatch_Opcodes_DESCRIPTION = u"آپکد های اسکریپت بوت پس از خروج از حالت خواب سیستم، باید محافظت شده باشد." # use \n for newlines!
Dispatch_Opcodes_REPR = "Entry-Point of\nDispatch Opcodes"
Dispatch_Opcodes_TEST_NAME = "S3 Resume Boot-Script\nProtections"

# ----------------------------------------------------------------------------- #
#				SMM TSEG Range Configuration Check
# ----------------------------------------------------------------------------- #

