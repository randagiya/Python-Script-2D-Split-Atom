import bpy
import math
from bpy import context, data, ops
from numpy import random
i=0
x=0
y=0
z=0
j=30
a_d = 0
b_d = 0
c_d = 0
i_d = 0
bpy.ops.object.select_all(action="SELECT")
objects_to_keep = ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8"]
for obj in bpy.context.selected_objects:
    if obj.name in objects_to_keep:
        obj.select_set(False)
        
bpy.ops.object.delete(use_global=False, confirm=False)

def atom(x,y,z):
    colo = random.randint(4)
    #ungu
    if colo == 1 : 
        red = 0.5
        green = 0
        blue = 0.5
        alp = 1
        color = (red, green, blue, alp)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(x,y,z))
        objek_atom = bpy.context.active_object
        objek_atom.name = "atom"
        material = bpy.data.materials.new("random_material")
        material.diffuse_color = color
        objek_atom.data.materials.append(material)
        bpy.ops.object.shade_smooth()
    #biru
    elif colo == 2:
        red = 0
        green = 0 
        blue = 1
        alp = 1
        color = (red, green, blue, alp)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(x,y,z))
        objek_atom = bpy.context.active_object
        objek_atom.name = "atom"
        material = bpy.data.materials.new("random_material")
        material.diffuse_color = color
        objek_atom.data.materials.append(material)
        bpy.ops.object.shade_smooth()
    #merah
    elif colo == 3 :
        red = 1
        green = 0.0 
        blue = 0
        alp = 1
        color = (red, green, blue, alp)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(x,y,z))
        objek_atom = bpy.context.active_object
        objek_atom.name = "atom"
        material = bpy.data.materials.new("random_material")
        material.diffuse_color = color
        objek_atom.data.materials.append(material)
        bpy.ops.object.shade_smooth()

