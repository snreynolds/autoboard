import sys

from slacker import Slacker
email = sys.argv[1]
print ("Processing %s" % email)
tkn = sys.argv[2]
ch = sys.argv[3]

slack = Slacker(tkn)
resp = slack.users.admin.invite(tkn, "", ch)
print ("output %s" % resp)






