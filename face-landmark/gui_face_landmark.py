# Creating GUI interface to load and show image
#
# Algorithm:
# Importing needed PyQt libraries -->
# --> Importing custom module with designed GUI -->
# --> Creating MainApp class with needed functionality -->
# --> Creating main function to initialize and run Qt Application
#
# Result:
# Designed in Qt Designer GUI window with loaded image


# Importing needed libraries
# We need sys library to pass arguments into QApplication
import sys
# QtWidgets to work with widgets
from PyQt5 import QtWidgets
# QPixmap to work with images
from PyQt5.QtGui import QPixmap

# Importing designed GUI in Qt Designer as module
import design
# Importing Image recognization module to Detect face landmark in a image
from face_landmark import detect_face_landmark


"""
Start of:
Main class to add functionality of designed GUI
"""


# Creating main class to connect objects in designed GUI with useful code
# Passing as arguments widgets of main window
# and main class of created design that includes all created objects in GUI
class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    # Constructor of the class
    def __init__(self):
        # We use here super() that allows multiple inheritance of all variables,
        # methods, etc. from file design
        # And avoiding referring to the base class explicitly
        super().__init__()

        # Initializing created design that is inside file design
        self.setupUi(self)

        # Connecting event of clicking on the button with needed function
        self.pushButton.clicked.connect(self.update_label_object)

    # Defining function that will be implemented after button is pushed
    def update_label_object(self):

        # Showing text while image is loading and processing
        self.label.setText('Processing ...')

        # Opening dialog window to choose an image file
        # Giving name to the dialog window --> 'Choose Image to Open'
        # Specifying starting directory --> '.'
        # Showing only needed files to choose from --> '*.png *.jpg *.bmp'
        image_path = \
            QtWidgets.QFileDialog.getOpenFileName(self, 'Choose Image to Open',
                                                  '.',
                                                  '*.png *.jpg *.bmp')

        # Variable 'image_path' now is a tuple that consists of two elements
        # First one is a full path to the chosen image file
        # Second one is a string with possible extensions

        # Checkpoint
        print(type(image_path))  # <class 'tuple'>
        print(image_path[0])  # /home/my_name/Downloads/example.png
        print(image_path[1])  # *.png *.jpg *.bmp

        # Slicing only needed full path
        image_path = image_path[0]  # /home/my_name/Downloads/example.png

 		# Passing full path to loaded image into face landmark algorithm
        detect_face_landmark(image_path)

        # Opening image with QPixmap class that is used to
        # show image inside Label object
        pixmap_image = QPixmap('result.jpg')

        # Passing opened image to the Label object
        self.label.setPixmap(pixmap_image)

        # Getting opened image width and height
        # And resizing Label object according to these values
        self.label.resize(pixmap_image.width(), pixmap_image.height())


"""
End of: 
Main class to add functionality of designed GUI
"""


"""
Start of:
Main function
"""


# Defining main function to be run
def main():
    # Initializing instance of Qt Application
    app = QtWidgets.QApplication(sys.argv)

    # Initializing object of designed GUI
    window = MainApp()

    # Showing designed GUI
    window.show()

    # Running application
    app.exec_()


"""
End of: 
Main function
"""


# Checking if current namespace is main, that is file is not imported
if __name__ == '__main__':
    # Implementing main() function
    main()
