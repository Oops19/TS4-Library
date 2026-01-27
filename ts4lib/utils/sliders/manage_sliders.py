#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


from typing import Any, Dict, Union, List

from ts4lib.custom_enums.custom_slider import CustomSlider
from ts4lib.modinfo import ModInfo
from ts4lib.enums.sculpt import Sculpt
from ts4lib.enums.sim_modifier import SimModifier

from protocolbuffers import PersistenceBlobs_pb2
from protocolbuffers.PersistenceBlobs_pb2 import BlobSimFacialCustomizationData
from sims.sim_info import SimInfo

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'ManageSliders')
log.enable()


class ManageSliders:

    def update_sculpt(self, sim_info: SimInfo, remove_sculpt_id: int = 0, add_sculpt_id: int = 0, resend_sliders: bool = None):
        facial_attributes = getattr(sim_info, 'facial_attributes', None)
        if facial_attributes is None:
            log.warn(f"Sim {sim_info} has no 'facial_attributes'.")
            return False

        appearance_attributes = PersistenceBlobs_pb2.BlobSimFacialCustomizationData()
        appearance_attributes.MergeFromString(facial_attributes)

        modifier_type = CustomSlider.BLOB_SIM_SCULPTS
        sculpts = self._get_modifiers(appearance_attributes, modifier_type)

        new_sculpts = []
        sculpt_name_del = Sculpt.MAP.get(remove_sculpt_id, f"{remove_sculpt_id:016X}")
        sculpt_name_add = Sculpt.MAP.get(add_sculpt_id, f"{add_sculpt_id:016X}")
        _sliders_modified = False
        _sculpt_removed_1 = False if sculpt_name_del else True
        _sculpt_removed_2 = False if sculpt_name_add else True
        for sculpt in sculpts:
            if _sculpt_removed_1 and _sculpt_removed_2:
                break
            if sculpt == remove_sculpt_id:
                log.debug(f"Removing {sim_info} sculpt {sculpt_name_del}")
                _sculpt_removed_1 = True
                _sliders_modified = True
                continue
            if sculpt == add_sculpt_id:
                log.info(f"Removing {sim_info} sculpt {sculpt_name_add} (will be added later)")
                _sculpt_removed_2 = True
                continue
            new_sculpts.append(sculpt)

        if add_sculpt_id > 0:
            log.debug(f"Adding {sim_info} sculpt {sculpt_name_add}")
            _sliders_modified = True
            new_sculpts.append(add_sculpt_id)

        if _sliders_modified:
            sculpts[:] = new_sculpts

        if resend_sliders is True or _sliders_modified and resend_sliders is None:
            sim_info.facial_attributes = appearance_attributes.SerializeToString()
            sim_info.resend_facial_attributes()
        return True

    def slide_to(self, sim_info: SimInfo, modifier_type: CustomSlider, slider_key: int, slider_value: float, resend_sliders: bool = None) -> bool:
        r"""
        This method changes the normal and the aged sliders when using modifier_type 1, 2, 3 or 4.
        HighHeelsConstants:
        BLOB_SIM_SCULPTS = 0  # not supported
        BLOB_SIM_FACE_MODIFIER = 1
        BLOB_SIM_BODY_MODIFIER = 2
        BLOB_SIM_AGED_FACE_MODIFIER = 3
        BLOB_SIM_AGED_BODY_MODIFIER = 4
        @param sim_info:
        @param modifier_type:
        @param slider_key:
        @param slider_value:
        @param resend_sliders: True: resend sliders; None: resend modified sliders only; False: don't resend sliders
        @return:
        """
        if modifier_type not in {CustomSlider.BLOB_SIM_FACE_MODIFIER, CustomSlider.BLOB_SIM_AGED_FACE_MODIFIER, CustomSlider.BLOB_SIM_BODY_MODIFIER, CustomSlider.BLOB_SIM_AGED_BODY_MODIFIER, }:
            log.warn(f"modifier_type {modifier_type} not supported.")
            return False

        facial_attributes = getattr(sim_info, 'facial_attributes', None)
        if facial_attributes is None:
            log.warn(f"Sim {sim_info} has no 'facial_attributes'.")
            return False

        appearance_attributes = PersistenceBlobs_pb2.BlobSimFacialCustomizationData()
        appearance_attributes.MergeFromString(facial_attributes)

        modifiers = self._get_modifiers(appearance_attributes, modifier_type)

        _sliders_modified = self._slide_to(sim_info, modifiers, slider_key, slider_value)

        if resend_sliders is True or _sliders_modified and resend_sliders is None:
            sim_info.facial_attributes = appearance_attributes.SerializeToString()
            sim_info.resend_facial_attributes()
        return True

    def _slide_to(self, sim_info: SimInfo, modifiers: Any, slider_key: int, slider_value) -> Union[bool, None]:
        r""" modifiers must not be 'appearance_attributes.sculpts' """
        slider_name = SimModifier.MAP.get(slider_key, f"{slider_key:016X}")

        try:
            if not (0 <= slider_value <= 1):
                return False

            if slider_value == 0:
                class Slider:
                    def __init__(self, key: int, amount: float):
                        self.key = key
                        self.amount = amount
                        
                new_sliders: List[Slider] = []
                old_slider_value = -1.0
                for modifier in modifiers:
                    if modifier.key != slider_key:
                        new_sliders.append(Slider(modifier.key, modifier.amount))
                    else:
                        old_slider_value = modifier.amount
                    continue
                if old_slider_value == -1.0:
                    log.debug(f"'{sim_info}': Remove: Slider '{slider_name}' not found.")
                    return None

                log.debug(f"'{sim_info}': Removing slider '{slider_name}' with {old_slider_value:.4f}")
                del modifiers[:]
                for slider in new_sliders:
                    modifier = BlobSimFacialCustomizationData.Modifier()
                    modifier.key = slider.key
                    modifier.amount = slider.amount
                    modifiers.append(modifier)
                return True

            for modifier in modifiers:
                if modifier.key == slider_key:
                    log.debug(f"'{sim_info}': Sliding '{slider_name}' from '{modifier.amount}' to {slider_value:.4f}")
                    modifier.amount = slider_value
                    return True

            if slider_value > 0:
                log.debug(f"'{sim_info}': Adding slider '{slider_name}' with {slider_value:.4f}")
                modifier = BlobSimFacialCustomizationData.Modifier()
                modifier.key = slider_key  # set key & value
                modifier.amount = slider_value
                modifiers.append(modifier)
            return True

        except Exception as e:
            log.error(f"Could not change slider '{slider_name}' for '{sim_info}' ({e})")
            return False

    # noinspection PyMethodMayBeStatic
    def _get_modifiers(self, appearance_attributes: Any, modifier_type: CustomSlider) -> Any:
        if modifier_type == CustomSlider.BLOB_SIM_SCULPTS:
            modifiers = appearance_attributes.sculpts
        elif modifier_type == CustomSlider.BLOB_SIM_FACE_MODIFIER:
            modifiers = appearance_attributes.face_modifiers
        elif modifier_type == CustomSlider.BLOB_SIM_BODY_MODIFIER:
            modifiers = appearance_attributes.body_modifiers
        elif modifier_type == CustomSlider.BLOB_SIM_AGED_FACE_MODIFIER:
            modifiers = appearance_attributes.aged_face_modifiers
        elif modifier_type == CustomSlider.BLOB_SIM_AGED_BODY_MODIFIER:
            modifiers = appearance_attributes.aged_body_modifiers
        else:
            modifiers = None
        return modifiers

    def get_sliders(self, sim_info: SimInfo) -> Dict[CustomSlider, Dict]:
        slider_info: Dict[CustomSlider, Dict] = {}

        facial_attributes = getattr(sim_info, 'facial_attributes', None)
        if facial_attributes is None:
            log.warn(f"Sim {sim_info} has no 'facial_attributes'.")
            return slider_info

        appearance_attributes = PersistenceBlobs_pb2.BlobSimFacialCustomizationData()
        appearance_attributes.MergeFromString(facial_attributes)

        for modifier_type in [CustomSlider.BLOB_SIM_FACE_MODIFIER, CustomSlider.BLOB_SIM_BODY_MODIFIER]:
            _slider_info = {}
            modifiers = self._get_modifiers(appearance_attributes, modifier_type)
            for modifier in modifiers:
                _slider_info.update({modifier.key: (modifier.amount, None)})

            modifiers = self._get_modifiers(appearance_attributes, CustomSlider(modifier_type.value + 2))
            for modifier in modifiers:
                slider_value, _ = _slider_info.get(modifier.key, (None, None))
                _slider_info.update({modifier.key: (slider_value, modifier.amount)})
            slider_info.update({modifier_type: _slider_info})

        modifier_type = CustomSlider.BLOB_SIM_SCULPTS
        modifiers = self._get_modifiers(appearance_attributes, modifier_type)
        _slider_info = {}
        for modifier in modifiers:
            _slider_info.update({modifier: None})
        slider_info.update({modifier_type: _slider_info})

        return slider_info
