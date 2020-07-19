from boxsdk import OAuth2, Client
import subprocess
import random
from boxsdk import JWTAuth
import time
auth = JWTAuth(
    client_id='t7o9oknjyfmavpz2vq8qyeh2tq3bgwkc',
    client_secret='tYjGJzz1iMiPA2JBW6csMyAFEXPrUj2c',
    enterprise_id='511092066',
    jwt_key_id='u4zebqgi',
    rsa_private_key_file_sys_path='private.pem'
)

access_token = auth.authenticate_instance()

client = Client(auth)

Supportid = random.randint(0000000000, 999999999)

def upload():
    auth = JWTAuth(
    client_id='t7o9oknjyfmavpz2vq8qyeh2tq3bgwkc',
    client_secret='tYjGJzz1iMiPA2JBW6csMyAFEXPrUj2c',
    enterprise_id='511092066',
    jwt_key_id='u4zebqgi',
    rsa_private_key_file_sys_path='private.pem'
)

    access_token = auth.authenticate_instance()

    client = Client(auth)

    user_to_impersonate = client.user(user_id='13315944066')
    client = client.as_user(user_to_impersonate)

    user = client.user().get()
    print('The current user ID is {0}'.format(user.id))

    subfolder = client.folder('0').create_subfolder(str(Supportid))
    print('Created subfolder with ID {0}'.format(subfolder.id))

    cmdfile = client.folder(subfolder.id).upload('specs-cmd.txt')
    print('File "{0}" uploaded to Circuit Technical Spec Storage with file ID {1}'.format(cmdfile.name, cmdfile.id))

    psfile = client.folder(subfolder.id).upload('specs-ps.txt')
    print('File "{0}" uploaded to Circuit Technical Spec Storage with file ID {1}'.format(psfile.name, psfile.id))
    pass

def showspecs():
    subprocess.run("SpecShow.cmd")
    print("This Data Will Be Sent To Circuit Technical. Do you want to continue?")
    specnotice = input("Type y for Yes and type n for No: ")
    if specnotice == "y":
        print("Thank You. Now Uploading...")
        pass
    elif specnotice == "n":
        print("Thank You. SpecSend Will Now Exit")
        exit()
        pass
    pass

def savespecs():
    subprocess.run("SpecSave.cmd")
    pass


print("NOTICE: This Application Sends Sytem Data To Circuit Technical")
uploadnotice = input("Type y for Yes and type n for No: ")

if uploadnotice == "y":
  print("Thank you")
  showspecs()
  savespecs()
  upload()
  print("Your Circuit Technical Support ID is: " + str(Supportid))
  subprocess.Popen("wscript SpecDialog.vbs " + str(Supportid))
  pass
elif uploadnotice == "n" :
    print("Thank you. SpecSend will now exit.")
    exit()


