#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The model file for the MVC structure of the phonebook program.
"""
from __future__ import absolute_import
from controller import Controller


if __name__ == "__main__":
    controller = Controller()
    controller.start_view()
