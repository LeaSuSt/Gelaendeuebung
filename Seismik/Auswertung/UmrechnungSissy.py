import numpy as np
import matplotlib.pyplot as plt

#31 in erster zeile
#18 in zweiter zeile
#sissyruck noch rumdrehen
sissyruck=np.array([1.2, 1.8, 2.4, 2.6, 3.2, 3.45, 3.7, 3.9, 4.1, 4.2, 4.3, 4.4, 4.6, 4.75, 4.9, 5.05, 5.45, 5.65, 6, 6.2, 6.3, 6.6, 6.9, 5.55+1.85, 5.55+2.1, 5.55+2.5, 5.55+2.7, 5.55+3.1, 5.55+3.2, 5.55+3.7, 5.55+3.9,
                    5.55+4.1, 5.55+4.25, 5.55+4.25, 5.55+4.4, 5.55+4.75, 5.55+4.9, 5.55+4.9, 5.55+5.05, 5.55+5.2, 5.55+5.25, 5.55+5.35, 5.55+5.4, 5.55+5.5, 5.55+5.5, 5.55+5.6, 5.55+5.8, 5.55+6, 5.55+5.95, 5.55+6.2, 5.55+6.3, 5.55+6.35, 5.55+6.6, 5.55+6.7, 5.55+6.9, 5.55+7, 9.25+3.6, 9.25+3.6, 9.25+3.75, 9.25+4, 9.25+4.1, 9.25+4.2, 9.25+4.7, 9.25+5, 9.25+5.2, 9.25+5.4, 9.25+5.5, 9.25+5.6, 9.25+5.7, 9.25+6.15, 9.25+6.25, 9.25+6.4
                    ])

sissyhin=np.array([1.2, 1.8, 2.4, 2.8, 3.5, 4.3, 4.8, 5.15, 5.5, 5.8, 5.9, 6, 6.05, 6.1, 6.2, 6.5, 6.6, 6.75, 6.85, 7.05, 5.55+1.7, 5.55+1.85, 5.55+2, 5.55+2.2, 5.55+2.3, 5.55+2.6, 5.55+2.8, 5.55+3.1, 5.55+3.2, 5.55+3.45, 5.55+3.6, 5.55+3.7, 5.55+4.05, 5.55+4.6, 5.55+4.7, 5.55+4.9, 5.55+5.15, 5.55+5.2, 5.55+5.5, 5.55+5.5, 5.55+5.9, 5.55+6, 5.55+6.2, 5.55+6.25, 5.55+6.4, 5.55+6.5, 5.55+6.7, 5.55+6.9, 5.55+7, 9.25+3.4, 9.25+3.5, 9.25+3.5, 9.25+3.5, 9.25+3.6, 9.25+3.7, 9.25+3.8, 9.25+3.9, 9.25+4, 9.25+4.2, 9.25+4.3, 9.25+4.4, 9.25+4.7, 9.25+4.9, 9.25+5, 9.25+5.2, 9.25+5.5, 9.25+5.7, 9.25+5.85, 9.25+6, 9.25+6.1, 9.25+6.2, 9.25+6.25])

print (len(sissyhin))
x = sissyruck 
xx=sissyhin
xs = x *0.02/3.7
xxs=xx *0.02/3.7

#print (xs)

y = [1.5, 2.5, 3.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 46.5, 48.5, 50.5, 52.5, 54.5, 56.5, 58.5, 60.5, 62.5, 64.5, 66.5, 68.5, 70.5, 72.5, 74.5, 76.5, 78.5, 80.5, 82.5, 84.5, 86.5, 88.5, 90.5, 92.5, 94.5, 96.5, 98.5, 100.5, 102.5, 104.5, 106.5, 108.5, 110.5, 112.5, 114.5, 116.5, 118.5, 120.5, 122.5, 124.5, 126.5, 128.5, 130.5, 132.5, 134.5, 135.5, 136.5, 137.5]
print (len(y))

reversed_y=y[::-1]

plt.plot(reversed_y, xs, "o")
plt.plot(y,xxs,"x")
plt.show()
