from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import sys
import sqlite3

class CalendarWindow(QWidget):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        loadUi("calendarView.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)

    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()

        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()

            query = "SELECT task, completed FROM tasks WHERE date = ?"
            row = (date,)
            results = cursor.execute(query, row).fetchall()
            for result in results:
                item = QListWidgetItem(str(result[0]))
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                if result[1] == "YES":
                    item.setCheckState(Qt.Checked)
                elif result[1] == "NO":
                    item.setCheckState(Qt.Unchecked)
                self.tasksListWidget.addItem(item)

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        finally:
            db.close()

    def saveChanges(self):
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            date = self.calendarWidget.selectedDate().toPyDate()

            for i in range(self.tasksListWidget.count()):
                item = self.tasksListWidget.item(i)
                task = item.text()
                if item.checkState() == Qt.Checked:
                    query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
                else:
                    query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
                row = (task, date,)
                cursor.execute(query, row)
            db.commit()

            messageBox = QMessageBox()
            messageBox.setText("Changes saved.")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        finally:
            db.close()

    def addNewTask(self):
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()

            newTask = str(self.taskLineEdit.text())
            date = self.calendarWidget.selectedDate().toPyDate()

            query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
            row = (newTask, "NO", date,)

            cursor.execute(query, row)
            db.commit()
            self.updateTaskList(date)
            self.taskLineEdit.clear()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        finally:
            db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec())
