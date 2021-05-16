import sys, os, traceback
import subprocess

def isUserAdmin():

    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False

def runAsAdmin(cmdLine):

    import win32con
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon

    showCmd = win32con.SW_HIDE
    lpVerb = 'runas'

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmdLine )

    p=input("Enter profile")
    print(subprocess.check_output(['netsh', 'wlan', 'show', 'profile',p,'Key=CLEAR']).decode('utf-8'))


def test():
    if not isUserAdmin():
        print("You're not an admin.")
        runAsAdmin((subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')))
    else:
        print("You are an admin!")

test()