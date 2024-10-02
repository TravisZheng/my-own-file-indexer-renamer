import codecs

def convert_encoding(source, destination):
    with codecs.open(source, 'r', encoding='<euc-kr>') as f:  # replace '<your-file-encoding>' with the original file encoding like 'GBK', 'UTF-8' etc.
        content = f.read()

    with codecs.open(destination, 'w', encoding='utf-8-sig') as f:  # utf-8-sig will automatically write BOM for UTF-8
        f.write(content)

convert_encoding('file_index.txt', 'file_index_utf8.txt')
