import random
import os
import time

num='abcdefghijklmnopqrstuvwxyz1234567890'
a=input("Enter the password:")
li_pass=list(a)
li_num=list(num)

print("Applying brute force attack.....")
getpass=""
time_elapsed=time.time()
for i in num:

    for j in num:

        for k in num:
            # getpass=i+j+k
            # if getpass==a:
            #     print("Your password is=", getpass)
            #     return

            for l in num:
                # getpass=i+j+k+l
                # if getpass==a:
                #     print("Your password is=", getpass)
                #     return

                for m in num:
                    getpass = i+j+k+l+m
                    if getpass == a:
                        print("Your password is=", getpass)
                        print(time.time()-time_elapsed)
                        exit()

                    # for n in num:
                    #     getpass = i+j+k+l+m+n
                    #     if getpass == a:
                    #         print("Your password is=", getpass)
                    #         print(time.time() - time_elapsed)
                    #
                    #
                    #     for o in num:
                    #         getpass = i+j+k+l+m+n+o
                    #         if getpass == a:
                    #             print("Your password is=", getpass)
                    #             return
                    #
                    #         for p in num:
                    #             getpass = i+j+k+l+m+n+o+p
                    #             if getpass == a:
                    #                 print("Your password is=", getpass)
                    #                 return
                    #
                    #             for q in num:
                    #                 getpass = i+j+k+l+m+n+o+p+q
                    #                 if getpass == a:
                    #                     print("Your password is=", getpass)
                    #                     return
                    #
                    #                 for r in num:
                    #                     getpass = i+j+k+l+m+n+o+p+q+r
                    #                     if getpass == a:
                    #                         print("Your password is=", getpass)
                    #                         return






