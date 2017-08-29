import numpy as np
import pandas as pd
from pandas import Series, DataFrame

regno=np.arange(171046001,171046011)
ads=np.random.randint(35,101,10)
fml=np.random.randint(35,101,10)
lsds=np.random.randint(35,101,10)
pdv=np.random.randint(35,101,10)
psi=np.random.randint(35,101,10)

student=list(zip(regno,ads,fml,lsds,pdv,psi))
df=DataFrame(data=student,columns=['RegNo','ADS','FML','LSDS','PDV','PSI'])
print df

res=df[['RegNo','ADS']][df.ADS==df.ADS.max()].values
for i in range(len(res)):
	print "RegNo",res[i][0],"scored highest in ADS with",res[i][1],"marks"

res=df[['RegNo','FML']][df.FML==df.FML.max()].values
for i in range(len(res)):
	print "RegNo",res[i][0],"scored highest in FML with",res[i][1],"marks"

res=df[['RegNo','LSDS']][df.LSDS==df.LSDS.max()].values
for i in range(len(res)):
	print "RegNo",res[i][0],"scored highest in LSDS with",res[i][1],"marks"

res=df[['RegNo','PDV']][df.PDV==df.PDV.max()].values
for i in range(len(res)):
	print "RegNo",res[i][0],"scored highest in PDV with",res[i][1],"marks"

res=df[['RegNo','PSI']][df.PSI==df.PSI.max()].values
for i in range(len(res)):
	print "RegNo",res[i][0],"scored highest in PSI with",res[i][1],"marks"

print "Average marks in LSDS=",np.mean(df['LSDS'].values)
print "Average marks in PSI=",np.mean(df['PSI'].values)