import boto3
import __future__ # print_function,  Python 2/3 compatibility
import datetime

from flask_dynamo import Dynamo
from flask import Flask
import flask_api
from flask import request
from flask_api import status, exceptions

# ==============================================================================================
# Method
# ==============================================================================================

def Create_Table(table_name, dynamodb_client, dynamodb_resource):
    myTable = dynamodb_client.create_table(
            
        TableName = table_name,

        AttributeDefinitions=[
            {
                'AttributeName': 'PostID',
                'AttributeType': 'N'
            }                        
        ],

        KeySchema=[
            {
                'AttributeName': 'PostID',
                'KeyType': 'HASH'

            },
        ],      #End KeySchema

        ProvisionedThroughput = {
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 100,
        }
    )

    # Wait until the table exists.
    dynamodb_resource.meta.client.get_waiter('table_exists').wait(TableName=table_name)

def Delete_Table(table_name, dynamodb_resource):
    delTable = dynamodb_resource.Table(table_name)
    delTable.delete()

def List_All_Table(dynamodb_client):
    existing_tables = dynamodb_client.list_tables()['TableNames']
    return existing_tables

def Table_Status(table_name, dynamodb_resource):
    myTable = dynamodb_resource.Table(table_name)
    status = myTable.table_status
    return status
    
def Table_Length(table_name, dynamodb_resource):
    myTable = dynamodb_resource.Table(table_name)
    table_length = myTable.item_count
    return table_length

def Scan_Table (table_name, dynamodb_resource):
    all_posts = []
    myTable = dynamodb_resource.Table(table_name)

    scanResponse = myTable.scan(TableName=table_name)
    items = scanResponse['Items']
    items.sort()
    i = 0
    while i < len(items):
        all_posts.append (items[i])
        i += 1
    return all_posts

def Create_Post (table_name, dynamodb_resource, username, posttitle, content, community, urlresource):
    table_length = Table_Length(table_name, dynamodb_resource)
    if table_length == 0:
        last_PostID = 0
    else:
        all_Posts = Get_All_Posts(table_name, dynamodb_resource)
        last_PostID = 1

        for post in all_Posts:
            if post['PostID']> last_PostID:
                last_PostID = post['PostID']

    currentID = last_PostID + 1

    now = datetime.datetime.now()
    strNow = str(now)

    input_json = {
        'PostID'      : currentID, 
        'Username'    : username,
        'PostTitle'   : posttitle,
        'PostDate'    : strNow,
        'Content'     : content,
        'Community'   : community,
        'URLResource' : urlresource,
    }

    myTable = dynamodb_resource.Table(table_name)

    myTable.put_item(Item = input_json)
    return input_json

