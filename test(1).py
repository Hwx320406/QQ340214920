import requests
login_url ='http://192.168.3.148/admin.php?m=mgr/admin.chklogin&ajax=1'
add_url = 'http://192.168.3.148/admin.php?m=mgr/member2.saveMemberInfo&id='


def login():
    data = {
        'username':'admin',
        'password':'admin',
    }
    ## 登陆业务
    result = requests.post(url=login_url,data=data)
    # 方法一
    r1 = result.cookies
    pid = r1['PHPSESSID']
    return pid


def add_teacher(pid):
    cookie = {
        'PHPSESSID': pid
    }
    add_data = dict(
        username = '001',
        realname = 'nibaba',
        password = '12345678',
        sex = '0',
        roleid = '5',
        orid1 = '24',
        email = 'aaa%40qq.com',
        phone = '13888888888',
        location_p = '%E5%8C%97%E4%BA%AC%E5%B8%82&',
        location_c = '%E5%B8%82%E8%BE%96%E5%8E%BF&',
        location_a = '%E5%AF%86%E4%BA%91%E5%8E%BF&',
        address = 'haha+',
        introduce = 'dddd',
        type = '1'
    )

    ## 添加教师
    r2 = requests.post(url=add_url,cookies=cookie,data=add_data)
    print(r2.text)


def run_main():
    pid = login()
    add_teacher(pid)

if __name__ == '__main__':
    run_main()
