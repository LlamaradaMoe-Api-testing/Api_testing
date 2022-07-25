#
# build_create_page.py Copyright (c) 2022 Jalasoft.
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

#from abc import ABC
#from abc import abstractmethod
import abc


class CreatePage(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        """Implement constructor method"""

    @abc.abstractmethod
    def create(self):
        """Implement create method"""

    @abc.abstractmethod
    def set_token(self):
        """Implement set token method"""
