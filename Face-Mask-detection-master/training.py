import numpy as np

data = np.load('data.npy')
target = np.load('target.npy')

from  keras.models import Sequential
from keras.models import Dense,Activation,Flatten,Dropout
from keras.layers import Conv2D,MaxPooling2D
from keras.callbacks import ModelCheckPoint

model = Sequential()

model.add(Conv2D(200,(3,3),input_shape =data.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(100,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())
model.add(Dropout(0.5))


model.add(Dense(50,activation='relu'))

model.add(Dense(2,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])



from sklearn.model_selection import train_test_split



train_data,test_data,train_target,test_target = train_test_split(datamtarget,test_size=0.1)


checkpoint = ModelCheckpoint('model-{epoch:03d}.model', monitor='val_loss', verbose=0,save_best_only=True,mode='auto')

history = model.fit(train_data,train_target,epochs=20,callbacks=[heckpoints],validation_split=0.2)

print(model.evaluate(test_data,test_target))
