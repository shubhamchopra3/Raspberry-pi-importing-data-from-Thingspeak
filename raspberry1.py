import urllib2,json,time
READ_API_KEY='IESQ780SEK11P3HH'
CHANNEL_ID=117550
def main():

    while True:
        conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" % (CHANNEL_ID,READ_API_KEY))

        response = conn.read()
        print "http status code=%s" % (conn.getcode())
        data=json.loads(response)
        print data['field3'],data['field5'],data['field7'],data['created_at']
conn.close()
        time.sleep(15)


if __name__ == '__main__':
    main()
