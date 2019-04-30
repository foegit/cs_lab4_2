import rarfile
from brute import brute
from time import time

class RarCracker():
  def format_time(self, total_seconds):
    tmp = total_seconds
    hours = tmp // 3600
    tmp -= hours * 3600
    minutes = tmp // 60
    tmp -= minutes * 60
    seconds = tmp
    return hours, minutes, seconds

  def crack(self, filename, pwd_start_len, pwd_len):
    start_time = time()
    file = rarfile.RarFile(filename)
    dict = list(brute(start_length=pwd_start_len, length=pwd_len,
                      letters=True, numbers=True, symbols=False, spaces=False))

    word_sum = len(dict) + 1
    for (i, word) in enumerate(dict):
      avg_time_per_iter = (time() - start_time) / (i + 1)
      time_left = (word_sum - i) * avg_time_per_iter
      time_passed = time() - start_time
      hours_left, minutes_left, seconds_left = self.format_time(time_left)
      hours_passed, minutes_passed, seconds_passed = self.format_time(
          time_passed)
      persent = round(((i+1) / word_sum) * 100, 2)
      print("{:05.2f}% | passed: {:02.0f}:{:02.0f}:{:02.0f} | left: {:02.0f}:{:02.0f}:{:02.0f} | {:.2f} it/s | {}"
            .format(persent, hours_passed, minutes_passed, seconds_passed,
                    hours_left, minutes_left, seconds_left, 1 / avg_time_per_iter, word))
      try:
        file.extractall(pwd=word, path='./extract')
        print('\nCracked: {}'.format(word))
        savefile = open('cracked_files.txt', 'a+')
        savefile.write(
            '{}:"{}":{:02.0f}:{:02.0f}:{:02.0f}\n'.format(filename, word, hours_passed, minutes_passed, seconds_passed))
        break
      except rarfile.RarWrongPassword:
        pass
      except:
        raise Exception('Unknown exception')

