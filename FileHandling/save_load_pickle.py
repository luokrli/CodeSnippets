## Save any python data (DateFrame, Series, etc.) as a binary file for future use

import pickle

def save_pickle(data, data_name):
    file_name = data_name + '.pickle'
    fp = open(file_name, 'wb')
    pickle.dump(data, fp)
    fp.close()
    print(file_name, "is saved!")

def load_pickle(data_name):
    file_name = data_name + '.pickle'
    fp = open(file_name, 'rb')
    data = pickle.load(fp)
    fp.close()
    print(file_name, "is loaded!")
    return data

if __name__ == "__main__":
    new_data = [1,2,3]
    data_name = 'new_data'
    try:
        if new_data:
            save_pickle(new_data, data_name)
    except NameError:
        new_data = load_pickle(data_name)
