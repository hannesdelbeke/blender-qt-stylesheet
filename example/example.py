import blender_stylesheet
from qtpy.QtWidgets import QApplication
import sys
import demo_widget


def main():
    app = QApplication(sys.argv + ['-platform', 'windows:darkmode=2'])
    app.setStyle("fusion")
    blender_stylesheet.setup(app)
    widget = demo_widget.TestWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()