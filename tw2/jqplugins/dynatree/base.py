
import tw2.core as twc
import tw2.jquery.base as twjq_c
import defaults

dynatree_css = twjq_c.jQueryPluginCSSLink(
    name=defaults._dynatree_name_,
    version = defaults._dynatree_version_,
    modname = 'tw2.jqplugins.dynatree',
    subdir = 'skin-vista',
)
dynatree_js = twjq_c.jQueryPluginJSLink(
    name=defaults._dynatree_name_,
    version=defaults._dynatree_version_,
    variant='min',
    modname='tw2.jqplugins.dynatree',
    subdir = '',
)

__all__ = ['dynatree_js', 'dynatree_css']
