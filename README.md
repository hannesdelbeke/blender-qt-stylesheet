# Blender Qt stylesheet
[![PyPI version](https://img.shields.io/pypi/v/blender-qt-stylesheet)](https://pypi.org/project/blender-qt-stylesheet/)
[![latest tag](https://img.shields.io/github/v/tag/hannesdelbeke/blender-qt-stylesheet?label=Github)](https://github.com/hannesdelbeke/blender-qt-stylesheet)


A Blender Qt stylesheet for PySide2, PySide6 PyQt5, PyQt6 (using qtpy)  

The top 3 images are this style in PySide6 & PySide2
| Blender PySide6 | Blender PySide2 |  Blender PySide2 + dark title bar |  
| -- | -- | -- | 
| ![image](https://github.com/hannesdelbeke/blender-qt-stylesheet/assets/3758308/21f5bec9-07c3-49e4-97aa-a2dd14f967f0) | ![image](https://github.com/hannesdelbeke/blender-qt-stylesheet/assets/3758308/56a571ba-e2de-4dfb-acb2-a835cff4d91b) | ![image](https://github.com/hannesdelbeke/blender-qt-stylesheet/assets/3758308/a9a5ecb4-7096-4380-aae0-b97de3768989) | -- | 
 | | notice bug with dial and scrollbar | | 
 | Default qt style | PySide6 fusion style | | 
 | ![image](https://github.com/hannesdelbeke/blender-qt-stylesheet/assets/3758308/046fd91f-6061-4892-9cff-072f1ea32bf4)  | ![image](https://github.com/hannesdelbeke/blender-qt-stylesheet/assets/3758308/36b96e02-28f5-4bcb-a624-4d3073f0ab56) |  | 

### Instructions
```python
import blender_stylesheet
blender_stylesheet.setup()
```
see `example/example.py`

### Features
- apply dark style to QApplication
- apply Blender Icon to QApplication

#### Dark title bar in PySide2
Optional in PySide2: Make your title bar dark when creating your QApplication  
Happens automatically in PySide6
```python
app = QApplication(sys.argv + ['-platform', 'windows:darkmode=2'])
``` 

---
Ported the original stylesheet from the [BQt](https://github.com/techartorg/bqt) project, to allow stylesheet use outside Blender.
