#!/usr/bin/env python3

from flask import Flask, request, redirect, url_for

import psycopg2


app = Flask(__name__)

dbname = "news"


@app.route('/', methods=['GET'])
def main():
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute("""select title, count(*) as name from log, articles where
              path='/article/' || articles.slug group by title order by
              name desc limit 3; """)
    query1 = c.fetchall()

    c.execute("""select authors.name, count(log.path) as counts from log,
              articles, authors where path ='/article/' || articles.slug
              and articles.author=authors.id group by authors.name
              order by counts desc; """)
    query2 = c.fetchall()

    c.execute("""select log1.date, (log1.counts * 100)/(log2.counts)as error
              from (select DATE(time) as date, cast(count(status) as float) as
              counts from log where status NOT LIKE '200 OK' group by
              DATE(time)) as log1, (select DATE(time) as date,
              cast(count(status) as float) as counts from log group by
              DATE(time)) as log2 where log1.date=log2.date
              and (log1.counts * 100)/(log2.counts) > 1; """)
    query3 = c.fetchall()

    data = 'Most popular three articles of all time' + '<br><br>'

    for query in query1:
        data += query[0] + '&nbsp' + '-' + '&nbsp' + str(query[1]) + '<br>'

    data += '<br><br>'
    data += 'Most Popular article authors of all time' + '<br><br>'

    for query in query2:
        data += query[0] + '&nbsp' + '-' + '&nbsp' + str(query[1]) + '<br>'

    data += '<br><br>'
    data += 'Day on which more than one leads to error  ' + '<br><br>'

    for query in query3:
        data += str(query[0]) + '&nbsp' + '-' + '&nbsp' + str(query[1])
        data += '<br>'

    return data
    db.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
