"""
Detetcing face landmark using face_recognition library
File: face_landmark.py
"""

# Detecting face landmarks on the Image with face_recognition and draw landmark points on the face
#
# How does Face Landmark works
# STEP1: Import libararies
# STEP2: Load the image
# STEP3: Get the landmark points as a list form
# STEP4: Loop around to convert to draw objects 
# STEP5: Save the new image
#
# Result:
# A new image will be created with the face landmark features engraved. 



# STEP1: Importing needed libraries
import face_recognition
from PIL import Image, ImageDraw

# Function for face detection
def detect_face_landmark(image):
	# STEP2: Load the image 
	face_image = face_recognition.load_image_file(image)

	# STEP3: Get the face landmarks list
	face_landmarks_list =  face_recognition.face_landmarks(face_image)

	#print the face landmarks list
	#print(face_landmarks_list)

	# STEP4: Loop around to convert to draw objects 
	for face_landmarks in face_landmarks_list:
		#convert the numpy array image into pil image object
		pil_image = Image.fromarray(face_image)

		#convert the pil image to draw object
		draw_face_landmark = ImageDraw.Draw(pil_image)

		#join each face landmark points
		draw_face_landmark.line(face_landmarks['chin'],fill=(255,255,255), width=2)
		draw_face_landmark.line(face_landmarks['left_eyebrow'],fill=(255,255,255), width=2)
		draw_face_landmark.line(face_landmarks['right_eyebrow'],fill=(255,255,255), width=2)
		draw_face_landmark.line(face_landmarks['nose_bridge'],fill=(255,255,255), width=2)
		draw_face_landmark.line(face_landmarks['nose_tip'],fill=(255,255,255), width=2)
		draw_face_landmark.line(face_landmarks['left_eye'],fill=(255,255,255), width=2)
		draw_face_landmark.line(face_landmarks['right_eye'],fill=(255,255,255), width=2)
		draw_face_landmark.line(face_landmarks['top_lip'],fill=(255,255,255), width=2)
		draw_face_landmark.line(face_landmarks['bottom_lip'],fill=(255,255,255), width=2)
  
	#show the final image    
	#pil_image.show()

	#STEP5: save the image
	pil_image.save("./result.jpg")


# Point to the image location
#image_loc = './actress.jpg'

# Print the location of Image
#print (image_loc)

# call the function 
#detect_face_landmark(image_loc)
