from typing import Union

from sims.sim import Sim
from sims.sim_info import SimInfo
from sims.sim_info_base_wrapper import SimInfoBaseWrapper
from sims4communitylib.utils.sims.common_sim_name_utils import CommonSimNameUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ts4lib.utils.singleton import Singleton


class SimName(object, metaclass=Singleton):
    SIM_NAMES_SEP = '#'

    @staticmethod
    def get(sim_identifier: Union[int, Sim,  SimInfo, SimInfoBaseWrapper, None] = None) -> str:
        """ Return 'First Name#Last Name' as one string. E.g. 'Ann Lee#Smith' or 'Ann#Lee Smith' """
        if isinstance is None:
            sim_info = CommonSimUtils.get_active_sim_info()
        else:
            sim_info = CommonSimUtils.get_sim_info(sim_identifier)

        f_name = CommonSimNameUtils.get_first_name(sim_info)
        l_name = CommonSimNameUtils.get_last_name(sim_info)
        return f"{f_name}{SimName.SIM_NAMES_SEP}{l_name}"