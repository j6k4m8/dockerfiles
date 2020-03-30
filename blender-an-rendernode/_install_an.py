import bpy
bpy.ops.preferences.addon_install(filepath='/animation_nodes.zip')
bpy.ops.wm.addon_enable(module='animation_nodes')
bpy.ops.wm.save_userpref()
