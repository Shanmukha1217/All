from amstrong_number import main as amstr
from amstr_num_ser import main as amstr_series
from automorphic_num import main as auto
from automorphic_serie import main as auto_seres
from palindrome import main as palin
from palindrome_serie import main as palin_ser
from perfect_number import main as perf
from perfect_series import main as perf_ser
from prime_num import main as prime
from prime_series import main as prim_ser
from reversenum import main as rever
from reverse_series import main as rever_ser
from strong_num import main as stron
from strong_num_series import main as stron_ser

def single(num: int):
    if num == 1:
        prime()
    elif num == 2:
        perf()
    elif num == 3:
        amstr()
    elif num == 4:
        auto()
    elif num == 5:
        rever()
    elif num == 6:
        palin()
    elif num == 7:
        stron()
    else:
        print('Invalid choice')


def series(num: int):
    if num == 1:
        prim_ser()
    elif num == 2:
        perf_ser()
    elif num == 3:
        amstr_series()
    elif num == 4:
        auto_seres()
    elif num == 5:
        rever_ser()
    elif num == 6:
        palin_ser()
    elif num == 7:
        stron_ser()
    else:
        print('Invalid choice')