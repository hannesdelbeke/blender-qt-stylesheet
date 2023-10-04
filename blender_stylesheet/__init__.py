
from qtpy.QtWidgets import QApplication
from qtpy.QtGui import QIcon, QImage, QPixmap

from pathlib import Path
import logging


STYLESHEET_PATH = Path(__file__).parent / "blender_stylesheet.qss"
ICON_FILEPATH = Path(__file__).parent / "images" / "blender_icon_16.png"


def apply_blender_stylesheet(qapp):
    if STYLESHEET_PATH.exists():
        qapp.setStyleSheet(STYLESHEET_PATH.read_text())
    else:
        logging.warning(f"Stylesheet not found: {STYLESHEET_PATH}")


def get_blender_icon():
    icon = QIcon()
    if ICON_FILEPATH.exists():
        image = QImage(str(ICON_FILEPATH))
        if not image.isNull():
            icon = QIcon(QPixmap().fromImage(image))
    return icon


def setup(qapp=None):
    """Setup the existing QApplication with the blender stylesheet and icon"""
    qapp = qapp or QApplication.instance()
    apply_blender_stylesheet(qapp)
    qapp.setWindowIcon(get_blender_icon())
    return qapp
