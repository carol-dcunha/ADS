import numpy as np
import pandas as pd
from pandas import Series, DataFrame


print "\nWORKING WITH SERIES\n"

data=[3,-5,7,8,-2]

obj1=Series(data)
print obj1

obj2=Series(data,index=['one','three','four','two','five'])
print obj2

print "\nobj2.values=",obj2.values
print "\nobj2['three']=",obj2['three']
print "\nobj2[['three','two']]\n",obj2[['three','two']]
print "\nobj2[:3]\n",obj2[:3]
print "\nobj2[obj2>0]\n",obj2[obj2>0]
print "\n'one' in obj2=",'one' in obj2
print "'six' in obj2=",'six' in obj2

sdata={'Ktaka':8500,'Kerala':5800,'Bihar':12000}
obj3=Series(sdata)
print "\n",obj3

states=['Ktaka','Kerala','Bihar','Punjab']
obj3=Series(sdata,states)
print "\n",obj3

obj3['Punjab']=76000
print "\n",obj3

obj3.name='Population'
obj3.index.name='State'
print "\n",obj3

obj3.index=['Kannada','Malayalam','Hindi','Hindi']
obj3.index.name='Language'
print "\n",obj3
print "Population that speaks hindi=",sum(obj3['Hindi'])

obj4=Series(np.arange(10,101,10))
obj5=Series(np.arange(5,51,5))
print "\nobj4[:2]+obj5[:2]\n",obj4[:2]+obj5[:2]


print "\nWORKING WITH DATAFRAME\n"
data={'State':['Ktaka','Goa','Delhi','Kerala'],
		'Year':[2001,2001,2002,2003],
		'Population':[1.5,1.2,1.7,1.7]}
frame1=DataFrame(data)
print frame1
frame1=DataFrame(data,columns=['State','Year','Population','Debt'],index=['one','two','three','four'])
print "\n",frame1


frame1.to_csv('population.csv',index=False,header=True)
df=pd.read_csv('population.csv')
print "\n",df

print frame1,"\n"
print "\nframe1['State'].values=",frame1['State'].values
print "\nframe1.Population\n",frame1.Population

print "\nframe1.ix['two']\n",frame1.ix['two']
print "\nframe1.iat[1,2]=",frame1.iat[1,2]

m=frame1['Population'].max()
print "\nMaximum populated states"
print frame1[['Year','State']][frame1['Population']==m]
