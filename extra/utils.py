import os


def check_users(cdir):
    '''To check for the Numbers of usersand directory in the datasets.'''
    print("\nFor ", cdir)
    lst_celeb = os.listdir(cdir)
    tot_celeb = len(lst_celeb)
    total["Users"]+= tot_celeb
    print('Total User - ', tot_celeb)


    tot = 0
    dcel = {}
    for cel in lst_celeb:
        dcel[cel]= len(os.listdir(cdir+cel))
        tot += dcel[cel]

    total["Images"] += tot
    print('Total Images - ', tot, '\nAvg Img/user - ', tot/tot_celeb)