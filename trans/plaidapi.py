from plaid import Client
import json
from trans.models import PlaidUserToken, PlaidAccount, PlaidTransaction
from django.utils import timezone


class PlaidAPI():
    client_id = '554e702a0effc0670b8c9454'
    public_key = '341f751f231458d8f651e072dd3184'
    secret = '09a1032a267857c25718ff0fdc102b'
    env = 'tartan'
    if (False):
        client_id = 'test_id'
        secret = 'test_secret'

    def exchangeLinkTokenForAccount(self, user, public_token):
        Client.config({
            'url': 'https://tartan.plaid.com'
        })
        print('creating client')
        self.client = Client(client_id=PlaidAPI.client_id,
                             secret=PlaidAPI.secret)
        print('getting response')
        response = self.client.exchange_token(public_token)
        print('response')
        print(response)
        access_token = self.client.access_token
        print("Access token {0}".format(access_token))

        ##create account and store in db
        plaiduser = PlaidUserToken()  # is there a good constructor syntax?
        plaiduser.user = user
        plaiduser.access_token = access_token
        plaiduser.status = 'new'
        plaiduser.status_text = "Created {0}".format(timezone.now())
        plaiduser.save()
        print('saved')
        return plaiduser

    def getTransactions(self, usertoken):
        # retrive transactions from a plaid usertoken
        # @todo:  need to specifiy retrieval since day X ago
        self.client = Client(client_id=PlaidAPI.client_id,
                             secret=PlaidAPI.secret,
                             access_token=usertoken.access_token)
        response = self.client.connect_get()
        print('parsing response')
        json_data = json.loads(response.content.decode('utf-8'))

        ##load in the accounts
        json_accounts = json_data['accounts']
        for a in json_accounts:
            account = PlaidAccount.objects.filter(_id=a['_id'])
            if account:
                account=account.get()
                created='updated'
            else:
                account = PlaidAccount()
                created='created'

            account.usertoken = usertoken
            account._id = a['_id']
            account._item = a['_item']
            account._user = a['_user']
            account.name = a['meta']['name']
            account.type = a['type']
            account.instituion_type = a['institution_type']

            account.save()
            print("{0} account: {1} id: {2}".format(created,account.name, account._id) )

        ##Load in the accounts
        json_transactions = json_data['transactions']
        new_transaction_list=[]
        for t in json_transactions:
            transaction = PlaidTransaction.objects.filter(_id=t['_id'])
            if transaction:
                transaction=transaction.get()
                created='updated'
            else:
                transaction = PlaidTransaction()
                created='created'
                transaction.state=PlaidTransaction.STATE_NEW
                new_transaction_list.append(transaction)

            transaction.usertoken = usertoken
            transaction._id = t['_id']
            transaction._account = t['_account']
            transaction.account=PlaidAccount.objects.filter(_id=t['_account']).get()
            transaction.amount = t['amount']
            transaction.name = t['name']
            transaction.date = t['date']
            transaction.type = t['type']
            if 'category' in t:
                transaction.category = t['category']
            if 'meta' in t:
                transaction.meta = t['meta']
                transaction.meta_score = t['score']

            transaction.save()
            print("{0} tx: {1} {2} ".format(created,transaction.date,transaction.name) )

        # parse the plaid response and create plaid transactions
        return new_transaction_list
