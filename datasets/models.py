from pydantic import BaseModel, validator
from typing import List

dataset_labels = {"label1", "label2"}

class Dataset(BaseModel):
    """
    A Pydantic model representing a Dataset.

    Attributes:
        name (str): The name of the dataset.
        path (str): The path to the dataset.
        description (str): A brief description of the dataset.
        labels Optional[Set[str]]: Optional, predefined set of labels associated with the dataset.
        documentation (str): The documentation associated with the dataset.
    """

    name: str
    path: str
    description: str
    labels: List[str] = []
    documentation: str

    @validator("labels", pre=True, always=True)
    def validate_labels(cls, value):
        # If labels are provided, ensure they are valid labels
        if value:
            invalid_labels = set(value) - dataset_labels
            if invalid_labels:
                raise ValueError(f"Invalid labels: {', '.join(invalid_labels)}")
        return value