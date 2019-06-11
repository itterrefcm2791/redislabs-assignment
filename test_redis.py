import redis


def main():
    '''
    Adding Data to Redis OSS
    '''
    redis_oss_host = "ec2-3-15-4-12.us-east-2.compute.amazonaws.com"
    #redis_oss_host = "13.15.4.12"
    redis_oss_port = 6379
    redis_oss_password = ""

    try:
        r = redis.StrictRedis(host=redis_oss_host,
                              port=redis_oss_port,
                              password=redis_oss_password,
                              decode_responses=True)
        # Define the set of numbers 1 - 100
        for n in range(1, 101, 1):
            # Add the numbers as simple keys
            r.set(n,"")
            # Add the numbers, as integers to a list
            r.lpush("example:list", n)
    except Exception as e:
        print(e)

    '''
    Reading Data from Redis Enterprise Replica
    '''

    redis_enterprise_host = "ec2-18-224-62-205.us-east-2.compute.amazonaws.com"
    #redis_enterprise_host = "18.224.62.205"
    redis_enterprise_port = "14878"
    redis_enterprise_password = ""

    try:
        # decode_repsonses converts responses into Python utf-8 strings
        r = redis.StrictRedis(host=redis_enterprise_host,
                              port=redis_enterprise_port,
                              password=redis_enterprise_password,
                              decode_responses=True
                              )

        # Read the simple keys we added ... 1 - 100
        # using scan to only get the numeric keys
        vals = r.keys(pattern="*[0/-9]*")
        #vals = r.keys(pattern="*")
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
