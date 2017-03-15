
import bpy

class OHCNewClip(bpy.types.Operator):
    """Add a clip at frame 1, draw waveforms and build 50% proxy"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "strip.ohc_new_clip"        # unique identifier for buttons and menu items to reference.
    bl_label = "OHC New Clip"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    newClipPath = bpy.props.StringProperty(name = "File Name:",description="The file you want to add",default="",maxlen=500,subtype='FILE_NAME')
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self,"newClipPath")
        row.operator("strip.ohc_new_clip",text="Add Clip")

    def execute(self, context):        # execute() is called by blender when running the operator.
        # The original script
        bpy.ops.sequencer.movie_strip_add(filepath="Users/toddmitchell/Movies/2017-02-07 16-37-19.mp4")
        selection = [seq for seq in context.scene.sequence_editor.sequences if seq.select]
        for seq in selection:
            if seq.type == 'SOUND':
                bpy.data.scenes['Scene'].sequence_editor.sequences_all[seq.name].show_waveform = True
            else:
                bpy.data.scenes['Scene'].sequence_editor.sequences_all[seq.name].use_proxy = True
                bpy.data.scenes['Scene'].sequence_editor.sequences_all[seq.name].proxy.build_25 = False
                bpy.data.scenes['Scene'].sequence_editor.sequences_all[seq.name].proxy.build_50 = True
                #bpy.ops.clip.rebuild_proxy()
                # Make a copy of the current context.
                ctx = bpy.context.copy()
                # Find the right area to override
                for area in bpy.context.screen.areas:
                    if area.type == 'CLIP_EDITOR':
                        # Override the area
                        ctx['area'] = area
                        # Proceed with operator
                        bpy.ops.clip.rebuild_proxy()
        
        return {'FINISHED'}            # this lets blender know the operator finished successfully.

    bpy.utils.register_class(OHCNewClip)

def unregister():
    bpy.utils.unregister_class(OHCNewClip)
    
# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()