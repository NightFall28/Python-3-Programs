# reverse file content

def file_reverse(file_object):
    file_text = file_object.read()
    file_text = file_text[::-1]
    file_object.seek(0)
    file_object.write(file_text)
    file_object.flush()
    return file_object

file_object = open("random.txt","r+")
file_reverse(file_object)
