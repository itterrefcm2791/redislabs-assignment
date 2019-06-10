import redis

def main():
    '''
    Use Case #1 - Write numbers 1 - 100 into Redis OSS
    '''
    redis_oss_host = "localhost"
    redis_oss_port = 6379
    redis_oss_password = ""

    try:
        r = redis.StrictRedis(host=redis_oss_host,
                              port=redis_oss_port,
                              password=redis_oss_password,
                              decode_responses=True)

        # Define the set of numbers 1 - 100
        x = range(1, 101, 1)

        for n in x:
            # Add the numbers as simple keys
            r.set(n,"")
            # Add the numbers, as integers to a list
            r.lpush("example:list", n)

    except Exception as e:
        print(e)


    '''
    Use Case #2 - Read numbers from Redis Replica
    '''
    redis_enterprise_host = "localhost"
    redis_enterprise_port = 6379
    redis_enterprise_password = ""

    try:
        # decode_repsonses converts responses into Python utf-8 strings
        r = redis.StrictRedis(host=redis_enterprise_host,
                              port=redis_enterprise_port,
                              password=redis_enterprise_password,
                              decode_responses=True)

        # Read the simple keys we added ... 1 - 100
        # using scan to only get the numeric keys
        vals = r.keys(pattern="*[0/-9]*")
        print("\nKeys 1-100 from Redis ... As They Are:\n")
        print(vals)
        # Make a list of integers. Redis stores the keys as strings
        int_keys = [int(v) for v in vals]
        print("\nKeys 1-100 From Redis, Cast As Integers Using int():\n")
        print(int_keys)
        # Print out the keys as they are
        print("\nKeys 1-100 From Redis, Cast As Integers Using int(), sorted in reverse:\n")
        print(sorted(int_keys, reverse=True))

        # Get the list from Redis
        vals = r.lrange(name="example:list", start=0, end=99)
        # Print the values, which are in reverse, based on order of insertion
        print("\nValues from Redis list \"example:list\", where numbers are in order they were inserted:\n")
        print(vals)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
