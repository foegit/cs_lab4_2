from rarhack import RarCracker
import rarfile

rarfile.UNRAR_TOOL = './unrar/unrar.exe'

cracker = RarCracker()

'''
Test archive with password H5
'''
# cracker.crack('./data/test.rar', 2, 2)


