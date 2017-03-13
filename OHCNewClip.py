bl_info = {
    "name": "OHC New Clip",
    "category": "Strip",
}

import bpy

class OHCNewClip(bpy.types.Operator):
    """Add a clip at frame 1, draw waveforms and build 50% proxy"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "strip.ohc_new_clip"        # unique identifier for buttons and menu items to reference.
    bl_label = "OHC New Clip"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.

        # The original script
        bpy.ops.sequencer.movie_strip_add(filepath="E:\\video\\2017-03-07 15-32-18.mp4")
        selection = [seq for seq in context.scene.sequence_editor.sequences if seq.select]
        for seq in selection:
            if seq.type == 'SOUND':
                bpy.data.scenes['Scene'].sequence_editor.sequences_all[seq.name].show_waveform = True
            else:
                bpy.data.scenes['Scene'].sequence_editor.sequences_all[seq.name].use_proxy = True
        
        return {'FINISHED'}            # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(OHCNewClip)


def unregister():
    bpy.utils.unregister_class(OHCNewClip)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()