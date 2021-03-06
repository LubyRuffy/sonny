from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from interfacing import imu

app = QtGui.QApplication([])

p = pg.plot()
p.setWindowTitle('IMU plot')
curve = p.plot()

data = [0]


def update():
    global curve, data
    line = imu.get_accel_data()
    data = [line[key] for key in line]
    xdata = np.array(data, dtype='float64')
    curve.setData(xdata)
    app.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()