def Initial_Posts(table_name, dynamodb_resource):
    input_json = Create_Post (table_name, dynamodb_resource, 'User 001', 'Post Title 001', 'Content 001', 'school', 'www.URLResource001.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 002', 'Post Title 002', 'Content 002', 'home', 'www.URLResource002.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 003', 'Post Title 003', 'Content 003', 'workplace', 'www.URLResource003.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 004', 'Post Title 004', 'Content 004', 'school', 'www.URLResource004.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 005', 'Post Title 005', 'Content 005', 'home', 'www.URLResource005.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 006', 'Post Title 006', 'Content 006', 'workplace', 'www.URLResource006.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 007', 'Post Title 007', 'Content 007', 'school', 'www.URLResource007.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 008', 'Post Title 008', 'Content 008', 'home', 'www.URLResource008.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 009', 'Post Title 009', 'Content 009', 'workplace', 'www.URLResource009.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 010', 'Post Title 010', 'Content 010', 'school', 'www.URLResource010.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 011', 'Post Title 011', 'Content 011', 'home', 'www.URLResource011.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 012', 'Post Title 012', 'Content 012', 'workplace', 'www.URLResource012.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 013', 'Post Title 013', 'Content 013', 'school', 'www.URLResource013.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 014', 'Post Title 014', 'Content 014', 'home', 'www.URLResource014.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 015', 'Post Title 015', 'Content 015', 'workplace', 'www.URLResource015.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 016', 'Post Title 016', 'Content 016', 'school', 'www.URLResource016.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 017', 'Post Title 017', 'Content 017', 'home', 'www.URLResource017.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 018', 'Post Title 018', 'Content 018', 'workplace', 'www.URLResource018.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 019', 'Post Title 019', 'Content 019', 'school', 'www.URLResource019.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 020', 'Post Title 020', 'Content 020', 'home', 'www.URLResource020.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 021', 'Post Title 021', 'Content 021', 'workplace', 'www.URLResource021.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 022', 'Post Title 022', 'Content 022', 'school', 'www.URLResource022.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 023', 'Post Title 023', 'Content 023', 'home', 'www.URLResource023.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 024', 'Post Title 024', 'Content 024', 'workplace', 'www.URLResource024.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 025', 'Post Title 025', 'Content 025', 'school', 'www.URLResource025.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 026', 'Post Title 026', 'Content 026', 'home', 'www.URLResource026.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 027', 'Post Title 027', 'Content 027', 'workplace', 'www.URLResource027.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 028', 'Post Title 028', 'Content 028', 'school', 'www.URLResource028.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 029', 'Post Title 029', 'Content 029', 'home', 'www.URLResource029.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 030', 'Post Title 030', 'Content 030', 'workplace', 'www.URLResource030.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 031', 'Post Title 031', 'Content 031', 'school', 'www.URLResource031.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 032', 'Post Title 032', 'Content 032', 'home', 'www.URLResource032.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 033', 'Post Title 033', 'Content 033', 'workplace', 'www.URLResource033.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 034', 'Post Title 034', 'Content 034', 'school', 'www.URLResource034.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 035', 'Post Title 035', 'Content 035', 'home', 'www.URLResource035.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 036', 'Post Title 036', 'Content 036', 'workplace', 'www.URLResource036.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 037', 'Post Title 037', 'Content 037', 'school', 'www.URLResource037.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 038', 'Post Title 038', 'Content 038', 'home', 'www.URLResource038.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 039', 'Post Title 039', 'Content 039', 'workplace', 'www.URLResource039.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 040', 'Post Title 040', 'Content 040', 'school', 'www.URLResource040.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 041', 'Post Title 041', 'Content 041', 'home', 'www.URLResource041.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 042', 'Post Title 042', 'Content 042', 'workplace', 'www.URLResource042.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 043', 'Post Title 043', 'Content 043', 'school', 'www.URLResource043.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 044', 'Post Title 044', 'Content 044', 'home', 'www.URLResource044.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 045', 'Post Title 045', 'Content 045', 'workplace', 'www.URLResource045.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 046', 'Post Title 046', 'Content 046', 'school', 'www.URLResource046.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 047', 'Post Title 047', 'Content 047', 'home', 'www.URLResource047.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 048', 'Post Title 048', 'Content 048', 'workplace', 'www.URLResource048.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 049', 'Post Title 049', 'Content 049', 'school', 'www.URLResource049.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 050', 'Post Title 050', 'Content 050', 'home', 'www.URLResource050.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 051', 'Post Title 051', 'Content 051', 'workplace', 'www.URLResource051.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 052', 'Post Title 052', 'Content 052', 'school', 'www.URLResource052.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 053', 'Post Title 053', 'Content 053', 'home', 'www.URLResource053.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 054', 'Post Title 054', 'Content 054', 'workplace', 'www.URLResource054.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 055', 'Post Title 055', 'Content 055', 'school', 'www.URLResource055.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 056', 'Post Title 056', 'Content 056', 'home', 'www.URLResource056.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 057', 'Post Title 057', 'Content 057', 'workplace', 'www.URLResource057.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 058', 'Post Title 058', 'Content 058', 'school', 'www.URLResource058.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 059', 'Post Title 059', 'Content 059', 'home', 'www.URLResource059.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 060', 'Post Title 060', 'Content 060', 'workplace', 'www.URLResource060.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 061', 'Post Title 061', 'Content 061', 'school', 'www.URLResource061.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 062', 'Post Title 062', 'Content 062', 'home', 'www.URLResource062.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 063', 'Post Title 063', 'Content 063', 'workplace', 'www.URLResource063.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 064', 'Post Title 064', 'Content 064', 'school', 'www.URLResource064.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 065', 'Post Title 065', 'Content 065', 'home', 'www.URLResource065.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 066', 'Post Title 066', 'Content 066', 'workplace', 'www.URLResource066.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 067', 'Post Title 067', 'Content 067', 'school', 'www.URLResource067.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 068', 'Post Title 068', 'Content 068', 'home', 'www.URLResource068.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 069', 'Post Title 069', 'Content 069', 'workplace', 'www.URLResource069.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 070', 'Post Title 070', 'Content 070', 'school', 'www.URLResource070.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 071', 'Post Title 071', 'Content 071', 'home', 'www.URLResource071.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 072', 'Post Title 072', 'Content 072', 'workplace', 'www.URLResource072.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 073', 'Post Title 073', 'Content 073', 'school', 'www.URLResource073.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 074', 'Post Title 074', 'Content 074', 'home', 'www.URLResource074.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 075', 'Post Title 075', 'Content 075', 'workplace', 'www.URLResource075.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 076', 'Post Title 076', 'Content 076', 'school', 'www.URLResource076.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 077', 'Post Title 077', 'Content 077', 'home', 'www.URLResource077.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 078', 'Post Title 078', 'Content 078', 'workplace', 'www.URLResource078.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 079', 'Post Title 079', 'Content 079', 'school', 'www.URLResource079.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 080', 'Post Title 080', 'Content 080', 'home', 'www.URLResource080.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 081', 'Post Title 081', 'Content 081', 'workplace', 'www.URLResource081.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 082', 'Post Title 082', 'Content 082', 'school', 'www.URLResource082.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 083', 'Post Title 083', 'Content 083', 'home', 'www.URLResource083.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 084', 'Post Title 084', 'Content 084', 'workplace', 'www.URLResource084.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 085', 'Post Title 085', 'Content 085', 'school', 'www.URLResource085.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 086', 'Post Title 086', 'Content 086', 'home', 'www.URLResource086.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 087', 'Post Title 087', 'Content 087', 'workplace', 'www.URLResource087.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 088', 'Post Title 088', 'Content 088', 'school', 'www.URLResource088.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 089', 'Post Title 089', 'Content 089', 'home', 'www.URLResource089.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 090', 'Post Title 090', 'Content 090', 'workplace', 'www.URLResource090.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 091', 'Post Title 091', 'Content 091', 'school', 'www.URLResource091.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 092', 'Post Title 092', 'Content 092', 'home', 'www.URLResource092.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 093', 'Post Title 093', 'Content 093', 'workplace', 'www.URLResource093.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 094', 'Post Title 094', 'Content 094', 'school', 'www.URLResource094.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 095', 'Post Title 095', 'Content 095', 'home', 'www.URLResource095.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 096', 'Post Title 096', 'Content 096', 'workplace', 'www.URLResource096.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 097', 'Post Title 097', 'Content 097', 'school', 'www.URLResource097.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 098', 'Post Title 098', 'Content 098', 'home', 'www.URLResource098.com')
    input_json = Create_Post (table_name, dynamodb_resource, 'User 099', 'Post Title 099', 'Content 099', 'workplace', 'www.URLResource099.com')

    input_json = Create_Post (table_name, dynamodb_resource, 'User 100', 'Post Title 100', 'Content 100', 'workplace', 'www.URLResource100.com')

