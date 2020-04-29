import requests
import time
import datetime
# ===================================

# test get all Posts

# ===================================

def case_Get_All_Posts():
    
    resp = requests.get('http://127.0.0.1:5000/posts/all')
    
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        print ('Test Get All Posts is FAILURE! or Data DOES NOT EXIST')
        return False, -1

# ===================================

# test get Post by ID

# ===================================

def case_Get_Post_By_ID(PostID):
   

    URL = 'http://localhost:5000/posts/' + f'{PostID}'
    resp = requests.get(URL)
    
    if resp.status_code == 200:
        obj = resp.json()
        return True, obj
    else:
        print (F'Test Get Data at index {PostID} is FAILURE or Data DOES NOT EXIST')
        return False, -1
    print()

# ===================================

# test get Post by community

# ===================================

def case_Get_Posts_By_Community(community, n):
    
    # http://localhost:5000/posts/Community_3?n=3

    URL = r"http://localhost:5000/posts/" + f'{community}?n={n}'

    resp = requests.get(URL)
    
    if resp.status_code == 200:

        obj = resp.json()
        return True, obj

    else:
        print (F'Test {n} recent posts by the {community} IS FAILURE or Data DOES NOT EXIST')
        return False, -1

# ===================================

# test get n Posts by times

# ===================================

def case_n_Posts_By_Time(n):

    # http://localhost:5000/posts?n=10

    URL = 'http://localhost:5000/posts?n=' + f'{n}'
    # print(URL)
    resp = requests.get(URL)
    # print('resp = ', resp)
    
    if resp.status_code == 200:
                
        obj = resp.json()

        return True, obj
    else:
        return False, -1

    print()


# ===================================

# test Post

# ===================================

def case_Post(**arg):

    # http://localhost:5000/posts?n=10

    URL = 'http://localhost:5000/posts'
    # print('arg = ', arg)

    resp = requests.post(URL, data = arg)

    # print('resp = ', resp)
    # print('resp.text = ', resp.text)
    # print('resp.status_code = ', resp.status_code)
    if resp.status_code == 201:
        return True, resp.text

    else:
        return False, -1
   
# ===================================

# test Delete by ID

# ===================================

def case_Delete(DelID):

    # http://localhost:5000/posts?n=10

    URL = r'http://localhost:5000/posts/delete/' + f'{DelID}'

    resp = requests.delete(URL)

    # print('resp = ', resp)
    # print('resp.text = ', resp.text)
    # print('resp.status_code = ', resp.status_code)


    if resp.status_code == 204:
        return True

    else:
        return False


# case_Get_Al()
# case_Get_Post_By_ID(5)
# case_Get_Posts_By_Community('Community_2', 2)
# case_n_Posts_By_Time(4)
# case_Post()
# case_Delete(10)


def addPosts():
    
    addData = [
        {
            "Username"      : "User 10",
            "PostTitle"     : "Post Title 10",
            "Content"       : "Content 10",
            "Community"     : "Community_1",
            "URLResource"   : "www.URLResource10.com"
        },
        {
            "Username"      : "User 11",
            "PostTitle"     : "Post Title 11",
            "Content"       : "Content 11",
            "Community"     : "Community_2",
            "URLResource"   : "www.URLResource11.com"
        },  
        {
            "Username"      : "User 12",
            "PostTitle"     : "Post Title 12",
            "Content"       : "Content 12",
            "Community"     : "Community_3",
            "URLResource"   : "www.URLResource12.com"
        },  
        {
            "Username"      : "User 13",
            "PostTitle"     : "Post Title 13",
            "Content"       : "Content 13",
            "Community"     : "Community_1",
            "URLResource"   : "www.URLResource13.com"
        },
        {
            "Username"      : "User 14",
            "PostTitle"     : "Post Title 14",
            "Content"       : "Content 14",
            "Community"     : "Community_2",
            "URLResource"   : "www.URLResource14.com"
        },  
        {
            "Username"      : "User 15",
            "PostTitle"     : "Post Title 15",
            "Content"       : "Content 15",
            "Community"     : "Community_3",
            "URLResource"   : "www.URLResource15.com"
        },  
        {
            "Username"      : "User 16",
            "PostTitle"     : "Post Title 16",
            "Content"       : "Content 16",
            "Community"     : "Community_1",
            "URLResource"   : "www.URLResource16.com"
        },
        {
            "Username"      : "User 17",
            "PostTitle"     : "Post Title 17",
            "Content"       : "Content 17",
            "Community"     : "Community_2",
            "URLResource"   : "www.URLResource17.com"
        },  
        {
            "Username"      : "User 18",
            "PostTitle"     : "Post Title 18",
            "Content"       : "Content 18",
            "Community"     : "Community_3",
            "URLResource"   : "www.URLResource18.com"
        },  
        {
            "Username"      : "User 19",
            "PostTitle"     : "Post Title 19",
            "Content"       : "Content 19",
            "Community"     : "Community_1",
            "URLResource"   : "www.URLResource19.com"
        } 
    ]
    for i in addData:
        isPassed, resp = case_Post(**i)
        # print(genData[i])
        time.sleep(1)

    return isPassed, resp








