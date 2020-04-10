bl_info = {
    "name": "Add Eye Mesh",
    "author": "Parker Bourassa",
    "version": (1, 0),
    "blender": (2, 81, 0),
    "location": "View3D > Add > Mesh > Eye Mesh",
    "description": "Adds an eye mesh for scultping",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

import bpy
import bmesh
from bpy_extras.object_utils import AddObjectHelper

from bpy.props import (
    BoolProperty,
    BoolVectorProperty,
    EnumProperty,
    FloatProperty,
    FloatVectorProperty,
)


class MESH_OT_AddEyeMesh(bpy.types.Operator):
    """Add an eye mesh"""
    bl_idname = "mesh.eye_add"
    bl_label = "Add Eye Mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    size: bpy.props.FloatProperty(
        name="Scale",
        default=1
    )
            
    location: FloatVectorProperty(
        name="Location",
        subtype='TRANSLATION',
        default=(2,0,0)
    )
    rotation: FloatVectorProperty(
        name="Rotation",
        subtype='EULER',
        default=(1.5708,0,0)
    )

    def execute(self, context):

        #mirrored eye
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=self.size, 
            enter_editmode=False, 
            location=(-self.location.x, self.location.y, self.location.z), 
            rotation=(self.rotation.x, self.rotation.y, -self.rotation.z) 
            )
        
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=self.size, 
            enter_editmode=False, 
            location=self.location, 
            rotation=self.rotation 
            )
        
        #bpy.context.object.modifiers["Mirror"].mirror_object = bpy.data.objects["Camera"]

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(MESH_OT_AddEyeMesh.bl_idname, icon='MESH_UV_SPHERE')


def register():
    bpy.utils.register_class(MESH_OT_AddEyeMesh)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(MESH_OT_AddEyeMesh)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.mesh.eye_add()