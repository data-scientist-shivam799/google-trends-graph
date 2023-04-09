from pytrends.request import TrendReq
pyTrends= TrendReq(hl='en-us')
keywords=['Python','R','C','Java','HTML']
pyTrends.build_payload(keywords,timeframe='today 5-y')
data=pyTrends.interest_over_time()
print(data)

import matplotlib.pyplot as plt
plt.plot(data)
plt.suptitle('Programming language search on google')
plt.xlabel('years')
plt.ylabel('weekly')
plt.legend(keywords,loc='upper left')
plt.show()
# plt.savefig('data.png')

focus=['Python','C']
plt.plot(data[focus])
plt.legend(focus)
plt.show()

data2=pyTrends.interest_by_region(resolution='COUNTRY',inc_low_vol=True)
data2=data2['Python'].nlargest(10)
print(data2)
data2=data2.to_frame()
print(data2)
data2.plot(kind='bar')
plt.show()
data3=pyTrends.interest_by_region(resolution='COUNTRY',inc_low_vol=True)
data3=data3[55:60]
data3.plot(kind='bar')
plt.show()