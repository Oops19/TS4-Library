#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


from typing import Dict

from ts4lib.custom_enums.custom_slider import CustomSlider
from ts4lib.modinfo import ModInfo
from ts4lib.enums.sculpt import Sculpt
from ts4lib.enums.sim_modifier import SimModifier

from sims.sim_info import SimInfo
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ts4lib.utils.sliders.manage_sliders import ManageSliders

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'SliderCheats')
log.enable()


class SliderCheats:
    # o19.sliders.set 2 10160417097015316330  0.0

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.ts4l.sculpt.set', 'Change slider of active sim',
                          command_arguments=(
                                  CommonConsoleCommandArgument('remove_sculpt_id', 'int', '...', is_optional=False, default_value=0),
                                  CommonConsoleCommandArgument('add_sculpt_id', 'int', '...', is_optional=False, default_value=0),
                          )
                          )
    def cheat_o19_sculpt_set(output: CommonConsoleCommandOutput, remove_sculpt_id: int = 0, add_sculpt_id: int = 0):
        sim_info: SimInfo = CommonSimUtils.get_active_sim_info()
        rv = ManageSliders().update_sculpt(sim_info, remove_sculpt_id, add_sculpt_id)
        output(f"See log ({rv})")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.ts4l.slider.set', 'Change slider of active sim',
                          command_arguments=(
                                  CommonConsoleCommandArgument('modifier_type', 'int', '...', is_optional=False, default_value=1),
                                  CommonConsoleCommandArgument('slider_key', 'int', '...', is_optional=False, default_value=0),
                                  CommonConsoleCommandArgument('slider_value', 'float', '...', is_optional=False, default_value=0.0),
                          )
                          )
    def cheat_o19_sliders_set(output: CommonConsoleCommandOutput, modifier_type: int = 1, slider_key: int = 0, slider_value: float = 0.0):
        sim_info: SimInfo = CommonSimUtils.get_active_sim_info()
        _modifier_type = CustomSlider(modifier_type)
        slider_name = SimModifier.MAP.get(slider_key, f"{slider_key:016X}")
        output(f"CustomSlider: {slider_name}")
        if slider_key > 0:
            ManageSliders().slide_to(sim_info, _modifier_type, slider_key, slider_value)
        output(f"See log")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.ts4l.sliders.dump', 'Dump sliders of active sim', )
    def cheat_o19_sliders_dump(output: CommonConsoleCommandOutput):
        sim_info: SimInfo = CommonSimUtils.get_active_sim_info()
        slider_info: Dict = ManageSliders().get_sliders(sim_info)
        if slider_info:
            log.debug(f"Sim: {sim_info}")
            for k, v in slider_info.items():
                log.debug(f"{k}: {v}")

            for k, v in slider_info.items():
                if k in {CustomSlider.BLOB_SIM_FACE_MODIFIER, CustomSlider.BLOB_SIM_BODY_MODIFIER, }:
                    _k1 = k.value
                    _k2 = _k1 + 2
                    for slider_key, values in v.items():
                        slider_name = SimModifier.MAP.get(slider_key, f"{slider_key:016X}")
                        _v1, _v2 = values
                        if _v1 is not None:
                            log.debug(f" o19.ts4l.slider.set {_k1} {slider_key} {_v1}  # {slider_name}")
                        if _v2 is not None:
                            log.debug(f" o19.ts4l.slider.set {_k2} {slider_key} {_v2}  # {slider_name}")
                elif k in {CustomSlider.BLOB_SIM_SCULPTS, }:
                    _k1 = k.value
                    for sculpt_key, _ in v.items():
                        sculpt_name = Sculpt.MAP.get(sculpt_key, f"{sculpt_key:016X}")
                        log.debug(f" o19.ts4l.sculpt.set 0 {sculpt_key}  # remove:- add:{sculpt_name}")
            output(f"See log")
        else:
            output(f"No sliders found")
