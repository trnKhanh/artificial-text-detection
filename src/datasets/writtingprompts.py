import os


class WrittingPromptsDataset(object):
    train_path = ["train.wp_source", "train.wp_target"]
    valid_path = ["valid.wp_source", "valid.wp_target"]
    test_path = ["test.wp_source", "test.wp_target"]

    def __init__(self, root: str, mode: str = "train"):
        self.root = root
        self.mode = mode

        self.data = self.__read_data(root)

    def __read_data(self, root: str):
        if self.mode == "train":
            data_path = self.train_path
        elif self.mode == "valid":
            data_path = self.valid_path
        elif self.mode == "test":
            data_path = self.test_path
        else:
            raise NameError(
                f"{self.mode} is not a valid mode for WrittingPromptsDataset"
            )

        data = dict()

        with open(os.path.join(root, data_path[0]), "r") as f:
            lines = f.readlines()
            data["prompts"] = [line[7:] for line in lines]

        with open(os.path.join(root, data_path[1]), "r") as f:
            lines = f.readlines()
            data["stories"] = [line for line in lines]

        return data
