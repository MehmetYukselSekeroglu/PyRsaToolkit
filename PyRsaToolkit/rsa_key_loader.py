import rsa
import os


def loadPrivateKey(private_key_file_path:str) -> dict:
    if not os.path.exists(private_key_file_path):
        return {
            "success": False,
            "message": f"{private_key_file_path} not found"
        }
        
    with open(private_key_file_path, "rb") as private_key_file:
        key_data = private_key_file.read()
        key_data = rsa.PrivateKey.load_pkcs1(key_data)
        return {
            "success":True,
            "data": key_data
        }
        


def loadPublicKey(public_key_file_path:str) -> dict:
    if not os.path.exists(public_key_file_path):
        return {
            "success" : False,
            "message" : f"{public_key_file_path} not found"
        }
    
    with open(public_key_file_path, "rb") as public_key_file:
        key_data = public_key_file.read()
        key_data = rsa.PublicKey.load_pkcs1(key_data)
        return {
            "success" : True,
            "data": key_data
        }