def main():
    # delete all Posts from 10 to 19 if exists
    # These item will be add later by different time
    DelID = 10
    # while DelID <= 19:
    #     isPassed1 = case_Delete(DelID)
    #     DelID += 1




    # add posts from 10 to 19  
    isPassed, resp = addPosts()
    
    # ============================================
    # 1. TEST GET ALL POST 
    # ============================================

    # print()
    # print('*'*50)
    # print('1. Test get all post'.upper())
    # print('*'*50)
    # print()

    isPassed, myDB = case_Get_All_Posts()
    

    # # Process the correct result from database
    # print('Correct result from database:\n')
    # print(f'Length = {len(myDB)}\n')
    # print('Post:\n')
    # for i in myDB:
    #     print(f'{i}\n')

    # print('-'*10 + '\n') # ------------------------

    # # Process result from the website

    # print('Result from test case\n')
    # print(f'Length of test case = {len(AllPost)}\n')
    # print('Post:\n')
    # for i in AllPost:
    #     print(f'{i}\n')

    # print('-'*10 + '\n') # ------------------------
    # print('Test Result: \n'.upper())

    # if isPassed and AllPost == myDB:
    #     print ('Test Get All Posts SUCCESS!\n')
        
    # else:
    #     print('Test Get All Posts is FAILURE!')

    # ============================================
    # 1. TEST GET POST AT PostID
    # ============================================

    DelID = 17

    print()
    print('*'*50)
    print(f'1. Test get Post at PostID = {DelID}')
    print('*'*50)
    print()

    # Process the correct result from database
    Answer1 = []

    for i in myDB:
        if i['PostID'] == DelID:
            Answer1.append(i)

    print('Correct result from database:\n')
    print(f'Length = {len(Answer1)}\n')
    print('Post:\n')
    print(f'{Answer1}\n')

    print('-'*10 + '\n') # ------------------------


    # Process result from the website
    isPassed, postByID = case_Get_Post_By_ID(DelID)
    if isPassed and (postByID in myDB):
        
        length = 1
        print('Result from test case\n')
        print(f'Length = {length}\n')
        print('Post:\n')
        print(f'{postByID}\n')

        print('-'*10 + '\n') # ------------------------
        print('Test Result:\n'.upper())
        print ('Test Get Posts by ID is SUCCESSFUL!\n')
    else:
        print(f'Test Posts at PostID = {DelID} is FAILURE!')



    # ============================================
    # 2. TEST GET n RECENT POST BY THE COMMUNITY
    # ============================================

    myCommunity = 'Community_2'
    n = 3

    print()
    print('*'*50)
    print(f'2. Test get {n} recent posts by the {myCommunity}')
    print('*'*50)
    print()

    # Process the correct result from database

    Answer=[]
    i = len(myDB) - 1

    while i > 0 and len(Answer) < n:
        if myDB[i]['Community'] == myCommunity:
            Answer.append(myDB[i])
            i -= 1
        else:
            i -= 1
    
    print('Correct Answer from database:\n')
    print(f'Length = {len(Answer)}\n')
    print('Post:\n')
    for i in Answer:
        print(f'{i}\n')
    
    
    print('-'*10 + '\n') # ------------------------


    # Process result from the website

    isPassed, result = case_Get_Posts_By_Community(myCommunity, n)

    print('Result from test case\n')
    print(f'Length = {len(result)}\n')
    print('Post:\n')
    
    for i in result:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------

    print('Test Result: \n'.upper())
    if isPassed and (result == Answer):
        print (f'Test Get {n} Posts by time in {myCommunity} is SUCCESSFUL!\n')
    else:
        print (f'Test Get {n} Posts by time in {myCommunity} is FAILURE!')



    
    # ============================================
    # 3. TEST GET n POST BY TIME
    # ============================================
    n = 4

    print()
    print('*'*50)
    print(f'3. Test get {n} posts by time')
    print('*'*50)
    print()

    # Process the correct result from database

    Answer=[]
    m = -n

    j = -1
    while j >= m:
        Answer.append(myDB[j])
        j -= 1
    
    print('Correct Answer from database:\n')
    print(f'Length = {len(Answer)}\n')
    print('Post:\n')
    for i in Answer:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------

    # Process result from the website
    isPassed, result = case_n_Posts_By_Time(n)

    print('Result from test case\n')
    print(f'Length = {len(result)}\n')
    print('Post:\n')

    for i in result:
        print(i)
        print()


    print('-'*10 + '\n') # ------------------------

    print('Test Result: \n'.upper())

    if isPassed and (result == Answer):
        print (f'Test Get {n} Posts by time is SUCCESSFUL!\n')
    else:
        print (f'Test Get {n} Posts by time is FAILURE!')


    # case_n_Posts_By_Time(4)




    # DelID = 10
    # while DelID <= 19:
    #     isPassed1 = case_Delete(DelID)
    #     DelID += 1
    # ============================================
    # 4. TEST POST 
    # ============================================

    print()
    print('*'*50)
    print(f'4. Test post'.upper())
    print('*'*50)
    print()

    myJSON = {
        "Username"      : "User 100",
        "PostTitle"     : "Post Title 100",
        "Content"       : "Content 100",
        "Community"     : "Community 100",
        "URLResource"   : "www.URLResource100.com"
    }   
    # ----------------------------------------------
    # Process the correct result from database
    myDB_Before_Post = myDB

    print('All posts from database BEFORE add the Post:\n')
    print(f'Length = {len(myDB_Before_Post)}\n')
    print('Post:\n')
    for i in myDB_Before_Post:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------

    # Process result from the website

    isPassed1, addJSON = case_Post(**myJSON)
    isPassed2, retrievedJson = case_Get_Posts_By_Community(myJSON['Community'], 2)
    tempBool, myDB_After_Post = case_Get_All_Posts()

    # print(myJSON['Community'])
    # print('isPassed1 = ', isPassed1)
    # print('isPassed2 = ', isPassed2)
    # print('retrievedJson = ', retrievedJson)

    print('Result from test case\n')
    print('All posts from database AFTER add the Post:\n')
    print(f'Length = {len(myDB_After_Post)}\n')
    print('Post:\n')

    for i in myDB_After_Post:
        print(f'{i}\n')

    # delta = len(myDB_After_Post)-len(myDB_Before_Post)
    # if isPassed and delta == 1:
    #     print("good")
    # case_Post(**myJson)

    print('-'*10 + '\n') # ------------------------
        
    print('Test Result: \n'.upper())

    if isPassed1 and isPassed2 == True:
        print ('Test Posts is SUCCESSFUL!\n')
    else:
        print(f'Test Posts is FAILURE!')


    # ============================================
    # 5. TEST DELETE 
    # ============================================

    DelID = 20

    print()
    print('*'*50)
    print(f'5. Test delete posts by PostID = {DelID}')
    print('*'*50)
    print()
    # ----------------------------------------------

    # Process the correct result from database
    myDB_Before_Del = myDB_After_Post

    print('All posts from database BEFORE delete the Post:\n')
    print(f'Length = {len(myDB_Before_Del)}\n')
    print('Post:\n')
    for i in myDB_Before_Del:
        print(f'{i}\n')

    print('-'*10 + '\n') # ------------------------

    # Process result from the website
    isPassed1 = case_Delete(DelID)
    isPassed2, retrievedJson = case_Get_Post_By_ID(DelID)
    tempBool, myDB_After_Del = case_Get_All_Posts()

    # print('isPassed1 = ', isPassed1)
    # print('isPassed2 = ', isPassed2)

    print('Result from test case\n')
    print('All posts from database AFTER delete the Post:\n')
    print(f'Length = {len(myDB_After_Del)}\n')
    print('Post:\n')

    for i in myDB_After_Del:
        print(f'{i}\n')


    print('-'*10 + '\n') # ------------------------
        
    print('Test Result: \n'.upper())

    if isPassed1 == True and isPassed2 == False and len(myDB_Before_Del)-len(myDB_After_Del) == 1:
        print ('Test Delete is SUCCESSFUL!\n')
    else:
        print(f'Test Delete is FAILURE!')


main()

