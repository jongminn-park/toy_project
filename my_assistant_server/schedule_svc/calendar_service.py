import datetime
from . import my_OAuth_client
from googleapiclient.discovery import build

def get_next_event(user_id):
    try:
        creds = my_OAuth_client.make_credentials(user_id)
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=1, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        if events:
            event = events.pop(0)
        else:
            return "no event"
        if not event:
            print('No upcoming events found.')
        start = event['start'].get('dateTime', event['start'].get('data'))
        return {"title": event['summary'], "location": event['location'], "time": start} 
    except Exception as other:
        print('Something else broke:' + str(other))

