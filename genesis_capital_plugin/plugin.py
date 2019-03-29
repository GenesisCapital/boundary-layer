import os
from boundary_layer.plugins import BasePlugin, PluginPriority
from boundary_layer_default_plugin.preprocessors import DateStringToDatetime, BuildTimedelta, EnsureRenderedStringPattern


class GenesisCapitalPlugin(BasePlugin):
    name = 'genesis_capital'

    configs_path = os.path.join(os.path.dirname(__file__), 'config')

    priority = PluginPriority.FINAL

    property_preprocessors = [
        DateStringToDatetime,
        BuildTimedelta,
        EnsureRenderedStringPattern
    ]
