import bpy

class OHCNewClipPanel(bpy.types.Panel):
    bl_label = "OHC New Clip"
    bl_idname = "RENDER_PT_OHCNewClip"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    newClipPath = bpy.props.StringProperty(name = "File Name:",description="The file you want to add",default="",maxlen=500,subtype='FILE_NAME')
    
    def draw(self, context):
        layout = self.layout
        
        render = context.render
        
        layout.label(text=" Add a clip:")
        row = layout.row()
        row.prop(self,"newClipPath")
        row.operator(self,"OHCNewClip.addClip")
        
def register():
    bpy.utils.register_class(OHCNewClipPanel)
    
def unregister():
    bpy.utils.unregister_class(OHCNewClipPanel)
    
if __name__ == "__main__":
    register()
        