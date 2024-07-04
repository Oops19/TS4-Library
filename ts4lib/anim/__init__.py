#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from interactions.base.super_interaction import SuperInteraction


class TS4LibraryPoseInteraction(SuperInteraction):
    __qualname__ = 'TS4LibraryPoseInteraction'

    def __init__(self, *args, pose_name=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.pose_name = pose_name

    def setup_asm_default(self, asm, *args, **kwargs):
        asm.set_parameter('pose_name', self.pose_name)
        return super().setup_asm_default(asm, *args, **kwargs)