def Get_Post(table_name, dynamodb_resource, postID):
    try:
        myTable = dynamodb_resource.Table(table_name)

        get_post = myTable.get_item(
            Key = {'PostID':postID}
        )
        post = get_post['Item']
        return post
    except:
        print('Post is not exist')

def Get_All_Posts(table_name, dynamodb_resource):
    all_posts = []
    myTable = dynamodb_resource.Table(table_name)

    scanResponse = myTable.scan(TableName=table_name)
    items = scanResponse['Items']
    i = 0
    while i < len(items):
        all_posts.append (items[i])
        i += 1

    sorted_all_posts = sorted(all_posts, key=lambda k: k['PostID'])
    return sorted_all_posts

def Get_n_Recent_Posts(table_name, dynamodb_resource, n):
    allPosts = Get_All_Posts(table_name, dynamodb_resource)

    table_length = Table_Length(table_name, dynamodb_resource)
    run = table_length - 1
    n_recent_posts = []

    i = 0
    while i < n:
        try:
            n_recent_posts.append(allPosts[run])
            i += 1
            if run > 0:
                run -= 1
            else:
                break
        except:
            run -= 1

            pass
    return n_recent_posts

def Get_n_Recent_Posts_by_Community(table_name, dynamodb_resource, n, community):
    allPosts = Get_All_Posts(table_name, dynamodb_resource)

    table_length = Table_Length(table_name, dynamodb_resource)
    run = table_length - 1
    n_recent_posts_by_community = []

    i = 0
    while i < n:
        try:
            if allPosts[run]['Community'] == community:
                # print('Community = ', community)
                n_recent_posts_by_community.append(allPosts[run])
                i += 1

            if run > 0:
                run -= 1
            else:
                break
        except:
            i += 1
            pass
    # print('n_recent_posts_by_community = ',n_recent_posts_by_community)
    return n_recent_posts_by_community

