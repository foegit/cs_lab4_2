from rarhack import RarCracker
import rarfile

rarfile.UNRAR_TOOL = './unrar/unrar.exe'


rarfile.RarFile('./data/test.rar').extractall(pwd='ok')
cracker = RarCracker()

print(rarfile.RarWrongPassword)
cracker.crack('./data/test.rar', 2, 2)
