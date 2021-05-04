f = open('D:/folders_put_in_desktop/Taipei_Tech/Programming/project_translete_subtitle/with_opencv/data/store_place.txt')
path = f.read()
path = '/'.join(path.split('\\'))
print(path)