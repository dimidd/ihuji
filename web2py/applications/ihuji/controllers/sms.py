parser = local_import('Parser')

def index():
    args = request.vars
    body = args['Body']
    num = args['From']
    sms = {'num': num, 'body': body}
    db.sms.validate_and_insert(**sms)

    par = parser.Parser()
    dic = par.str_parser(body, num)
    if dic['type'] == 'vote':
        vote = {'speed' : dic['speed'], 'co_id' : dic['course']}
        db.votes.validate_and_insert(**vote)

    return dict(args = args)

def votes():
    res = "2"
#    v = db.executesql("SELECT speed, stamp, datetime('now', '-30 seconds') FROM votes WHERE stamp < datetime('now', '-30 seconds');")
    v = db.executesql("SELECT AVG(speed) FROM votes;")[0][0]
    return dict(avg = str(int(v)))