from imports import *
from preprocessing import network_params
from make_data import make

def  lstm_model(inputs, total_classes):
	model = Sequential()
	model.add(LSTM(520, return_sequences = True, input_shape = (inputs.shape[1], inputs.shape[2])))
	model.add(Dropout(0.4))
	model.add(LSTM(520, return_sequences = True))
	model.add(Dropout(0.4))
	model.add(LSTM(520, return_sequences = True))
	model.add(Dropout(0.4))
	model.add(LSTM(520))
	model.add(Dense(total_classes))
	model.add(Dropout(0.4))
	model.add(Activation('softmax'))
	model.compile(loss = 'categorical_crossentropy', optimizer = 'rmsprop')
	return model


#Testing purposes
if __name__ == "__main__":
	notes = make()
	arr = network_params(notes[0], notes[1], 100)
	inputs = arr[0]
	total_classes = notes[1]
	model = lstm_model(inputs, total_classes)