def Update_Post(table_name, dynamodb_resource, postID, 
                username, posttitle, content, community, urlresource):

    myTable = dynamodb_resource.Table(table_name)

    now = datetime.datetime.now()
    strNow = str(now)

    myTable.update_item(
    Key={
        'PostID': postID,
    },
    UpdateExpression=
        'SET Username=:newusername, PostTitle=:newposttitle, PostDate=:newstrNow, Content=:newcontent, Community=:newcommunity, URLResource=:newurlresource',
    ExpressionAttributeValues={
        ':newusername'      : username,
        ':newposttitle'     : posttitle,
        ':newstrNow'        : strNow,
        ':newcontent'       : content,
        ':newcommunity'     : community,
        ':newurlresource'   : urlresource,
    }
    )

def Delete_Post(table_name, dynamodb_resource, postID):
    myTable = dynamodb_resource.Table(table_name)
    
    myTable.delete_item(
        Key= { 'PostID':postID }
    )

def Delete_All_Posts(table_name, dynamodb_resource):
    postID = 1
    while postID < 100:
        Delete_Post(table_name, dynamodb_resource, postID)
        postID += 1


# ==============================================================================================
# Start Program
# ==============================================================================================

app = flask_api.FlaskAPI(__name__)

table_name = "posts"
print(table_name)

