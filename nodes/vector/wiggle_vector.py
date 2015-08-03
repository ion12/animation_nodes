import bpy
from mathutils import Vector
from ... events import propertyChanged
from ... base_types.node import AnimationNode
from ... algorithms.perlin_noise import perlinNoise

class VectorWiggle(bpy.types.Node, AnimationNode):
    bl_idname = "mn_VectorWiggle"
    bl_label = "Vector Wiggle"
    isDetermined = True

    inputNames = { "Seed" : "seed",
                   "Evolution" : "evolution",
                   "Amplitude" : "amplitude",
                   "Octaves" : "octaves",
                   "Persistance" : "persistance" }

    outputNames = { "Vector" : "vector" }

    additionalSeed = bpy.props.IntProperty(update = propertyChanged)

    def create(self):
        self.inputs.new("mn_FloatSocket", "Seed")
        self.inputs.new("mn_FloatSocket", "Evolution")
        self.inputs.new("mn_VectorSocket", "Amplitude").value = [5, 5, 5]
        self.inputs.new("mn_IntegerSocket", "Octaves").value = 2
        self.inputs.new("mn_FloatSocket", "Persistance").value = 0.3
        self.outputs.new("mn_VectorSocket", "Vector")

    def draw_buttons(self, context, layout):
        layout.prop(self, "additionalSeed", text = "Additional Seed")

    def execute(self, seed, evolution, amplitude, octaves, persistance):
        vector = Vector()
        evolution = evolution + 2541 * seed + 823 * self.additionalSeed
        vector[0] = perlinNoise(evolution, persistance, octaves) * amplitude[0]
        evolution += 79
        vector[1] = perlinNoise(evolution, persistance, octaves) * amplitude[1]
        evolution += 263
        vector[2] = perlinNoise(evolution, persistance, octaves) * amplitude[2]
        return vector