<%namespace name="tw" module="tw2.core.mako_util"/>
<div>
<div ${tw.attrs(attrs=w.attrs)}></div>
<script type="text/javascript">
$(document).ready(function(){
   $("#${w.selector}").dynatree(${w._options});
});
</script>
</div>