def atom_merah(x,y,z,roy,loz,chos,star):
    red = 1
    green = 0.0 
    blue = 0
    alp = 1
    color = (red, green, blue, alp)
    co_ekor = ()
    
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(x, y, z))
    objek_atom = bpy.context.active_object
    if chos == 1 :
        sembu(objek_atom,1,100)
    anim_mer(x,y,z,star)
    objek_atom.name = "atom"
    material = bpy.data.materials.new("random_material")
    material.diffuse_color = color
    objek_atom.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    
    bpy.ops.mesh.primitive_cone_add(vertices=32, radius1=1.0, radius2=0.0, depth=6.0, 
    align='WORLD', end_fill_type='NGON', location=(x-4.5, y, z+loz), rotation=(0, 4.712+roy, 0))
    cone = bpy.context.active_object
    if chos == 1 :
        sembu(cone,1,99)
    mat = bpy.data.materials.new(name="New_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    teximage = mat.node_tree.nodes.new("ShaderNodeTexImage")
    teximage.image = bpy.data.images.load("D:\\texture_ekor2.jpg")
    mat.node_tree.links.new(bsdf.inputs['Base Color'], teximage.outputs['Color'])
    
    bsdf.inputs['Alpha'].default_value = 0.2
    
    ob = bpy.context.view_layer.objects.active
    bpy.ops.object.shade_smooth()
    if ob.data.materials:
        ob.data.materials[0] = mat
    else:
        ob.data.materials.append(mat)
    bpy.context.view_layer.objects.active.select_set(False)
    
            
def sembu(obj,disappear,reappear):
    cone = obj
    frame_disappear = disappear
    frame_reappear = reappear
    cone.hide_viewport = True
    cone.keyframe_insert(data_path="hide_viewport", frame=frame_disappear - 1)
    cone.keyframe_insert(data_path="hide_viewport", frame=frame_disappear)
    cone.hide_viewport = False
    cone.keyframe_insert(data_path="hide_viewport", frame=frame_reappear - 1)
    cone.keyframe_insert(data_path="hide_viewport", frame=frame_reappear)
    
def ledak(x,y,z):
    verts=[
    (0+x,1.75+y,z),(1.1+x,2.5+y,z),(1.29+x,2.74+y,z),(1.2+x,2.9+y,z),(0.64+x,3.15+y,z),(1.3+x,3.25+y,z),(1.49+x,3.38+y,z),(1.48+x,3.5+y,z), #8
    (0.669+x,4.51+y,z),(1.8+x,4+y,z),(1.9+x,4.05+y,z),(1.95+x,4.15+y,z),(1.95+x,5+y,z),(2.5+x,4.09+y,z),(2.6+x,4.04+y,z),(2.7+x,4.09+y,z), #16
    (3.16+x,4.87+y,z),(3.2+x,4.1+y,z),(3.25+x,4+y,z),(3.375+x,3.962+y,z),(4.52+x,4.58+y,z),(3.73+x,3.53+y,z),(3.73+x,3.4+y,z),(3.86+x,3.32+y,z), #24
    (4.57+x,3.23+y,z),(3.88+x,2.88+y,z),(3.81+x,2.78+y,z),(3.86+x,2.63+y,z),(4.89+x,1.89+y,z),(3.62+x,2.16+y,z),(3.53+x,2.12+y,z),(3.49+x,2.03+y,z), #32
    (3.71+x,1.26+y,z),(3.1+x,1.74+y,z),(3+x,1.76+y,z),(3+x,1.76+y,z),(2.9+x,1.7+y,z),(2.625+x,0.4+y,z),(2.35+x,1.65+y,z),(2.25+x,1.74+y,z), #40
    (2.07+x,1.68+y,z),(1.565+x,1.23+y,z),(1.7+x,1.85+y,z),(1.65+x,2.03+y,z),(1.42+x,2.1+y,z)] #45

    faces=[(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,0)]

    new_mesh=bpy.data.meshes.new("titik") 
    new_mesh.from_pydata(verts,[],faces) 
    new_mesh.update()

    ob = bpy.data.objects.new("titik", new_mesh)

    mat = bpy.data.materials.new(name="New_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    teximage = mat.node_tree.nodes.new("ShaderNodeTexImage")
    teximage.image = bpy.data.images.load("D:\\texture_ledakan3.jpg")
    mat.node_tree.links.new(bsdf.inputs['Base Color'], teximage.outputs['Color'])


    bpy.ops.object.shade_smooth()
    if ob.data.materials:
        ob.data.materials[0] = mat
    else:
        ob.data.materials.append(mat)

    bpy.context.collection.objects.link(ob)

    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)

    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0.3, -0.3, 0.5)})

    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.uv.select_all(action='SELECT')
    bpy.ops.uv.pack_islands(margin=0.001)

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.shade_smooth()
    
    rotation_angle_degrees = 90
    rotation_angle_radians = math.radians(rotation_angle_degrees)
    ob.rotation_euler = (rotation_angle_radians, 0, 0)
    
    scale_factor = 1.5
    ob.scale = (scale_factor, scale_factor, scale_factor)
    
    anim(0,0)
    
def anim(scale_f,anim_du):
    if scale_f == 0:
        scale_factor = 1.5 
    if anim_du == 0:
        animation_duration = 100
          
    obj = bpy.context.active_object
    animate_scaling(obj, scale_factor, animation_duration)
    
def animate_scaling(obj, scale_factor, animation_duration):
   # Set the initial scale of the object
    obj.scale = (1.0, 1.0, 1.0)

    # Set keyframes for the scale properties at frame 0
    obj.scale.x = 1.0
    obj.scale.y = 1.0
    obj.scale.z = 1.0
    obj.keyframe_insert(data_path="scale", frame=0)

    # Set keyframes for the scale properties at the animation_duration (in frames)
    obj.scale.x = scale_factor
    obj.scale.y = scale_factor
    obj.scale.z = scale_factor
    obj.keyframe_insert(data_path="scale", frame=animation_duration)
    
def animate_movement(obj, start_pos, end_pos, animation_duration, start_frame):
    for frame in range(start_frame, start_frame + animation_duration):
        # Calculate the position for the current frame
        t = (frame - start_frame) / animation_duration
        frame_pos = [start + (end - start) * t for start, end in zip(start_pos, end_pos)]

        # Set the position of the object for the current frame
        obj.location = frame_pos
        obj.keyframe_insert(data_path="location", frame=frame)
        
def anim_mer(x,y,z,star):
    obj = bpy.context.active_object
    animation_duration = 100
    start_pos = (x, y, z)
    end_pos = (x+1.5, y, z)
    start_frame = star
    animate_movement(obj, start_pos, end_pos, animation_duration, start_frame) 

    
