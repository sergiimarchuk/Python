

```python
#!/usr/bin/python

import sys, pexpect

def get_passwd():
        """Generates password for Oracle.
        - should begins with letter
        - should contain only letters and numbers
        """
        import random
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pw_length = 11
        first_letter = ""
        mypw = ""

        first_letter_index = random.randrange(len(letters))
        first_letter = letters[first_letter_index]

        for i in range(pw_length):
                next_index = random.randrange(len(alphabet))
                mypw = mypw + alphabet[next_index]

        final_pass = str(first_letter) + str(mypw)
        return final_pass

#newuser = "newuserA21"

def add_user():
        try:
                if len(sys.argv[1]) > 3: 
                        newuser = sys.argv[1]
                
                        password = get_passwd()

                        child = pexpect.spawn("pwsafe -f /root/.pwsafe.dat --add %s" % newuser)
                        child.expect ('passphrase')
                        child.sendline ('123456')
                        child.expect ('group')
                        child.sendline ('admin')
                        child.expect ('username:')
                        child.sendline (newuser)
                        child.expect ('password')
                        child.sendline (password)
                        child.expect ('again:')
                        child.sendline (password)
                        child.expect ('notes:')
                        child.sendline ('admin user')
                        child.expect(pexpect.EOF)
                        print "User   " + newuser + "    was created in pwsafe."
                        #print child.before
                        #print len(sys.argv[1]),"newuser is  ___",newuser
                else:
                        print 'Argument has to be longer then 3 symbol' #,len(sys.argv[1]),"   --",str(sys.argv[1:])
        except IndexError:

                print "Please input argument. "
                sys.exit()


main = add_user()



#!/usr/bin/python

import sys, pexpect

def add_user():
        newuser = sys.argv[1]
        child = pexpect.spawn("pwsafe -f /root/.pwsafe.dat --list %s" % newuser)
        child.expect ('passphrase')
        child.sendline ('123456')
        child.expect(pexpect.EOF)
        #print (((child.before).split("\n")[1]).split(".")[1])
        print "00000:",newuser,"          ..",(((child.before).split("\n")[1]).split(".")[1])
        if newuser is ((child.before).split("\n")[1]).split(".")[1]:
                print "Found user in SYSDB ",newuser
        #else:
        #       print "User was not found in SYSDB."
        #print len(sys.argv[1]),"newuser is  ___",newuser

        print "aaaaa"
main = add_user()




