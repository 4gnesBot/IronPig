def GetPath():
    import os
    directory_path = os.getcwd()
    return directory_path

def txt_to_list(filepath):
    list = []
    f = open(filepath, 'r')
    list = f.readlines()

    return list

def list_to_txt(list, filepath):
        ff = open(filepath, 'w')

        for lin in list:
            if lin.__contains__("\n"):
                ff.write(lin)
            else:
                ff.write(lin + "\n")

        ff.close()

def download(url, caminho):
    import urllib.request

    urllib.request.urlretrieve(url, caminho)

def extrairTudo(arquivo, caminho):
    from zipfile import ZipFile

    z = ZipFile(arquivo, 'r')
    z.extractall(caminho)
    z.close()