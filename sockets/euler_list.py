import bpy
from .. base_types.socket import AnimationNodeSocket

class EulerListSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_EulerListSocket"
    bl_label = "Euler List Socket"
    dataType = "Euler List"
    allowedInputTypes = ["Euler List"]
    drawColor = (0.1, 0.0, 0.4, 0.5)
    storable = True
    comparable = False

    def getValueCode(self):
        return "[]"

    def getCopyExpression(self):
        return "[element.copy() for element in value]"
