#!/usr/bin/env python3
# ================================
# KP FILE CLONE - Kali Linux Edition
# Author: MYANMAR (KP)
# Edited for Linux by ChatGPT
# ================================

import os, re, random, uuid, time, json, sys
from concurrent.futures import ThreadPoolExecutor as threadpol

# ===============================
# BASE DIRECTORY (Linux Storage)
# ===============================

BASE_DIR = os.path.expanduser("~/kp_file_clone")
os.makedirs(BASE_DIR, exist_ok=True)

TOKEN_FILE = os.path.join(BASE_DIR, ".MrSxR_TkN.txt")
TMP_FILE = os.path.join(BASE_DIR, ".MrSxR_UNLiMTD.txt")
SEP_FILE = os.path.join(BASE_DIR, ".MrSxR_SPrT.txt")

# ===============================
# INSTALL LIBRARIES
# ===============================

try:
    import requests
except:
    os.system("pip3 install requests")
    import requests

try:
    from bs4 import BeautifulSoup as bs
except:
    os.system("pip3 install bs4")
    from bs4 import BeautifulSoup as bs


# ===============================
# COLOR VARIABLES
# ===============================

a = "\033[1;97m"; b = "\033[1;92m"; c = "\033[1;91m"
f = "\033[1;96m"; j = "\x1b[38;5;208m"

l1 = f"{b}[{c}1{b}]"; l2 = f"{b}[{c}2{b}]"
l3 = f"{b}[{c}3{b}]"; l4 = f"{b}[{c}4{b}]"
l5 = f"{b}[{c}5{b}]"; l6 = f"{b}[{c}6{b}]"
l7 = f"{b}[{c}7{b}]"; l8 = f"{b}[{c}8{b}]"
l0 = f"{b}[{c}0{b}]"; ekl = f"{f}:{a}"

sxrline = f"{f}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"


# ===============================
# GLOBAL DATA
# ===============================

id_alx = []
extrt = []

sm_hni = str(random.randint(20000, 40000))
bnd_wh = str(random.randint(20000000, 30000000))
trc_id = str(uuid.uuid4())


# ===============================
# USER AGENT GENERATOR
# ===============================

def uaua():
    fbav = "485.0.0.0.51"
    fbbv = "456005032"
    phone = random.choice(["Samsung","OPPO","Infinix","OnePlus"])
    model = "SM-A515F"

    return f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBMF/{phone};FBDV/{model};]"

ua = uaua()


# ===============================
# STATUS CHECK
# ===============================

def ck_sttus():

    try:
        token = open(TOKEN_FILE).read()
    except:
        return "None"

    try:
        uid = "61565919664817"

        data = {
            "User-Agent": ua,
            "method": "post",
            "format": "json",
            "variables": f'{{"profile_id":{uid}}}'
        }

        headers = {
            "Authorization": f"OAuth {token}"
        }

        r = requests.post("https://graph.facebook.com/graphql",
                          headers=headers, data=data).json()

        if "data" in r:
            return "Active"

        return "Expire"

    except:
        return "Expire"


# ===============================
# LOGO
# ===============================

def clr_logo(stts=True):

    global status

    if stts:
        status = ck_sttus()

    os.system("clear")

    print(f"""{b}

   KP FILE CLONE (Linux Edition)

{sxrline}
 Developer : KP
 Folder    : {BASE_DIR}
 Status    : {status}
{sxrline}
""")


# ===============================
# MAIN MENU
# ===============================

def sxr_main():

    clr_logo(True)

    if "Active" in status:

        print(f"""
 {l1} MAKE DUMP FILE
 {l2} DUPLICATE REMOVE
 {l3} REMOVE STYLIST NAME
 {l4} REMOVE FIRST IDS
 {l5} SEPARATE IDS
 {l6} SEPARATE NAMES
 {l7} DIVIDE FILE
 {l8} REMOVE TOKEN
 {l0} EXIT
{sxrline}
""")

        ch = input(" Choose : ")

        if ch == "1": smpl_fbmkr()
        elif ch == "2": duplicte_rmv()
        elif ch == "3": stylist_rmv()
        elif ch == "4": line_rmv()
        elif ch == "5": saprt_ids()
        elif ch == "6": saprt_nam()
        elif ch == "7": divider()
        elif ch == "8": ckki_rmv()
        elif ch == "0": exit()

    else:

        print(f"""
 {l1} LOGIN TOKEN
 {l2} DUPLICATE REMOVE
 {l3} REMOVE STYLIST NAME
 {l4} REMOVE FIRST IDS
 {l5} SEPARATE IDS
 {l6} SEPARATE NAMES
 {l7} DIVIDE FILE
 {l8} REMOVE TOKEN
 {l0} EXIT
{sxrline}
""")

        ch = input(" Choose : ")

        if ch == "1": login_tkkn()
        elif ch == "2": duplicte_rmv()
        elif ch == "3": stylist_rmv()
        elif ch == "4": line_rmv()
        elif ch == "5": saprt_ids()
        elif ch == "6": saprt_nam()
        elif ch == "7": divider()
        elif ch == "8": ckki_rmv()
        elif ch == "0": exit()


