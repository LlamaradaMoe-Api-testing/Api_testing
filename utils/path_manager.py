#
# path_manager.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import pathlib
from pathlib import Path


class PathManager:
    @staticmethod
    def get_absolute_path():
        absolute_path = pathlib.Path().absolute()
        return absolute_path

    @staticmethod
    def get_parent_path():
        parent_path = Path(__file__).parents[1]
        return parent_path
