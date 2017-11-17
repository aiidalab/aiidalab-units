from __future__ import division
import ipywidgets as ipw
import ase
from ase.units import *


def get_start_widget(appbase, jupbase):
    
    def on_drop_changed(c):
        global factor
        lu, ru = drop.value.split(" <=> ")
        left.description = lu
        right.description = ru
        factor = eval("(%s) / (%s)"%(lu, ru))
        on_left_changed(None)

    
    def on_left_changed(c):
        right.value = left.value * factor

    def on_right_changed(c):
        left.value = right.value / factor

    left = ipw.FloatText(value=1.0)
    left.observe(on_left_changed, names="value")
    right = ipw.FloatText()
    right.observe(on_right_changed, names="value")
    
    options = ['Hartree <=> eV', 'Hartree <=> kcal/mol', 'Bohr <=> Angstrom']
    drop = ipw.Dropdown(options=options)
    drop.observe(on_drop_changed)
    
    on_drop_changed(None)
    
    return ipw.HBox([drop, left, right])

#EOF
