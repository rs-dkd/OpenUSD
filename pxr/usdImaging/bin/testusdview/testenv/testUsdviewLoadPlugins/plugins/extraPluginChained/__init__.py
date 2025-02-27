#
# Copyright 2018 Pixar
#
# Licensed under the terms set forth in the LICENSE.txt file available at
# https://openusd.org/license.
#
from __future__ import print_function

from pxr import Tf
from pxr.Usdviewq.plugin import PluginContainer

import extraPlugin


class ExtraContainerChained(PluginContainer):

    def registerPlugins(self, plugRegistry, plugCtx):

        self._extra1 = plugRegistry.registerCommandPlugin(
            "ExtraContainerChained.extraCommand1",
            "Extra Command 1", lambda plugCtx: print("Extra Command 1 Invoked"))
        self._extra2 = plugRegistry.registerCommandPlugin(
            "ExtraContainerChained.extraCommand2",
            "Extra Command 2", lambda plugCtx: print("Extra Command 2 Invoked"))

        self._extraContainer = extraPlugin.ExtraContainer()
        self._extraContainer.registerPlugins(plugRegistry, plugCtx)

    def configureView(self, plugRegistry, plugUIBuilder):

        extraMenu = plugUIBuilder.findOrCreateMenu("Extra")
        extraMenu.addItem(self._extra1)
        extraMenu.addItem(self._extra2)

        self._extraContainer.configureView(plugRegistry, plugUIBuilder)

Tf.Type.Define(ExtraContainerChained)
