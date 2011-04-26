


from tw2.core.resources import encoder
import tw2.core as twc

import tw2.jquery
import tw2.jqplugins.ui.base as tw2_jq_ui

import base

class DynaTreeWidget(tw2_jq_ui.JQueryUIWidget):
    resources = [
        tw2.jquery.jquery_js,
        tw2_jq_ui.jquery_ui_js, tw2_jq_ui.jquery_ui_css,
        base.dynatree_js, base.dynatree_css,
    ]
    template = "tw2.jqplugins.dynatree.templates.dynatree"

    options = twc.Param("Configuration options to pass to dynatree", default={})

    def prepare(self):
        self._options = encoder.encode(self.options)
        super(DynaTreeWidget, self).prepare()
