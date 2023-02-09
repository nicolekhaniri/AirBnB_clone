#!/usr/bin/python3
import uuid
import datetime

"""Class BaseModel that defines all common attributes/methods for other classes"""
class BaseModel:
    """Public instance attribute"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if **kwargs:
            """exists"""
            for key,value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, date_format)
                else:
                    setattr(self, key, value)

        else:
            """does not exist"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    """Public instance methods"""
    def save(self):
        """updating time to now"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary containing keys and values of instances"""
        dict_rep = self.__dict__.copy()
        dict_rep["class"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isformat()
        dict_rep["updated_at"] = self.updated_at.isformat()
        return dict_rep
    

    """This is last"""
    def __str__(self):
        """To return the str rep of BaseModel instance"""
        clsn = self.__class__.__name__
        return "[{}] ({}) {}".format(clsn, self.id, __dict__)
