#Answer number1:
import datetime
tm = datetime.datetime.now()
print tm.strftime("%Y-%m-%d")
#Answer Number2:
import webbrowser
webbrowser.open_new_tab('https://youtu.be/FCXYYnr6ZZA')
#Answer Number3:
import os
path = '/Users/ashutoshsharma/Desktop/images'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
