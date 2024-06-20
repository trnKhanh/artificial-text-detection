import json
import os


class SQuADDataset(object):
    valid_path = "dev-v2.0.json"
    train_path = "train-v2.0.json"

    def __init__(self, root: str, mode:str="train"):
        self.root = root
        self.mode = mode

        self.data = self.__read_data(root)

    def __read_data(self, root: str):
        if self.mode == "train":
            data_path = self.train_path
        elif self.mode == "valid":
            data_path = self.valid_path
        else:
            raise NameError(
                f"{self.mode} is not a valid mode for SQuADDataset"
            )

        with open(os.path.join(root, data_path), "r") as f:
            data = json.load(f)

        return data
