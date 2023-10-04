import blender_stylesheet
from PySide2.QtWidgets import QApplication
import sys
import demo_widget


def main():
    app = QApplication(sys.argv + ['-platform', 'windows:darkmode=2'])
    blender_stylesheet.setup(app)
    widget = demo_widget.TestWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()