def plane(x,y,z,ro,si):
    rotat = math.radians(ro)
    bpy.ops.mesh.primitive_plane_add(size=si, enter_editmode=False, location=(x, y, z),rotation=(rotat,0,0))

    plane_obj = bpy.context.active_object

    plane_obj.name = "My_Plane"

    plane_mat = bpy.data.materials.new(name="Plane_Material")
    plane_obj.data.materials.append(plane_mat)
    
    plane_obj.scale.x = 3
    plane_obj.scale.y = 2
    plane_obj.scale.z = 1

    plane_mat.use_nodes = False
    plane_mat.diffuse_color = (0.8, 0.8, 0.8, 1.0) 
    
    bpy.ops.object.shade_smooth()
    
def sun(x,y,z):
    bpy.ops.object.light_add(type='SUN', align='WORLD', location=(x, y, z))

    sun_lamp = bpy.context.active_object

    sun_lamp.name = "Sun_Lamp"

    sun_lamp.data.energy = 15.0
    sun_lamp.data.angle = 2 
    sun_lamp.data.specular_factor = 0.6

#    sun_lamp.data.shadow_soft_size = 0.1
    sun_lamp.data.use_shadow = False

    sun_lamp.hide_viewport = False
    sun_lamp.hide_render = False
    
def camera(x,y,z):
    camera_x = x
    camera_y = y
    camera_z = z 

    camera_rot_x = math.radians(90)
    camera_rot_y = math.radians(0)
    camera_rot_z = math.radians(0)

    bpy.ops.object.camera_add(location=(camera_x, camera_y, camera_z), rotation=(camera_rot_x, camera_rot_y, camera_rot_z))

    camera_obj = bpy.context.active_object

    camera_obj.name = "Camera"

    bpy.context.scene.camera = camera_obj  # Make the newly added camera the active camera
    bpy.data.cameras[camera_obj.data.name].lens = 19  # Set the focal length to 50mm (adjust as needed)

    camera_obj.hide_viewport = False
    camera_obj.hide_render = False
    
def garis():
    verts=[(5.5,0,11),(5.5,0,9.5),
    (10.5,0,11),(10.5,0,16),
    (26,0,2.5),(26,0,4.5),
    (35,0,17),(41,0,13),
    (41,0,3),(41,0,2.5),
    (49,0,19),(51,0,18),
    (61,0,23),(61,0,13),(62,0,12),(61,0,11),(61,0,2), #12-16
    (60.5,0,23), (60.5,0,2)]
    edges=[(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(13,14),(14,15),(15,16),(12,17),(16,18)]
    new_mesh = bpy.data.meshes.new("garis")
    new_mesh.from_pydata(verts, edges, [])

    new_obj = bpy.data.objects.new("Garis", new_mesh)
    bpy.context.collection.objects.link(new_obj)
    bpy.context.view_layer.update()

if __name__=="__main__":
    garis()
    atom_merah(4,0,11.5,0,0,0,0)
    for x in range(j+5) :
        x=10
        l = 4
        k = random.randint(-1,1)
        a = random.randint(7,10)
        b = random.randint(0.5,3.2)
        c = random.randint(2.5)
        atom(x + b, y + c+k, a+k+l)
        while (i <= 8):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,0)
            atom(x+b,y+c,a+k+l)
            i=i+1
        while (i <= 10):
            a = random.randint(7,10)
            b = random.randint(3)
            c = random.randint(-1,1)
            atom(x+b-1,y,a+k+l)
            i=i+1
        while (i <= 12):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,1)
            atom(x+b-1,y-1.5,a+k+l)
            i=i+1
    i=0    
    for x in range(j+40) :
        x=25
        while(i <= 30):
            a = random.randint(5,11)
            b = random.randint(-0.5,3)
            c = random.randint(-1.5,1.5)
            atom(x+b,y+c,a+k+4)
            i=i+1
        while (i <= 60):
            a = random.randint(11,14)
            b = random.randint(-2,5)
            c = random.randint(-2,3)
            if (a == a_d):
                atom(x+b,y+c,a+k+0.5+3)
            atom(x+b,y+c,a+k+4)
            a_d = a
#            b_d = b
#            c_d = c
            i_d = i
            i=i+1