# Get the service client.
dynamodb_client = boto3.client('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")


# Get the service resource.
dynamodb_resource = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

app.config['DYNAMO_TABLES'] = [
    dict(
        TableName=table_name,
        KeySchema=[dict(AttributeName='PostID', KeyType='HASH')],
        AttributeDefinitions=[dict(AttributeName='PostID', AttributeType='N')],
        ProvisionedThroughput=dict(ReadCapacityUnits=100, WriteCapacityUnits=100)
    ), 
 ],
print('app.config = ', app.config['DYNAMO_TABLES'])

existing_tables = List_All_Table(dynamodb_client)


if table_name in existing_tables:   # posts table exist -> do nothing
    Delete_All_Posts(table_name, dynamodb_resource)
    Delete_Table(table_name, dynamodb_resource)


Create_Table(table_name, dynamodb_client, dynamodb_resource)


describeTable = dynamodb_client.describe_table(TableName=table_name)
Initial_Posts(table_name, dynamodb_resource)


# ==============================================================================================
# Routing
# ==============================================================================================

@app.route('/', methods=['GET'])
def home():
    return '''
        <ul>
            <li>
                Display all posts: <br> 
                <a> http://localhost:5000/posts/all</a> 
            </li><br>

            <li>
                Delete post by PostID = 100: <br> 
                <a>http://localhost:5000/posts/delete/100</a> 
            </li><br>

            <li>
                Display post by PostID = 10: <br> 
                <a>http://localhost:5000/posts/10</a> 
            </li><br>

            <li>
                Display default 2 recent posts with create post <br>
                <a>http://localhost:5000/posts</a> <br>

                Please copy this Json structure <br>
                {"Username": "User 100", "PostTitle": "Post Title 100", "Content": "Content 100", "Community": "home", "URLResource": "www.URLResource100.com"}


            </li><br>
            <li>
                Display 15 recent post with create post <br>
                <a>http://localhost:5000/posts?n=15</a><br>

                Please copy this Json structure <br>
                {"Username": "User 100", "PostTitle": "Post Title 100", "Content": "Content 100", "Community": "home", "URLResource": "www.URLResource100.com"}

            </li><br>

            <li>
                Display 5 most recent post in school community <br>
                <a>http://localhost:5000/posts/school/5</a>
            </li>
            <li></li>
            <li></li>

        </ul>
      
        '''
    
    
# Get all posts
@app.route('/posts/all', methods=['GET'])
def all_posts():
    allPosts = Get_All_Posts(table_name, dynamodb_resource)
    return list(allPosts)


# Get post by PostID
@app.route('/posts/<int:PostID>', methods=['GET'])
def post_ID(PostID):

    try:
        post = Get_Post(table_name, dynamodb_resource, PostID)
        return post
    except:
        return '', status.HTTP_204_NO_CONTENT



# Get n recent post
@app.route('/posts', methods=['GET', 'POST'])
def n_recent_posts():
    if request.method == 'GET':
        n = request.args.get('n', 2)
        n = int(n)
        n_recent_posts = Get_n_Recent_Posts(table_name, dynamodb_resource, n)

        return list(n_recent_posts)

       
    print('='*20)
    if request.method == 'POST':
        Username = str(request.data.get('Username', ''))
        PostTitle   = str(request.data.get('PostTitle', ''))
        Content   = str(request.data.get('Content', ''))
        Community   = str(request.data.get('Community', ''))
        URLResource   = str(request.data.get('URLResource', ''))

        # print('Username = ', Username)
        # print('PostTitle = ', PostTitle)
        # print('Content = ', Content)
        # print('Community = ', Community)
        # print('URLResource = ', URLResource)


        input_json = Create_Post (table_name, dynamodb_resource, Username, PostTitle, Content, Community, URLResource)
        return input_json

# Delete Post by PostID
@app.route('/posts/delete/<int:PostID>', methods=['GET', 'DELETE'])
def delete(PostID):
    if request.method == 'DELETE':

        Delete_Post(table_name, dynamodb_resource, PostID)

    else:
        return {'status': 'OK'}



# List the n most recent posts to a particular community
@app.route('/posts/<string:Community>/<int:n>', methods=['GET'])
def post_by_community(Community, n):
    print('Community = ', Community)
    print('n = ', n)
    
    n_recent_posts_by_community = Get_n_Recent_Posts_by_Community(table_name, dynamodb_resource, n, Community)

    return list(n_recent_posts_by_community)



# # @app.route('/posts/<string:Community>', methods=['GET'])
# # def post_by_community(Community):
# #     # Community = request.args.get('Community')
# #     print('Community = ', Community)
# #     n = request.args.get('n',5)
# #     n = int(n)
# #     # print('n = ', n)
# #     n_recent_posts_by_community = Get_n_Recent_Posts_by_Community(table_name, dynamodb_resource, n, Community)

# #     return list(n_recent_posts_by_community)



#     #     post = queries.n_post_by_time(n=n)
#     #     if post:
#     #         return list(post)
#     #     else:
#     #         raise exceptions.NotFound()

#     #     # return filter_posts(request.args)
#     # elif request.method == 'POST':
#     #     return create_post(request.data)




# # # http://localhost:5000/posts?n=10
# # # http://localhost:5000/posts/Community_3?n=3


