"""
Performing digital makeup using face_recognition library
File: digital_makeup.py
"""

# Detecting face landmarks on the Image with face_recognition and perform digital makeup on the face
#
# How does Face Landmark works
# STEP1: Import libararies
# STEP2: Load the image
# STEP3: Get the landmark points as a list form
# STEP4: Loop around to convert to draw objects 
# STEP5: Save the new image
#
# Result:
# A new image will be created with the digital face makeup. 



# STEP1: Importing needed libraries
import face_recognition
from PIL import Image, ImageDraw

# Function for face detection
def digital_makeup(image):
	# STEP2: Load the image 
	face_image = face_recognition.load_image_file(image)

	# STEP3: Get the face landmarks list
	face_landmarks_list =  face_recognition.face_landmarks(face_image)

	#print the face landmarks list
	print(face_landmarks_list)

	# STEP4: Loop around to convert to draw objects 
	for face_landmarks in face_landmarks_list:
		#convert the numpy array image into pil image object
		pil_image = Image.fromarray(face_image)

		#convert the pil image to draw object
		draw_landmark_for_makeup = ImageDraw.Draw(pil_image,"RGBA")

		#draw the shapes and fill with color 
		# Make left, right eyebrows darker 
		# Polygon on top and line on bottom with dark color
		draw_landmark_for_makeup.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
		draw_landmark_for_makeup.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
		draw_landmark_for_makeup.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
		draw_landmark_for_makeup.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)


		# Add lipstick to top and bottom lips
    	# using red polygons and lines filled with red
		draw_landmark_for_makeup.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
		draw_landmark_for_makeup.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
		draw_landmark_for_makeup.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
		draw_landmark_for_makeup.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)


		# Make left and right eyes filled with Green
		draw_landmark_for_makeup.polygon(face_landmarks['left_eye'], fill=(0, 255, 0, 0))
		draw_landmark_for_makeup.polygon(face_landmarks['right_eye'], fill=(0, 255, 0, 0))

		# Eyeliner to left and right eyes as lines
		draw_landmark_for_makeup.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 90), width=6)
		draw_landmark_for_makeup.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 90), width=6)

	#show the final image    
	#pil_image.show()

	#STEP5: save the image
	pil_image.save("./result.jpg")



# Point the location where the image file is located
#image_loc = './actress.jpg'

# call the function 
#digital_makeup(image_loc)
