def index():
    args = request.vars
    body = args['Body']
    num = args['From']
    sms = {'num': num, 'body': body}
    db.sms.validate_and_insert(**sms)
    return dict(args = args)
