# FTP Program - A file transfer program which can transfer files back and
#forth from a remote web sever.

from ftplib import FTP
from argparse import ArgumentParser


def parseargs():
     # create command line options
    parser = ArgumentParser()
    parser.add_argument("-f", "--filename", help="File to be retreived or" +
                        "uploaded to remote server.")
    parser.add_argument("-u", "--username", help="username for remote host.")
    parser.add_argument("-s", "--host", help="remote server.")
    parser.add_argument("-p", "--password", help="password for remote host.")
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
        return "Could not connect to remote server"


def ftpTransfer(filename, ftp):
    try:
        ftp.transfercmd('STOR ' + filename)
        return "Upload complete!"
    except:
        return "Upload failed!"


def ftpRetreive(filename, ftp, outfile=None):
    try:
        ftp.retrlines('RETR ' + filename, open(filename, 'wb').write)
        return "Download complete!"
    except:
        return "Download failed!"


def main(args):
    # more readable names
    server = args.host
    username = args.username
    password = args.password
    txtfile = args.filename

    #check options
    ftp = createFtpConnect(server, username, password)
    if args.retreive:
        ftpRetreive(txtfile, ftp)
    elif args.upload:
        ftpTransfer(txtfile, ftp)


if __name__ in ['__console__', '__main__']:
    main(parseargs())