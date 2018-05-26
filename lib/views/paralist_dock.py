# -*- coding: utf-8 -*-

# =============================================================================
# =======概述
# 创建日期：2018-05-17
# 编码人员：王学良
# 简述：参数窗口类
#
# =======使用说明
# 。。。
#
# =======日志
# 
# =============================================================================

# =============================================================================
# Qt imports
# =============================================================================
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (QWidget, QDockWidget, QStackedWidget, QLineEdit,
                             QTreeWidget, QTreeWidgetItem, QSizePolicy,
                             QVBoxLayout, QAbstractItemView)

# =============================================================================
# Stacked Widget
# =============================================================================
class ParalistDock(QDockWidget):
    signal_close = pyqtSignal()
    
    def __init__(self):
        QStackedWidget.__init__(self)
    
    def setup(self):
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.layout_paralist_dock = QWidget(self)
        self.layout_paralist_dock.setObjectName("layout_paralist_dock")
        self.vlayout_paralist_dock = QVBoxLayout(self.layout_paralist_dock)
        self.vlayout_paralist_dock.setContentsMargins(1, 1, 1, 1)
        self.vlayout_paralist_dock.setSpacing(2)
        self.vlayout_paralist_dock.setObjectName("vlayout_paralist_dock")
        self.line_edit_search_para = QLineEdit(self.layout_paralist_dock)
        self.line_edit_search_para.setToolTip("")
        self.line_edit_search_para.setInputMask("")
        self.line_edit_search_para.setText("")
        self.line_edit_search_para.setMaxLength(32766)
        self.line_edit_search_para.setFrame(True)
        self.line_edit_search_para.setEchoMode(QLineEdit.Normal)
        self.line_edit_search_para.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.line_edit_search_para.setReadOnly(False)
        self.line_edit_search_para.setObjectName("line_edit_search_para")
        self.vlayout_paralist_dock.addWidget(self.line_edit_search_para)
        self.tree_widget_display_datafile = QTreeWidget(self.layout_paralist_dock)
        self.tree_widget_display_datafile.setObjectName("tree_widget_display_datafile")
        self.tree_widget_display_datafile.headerItem().setText(0, "1")
        self.tree_widget_display_datafile.header().setVisible(False)
        self.tree_widget_display_datafile.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.vlayout_paralist_dock.addWidget(self.tree_widget_display_datafile)
        self.setWidget(self.layout_paralist_dock)  
    
    def display_file_group(self, file_group):

        self.tree_widget_display_datafile.clear()        
        if file_group:  #file_name is a dict            
            for file in file_group:
                root = QTreeWidgetItem(self.tree_widget_display_datafile) #QTreeWidgetItem object: root
                root.setText(0,file) #set text of treewidget
                for para in file_group[file]:
                    child = QTreeWidgetItem(root)  #child of root
                    child.setText(0,para)   

#    重载关闭事件，需要增加一个关闭的信号让菜单栏下的勾选去掉        
    def closeEvent(self, event: QCloseEvent):
        event.accept()
        self.signal_close.emit()
        