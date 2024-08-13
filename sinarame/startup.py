import os
from os import path

from .application_info import info
from .settings_smn import SettingsSMN as Settings


class Startup:

    def __init__(self, module_file_path: str) -> None:
        self._module_file_path: str = module_file_path

    def run(self) -> Settings:
        # Obtener la ruta del directorio de instalación del módulo
        # y el directorio de trabajo actual

        install_dir: str = self._get_module_dir_path()
        current_dir: str = os.getcwd()

        # Cargar la configuración del usuario
        user_settings_path: str = path.join(current_dir, info.user_settings)

        settings: Settings = Settings.load(
            user_settings_path, fail_if_not_exists=False
        )

        settings.root.update(
            {
                "path": {
                    "current_dir": current_dir,
                    "install_dir": install_dir,
                }
            }
        )

        return settings

    def _get_module_dir_path(self) -> str:
        return path.dirname(path.abspath(self._module_file_path))
