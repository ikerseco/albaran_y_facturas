from localStoragePy import localStoragePy
l = localStoragePy('me.jkelokky.mypythonapp', 'json')
mailLocal = l.getItem('mailUser')
print(mailLocal)