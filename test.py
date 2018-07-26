import zipfile
import optparse
from threading import Thread

def extract_file(zFile, psd):
    try:
        print('found password: ', psd)
        zFile.extractall(pwd=psd)
        exit(0)
    except RuntimeError:
        print('error msg: ' + str(RuntimeError) + '\n')
        # pass
def main():
    parser = optparse.OptionParser("usage%prog "+\
                                   "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', \
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', \
                      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if(options.zname == None ) | ( options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    keys = passFile.readlines()
    if keys is None:
        print('no keys')
        exit(0)
    else:
        print(keys)
    for key in keys:
        password = key.strip()
        print('get password: ' + password + '\n')
        # t = Thread(target=extract_file, args=(zFile, password))
        # t.start()
        extract_file(zFile, password)

    # keys = ['1', '12', '123', 'secret', '56']
    # for key in keys:
    #     extract_file(zFile, key)

if __name__ == '__main__':
    main()

