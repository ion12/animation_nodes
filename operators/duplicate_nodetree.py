import bpy

class DuplicateNodeTree(bpy.types.Operator):
    bl_idname = "an.duplicate_node_tree"
    bl_label = "Duplicate Animation Node Tree"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        if not space: return False
        if space.type != "NODE_EDITOR": return False
        if space.tree_type != "an_AnimationNodeTree": return False
        return space.node_tree is not None

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        tree = context.space_data.node_tree
        copy = tree.copy()
        context.space_data.node_tree = copy
        return {"FINISHED"}
