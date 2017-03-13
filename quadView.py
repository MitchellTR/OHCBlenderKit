bl_info = {
    "name": "Quad View",
    "category": "Strip",
}

import bpy


class QuadView(bpy.types.Operator):
    """Put selected strips in quad view"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "strip.quad_view"        # unique identifier for buttons and menu items to reference.
    bl_label = "Implement Quad View"         # display name in the interface.
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
            active_seq.scale_start_x = .5
            active_seq.scale_start_y = .5
            active_seq.blend_type = "OVER_DROP"
            if stripCount == 1:
                active_seq.name = "TopLeftScreen"
                active_seq.translate_start_x = -25
                active_seq.translate_start_y = 25
            elif stripCount == 2:
                active_seq.name = "TopRightScreen"
                active_seq.translate_start_x = 25
                active_seq.translate_start_y = 25
            elif stripCount == 3:
                active_seq.name = "BottomLeftScreen"
                active_seq.translate_start_x = -25
                active_seq.translate_start_y = -25
            if stripCount == 4:
                active_seq.name = "TopLeftCard"
                active_seq.translate_start_x = -25
                active_seq.translate_start_y = 25
            elif stripCount == 5:
                active_seq.name = "TopRightCard"
                active_seq.translate_start_x = 25
                active_seq.translate_start_y = 25
            elif stripCount == 6:
                active_seq.name = "BottomLeftCard"
                active_seq.translate_start_x = -25
                active_seq.translate_start_y = -25
            stripCount += 1

        return {'FINISHED'}            # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(QuadView)


def unregister():
    bpy.utils.unregister_class(QuadView)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()