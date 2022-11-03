import pickle
import model

ridge = model.ridge
with open('./model.pkl','wb') as pickle_file:
    pickle.dump(ridge, pickle_file)