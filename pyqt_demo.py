# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('List View')

        self.k = QtGui.QStringListModel(['A', 'B', 'C', 'D'])
        self.listView = QtGui.QListView()
        self.listView.setModel(self.k)
        self.listView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listView.customContextMenuRequested.connect(self.onRightClick)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.listView)
        self.setLayout(vbox)

    def onRightClick(self, pos):
        menu = QtGui.QMenu(self)
        delete = QtGui.QAction('Delete', self, triggered=self.deleteItem)
        menu.addAction(delete)
        menu.exec_(self.listView.mapToGlobal(pos))

    def deleteItem(self):
        index = self.listView.currentIndex()
        print 'Delete: %s' % index.data().toString()
        self.k.removeRow(index.row())


def main():
    app = QtGui.QApplication(sys.argv)
    ui = Example()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()