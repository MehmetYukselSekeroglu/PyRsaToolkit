import rsa


def generate_rsa_key(KEYSIZE:int=4096) -> dict:
    """
    KEYSIZE -> int deafult 4096 
    
    Generate and return RSA keys 
    
    returns:
        dict :
        {
            "success":bool,
            "pub":public_key,
            "priv":private_key"
        }
    
    """
    pub_key, private_key = rsa.newkeys(KEYSIZE)

    return {
        "success":True,
        "pub":pub_key,
        "priv":private_key
    }