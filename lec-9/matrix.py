from numpy import * 

# recording temprature for 1 week measured in the morning, mid-day, evening and mid-night
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
m = reshape(a,(7,5))
print(m)
print()

m_r = append(m,[['Avg',12,15,13,11]],0)
print(m_r)
print()

m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(m_c)
print()

m = delete(m,[2],0)
print(m)
print()

m = delete(m,s_[2],1)
print(m)
print()

m[3] = ['Thu',0,0,0]
print(m)