# ===============================
# LOGIN TOKEN
# ===============================

def login_tkkn():

    token = input(" Enter Token : ")

    open(TOKEN_FILE,"w").write(token)

    print(" Login Saved")

    time.sleep(1)

    sxr_main()


# ===============================
# SIMPLE DUMP
# ===============================

def smpl_fbmkr():

    clr_logo(False)

    token = open(TOKEN_FILE).read()

    fname = input(" File name : ")

    save_file = os.path.join(BASE_DIR, fname)

    if os.path.exists(save_file):
        os.remove(save_file)

    print(" Paste UIDs (blank to stop)")

    while True:

        x = input()

        if x == "":
            break

        id_alx.append(x.split("|")[0])


    with threadpol(max_workers=20) as ex:

        total = len(id_alx)

        for uid in id_alx:

            ex.submit(simpl_lop, uid, token, save_file, total)

    print("\n DONE:", save_file)

    input(" Enter...")

    sxr_main()


def simpl_lop(uid, token, file, total):

    try:

        data = {
            "User-Agent": ua,
            "method": "post",
            "format": "json",
            "variables": f'{{"profile_id":{uid}}}'
        }

        headers = {
            "Authorization": f"OAuth {token}"
        }

        r = requests.post("https://graph.facebook.com/graphql",
                          headers=headers, data=data).json()

        if "data" not in r:
            return

        open(file,"a").write(uid+"\n")

        extrt.append(uid)

        print(f"[{len(extrt)}/{total}] {uid}")

    except:
        pass


# ===============================
# FILE CLEAN
# ===============================

def clean_file(path):

    lines = []

    with open(path,"rb") as f:

        for l in f:

            try:
                lines.append(l.decode())
            except:
                pass

    with open(path,"w") as f:
        f.writelines(lines)


# ===============================
# DUPLICATE REMOVE
# ===============================

def duplicte_rmv():

    clr_logo(False)

    path = input(" File Path : ")

    clean_file(path)

    lines = list(set(open(path).readlines()))

    open(path,"w").writelines(lines)

    print(" Done")

    input()

    sxr_main()


# ===============================
# STYLIST REMOVE
# ===============================

def stylist_rmv():

    clr_logo(False)

    path = input(" File Path : ")

    clean_file(path)

    rg = re.compile(r'[#@%&*+()!":;/\\?,<>{}_~`$^\[\]=]')

    new = []

    for l in open(path):

        if not rg.search(l):
            new.append(l)

    open(path,"w").writelines(new)

    print(" Done")

    input()

    sxr_main()


# ===============================
# REMOVE FIRST IDS
# ===============================

def line_rmv():

    clr_logo(False)

    path = input(" File Path : ")

    n = int(input(" Remove First : "))

    lines = open(path).readlines()

    open(path,"w").writelines(lines[n:])

    print(" Done")

    input()

    sxr_main()


# ===============================
# SEPARATE IDS
# ===============================

def saprt_ids():

    clr_logo(False)

    path = input(" File Path : ")

    out = input(" Output File : ")

    key = input(" UID Part : ")

    data = []

    rem = []

    for l in open(path):

        if key in l:
            data.append(l)
        else:
            rem.append(l)

    open(out,"w").writelines(data)

    open(path,"w").writelines(rem)

    print(" Done")

    input()

    sxr_main()


# ===============================
# SEPARATE NAME
# ===============================

def saprt_nam():

    clr_logo(False)

    path = input(" File Path : ")

    out = input(" Output File : ")

    key = input(" Name : ").lower()

    a1=[]; a2=[]

    for l in open(path):

        if key in l.lower():
            a1.append(l)
        else:
            a2.append(l)

    open(out,"w").writelines(a1)

    open(path,"w").writelines(a2)

    print(" Done")

    input()

    sxr_main()


# ===============================
# DIVIDER
# ===============================

def divider():

    clr_logo(False)

    path = input(" File Path : ")

    parts = int(input(" Parts : "))

    lines = open(path).readlines()

    size = len(lines)//parts

    for i in range(parts):

        name = input(f" Output {i+1} : ")

        open(name,"w").writelines(lines[i*size:(i+1)*size])

    print(" Done")

    input()

    sxr_main()


# ===============================
# REMOVE TOKEN
# ===============================

def ckki_rmv():

    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)

    print(" Token Removed")

    time.sleep(1)

    sxr_main()


# ===============================
# START
# ===============================

sxr_main()
