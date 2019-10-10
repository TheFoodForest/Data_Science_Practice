import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

def LinearRegression(xdata, ydata):
    nx = len(xdata)
    ny = len(ydata)
    ymean = sum(ydata)/ny
    xmean = sum(xdata)/nx
    #b1 = slope, b0 = y intercept
    b1 = (sum((ydata[i]-ymean)*(xdata[i]-xmean) for i in range(nx))/
          sum((xdata[i]-xmean)**2 for i in range(nx)))
    b0 = ymean - (b1*xmean)
    ypred = []   # list y predicted values
    for i in range(nx):
        ypred.append(b0 +b1*xdata[i])

    #total sum of squares TSS
    TSS = sum((ydata[i]-ymean)**2 for i in range(nx))
    #Explained sum of squares
    ESS = sum((ypred[i]-ymean)**2 for i in range(nx))
    #Residual sum of squares
    RSS = sum((ydata[i]-ypred[i])**2 for i in range(nx))
    #Standard Error of regression
    Se = np.sqrt(RSS/(nx-2))      #Standard Error of regression
    #r = R correlation, R2 = r^2 (only true in simple regress)
    R2 = ESS/TSS
    r = np.sqrt(R2)
    adjR2 = 1-(RSS/TSS)
    #standard error of slope coef
    Seb1 = np.sqrt(RSS/((nx-2)*sum((xdata[i]-xmean)**2 for i in range(nx))))
    #standard error of int coef
    Seb0 = Seb1*(np.sqrt((1/nx)*(np.dot(xdata,xdata))))
    # t test b0 and b1 
    tb0 = (b0-0)/(Seb0)
    tb1 = (b1-0)/(Seb1)
    #probability desity function for y int
    statsframe = DataFrame({' ':['Degrees of Freedom','R^2','Adj. R^2',
                                       'Correlation Coefficient'],
                            '*':[round((nx-1),4),round(R2,4),round(adjR2,4),
                                 round(r,4)]},{1,2,3,4})
    coefframe = DataFrame({'coefficient':['slope','y int.'],
                           'Stand Err':[round(Seb1,4),round(Seb0,4)],
                           'T test':[round(tb1,4),round(tb0,4)]},{1,2})
    print('='*13,'RESULTS','='*13)         
    print(statsframe)
    print('='*35)
    print(coefframe)
    print('='*35)
    print('Best fit line: y =',round(b1,4),'x + ',round(b0,4))
        
def plotregression(xdata, ydata, gtitle, xlabel, ylabel):
    plt.scatter(xdata,ydata)
    plt.title(gtitle)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    ax_histx = plt.axes()
    plt.scatter.tic_params(direction='in', top=True, right=True)
    ax_histy = plt.axes()
    ax_histx.hist(xdata)
    ax_histx.tic_params(direction='in', labelbottom=False)
    ax_histy.hist(ydata)
    ax_histy.tic_params(direction='in', labelbottom=False)
    nx = len(xdata)
    ymean = sum(ydata)/nx
    xmean = sum(xdata)/nx
    b1 = (sum((ydata[i]-ymean)*(xdata[i]-xmean) for i in range(nx))/
          sum((xdata[i]-xmean)**2 for i in range(nx)))
    b0 = ymean - (b1*xmean)
    nx = len(xdata)
    yreg = [b0 + b1 * xdata[i] for i in range(nx)]
    plt.plot(xdata, yreg)
    plt.show()
    
Xin = input('Enter X values sep by ",": ')
Yin = input('Enter Y values sep by ",": ')
Xlist = Xin.split(',')
Ylist = Yin.split(',')
x = np.array(Xlist, dtype= float)   
y = np.array(Ylist, dtype= float)
while len(x) != len(y):
    print('Error: X and Y must have the same number of data points.',
              '\n length of x = ', len(x),
              '\n length of y = ', len(y))
        
    Yin = input('Please re-enter y values sep by ","'
                '\nPress enter if no change desired: ')
    Xin = input('Please re-enter x values sep by ","'
                '\nPress enter if no change desired: ')
    if Yin != '':
        Ylist = Yin.split(',')
        y = np.array(Ylist, dtype= float)
        continue

    if Xin != '':
        Xlist = Xin.split(',')
        x = np.array(Xlist, dtype= float)
        continue
    
   
if len(x) == len(y):
    LinearRegression(x,y)
    response = input('Graph Regression?: ')
    if response in ('y','yep','yes','yea','yeah'):
        title = input('Graph Title: ')
        xname = input('x axis label: ')
        yname = input('y axis label: ')
        plotregression(x,y,title,xname,yname)
    
    else:
        print('No graph needed')
        
print(input('\n\npress enter to exit: '))