#            atom(0,0,0)
        while (i <= 65):
            a = random.randint(14,15)
            b = random.randint(-1,2)
            c = random.randint(-1,2)
            atom(x+b,y+c,a+k+0.5+4)
            i=i+1
        while (i <= 95):
            a = random.randint(3.5,7)
            b = random.randint(-2,5)
            c = random.randint(-2,3)
            if (a == a_d):
                atom(x+b,y+c,a+k-0.5+3)
            atom(x+b,y+c,a+k+4)
            a_d = a
            i_d = i
            i=i+1
    i=0 
    x=0 
    for x in range(j+5) :
        x = 40
        l = 10
        k = random.randint(-1,1)
        a = random.randint(7,10)
        b = random.randint(0.5,3.2)
        c = random.randint(2.5)
        atom(x + b, y + c+k, a+k+l)
        while (i <= 8):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,0)
            atom(x+b,y+c,a+k+l)
            i=i+1
        while (i <= 10):
            a = random.randint(7,10)
            b = random.randint(3)
            c = random.randint(-1,1)
            atom(x+b-1,y,a+k+l)
            i=i+1
        while (i <= 12):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,1)
            atom(x+b-1,y-1.5,a+k+l)
            i=i+1   
    i=0 
    x=0 
    for x in range(j+5) :
        x = 40
        l = -2
        k = random.randint(-1,1)
        a = random.randint(7,10)
        b = random.randint(0.5,3.2)
        c = random.randint(2.5)
        atom(x + b, y + c+k, a+k+l)
        while (i <= 8):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,0)
            atom(x+b,y+c,a+k+l)
            i=i+1
        while (i <= 10):
            a = random.randint(7,10)
            b = random.randint(3)
            c = random.randint(-1,1)
            atom(x+b-1,y,a+k+l)
            i=i+1
        while (i <= 12):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,1)
            atom(x+b-1,y-1.5,a+k+l)
            i=i+1  
             
    atom_merah(51.2,0,18,-0.62,-3,1,100)
    atom_merah(52,0,12,0,0,1,100)
    atom_merah(51.5,0,6.5,0.62,3,1,100)
            
    i=0 
    x=0         
    
    ledak(25,5,0) 
    
    for x in range(j+5) :
        x = 55
        l = -3
        k = random.randint(-1,1)
        a = random.randint(7,10)
        b = random.randint(0.5,3.2)
        c = random.randint(2.5)
        atom(x + b, y + c+k, a+k+l)
        while (i <= 8):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,0)
            atom(x+b,y+c,a+k+l)
            i=i+1
        while (i <= 10):
            a = random.randint(7,10)
            b = random.randint(3)
            c = random.randint(-1,1)
            atom(x+b-1,y,a+k+l)
            i=i+1
        while (i <= 12):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,1)
            atom(x+b-1,y-1.5,a+k+l)
            i=i+1   
    i=0
    x=0     
    for x in range(j+5) :
        x = 55
        l = 12
        k = random.randint(-1,1)
        a = random.randint(7,10)
        b = random.randint(0.5,3.2)
        c = random.randint(2.5)
        atom(x + b, y + c+k, a+k+l)
        while (i <= 8):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,0)
            atom(x+b,y+c,a+k+l)
            i=i+1
        while (i <= 10):
            a = random.randint(7,10)
            b = random.randint(3)
            c = random.randint(-1,1)
            atom(x+b-1,y,a+k+l)
            i=i+1
        while (i <= 12):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,1)
            atom(x+b-1,y-1.5,a+k+l)
            i=i+1   
    i=0
    x=0     
    for x in range(j+5) :
        x = 57
        l = 4
        k = random.randint(-1,1)
        a = random.randint(7,10)
        b = random.randint(0.5,3.2)
        c = random.randint(2.5)
        atom(x + b, y + c+k, a+k+l)
        while (i <= 8):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,0)
            atom(x+b,y+c,a+k+l)
            i=i+1
        while (i <= 10):
            a = random.randint(7,10)
            b = random.randint(3)
            c = random.randint(-1,1)
            atom(x+b-1,y,a+k+l)
            i=i+1
        while (i <= 12):
            a = random.randint(7,10)
            b = random.randint(4)
            c = random.randint(-1,1)
            atom(x+b-1,y-1.5,a+k+l)
            i=i+1   
    i=0 
    x=0  
    # x,y,z,rotasi,size  
    plane(30,5,15,90,30)    
    plane(30,0,0,0,30)  
    
    sun(30,0,30)
    camera(31,-38,12)
      
      
        