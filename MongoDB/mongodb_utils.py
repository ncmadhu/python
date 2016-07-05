from pymongo import MongoClient

def debug_api(level, message):

    print level + ": " + message
 
def insert_data(database, collection, data):
    # defaults to mongodb running in localhost on port 27017
    client = MongoClient()
    db =  client[database]
    coll_obj = db[collection]
    debug_api("DEBUG","Inserting data in DB - %s, Collection - %s" % (database, collection))
    debug_api("DEBUG","Data - %s" % data)
    result = coll_obj.insert_one(data)
    return result.acknowledged
 
def get_data(database, collection, key):
    client =  MongoClient()
    db = client[database]
    coll_obj = db[collection]
    debug_api("DEBUG","Getting data in DB - %s, Collection - %s" % (database, collection))
    debug_api("DEBUG","Filter Key - %s" % key)
    result = coll_obj.find_one(key)
    debug_api("DEBUG","Data - %s" % result)
    return result
 
def remove_data(database, collection, key):
    client =  MongoClient()
    db = client[database]
    coll_obj = db[collection]
    debug_api("DEBUG","Removing data in DB - %s, Collection - %s" % (database, collection))
    debug_api("DEBUG","Filter Key - %s" % key)
    result = coll_obj.delete_one(key)
    return result.acknowledged

def replace_data(database, collection, key, data):
    client =  MongoClient()
    db = client[database]
    coll_obj = db[collection]
    debug_api("DEBUG","Replacing data in DB - %s, Collection - %s" % (database, collection))
    debug_api("DEBUG","Data - %s" % data)
    result = coll_obj.replace_one(key, data)
    return result.acknowledged
 
def update_data(database, collection, key, update_key, data):
    client =  MongoClient()
    db = client[database]
    coll_obj = db[collection]
    debug_api("DEBUG","Updating data in DB - %s, Collection - %s" % (database, collection))
    debug_api("DEBUG","Filter Key - %s" % key)
    update_data = { "$set": {update_key: data}}
    debug_api("DEBUG","Update Data - %s" % update_data)
    result = coll_obj.update_one(key, update_data)
    debug_api("DEBUG","Result - %s" % result.modified_count)
    return result.acknowledged
    
def increment_data(database, collection, key, data):
    client =  MongoClient()
    db = client[database]
    coll_obj = db[collection]
    debug_api("DEBUG","Incrementing data in DB - %s, Collection - %s" % (database, collection))
    debug_api("DEBUG","Filter Key - %s" % key)
    inc_data = { "$inc": data}
    debug_api("DEBUG","Increment Data - %s" % inc_data)
    result = coll_obj.update_one(key, inc_data)
    debug_api("DEBUG","Result - %s" % result.modified_count)
    return result.acknowledged

if __name__ == "__main__":
    #data = {"test-id": 12345, "data": {"setup": 123}}
    data = {
    "test-id": 123456,
    "setup-completed-servers": [],
    "data": {
        "setup": {
            "setup-suite": "sg_ts_open",
            "test-input": "test_params",
            "test-id": "12345.setup"
        },
        "execution": {
            "execution-suite": "sg_con_disconn",
            "test-id": "12345.exec",
            "run-count": 0,
            "test-duration": 0
        },
        "cleanup": {
            "cleanup-suite": "sg_cleanup",
            "test-id": "12345.cleanup"
        }
    }
}
    #response = insert_data("record", "record", data)
    #response = get_data("record", "record", {"test-id": 123456})
    #server_list = ["server1", "server2"]
    #response = update_data("record", "record", {"test-id": 123456}, "setup-completed-servers", server_list)
    response = update_data("tests", "record", {"test-id": "2310132140559"}, "phase", "cleanup")
    #response = get_data("record", "record", {"test-id": 123456})
    response = get_data("tests", "record", {"test-id": "2310132140559"})
    #response = remove_data("record", "record", {"test-id": 12345})
    #response = get_data("record", "record", {"test-id": 12345})
    #data["data"]["setup"]["test-id"] = "123456.setup"
    #response = replace_data("record", "record", {"test-id": 123456}, data)
    #response = get_data("record", "record", {"test-id": 12345})
    print response
