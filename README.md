# Blender Qt stylesheet

A Blender Qt stylesheet for PySide2.  

| Dark style |  Dark style + dark title bar |  Default qt style  |
| -- | -- | -- | 
| ![image](https://github.com/hannesdelbeke/blender-qt-stylesheet/assets/3758308/56a571ba-e2de-4dfb-acb2-a835cff4d91b) | ![image](https://github.com/hannesdelbeke/blender-qt-stylesheet/assets/3758308/a9a5ecb4-7096-4380-aae0-b97de3768989) | ![image](https://github.com/hannesdelbeke/blender-qt-stylesheet/assets/3758308/046fd91f-6061-4892-9cff-072f1ea32bf4) |
 | | notice bug with dial and scrollbar | |

### Instructions
```python
import blender_stylesheet
blender_stylesheet.setup()
```
see `example/example.py`

### Features
- apply dark style to QApplication
- apply Blender Icon to QApplication

#### Dark title bar
Optional: Make your title bar dark when creating your QApplication
```python
app = QApplication(sys.argv + ['-platform', 'windows:darkmode=2'])
``` 

---
Ported the original stylesheet from the [BQt](https://github.com/techartorg/bqt) project, to allow stylesheet use outside Blender.
