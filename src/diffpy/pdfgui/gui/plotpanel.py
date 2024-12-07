#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.9.3 on Fri Jul 19 16:05:24 2019


import wx

from diffpy.pdfgui.control.controlerrors import ControlConfigError
from diffpy.pdfgui.gui import tooltips
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui.wxextensions.listctrls import KeyEventsListCtrl
from diffpy.pdfgui.gui.wxextensions.validators import FLOAT_ONLY, TextValidator
from diffpy.pdfgui.utils import numericStringSort


class PlotPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: PlotPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SetSize((456, 659))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "X"), wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)

        self.xDataCombo = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_READONLY)
        sizer_3.Add(self.xDataCombo, 1, wx.ALL, 5)

        sizer_4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Y"), wx.HORIZONTAL)
        sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)

        self.yDataList = KeyEventsListCtrl(
            self, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_NO_HEADER | wx.LC_REPORT
        )
        sizer_4.Add(self.yDataList, 1, wx.ALL | wx.EXPAND, 5)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_6, 0, wx.EXPAND, 0)

        self.offsetLabel = wx.StaticText(self, wx.ID_ANY, "offset", style=wx.ALIGN_RIGHT)
        sizer_6.Add(self.offsetLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.offsetTextCtrl = wx.TextCtrl(self, wx.ID_ANY, "-5", style=wx.TE_PROCESS_ENTER)
        sizer_6.Add(self.offsetTextCtrl, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(self.static_line_1, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)

        self.plotButton = wx.Button(self, wx.ID_ANY, "Plot")
        sizer_2.Add(self.plotButton, 0, wx.ALL, 5)

        self.resetButton = wx.Button(self, wx.ID_ANY, "Reset")
        sizer_2.Add(self.resetButton, 0, wx.ALL, 5)

        self.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.onEnter, self.offsetTextCtrl)
        self.Bind(wx.EVT_BUTTON, self.onPlot, self.plotButton)
        self.Bind(wx.EVT_BUTTON, self.onReset, self.resetButton)
        # end wxGlade
        self.Bind(wx.EVT_COMBOBOX, self._check, self.xDataCombo)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._check, self.yDataList)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self._check, self.yDataList)
        self.__customProperties()

    # USER CONFIGURATION CODE #################################################
    def __customProperties(self):
        """Custom Properties go here."""
        self.yDataList.InsertColumn(0, "Y data")
        self.offsetTextCtrl.SetValidator(TextValidator(FLOAT_ONLY, allowNeg=True))

        # Define tooltips.
        self.setToolTips(tooltips.plotpanel)

        # Testing Code. Comment or delete this block when finished.
        # self.yDataList.InsertStringItem(sys.maxint, "y1")
        # self.yDataList.InsertStringItem(sys.maxint, "y2")
        # self.yDataList.InsertStringItem(sys.maxint, "y3")
        # self.yDataList.InsertStringItem(sys.maxint, "y4")
        # self.yDataList.InsertStringItem(sys.maxint, "y5")
        # Initialize the sorter.
        # self.yDataList.makeIDM()
        # self.yDataList.initializeSorter()

        return

    def enableWidgets(self, on=True):
        """Enable or disable the widgets."""
        self.xDataCombo.Enable(on)
        self.yDataList.Enable(on)
        self.offsetTextCtrl.Enable(on)
        self.resetButton.Enable(on)
        self.plotButton.Enable(on)
        return

    def updateWidgets(self):
        """Enable or disable certain widgets depending upon what is selected in
        the tree and in the plotting widgets.
        """
        # selections: selected nodes in treeCtrl
        # fits:  only different fittings
        # refs:  data item ids ( can be calculation, fit, structure and dataset
        selections = self.treeCtrlMain.GetSelections()
        # Only proceed if we have compatible items selected from the tree.
        if not selections:
            self.enableWidgets(False)
            return
        self.enableWidgets(True)
        fits = dict.fromkeys(
            [self.treeCtrlMain.GetControlData(self.treeCtrlMain.GetFitRoot(sel)) for sel in selections]
        )
        refs = [self.treeCtrlMain.GetControlData(sel) for sel in selections]

        xdata = []
        # step is added if selections include type other than calculation
        for type in [self.treeCtrlMain.GetNodeType(sel) for sel in selections]:
            if type != "calculation":
                xdata.append("step")
                break

        # index is added if multiple selections are chosen from different fits
        if len(fits) > 1:
            xdata.append("index")

        for ref in refs:
            xdata.extend(ref.getXNames())

        for fit in fits:
            xdata.extend(fit.getMetaDataNames())
            # also can plot y against y so add yNames as well
            xdata.extend(fit.getYNames())

        # reduce
        xdata = list(set(xdata))

        # Make the parameter entries a bit more presentable.
        def _represent(mixedNames):
            vals = ["@%i" % item for item in mixedNames if isinstance(item, int)]
            others = [item for item in mixedNames if not isinstance(item, int)]
            vals.extend(others)
            numericStringSort(vals)
            return vals

        xvals = _represent(xdata)
        try:
            xvals.remove("rw")
        except ValueError:
            pass
        numericStringSort(xvals)

        # Fill the xDataCombo
        if self.xDataCombo.GetCount():
            current = self.xDataCombo.GetValue()
        else:
            current = None
        self.xDataCombo.Clear()
        for item in xvals:
            self.xDataCombo.Append(item)

        # Set default value for xDataCombo
        # Either keep the current plot value selected, select 'r', or the
        # first in the list.
        defaultOrders = ["r", "step", "index"]
        if current:
            defaultOrders.insert(0, current)
        for item in defaultOrders:
            if item in xvals:
                self.xDataCombo.SetValue(item)
                break
        else:
            self.xDataCombo.SetSelection(0)

        # Y-DATA is the common subset of all data id
        ydata = refs[0].getYNames()
        for ref in refs[1:]:
            for name in ydata[:]:
                if name not in ref.getYNames():
                    ydata.remove(name)

        yvals = _represent(ydata)

        # Fill the List
        self.yDataList.DeleteAllItems()
        for val in yvals:
            # self.yDataList.InsertItem(sys.maxsize, str(val)) #doesn't work for windows
            self.yDataList.InsertItem(100000, str(val))
        self.yDataList.makeIDM()
        self.yDataList.initializeSorter()
        if yvals:
            self.yDataList.Select(0)

        # self.prevSelectionType = selectiontype
        self._check(None)

        return

    def getSelectedYVals(self):
        """Get the y-values selected in the y-value ListCtrl."""
        yvals = []
        item = self.yDataList.GetFirstSelected()
        while item != -1:
            name = self.yDataList.GetItemText(item)
            yvals.append(name)
            item = self.yDataList.GetNextSelected(item)
        return yvals

    # EVENT CODE #############################################################
    def onPlot(self, event):  # wxGlade: PlotPanel.<event_handler>
        """Plot some stuff."""
        self._plot(event)
        return

    def _plot(self, event):
        """This function is not wrapped"""
        selections = self.treeCtrlMain.GetSelections()
        refs = [self.treeCtrlMain.GetControlData(node) for node in selections]
        xval = self.xDataCombo.GetValue()
        if xval[0] == "@":
            xval = int(xval[1:])
        temp = self.getSelectedYVals()
        # Clean up some formatting so the control can understand this.
        yvals = [int(par[1:]) for par in temp if par[0] == "@"]
        yvals.extend([val for val in temp if val[0] != "@"])
        offset = self.offsetTextCtrl.GetValue()
        try:
            offset = float(offset)
        except ValueError:  # offset can be empty string
            offset = 0.0

        self.mainFrame.control.plot(xval, yvals, refs, shift=offset, dry=(event is None))
        return

    def onEnter(self, event):
        """Reset plot."""
        self.onPlot(event)
        return

    def onReset(self, event):  # wxGlade: PlotPanel.<event_handler>
        """Reset everything."""
        self.offsetTextCtrl.SetValue("-5")
        self.refresh()
        return

    # Methods overloaded from PDFPanel
    def refresh(self):
        """Refresh this panel."""
        self.updateWidgets()
        return

    def _check(self, event):
        try:
            self._plot(None)
            self.plotButton.Enable()
        except ControlConfigError:
            self.plotButton.Disable()
