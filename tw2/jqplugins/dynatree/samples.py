"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import tw2.core as twc
from tw2.core.resources import encoder

from widgets import DynaTreeWidget


class DemoDynaTree(DynaTreeWidget):
    options = {
        'onActivate': twc.JSSymbol(
            src="""function(node) {
            alert("You activated " + node.data.title);
        }"""),
        'children': [
            {'title': "Item 1"},
            {'title': "Folder 2",
             'isFolder': True,
             'key': "folder2",
             'children': [
                 {'title': "Sub-item 2.1"},
                 {'title': "Sub-item 2.2"}
             ]
            },
            {'title': "Item 3"}
        ]
    }
