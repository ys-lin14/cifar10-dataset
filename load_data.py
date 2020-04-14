import pickle

def unpickle(file):
    """Load CIFAR-10 data from a pickle file into a dictionary. 
    Code from https://www.cs.toronto.edu/~kriz/cifar.html
    
    Args: 
        file (str): path to data
    
    Returns:
        data (dict): CIFAR-10 data
    """
    
    with open(file, "rb") as f:
        data = pickle.load(f, encoding="bytes")
    return data
