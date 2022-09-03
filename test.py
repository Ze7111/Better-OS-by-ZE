try:
    import
except Exception as e:
    import os
    string = str(e)
    module = string.split("'")[1].split("'")[0]
    os.system(f'pip install {module}')