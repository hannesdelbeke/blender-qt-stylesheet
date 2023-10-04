import sys
from PySide2.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QVBoxLayout, QWidget, QScrollArea, QPushButton, QLabel, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QComboBox, QListWidget, QSlider, QSpinBox, QProgressBar, QDial, QScrollBar, QTableWidget, QTableWidgetItem


class TestWidget(QMainWindow):
    def __init__(self):
        super(TestWidget, self).__init__()

        self.setWindowTitle("PySide2 Widget Test")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        # Left column
        left_column = QVBoxLayout()

        sample_text = """Strong Son of God, immortal Love,
Whom we, that have not seen thy face,
By faith, and faith alone, embrace,
Believing where we cannot prove;
Thine are these orbs of light and shade;
Thou madest Life in man and brute;
Thou madest Death; and lo, thy foot
Is on the skull which thou hast made."""
        left_column.addWidget(QLabel("Label"))
        left_column.addWidget(QPushButton("Push Button"))
        left_column.addWidget(QLineEdit("Line Edit"))
        left_column.addWidget(QTextEdit(sample_text))
        left_column.addWidget(QCheckBox("Check Box"))
        left_column.addWidget(QRadioButton("Radio Button"))

        # Add dummy data to ComboBox
        combo_box = QComboBox()
        combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        left_column.addWidget(combo_box)

        # Add dummy data to ListWidget
        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])
        left_column.addWidget(list_widget)
        list_widget.setSelectionMode(QListWidget.ExtendedSelection)

        # Add dummy data to Slider
        slider = QSlider()
        # slider.setOrientation(1)  # Set horizontal orientation
        left_column.addWidget(slider)

        # Add dummy data to SpinBox
        spin_box = QSpinBox()
        spin_box.setValue(50)
        left_column.addWidget(spin_box)

        layout.addLayout(left_column)

        # Right column
        right_column = QVBoxLayout()

        bar = QProgressBar()
        bar.setValue(50)
        right_column.addWidget(bar)
        dial = QDial()
        dial.setValue(50)
        right_column.addWidget(dial)

        # Add dummy data to ScrollArea
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        for i in range(4):
            scroll_layout.addWidget(QPushButton(f"Item {i + 1}"))
        for i in range(5):
            scroll_layout.addWidget(QLabel(f"Item {i+1}"))


        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)
        right_column.addWidget(scroll_area)

        # Create a table widget and add some items
        table_widget = QTableWidget(2, 2)
        table_widget.setItem(0, 0, QTableWidgetItem("Item 1"))
        table_widget.setItem(0, 1, QTableWidgetItem("Item 2"))
        table_widget.setItem(1, 0, QTableWidgetItem("Item 3"))
        table_widget.setItem(1, 1, QTableWidgetItem("Item 4"))
        right_column.addWidget(table_widget)

        layout.addLayout(right_column)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWidget()
    window.show()
    sys.exit(app.exec_())
