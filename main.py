##by:: mohamed dawoud
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import sqrt

#return array of y axis same length as x axis :
  #symetric speedup
def speedA(f,n):
	return [ 1/((1-f)/sqrt(r) + (f*r)/(sqrt(r)*n))  for r in R ]
	 
  #asymetric speedup
def speedB(f,n):
	return [ 1 / ((1 - f) / sqrt(r) + f / (sqrt(r) + n - r)) for r in R  ]    
	
  #dynmic speedup
def speedC(f,n):
	return [1/((1-f)/sqrt(r) + f/n)  for r in R]
	

#plot :
R = [s for s in range(1,240,4)] #x_axis

fig = plt.figure(figsize=(12,7))
plt.subplots_adjust(left=0.10, bottom=0.25)

p1,=plt.plot(R,speedA(0.3,200) )
p2,=plt.plot(R,speedB(0.3,200) )
p3,=plt.plot(R,speedC(0.3,200) )
plt.xlim(0,250 )
plt.ylim(0, 180 )
plt.xlabel("BCEs ")
plt.ylabel("speed")


#slider1
#set slider opject dimention
slider_ax = plt.axes([0.1, 0.14, 0.8, 0.04])
# create the slider
a_slider = Slider(slider_ax, 'f symetric', 0.4, 0.99,valinit=0.2, color='blue' )

#slider2
#set slider opject dimention
slider_bx = plt.axes([0.1, 0.08, 0.8, 0.04])
# create the slider
b_slider = Slider(slider_bx, 'f Asymetric', 0.5, 0.99,valinit=0.7, color='orange')

#slider3
#set slider opject dimention
slider_cx = plt.axes([0.1, 0.02, 0.8, 0.04])
# create the slider
c_slider = Slider(slider_cx, 'f dynmic', 0.4, 0.970,valinit=0.4 ,color='green')

#slider4
#set slider opject dimention
slider_nx = plt.axes([0.1, 0.9, 0.8, 0.04])
# create the slider
n_slider = Slider(slider_nx, 'n', 1, 256,valinit=200 ,color='cyan')

def update(val):
	a1=a_slider.val
	a2=b_slider.val
	a3=c_slider.val
	n= n_slider.val
	p1.set_ydata(speedA(a1,n))
	p2.set_ydata(speedB(a2,n))
	p3.set_ydata(speedC(a3,n))
	fig.canvas.draw_idle()

a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)
n_slider.on_changed(update)

plt.show()