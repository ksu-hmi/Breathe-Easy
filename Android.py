#install package
pip install buildozer

#create folder to navigate then run this command
buildozer init 

#(str) Title application
title=KvCalc

#(str) Package name
package.name =kvcalc

#(str) Package domain 
package.domain = org.kvcalc

#Install some dependencies then Run Code
buildozer -v android debug