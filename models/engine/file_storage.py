#!/usr/bin/python3
import json

"""Class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""
class FileStorage:
    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    """Public instance methods"""
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            saves = {}
            for key, value in FileStorage.__objects.items():
                saves[key] = value.to_dict()
            json.dump(saves ,f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                objects_dict = json.load(f)
                for key, value in objects_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**obj_dict)
                    if class_name == "User":
                         FileStorage.__objects[key] = User(**obj_dict)
                    if class_name == "Place":
                         FileStorage.__objects[key] = Place(**obj_dict)
                    if class_name == "State":
                         FileStorage.__objects[key] = State(**obj_dict)
                    if class_name == "City":
                         FileStorage.__objects[key] = City(**obj_dict)
                    if class_name == "Amenity":
                         FileStorage.__objects[key] = Amenity**obj_dict)
                    if class_name == "Review":
                         FileStorage.__objects[key] = Review(**obj_dict)
        except FileNotFoundError:
            pass
