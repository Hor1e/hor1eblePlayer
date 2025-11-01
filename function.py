import os
import random
def grf(directory):
    try:                      
        files = os.listdir(directory)                         
        if not files:                        
            return None                    
        return random.choice(files)                       
                               
    except FileNotFoundError:
        return None                      
                            
                            
    except Exception as e:                      
        print(f"Произошла ошибка: {e}")
        return None                      
                            
                            

                       