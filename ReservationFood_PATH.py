PATH = {
    'main_page' : {
        'samaneMorvarid' : '/html/body/div[2]/div/section[2]/div/div[2]/div[2]/div/div[1]/a[1]'
    },
    'dashbord' :{
        'vorodBeSamane' : '//*[@id="agLoad"]/div/div/app-root/app-profile-public/div/app-public/mat-sidenav-container/mat-sidenav-content/div/div/div[2]/mat-list[1]/div/mat-grid-list/div/mat-grid-tile[1]/div/div/a'
    },
    'login_page' : {
        'username' : 'mat-input-0',
        'password' : "mat-input-1",
        'vorod' : "/html/body/div[1]/div/div/app-root/app-singin/div/app-singin-user/div/div/div[2]/form/div[1]/div[2]/div/mat-card-content/div/mat-card-actions/div/button"   
    },
    'user_panel' :{
        'tabligh' : "/html/body/div[1]/div/div/app-root/app-main/div/app-dashboard/mat-sidenav-container/mat-sidenav-content/div/div[1]/div/mat-tab-group/mat-tab-header/div/div/div/div[2]/div/div/div[3]/mat-icon",
        'omorTaghzie' : "/html/body/div[1]/div/div/app-root/app-profile-std/div/app-std/div/div[2]/div/app-search-menu/div/div[2]/mat-list/mat-grid-list/div/mat-grid-tile[4]/div/div/div/a",
    },
    'omorTaghzie' :{
        'rezervGhaza' : "/html/body/div[1]/div/div/app-root/app-profile-std/div/app-std/div/div[2]/div/app-search-menu/div/div[2]/mat-list/mat-grid-list/div/mat-grid-tile[1]/div/div/div/a",
    },
    'rezervGhaza' : {
        'rezervGhaza_frame' : 'iframe_4825',
        'male_list' : '//*[@id="Meal_Drp"]',
        'select_diner' : '/html/body/form/div[3]/div[2]/div[2]/select/option[2]'
    }
}




def get_PATH (part , element):

    return PATH[part][element]
