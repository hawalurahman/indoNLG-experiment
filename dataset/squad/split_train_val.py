import json
import numpy as np
import argparse

def main(file, size):

    with open(file, 'r') as f:
        data = json.load(f)[:size]

    train_set, val_set = np.split(data, [int(0.80 * len(data))])

    train_set = train_set.tolist()
    val_set = val_set.tolist()

    base_name = file.split(".json")[0]
    print(file, base_name)

    with open(f"{base_name}-trainset.json", 'w') as f:
        json.dump(train_set, f)
    
    with open(f"{base_name}-valset.json", 'w') as f:
        json.dump(val_set, f)

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="split train into train and val")
    parser.add_argument("--data", type=str, required=True, help="source data")
    parser.add_argument("--size", type=int, help="len of data preferred")

    args = parser.parse_args()
    main(
        args.data,
        args.size, 
    )