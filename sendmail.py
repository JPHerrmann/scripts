#!/usr/bin/python
# send email with python, through gmail!
# @author <bprinty@gmail.com>
# --------------------------------------

# imports
import smtplib
import argparse
import sys
from email.MIMEText import MIMEText

# args
usage = 'usage: sendmail.py [options] --to <theirs@email.com> --user <yours@gmail.com> --password <yourpass> --message <msgfile>' 
parser = argparse.ArgumentParser( usage=usage )
parser.add_argument( "-t", "--to", help="recipient of email", default=False )
parser.add_argument( "-f", "--user", help="sender of email", default=False )
parser.add_argument( "-p", "--password", help="password for sender", default=False )
parser.add_argument( "-m", "--message", help="file with message to send", default=False )
parser.add_argument( "-s", "--subject", help="subject line for email", default=None )
args = parser.parse_args()

# stoopid check
if not args.to or not args.user or not args.password or not args.message:
    sys.exit( usage )

# reading message
message = []
for l in open( args.message, 'r' ):
    message.append( l.rstrip() )
message = '\n'.join(message)

# composing email
message = MIMEText( message, 'plain' )
message['Subject'] = args.subject

# sending mail
server = smtplib.SMTP( 'smtp.gmail.com', 587 )
server.ehlo()
server.starttls()
server.ehlo()
server.login( args.user, args.password )
server.sendmail( args.user, args.to, message.as_string() )
server.rset()
server.quit()

