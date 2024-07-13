# run soffice as 'server'
from subprocess import Popen

officepath = '/Applications/LibreOffice.app/Contents/MacOS/soffice' #respectivly the full path
calc = '--calc'
pipe = "--accept=pipe,name=abraxas;urp;StarOffice.Servicemanager"
Popen([officepath, calc, pipe]);

