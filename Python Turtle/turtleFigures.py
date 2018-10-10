from turtle import *
import math


def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end 

def tree4(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)

#end


def fern(n, l, pen):
     # termination
     if n==0 or l<2:
          return
     #end if

     pen.forward(2*l/3)
     pen.right(45);fern(n-1, l/2, pen);pen.left(45)
     pen.forward(2*l/3)
     pen.left(30);fern(n-1, l/2, pen);pen.right(30);
     pen.forward(2*l/3)
     pen.right(10);fern(n-1, 0.8*l, pen);pen.left(10)
     pen.backward(2*l)
#end

def koch(n,l,pen):
     # termination
     if n==0 or l<2:
          pen.forward(l)
          return
     #endif

     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
     pen.right(120)
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
#end


def flake(n,l,pen):
     for i in range(3):
          koch(n,l,pen)
          pen.right(120)
     #end for
#end

def gasket(n,l,pen):
     # termination
     if n==0 or l<2:
          for i in range(3):
               pen.forward(l)
               pen.left(120)
          #endfor
          return
     #endif

     for i in range(3):
          gasket(n-1, l/2, pen)
          pen.forward(l)
          pen.left(120)
     #endfor
#end

     
def swiss(n, l,pen):
     if n==0 or l<2:
          for i in range(4):
               pen.forward(l)
               pen.left(90)
          #endfor
          return
     #endif

     for i in range(4):
          swiss(n-1, l/3, pen)
          pen.forward(l)
          pen.left(90)
     #endfor
#end

def square(n, l, pen):
     if n==0 or l<2:
          for i in range(4):
               pen.forward(l)
               pen.left(90)
          #endfor
          return
     #endif

     for i in range(4):
          square(n-1, l/3, pen)
          pen.forward(l)
          pen.left(90)
     #endfor

     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.right(90)
     square(n-1, l/3, pen)
     pen.backward(l/3)
     pen.left(90)
     pen.backward(l/3)
     pen.right(90)
#end


def circle(n, l, pen):
     pen.circle(l)
     if n==0 or l<2:
          return
              
     #end
     for i in range(4):
          circle(n-1, l/3, pen)
          pen.up()
          pen.forward(l)
          pen.left(90)
          pen.forward(l)
          pen.down()
          pen.circle(l/3)
    
          #endfor
         
     #endif

def colorful(n, l, pen):
     if n==0 or l<2:
          return
     #end
     colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
     for i in range(360):
          pencolor(colors[i % 6])
          width(i/100 + 1)
          forward(i)
          left(59)
          #end for
               

     
     
