bl_info = {
    "name": "Dual View",
    "category": "Strip",
}

import bpy


class DualView(bpy.types.Operator):
    """Put selected strips in dual view"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "strip.dual_view"        # unique identifier for buttons and menu items to reference.
    bl_label = "Implement Dual View"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.

        # The original script
        stripCount = 1
        selection = [seq for seq in context.scene.sequence_editor.sequences if seq.select and seq.type not in ['SOUND','TRANSFORM']]
        for seq in selection:            
            bpy.ops.sequencer.select_all(action='DESELECT')
            context.scene.sequence_editor.active_strip = seq
            bpy.ops.sequencer.effect_strip_add(type = "TRANSFORM")
            active_seq = context.scene.sequence_editor.active_strip
            active_seq.scale_start_y = .5
            active_seq.blend_type = "OVER_DROP"
            if stripCount == 1:
                active_seq.name = "TopScreen"
                active_seq.scale_start_x = .75
                active_seq.translate_start_y = 25
            elif stripCount == 2:
                active_seq.name = "BottomScreen"
                active_seq.scale_start_x = .75
                active_seq.translate_start_y = -25
            elif stripCount == 3:
                active_seq.name = "TopCard"
                active_seq.scale_start_x = .5
                active_seq.translate_start_y = 25
            if stripCount == 4:
                active_seq.name = "BottomCard"
                active_seq.scale_start_x = .5
                active_seq.translate_start_y = -25
            stripCount += 1

        return {'FINISHED'}            # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(DualView)


def unregister():
    bpy.utils.unregister_class(DualView)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()