import cv2,os

data_path = 'dataset'
categories= os.listdir(data_path)
labels = [ i for i in range(len(categories))]

print(label_dict)

img_size = 100
data = []
target = []

for category in categories:
	dataset/mask = os.path.join(data_path,category)
	img_names= os.listdir(folder_path)

	for img_name in img_names:
		img_path = os.path.join(folder_path,img_name)
		img = cv2.imread(img_path)

		try:
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

			resized = cv2.resize(gray,(ing_size,img_size))

			data.append(resized)
			target.append(label_dict[category])


		except Exception as e:
			print('Exception:',e)


import numpy as np
data = np.array(data)
data = np.reshape(data,(data.shape[0],img_size,img_size,1))
target = np.array(target)

from keras.utils import np_utils

new_target = np_utils.to_categorical(target)


np.save('data',data)
np.save('target',new_target)
