bl_info = {
    "name": "Single View",
    "category": "Strip",
}

import bpy


class SingleView(bpy.types.Operator):
    """Put selected strips in single view"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "strip.single_view"        # unique identifier for buttons and menu items to reference.
    bl_label = "Implement Single View"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.

        # The original script
        stripCount = 1
        selection = [seq for seq in context.scene.sequence_editor.sequences if seq.select and seq.type not in ['SOUND','TRANSFORM']]
        for seq in selection:            
            bpy.ops.sequencer.select_all(action='DESELECT')
            context.scene.sequence_editor.active_strip = seq
            if stripCount == 2:
                bpy.ops.sequencer.effect_strip_add(type = "TRANSFORM")
                active_seq = context.scene.sequence_editor.active_strip
                active_seq.blend_type = "OVER_DROP"
                active_seq.name = "PlayerCard"
            stripCount += 1

        return {'FINISHED'}            # this lets blender know the operator finished successfully.

def register():
    bpy.utils.register_class(SingleView)


def unregister():
    bpy.utils.unregister_class(SingleView)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()