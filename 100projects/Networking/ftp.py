# FTP Program - A file transfer program which can transfer files back and
# forth from a remote web sever.

from ftplib import FTP, error_perm
from argparse import ArgumentParser
from getpass import getpass


def parseargs():
     # create command line options
    parser = ArgumentParser()
    parser.add_argument("-f", "--filename", help="File to be retreived or" +
                        "uploaded to remote server.")
    parser.add_argument("-s", "--host", help="remote host.")
    parser.add_argument("-r", "--retreive", help="retreive file from " +
                        "remote host")
    parser.add_argument("-t", "--upload", help="upload file to remote host.")
    args = parser.parse_args()

    return args


def createFtpConnect(server, user, passwd):

    try:
        # login to ftp server
        ftp = FTP(server)
        ftp.login(user, passwd)
        return ftp
    except:
        print(error_perm())


def ftpTransfer(filename, ftp):
    try:
        ftp.transfercmd('STOR ' + filename)
        print("Upload complete!")
    except:
        print(error_perm())


def ftpRetreive(filename, ftp, outfile=None):
    try:
        ftp.retrlines('RETR ' + filename, open(filename, 'wb').write)
        print("Download complete!")
    except:
        print(error_perm())


def login():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    return username, password


def main(args):
    # more readable names
    server = args.host
    txtfile = args.filename
    username, password = login()

    #check options
    ftp = createFtpConnect(server, username, password)
    if args.retreive:
        ftpRetreive(txtfile, ftp)
    elif args.upload:
        ftpTransfer(txtfile, ftp)


if __name__ in ['__console__', '__main__']:
    main(parseargs())