from matplotlib import pyplot as plt 
import numpy as np 
from time import perf_counter
import sys

def pie_image(n):
 start=perf_counter()
 x=np.linspace(0,1,n)
 y=np.sqrt(1-(x**2))
 fig,ax=plt.subplots()
 plt.figure(num=1,figsize=(12,12),dpi=1000)
 ax.plot(x,y,color="yellow",label="circle curve")
 ax.set_facecolor("black")
 rx=np.random.random(n)
 ry=np.random.random(n)
 points=np.array(list(zip(rx,ry)))
 good=np.array([(i,j) for i,j in points if j<=np.sqrt(1-(i**2))])
 bad=np.array([(i,j) for i,j in points if (i,j) not in good])
 green_x=np.array([i for i in map(lambda x:x[0],good)])
 green_y=np.array([i for i in map(lambda x:x[1],good)])
 red_x = np.array([i for i in map(lambda x:x[0],bad)])
 red_y=np.array([i for i in map(lambda x:x[1],bad)])
 a= 1 if n<=1000 else 0.6
 ax.scatter(green_x,green_y,color="green",s=1.3,alpha=a,marker="o",label="points in the circle")
 ax.scatter(red_x,red_y,color="red",s=1.3,marker="o",alpha=a,label="points out of the circle")
 ax.set_xlabel("x")
 ax.set_ylabel("y")
 ax.set_title("Pi approximation of {} random numbers is {} \n".format(n,(len(green_x)/n)*4).format(n))
 ax.legend()
 print("Pi approximation of {} random numbers is {} \n".format(n,(len(green_x)/n)*4))
 print("Took %s seconds to complete with size %d" %(round(perf_counter(),4)-start,n))
 plt.show()
if __name__=="__main__":
    if len(sys.argv)==1:
        pie_image(10000)
    elif len(sys.argv)==2:
        pie_image(int(sys.argv[1]))
    else:
        print("You gave more than one arguments\n")