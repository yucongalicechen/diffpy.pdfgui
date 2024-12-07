#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow, Dmitriy Bryndin
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.9.3 on Fri Jul 19 16:04:47 2019

import wx
import wx.grid

from diffpy.pdffit2 import is_element
from diffpy.pdfgui.control.controlerrors import TempControlSelectError
from diffpy.pdfgui.gui import phasepanelutils, tooltips
from diffpy.pdfgui.gui.insertrowsdialog import InsertRowsDialog
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui.wxextensions import wx12
from diffpy.pdfgui.gui.wxextensions.autowidthlabelsgrid import AutoWidthLabelsGrid
from diffpy.pdfgui.gui.wxextensions.textctrlutils import textCtrlAsGridCell
from diffpy.pdfgui.gui.wxextensions.validators import FLOAT_ONLY, TextValidator
from diffpy.structure import Atom
from diffpy.utils.wx import gridutils


class PhaseConfigurePanel(wx.Panel, PDFPanel):
    """Panel for configuring a phase.

    Data members:
        structure       -- reference to PDFStructure
        _focusedText    -- value of a cell or textctrl before it changes
        lConstraintsMap -- map of TextCtrl name to parameter name
        _row            -- row,    where rightclick occurred
        _col            -- column, where rightclick occurred
    """

    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: PhaseConfigurePanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SetFocus()

        sizerMain = wx.BoxSizer(wx.VERTICAL)

        sizerPanelName = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizerMain.Add(sizerPanelName, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        self.labelPanelName = wx.StaticText(self, wx.ID_ANY, "Phase Configuration")
        self.labelPanelName.SetFont(
            wx.Font(
                18,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD,
                0,
                "",
            )
        )
        sizerPanelName.Add(self.labelPanelName, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 5)

        sizerLatticeParameters = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizerMain.Add(sizerLatticeParameters, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        grid_sizer_3 = wx.FlexGridSizer(2, 6, 0, 0)
        sizerLatticeParameters.Add(grid_sizer_3, 1, wx.EXPAND, 0)

        self.labelA = wx.StaticText(self, wx.ID_ANY, "a")
        grid_sizer_3.Add(self.labelA, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlA = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlA, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelB = wx.StaticText(self, wx.ID_ANY, "b")
        grid_sizer_3.Add(self.labelB, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlB = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlB, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelC = wx.StaticText(self, wx.ID_ANY, "c")
        grid_sizer_3.Add(self.labelC, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlC = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlC, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelAlpha = wx.StaticText(self, wx.ID_ANY, "alpha")
        grid_sizer_3.Add(self.labelAlpha, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlAlpha = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlAlpha, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelBeta = wx.StaticText(self, wx.ID_ANY, "beta")
        grid_sizer_3.Add(self.labelBeta, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlBeta = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlBeta, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelGamma = wx.StaticText(self, wx.ID_ANY, "gamma")
        grid_sizer_3.Add(self.labelGamma, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlGamma = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_3.Add(self.textCtrlGamma, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        sizerAdditionalParameters = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizerMain.Add(sizerAdditionalParameters, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        grid_sizer_4 = wx.FlexGridSizer(3, 6, 0, 0)
        sizerAdditionalParameters.Add(grid_sizer_4, 1, wx.EXPAND, 0)

        self.labelScaleFactor = wx.StaticText(self, wx.ID_ANY, "Scale Factor")
        grid_sizer_4.Add(
            self.labelScaleFactor,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL,
            5,
        )

        self.textCtrlScaleFactor = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_4.Add(self.textCtrlScaleFactor, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        grid_sizer_4.Add((20, 10), 0, 0, 0)

        grid_sizer_4.Add((20, 10), 0, 0, 0)

        grid_sizer_4.Add((20, 10), 0, 0, 0)

        grid_sizer_4.Add((20, 10), 0, 0, 0)

        self.labelDelta1 = wx.StaticText(self, wx.ID_ANY, "delta1")
        grid_sizer_4.Add(self.labelDelta1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlDelta1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_4.Add(self.textCtrlDelta1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelDelta2 = wx.StaticText(self, wx.ID_ANY, "delta2")
        grid_sizer_4.Add(self.labelDelta2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlDelta2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_4.Add(self.textCtrlDelta2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelSpdiameter = wx.StaticText(self, wx.ID_ANY, "spdiameter")
        grid_sizer_4.Add(
            self.labelSpdiameter,
            0,
            wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL,
            5,
        )

        self.textCtrlSpdiameter = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_4.Add(self.textCtrlSpdiameter, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelSratio = wx.StaticText(self, wx.ID_ANY, "sratio")
        grid_sizer_4.Add(self.labelSratio, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlSratio = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_4.Add(self.textCtrlSratio, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelRcut = wx.StaticText(self, wx.ID_ANY, "rcut")
        grid_sizer_4.Add(self.labelRcut, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlRcut = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_4.Add(self.textCtrlRcut, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.labelStepcut = wx.StaticText(self, wx.ID_ANY, "stepcut")
        grid_sizer_4.Add(self.labelStepcut, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.textCtrlStepcut = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_4.Add(self.textCtrlStepcut, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        sizerAtoms = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.VERTICAL)
        sizerMain.Add(sizerAtoms, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerAtoms.Add(sizer_1, 0, wx.EXPAND, 0)

        self.labelIncludedPairs = wx.StaticText(self, wx.ID_ANY, "Included Pairs")
        sizer_1.Add(self.labelIncludedPairs, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.textCtrlIncludedPairs = wx.TextCtrl(self, wx.ID_ANY, "all-all")
        self.textCtrlIncludedPairs.SetMinSize((240, 25))
        sizer_1.Add(self.textCtrlIncludedPairs, 0, wx.ALL, 5)

        self.gridAtoms = AutoWidthLabelsGrid(self, wx.ID_ANY, size=(1, 1))
        self.gridAtoms.CreateGrid(0, 11)
        self.gridAtoms.EnableDragRowSize(0)
        self.gridAtoms.SetColLabelValue(0, "elem")
        self.gridAtoms.SetColLabelValue(1, "x")
        self.gridAtoms.SetColLabelValue(2, "y")
        self.gridAtoms.SetColLabelValue(3, "z")
        self.gridAtoms.SetColLabelValue(4, "u11")
        self.gridAtoms.SetColLabelValue(5, "u22")
        self.gridAtoms.SetColLabelValue(6, "u33")
        self.gridAtoms.SetColLabelValue(7, "u12")
        self.gridAtoms.SetColLabelValue(8, "u13")
        self.gridAtoms.SetColLabelValue(9, "u23")
        self.gridAtoms.SetColLabelValue(10, "occ")
        sizerAtoms.Add(self.gridAtoms, 1, wx.EXPAND, 0)

        self.SetSizer(sizerMain)
        sizerMain.Fit(self)

        self.Layout()

        self.Bind(wx.grid.EVT_GRID_CMD_CELL_CHANGED, self.onCellChange, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.onCellRightClick, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_EDITOR_SHOWN, self.onEditorShown, self.gridAtoms)
        self.Bind(
            wx.grid.EVT_GRID_CMD_LABEL_RIGHT_CLICK,
            self.onLabelRightClick,
            self.gridAtoms,
        )
        # end wxGlade
        self.__customProperties()

    # ########################################################################
    # Misc Methods

    def __customProperties(self):
        """Custom properties for the panel."""
        self.structure = None
        self.constraints = {}
        self.results = None
        self._row = 0
        self._col = 0
        self._focusedText = None
        self._selectedCells = []

        self.lAtomConstraints = [
            "x",
            "y",
            "z",
            "u11",
            "u22",
            "u33",
            "u12",
            "u13",
            "u23",
            "occ",
        ]
        # pdffit internal naming
        self.lConstraintsMap = {
            "textCtrlA": "lat(1)",
            "textCtrlB": "lat(2)",
            "textCtrlC": "lat(3)",
            "textCtrlAlpha": "lat(4)",
            "textCtrlBeta": "lat(5)",
            "textCtrlGamma": "lat(6)",
            "textCtrlScaleFactor": "pscale",
            "textCtrlDelta1": "delta1",
            "textCtrlDelta2": "delta2",
            "textCtrlSratio": "sratio",
            "textCtrlRcut": "rcut",
            "textCtrlStepcut": "stepcut",
            "textCtrlSpdiameter": "spdiameter",
        }

        # bind onSetFocus onKillFocus events to text controls
        for tname in self.lConstraintsMap:
            self.__dict__[tname].Bind(wx.EVT_SET_FOCUS, self.onSetFocus)
            self.__dict__[tname].Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)
            self.__dict__[tname].SetValidator(TextValidator(FLOAT_ONLY))
            self.__dict__[tname].Bind(wx.EVT_KEY_DOWN, self.onTextCtrlKey)

        self.textCtrlIncludedPairs.Bind(wx.EVT_SET_FOCUS, self.onSetFocus)
        self.textCtrlIncludedPairs.Bind(wx.EVT_KILL_FOCUS, self.onSelectedPairs)
        self.textCtrlIncludedPairs.Bind(wx.EVT_KEY_DOWN, self.onTextCtrlKey)

        # define tooltips
        self.setToolTips(tooltips.phasepanel)
        # make sure tooltips exist for all lConstraintsMap controls as
        # this is later assumed in restrictConstrainedParameters code
        for tname in self.lConstraintsMap:
            assert getattr(self, tname).GetToolTip() is not None

        # catch key events and apply them to the grid
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        return

    # Create the onTextCtrlKey event handler from textCtrlAsGridCell from
    # wxextensions.textctrlutils
    onTextCtrlKey = textCtrlAsGridCell

    def _cache(self):
        """Cache the current structure and constraints for future comparison."""
        pass

    __this_is_first_refresh = True

    def refresh(self):
        """Refreshes widgets on the panel."""
        phasepanelutils.refreshTextCtrls(self)
        pairs = self.structure.getSelectedPairs()
        self.textCtrlIncludedPairs.SetValue(pairs)
        phasepanelutils.refreshGrid(self)
        self.restrictConstrainedParameters()
        # wxpython 3.0 on Windows 7 prevents textCtrlA from receiving
        # left-click input focus and can be only focused with a Tab key.
        # This only happens for the first input, the text control behaves
        # normally after receiving focus once.
        # Workaround: do explicit focus here for the first rendering.
        if self.__this_is_first_refresh:
            self.__this_is_first_refresh = False
            focusowner = self.textCtrlA.FindFocus()
            wx.CallAfter(self.textCtrlA.SetFocus)
            if focusowner is not None:
                wx.CallAfter(focusowner.SetFocus)
        return

    def restrictConstrainedParameters(self):
        """Set 'read-only' boxes that correspond to constrained parameters."""

        self.setToolTips(tooltips.phasepanel)
        self.textCtrlA.DefaultStyle.BackgroundColour

        # First the TextCtrls
        for key, var in self.lConstraintsMap.items():
            textCtrl = getattr(self, key)
            if var in self.constraints:
                textCtrl.SetEditable(False)
                textCtrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))
                tt = textCtrl.GetToolTip()
                tt.SetTip(self.constraints[var].formula)
            else:
                textCtrl.SetEditable(True)
                # textCtrl.SetBackgroundColour(txtbg)
                textCtrl.SetBackgroundColour(wx.WHITE)

        # Now the grid
        rows = self.gridAtoms.GetNumberRows()
        cols = self.gridAtoms.GetNumberCols()

        for i in range(rows):
            for j in range(1, cols):
                var = self.lAtomConstraints[j - 1]
                var += "(%i)" % (i + 1)
                if var in self.constraints:
                    self.gridAtoms.SetReadOnly(i, j, True)
                    self.gridAtoms.SetCellBackgroundColour(
                        i, j, wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT)
                    )
                else:
                    self.gridAtoms.SetReadOnly(i, j, False)
                    self.gridAtoms.SetCellBackgroundColour(i, j, wx.NullColour)

        return

    def applyTextCtrlChange(self, id, value):
        """Update a structure according to a change in a TextCtrl.

        id      --  textctrl id
        value   --  new value
        """
        if self.structure is None:
            return

        try:
            value = float(value)
            if id == self.textCtrlA.GetId():
                self.structure.lattice.setLatPar(a=value)
            elif id == self.textCtrlB.GetId():
                self.structure.lattice.setLatPar(b=value)
            elif id == self.textCtrlC.GetId():
                self.structure.lattice.setLatPar(c=value)
            elif id == self.textCtrlAlpha.GetId():
                self.structure.lattice.setLatPar(alpha=value)
            elif id == self.textCtrlBeta.GetId():
                self.structure.lattice.setLatPar(beta=value)
            elif id == self.textCtrlGamma.GetId():
                self.structure.lattice.setLatPar(gamma=value)
            elif id == self.textCtrlScaleFactor.GetId():
                self.structure.pdffit["scale"] = value
            elif id == self.textCtrlDelta1.GetId():
                self.structure.pdffit["delta1"] = value
            elif id == self.textCtrlDelta2.GetId():
                self.structure.pdffit["delta2"] = value
            elif id == self.textCtrlSratio.GetId():
                self.structure.pdffit["sratio"] = value
            elif id == self.textCtrlRcut.GetId():
                self.structure.pdffit["rcut"] = value
            elif id == self.textCtrlStepcut.GetId():
                self.structure.pdffit["stepcut"] = value
            elif id == self.textCtrlSpdiameter.GetId():
                self.structure.pdffit["spdiameter"] = value

            return value

        except Exception:
            return None

    def applyCellChange(self, i, j, value):
        """Update an atom according to a change in a cell.

        i       --  cell position
        j       --  cell position
        value   --  new value
        """
        if not self.mainFrame or self.structure is None:
            return

        # The element name
        if j == 0:
            value = value.title()
            if not is_element(value):
                return
            self.structure[i].element = value  # element
            return value

        # Other entries
        # ignore the change if the value is not valid
        try:
            value = float(value)
            if value == "":
                value = 0.0
            if j == 1:
                self.structure[i].xyz[0] = value  # x
            elif j == 2:
                self.structure[i].xyz[1] = value  # y
            elif j == 3:
                self.structure[i].xyz[2] = value  # z
            elif j == 4:
                self.structure[i].U[0, 0] = value  # U(1,1)
            elif j == 5:
                self.structure[i].U[1, 1] = value  # U(2,2)
            elif j == 6:
                self.structure[i].U[2, 2] = value  # U(3,3)
            elif j == 7:
                self.structure[i].U[0, 1] = self.structure[i].U[1, 0] = value  # U(1,2)
            elif j == 8:
                self.structure[i].U[0, 2] = self.structure[i].U[2, 0] = value  # U(1,3)
            elif j == 9:
                self.structure[i].U[1, 2] = self.structure[i].U[2, 1] = value  # U(2,3)
            elif j == 10:
                self.structure[i].occupancy = value  # occupancy

            self.mainFrame.needsSave()
            return value

        except ValueError:
            return

    # ########################################################################
    # Event Handlers

    # TextCtrl Events
    def onSetFocus(self, event):
        """Saves a TextCtrl value, to be compared in onKillFocus later."""
        self._focusedText = event.GetEventObject().GetValue()
        event.Skip()
        return

    def onKillFocus(self, event):
        """Check value of TextCtrl and update structure if necessary."""
        if not self.mainFrame:
            return
        textctrl = event.GetEventObject()
        value = textctrl.GetValue()
        if value != self._focusedText:
            self.applyTextCtrlChange(textctrl.GetId(), value)
            phasepanelutils.refreshTextCtrls(self)
            self.mainFrame.needsSave()
        self._focusedText = None
        event.Skip()
        return

    def onSelectedPairs(self, event):
        """Check to see if the value of the selected pairs is valid."""
        if not self.mainFrame:
            return
        value = self.textCtrlIncludedPairs.GetValue()
        self.structure.setSelectedPairs(value)
        value = self.structure.getSelectedPairs()
        self.textCtrlIncludedPairs.SetValue(value)
        event.Skip()
        return

    # Grid Events
    def onLabelRightClick(self, event):  # wxGlade: PhaseConfigurePanel.<event_handler>
        """Bring up right-click menu."""
        if self.structure is not None:
            dx = dy = 0
            if event.GetRow() == -1:
                dy = self.gridAtoms.GetGridCornerLabelWindow().GetSize().y
            if event.GetCol() == -1:
                dx = self.gridAtoms.GetGridCornerLabelWindow().GetSize().x

            # do not popup menu if the whole grid is set to read only
            if len(self.structure) == 0:
                self.popupMenu(
                    self.gridAtoms,
                    event.GetPosition().x - dx,
                    event.GetPosition().y - dy,
                )
        event.Skip()
        return

    def onCellRightClick(self, event):  # wxGlade: PhaseConfigurePanel.<event_handler>
        """Bring up right-click menu."""
        self._row = event.GetRow()
        self._col = event.GetCol()

        # If the right-clicked node is not part of a group, then make sure that
        # it is the only selected cell.
        append = False
        r = self._row
        c = self._col
        if self.gridAtoms.IsInSelection(r, c):
            append = True
        self.gridAtoms.SelectBlock(r, c, r, c, append)

        self.popupMenu(self.gridAtoms, event.GetPosition().x, event.GetPosition().y)
        event.Skip()
        return

    def onEditorShown(self, event):  # wxGlade: PhaseConfigurePanel.<event_handler>
        """Capture the focused text when the grid editor is shown."""
        i = event.GetRow()
        j = event.GetCol()
        self._focusedText = self.gridAtoms.GetCellValue(i, j)
        # self._selectedCells = gridutils.getSelectedCells(self.gridAtoms)
        # TODO: temporary show the error message for control-select.
        try:
            self._selectedCells = gridutils.getSelectedCells(self.gridAtoms)
        except TypeError:
            raise TempControlSelectError("controlselecterror")
        return

    def onCellChange(self, event):  # wxGlade: PhaseConfigurePanel.<event_handler>
        """Update focused and selected text when a cell changes."""
        # NOTE: be careful with refresh(). It calls Grid.AutoSizeColumns, which
        # creates a EVT_GRID_CMD_CELL_CHANGED event, which causes a recursion
        # loop.
        i = event.GetRow()
        j = event.GetCol()

        value = self.gridAtoms.GetCellValue(i, j)
        while (i, j) in self._selectedCells:
            self._selectedCells.remove((i, j))
        # We need the edited cell to be at the front of the list
        self._selectedCells.insert(0, (i, j))
        self.fillCells(value)
        self._focusedText = None
        return

    def fillCells(self, value):
        """Fill cells with a given value.

        value       --  string value to place into cells

        This uses the member variable _selectedCells, a list of (i,j) tuples for
        the selected cells.
        """
        for i, j in self._selectedCells:
            if not self.gridAtoms.IsReadOnly(i, j):
                # Get the last valid text from the cell. For the cell that triggered
                # this method, that is the _focusedText, for other cells it is the
                # value returned by GetCellValue
                oldvalue = self._focusedText or self.gridAtoms.GetCellValue(i, j)
                self._focusedText = None
                newvalue = self.applyCellChange(i, j, value)
                # print i, j, value, oldvalue, newvalue
                if newvalue is None:
                    newvalue = oldvalue
                self.gridAtoms.SetCellValue(i, j, str(newvalue))

        gridutils.quickResizeColumns(self.gridAtoms, self._selectedCells)
        return

    def onKey(self, event):
        """Catch key events in the panel."""
        key = event.GetKeyCode()

        # Select All
        # Ctrl A
        if event.ControlDown() and key == 65:
            rows = self.gridAtoms.GetNumberRows()
            cols = self.gridAtoms.GetNumberCols()
            self.gridAtoms.SelectBlock(0, 0, rows, cols)

        # context menu key
        elif key == wx.WXK_MENU:
            self.popupMenu(self.gridAtoms, event.GetPosition().x, event.GetPosition().y)

        # Vim-like search for atom selection
        elif key == 47:
            self.onPopupSelect(event)

        # Delete an atom
        # Delete
        elif key == 127:
            selected = self.gridAtoms.GetSelectedRows()
            if selected:
                self.structure.deleteAtoms(selected)
                self.refresh()
                self.mainFrame.needsSave()

        # Ctrl -
        elif event.ControlDown() and key == 45:
            indices = gridutils.getSelectionRows(self.gridAtoms)
            self.structure.deleteAtoms(indices)
            self.refresh()
            self.mainFrame.needsSave()

        # Append an atom
        # Ctrl + or Ctrl =
        elif event.ControlDown() and (key == 61 or key == 43):
            indices = gridutils.getSelectionRows(self.gridAtoms)
            pos = 0
            if indices:
                pos = 1 + indices[-1]
            elif self.structure:
                pos = len(self.structure)
            # insert "rows" atoms into the structure
            atoms = [_defaultNewAtom()]
            self.structure.insertAtoms(pos, atoms)
            self.refresh()
            self.mainFrame.needsSave()

        else:
            event.Skip()

        return

    # ########################################################################
    # Grid popup menu and handlers

    def popupMenu(self, window, x, y):
        """Creates the popup menu

        window  --  window, where to popup a menu
        x       --  x coordinate
        y       --  y coordinate
        """
        # only do this part the first time so the events are only bound once
        if not hasattr(self, "insertID"):
            self.insertID = wx12.NewIdRef()
            self.deleteID = wx12.NewIdRef()
            self.selectID = wx12.NewIdRef()
            self.copyID = wx12.NewIdRef()
            self.pasteID = wx12.NewIdRef()
            self.supercellID = wx12.NewIdRef()
            self.spaceGroupID = wx12.NewIdRef()

            self.Bind(wx.EVT_MENU, self.onPopupInsert, id=self.insertID)
            self.Bind(wx.EVT_MENU, self.onPopupDelete, id=self.deleteID)
            self.Bind(wx.EVT_MENU, self.onPopupSelect, id=self.selectID)
            self.Bind(wx.EVT_MENU, self.onPopupCopy, id=self.copyID)
            self.Bind(wx.EVT_MENU, self.onPopupPaste, id=self.pasteID)
            self.Bind(wx.EVT_MENU, self.onPopupSupercell, id=self.supercellID)
            self.Bind(wx.EVT_MENU, self.onPopupSpaceGroup, id=self.spaceGroupID)

        # make a menu
        menu = wx.Menu()

        # add some other items
        menu.Append(self.insertID, "&Insert atoms...")
        menu.Append(self.deleteID, "&Delete atoms")
        menu.AppendSeparator()
        menu.Append(self.selectID, "Select &atoms...")
        menu.Append(self.copyID, "&Copy")
        menu.Append(self.pasteID, "&Paste")
        menu.AppendSeparator()
        menu.Append(self.supercellID, "Create supercell...")
        menu.Append(self.spaceGroupID, "Expand space group...")

        # Disable some items if there are no atoms selected
        indices = gridutils.getSelectionRows(self.gridAtoms)
        if not indices:
            menu.Enable(self.deleteID, False)
            menu.Enable(self.spaceGroupID, False)

        # Disable some items if there is no structure
        if self.structure is None or len(self.structure) == 0:
            menu.Enable(self.deleteID, False)
            menu.Enable(self.supercellID, False)
            menu.Enable(self.spaceGroupID, False)

        # Check for copy/paste
        if not phasepanelutils.canCopySelectedCells(self):
            menu.Enable(self.copyID, False)
        if not phasepanelutils.canPasteIntoCells(self):
            menu.Enable(self.pasteID, False)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        window.PopupMenu(menu, wx.Point(x, y))
        menu.Destroy()
        return

    def onPopupInsert(self, event):
        """Adds rows to the grid."""
        if self.structure is not None:
            dlg = InsertRowsDialog(self)
            if dlg.ShowModal() == wx.ID_OK:
                rows = dlg.spin_ctrl_Rows.GetValue()

                if len(self.structure) == 0:
                    self._row = 0
                elif dlg.radio_box_where.GetSelection() == 1:  # if selected "below"
                    self._row += 1

                # insert "rows" atoms into the structure
                atoms = [_defaultNewAtom() for i in range(rows)]
                self.structure.insertAtoms(self._row, atoms)
                self.refresh()
                self.mainFrame.needsSave()

                # Highlight the elements of the new rows so that they can be
                # changed by the user.
                self.gridAtoms.SetFocus()
                self.gridAtoms.SelectBlock(self._row, 0, self._row + len(atoms) - 1, 0)
                self.gridAtoms.SetGridCursor(self._row, 0)

            dlg.Destroy()
        return

    def onPopupDelete(self, event):
        """Deletes the row under mouse pointer from the grid."""
        if self.structure is not None:
            indices = gridutils.getSelectionRows(self.gridAtoms)
            self.structure.deleteAtoms(indices)
            self.refresh()
            self.mainFrame.needsSave()
        return

    def onPopupSelect(self, event):
        """Limit cell selection to specified atom selection string."""
        phasepanelutils.showSelectAtomsDialog(self)
        return

    def onPopupCopy(self, event):
        """Copy selected cells."""
        phasepanelutils.copySelectedCells(self)
        return

    def onPopupPaste(self, event):
        """Paste previously copied cells."""
        phasepanelutils.pasteIntoCells(self)
        return

    def onPopupSupercell(self, event):
        """Create a supercell with the supercell dialog."""
        from diffpy.pdfgui.gui.supercelldialog import SupercellDialog

        if self.structure is not None:
            dlg = SupercellDialog(self)
            if dlg.ShowModal() == wx.ID_OK:
                mno = dlg.getMNO()
                self.structure.expandSuperCell(mno)
                self.refresh()
                self.mainFrame.needsSave()
            dlg.Destroy()
        return

    def onPopupSpaceGroup(self, event):
        """Create a supercell with the supercell dialog."""
        from diffpy.pdfgui.gui.sgstructuredialog import SGStructureDialog

        if self.structure is not None:

            indices = gridutils.getSelectionRows(self.gridAtoms)
            dlg = SGStructureDialog(self)
            dlg.mainFrame = self.mainFrame
            dlg.indices = indices
            dlg.setStructure(self.structure)
            if dlg.ShowModal() == wx.ID_OK:
                spcgrp = dlg.getSpaceGroup()
                offset = dlg.getOffset()
                self.structure.expandAsymmetricUnit(spcgrp, indices, offset)
                self.refresh()
                self.mainFrame.needsSave()
            dlg.Destroy()
        return


# end of class PhaseConfigurePanel

# Local helpers --------------------------------------------------------------


def _defaultNewAtom():
    """Create new atom instance with non-zero initial U."""
    uii = 0.003
    rv = Atom("C", [0.0, 0.0, 0.0], U=[[uii, 0, 0], [0, uii, 0], [0, 0, uii]])
    return rv
