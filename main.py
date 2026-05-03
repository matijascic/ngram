import os

if __name__ == "__main__":

    DIR="./shakespeare-dataset/"

    dataset = {}

    for name in os.listdir(DIR):
        dataset[name]={}
        dataset[name]["title"]=name
        dataset[name]["path"]=DIR+name
        print(dataset[name])
        f = open(dataset[name]["path"], 'r')
        dataset[name]["content"]=f.read()
        f.close()

    
