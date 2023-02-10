from typing import Any, Mapping
import toml

class venv_builder:
    def __init__(self, type):
        self.config_file="./templates/"+type+".toml"

    def load_config(self):
        parsed_conf:dict=toml.load(self.config_file)
        return [new_instance(venv, parsed_conf[element]) for element in parsed_conf if type(parsed_conf[element]) is dict and element.__contains__('venv')]



class venv:
    def __repr__(self) -> str:
        return str([a for a in dir(self) if not a.startswith('__')])
    
    def create():
        #Create venv

        #import dependancies



def new_instance(of: type, with_fields: Mapping[str, Any]):
    obj = of.__new__(of)
    for attr, value in with_fields.items():
        setattr(obj, attr, value)
    return obj


if __name__=="__main__":
    testvenv = venv_builder("example")
    print(testvenv.load_config()[0].get_build_version())